import sys
'''
#下载三方插件包pip install Pillow（处理图像）
from PIL import Image
img=Image.open("my.png")
print(img.format,img.size,img.mode)
img.thumbnail((200,100))
#全路径保存
img.save("C:/Users/Administrator/Desktop/haha.jpg","JPEG")
#当前工程目录下保存
img.save("md/haha.jpg","JPEG")
'''
#导入不存在的模块会编译报错
'''
import mymodule
print("111")
'''

#类的定义，函数定义，函数调用
'''
class People (object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("__init__")

    def tion():
        print("hehe")

    def information(self):
        print('%s:%s'% (self.name,self.age))
       

haha=People("hehe",19)
haha.information()#输出hehe:19
haha.name="Mary"
haha.age=18
haha.information()#输出Mary:18
'''

#类定义私有变量：不能修改类的属性值;可以通过设置方法获取和修改值
'''
class Vehicle(object):
    def __init__(self,name,price):
        self.__name=name
        self.__price=price 

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name

    def info(self):
        print("%s,%s"%(self.__name,self.__price))


car=Vehicle("motocar",500)	
car.info()#输出motocar,500
car.__name="bycycle"
print(car.__name)#相当于添加了新属性，而非修改了原属性
print(car.get_name())
car.__price=100
car.info()#输出motocar,500
car.set_name("taxi")
car.info()#输出taxi,500
print(car.__name)
		
#判断一个对象是不是某个类的成员,继承多态略去		
flag=isinstance(car, Vehicle)		
print(flag)	
'''
#python 与 java 在继承上的区别
#后者必须传入父类型，则传入的对象必须是父类型或者它的子类，否则，将无法调用父类的方法。
#对于Python这样的动态语言来说，一个函数则不一定需要传入父类型。我们只需要保证传入的对象有一个对应的方法就可以
#1父类
'''
class Fruit(object):
    def __init__(self,name):
        self.name=name
		
    def showName(self):
        print("Fruit")
#2子类
class Apple(Fruit):
    def showName(self):
        print("Apple")
#不相关类
class Car(object):
    def __init__(self,name):
        self.name=name
		
    def showName(self):
        print("car")
#类外方法		
def kkk(going):
    going.showName()
#---测试代码
f1=Fruit("apple")
kkk(f1)
f2=Apple("apple")
kkk(f2)
f3=Car("taxi")
kkk(f3)
'''
#类型检查与查询,isinstance()进行类的检查，type()基本数据类型检查
'''
print(type(123))
print(type("234"))
print(type(123)==type("123"))
print(type(123)==type(456))
'''

#类属性--相当于java的成员变量，通过对象或者类直接获得】
#对象的属性有对象自己附加，与java不同

class Phone(object):
    name="Phone"
    price="unknow"

    def __init__(self,imid):
        self.imid=imid

myphone=Phone("12121")
print(myphone.name) #Phone
print(myphone.price)#unknow
print(Phone.name)   #Phone
print(myphone.imid) #12121
myphone.name="hehe" 
print(myphone.name) #hehe 此处对name，重新赋值，值改变
myphone.weight=11;
print(myphone.weight) #11  此处为自己新定义属性，与类无关，只与当前对象有关
print(Phone.weight)




		
		
		