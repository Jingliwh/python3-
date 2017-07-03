#python 高级面向对象属性
#动态绑定属性和方法
#定义类后,再将方法和属性绑定
'''
class Ball(object):
    name="ball"

def ball_add(self):
    print("ball method")

from types import MethodType
#给某个类的对象绑定方法，不影响其他类的对象
pingpang=Ball()
pingpang.ball_add=MethodType(ball_add,pingpang)
pingpang.ball_add() #ball method

#volleyball=Ball()
#volleyball.ball_add()#报错，volleyball没有该方法

#给类绑定方法，所有类的对象拥有该方法
Ball.ball_add=ball_add
volleyball=Ball()
volleyball.ball_add() #ball method
'''
#python 限制类的属性扩展(__slots__)
#定义后类的属性不能在类的对象上进行扩展
#：注意，__slots__只对当前类作用，对子类无作用
'''
class People(object):
    __slots__=("name","age","height") #元组定义属性

xiaoming=People()
xiaoming.name="xiaoming"
xiaoming.age=18
xiaoming.height=176
#xiaoming.weight=77  #报错，People object has no attribute 'weight'
print(xiaoming.age,xiaoming.name,xiaoming.height)
'''
#装饰器，@property广泛应用在类的定义中，可以让调用者写出简短的代码，
#同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
#_xxx (受保护)     不能用'from module import *'导入
#__xxx__ 系统定义名字
#__xxx    类中的私有变量名
'''
class Screen(object):
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError("不是一个整数 not a integer")
        if value<0 or value>1080:
            raise ValueError("超出范围 must between 0-1080")
        self.__width=value
		
    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError("不是一个整数 not a integer")
        if value<0 or value>1920:
            raise ValueError("超出范围 must between 0-1920")
        self.__height=value

    @property
    def resolution(self):
        return 1920*1080

mycall=Screen()
mycall.width=1000
print("mycall.width=",mycall.width)
mycall.height=986
print("mycall.height=",mycall.height)
print("mycall.resolution=",mycall.resolution)
mycall.height=10
print("mycall.height=",mycall.height)
#mycall.resolution=600  #AttributeError: can't set attribute
print("mycall.resolution=",mycall.resolution)
'''

#python 支持多种继承 子类可继承过个父类
#class Apple(Fruit,Plant)

#python 系统自定义函数__xxx__  如果需要改写相应功能，也可以自己实现，
#类似与java Object类的toString() equals()---
#主要方法如下
#1：__str__        类似于toString()方法
#2：__iter__       类似于iterator迭代输出
#3：__slots__      限制类的属性扩展
#4：__getitem__   #像list那样按照下标取出元素
#5：__getattr__   #只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
#6：__call__      #s(),类似于java构造方法

#python 枚举
from enum import Enum
#定义枚举类1
'''
Season=Enum('Season',('Spring','Summer','Autumn','Winter'))

for name,member in Season.__members__.items():
    print(name,"=>",member,",",member.value)

#Spring => Season.Spring , 1
#Summer => Season.Summer , 2
#Autumn => Season.Autumn , 3
#Winter => Season.Winter , 4
'''
#定义枚举类2
'''
class Season(Enum):
    Spring=1
    Summer=2
    Autumn=3
    Winter=4

for name,member in Season.__members__.items():
    print(name,"=>",member,",",member.value)
	
#Spring => Season.Spring , 1
#Summer => Season.Summer , 2
#Autumn => Season.Autumn , 3
#Winter => Season.Winter , 4
'''
#元类
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#ORM 对象关系映射
#type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类
#metaclass就可以根据这个类创建出实例，先定义metaclass，然后创建类

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

h = Hello()
print('call h.hello():')
h.hello()
print('type(Hello) =', type(Hello))

#.lambda匿名函数
'''
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

l=MyList()
l.add(13)
l.add(15)
print(l[0])
print(l[1])
'''
#ORM例子
#首先来定义Field类，它负责保存数据库表的字段名和字段类型：
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Simple ORM using metaclass '

class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# testing code:

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
'''