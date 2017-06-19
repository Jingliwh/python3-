#sorted高阶函数，排序列表
'''
l1=[-3.4,5,2,37,-8]

l2=sorted(l1)
print(l2[0:len(l2)])

l3=sorted(l1,key=abs)
print(l3[0:len(l3)])

tup1=[('Bob', 75), ('Adam', 92), ('Bart', 66),('Adam', 66), ('Lisa', 88)]
print(tup1[1][1])

#实现对列表里面的元组进行排序，te代表列表中的元组，te[1]代表元组的第二个元素
l4=sorted(tup1,key=lambda te:te[1])
print(l4[0:len(l4)])

#实现对列表里面的元组进行排序，te代表列表中的元组，te[1]代表元组的第二个元素,reverse代表反向排序
l5=sorted(tup1,key=lambda te:te[1],reverse=1)
print(l5[0:len(l5)])

#扩展，itemgetter 实现对列表中的元组进行排序,itemgetter(0,1)表示先按第一个元素
#排序，然后在按第二个元素排序
from operator import itemgetter

l6=sorted(tup1,key=itemgetter(0,1))
print(l6[0:len(l6)])
l7=sorted(tup1,key=itemgetter(0))
print(l7[0:len(l7)])
'''

#匿名函数 lambda
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
'''
L8=list(map(lambda x:x*x,[1,2,3,5]))
print(L8[0:len(L8)])
f=lambda x:x*x+2
print(f(8)) #66
'''

#装饰器
#decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
'''
def decoratorfun(funz):
    def wrapper(*args, **kw):
        print("装饰函数")
        return funz(*args, **kw)
    return wrapper

@decoratorfun
def beizhuangshifun():
    print("我是被装饰函数")

beizhuangshifun()
'''

#偏函数
'''
li=int("12345",base=16)
ln=int("12345",base=8)
print(li)
print(ln)
import functools
#int2 = functools.partial(int, base=2)
#十进制转二进制
def int2(x, base=2):
    return int(x, base)
	
print(int2("11100"))
'''
