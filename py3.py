#!/usr/bin/python
# -*- coding: utf-8 -*-
#首字母大写的方法
'''
def normalize(name):
	return name.capitalize()

li= ["adam","Lisa","BARt"]
l2=list(map(normalize,li))
print(l2)

print("1024*768=",1024*768)
'''
#if 语句应用
'''
import sys
xiaoming = {"height":1.66,"weight":72}
xiaomingbmi=xiaoming["weight"]/(xiaoming["height"]*xiaoming["height"])
if(xiaomingbmi>32):
    print("小明过于肥胖",xiaomingbmi)
elif(xiaomingbmi>=28 and xiaomingbmi<32):
    print("小明肥胖",xiaomingbmi)
elif(xiaomingbmi>=25 and xiaomingbmi<28):
    print("小明过重",xiaomingbmi)
elif(xiaomingbmi>=18.5 and xiaomingbmi<25):
    print("小明正常",xiaomingbmi)
elif(xiaomingbmi<18.5):
    print("小明过轻",xiaomingbmi)
else:
    print("输入有误")
'''

#合并列表为字典
'''
names=["mike","Jack","Mary"]
for name in names:
    print("hello,",name+"!")
scores=[78,87,95]
dict(map(lambda x,y:[x,y], names,scores))
'''

#hex()十进制转化为十六进制
'''
x1=hex(100)
print(x1)
'''
#自定义函数
def my_abs(x):
    if x>=0:
        x=x
    else:
        x=-x
    return x
	
#递归
'''	
def fact(n):
    if n==1:
        return 1
    else:
	    return n*fact(n-1)
print(fact(5))
'''
#循环构造列表,切片打印列表问题
'''
L1=[]
n=1
while n<99:
    L1.append(n)
    n+=2
print(L1)
print(L1[0:15])
print(L1[10:15])
print(L1[-10:])
print(L1[::10])
print(L1[0:len(L1)//2])
'''
#列表生成式
'''
L2=[]
for x in range(1,11):
    L2.append(x*x)

print(L2)

l3=[x*x for x in range(1,11) if x%2==0]
print(l3)
print([x*x for x in range(1,11)])
l4=[m+n for m in 'ABC' for n in "XYZ"]
print(l4)
'''
#列出当前目录下所有文件和目录名
'''
import os
l5=[d for d in os.listdir(".")]
print(l5)
#generator生成器;101行代码
#t=(b,a+b)
#a=t[0]
#b=t[1]
'''
#fabric函数
'''
---------------
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a, b = b, a + b
        n=n+1
    return 'ok'
k=fib(8)
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
---------------
'''
#杨辉三角的打印
'''
-------------------
t=[]
def yanghuitangle(line):
    l=[1]
    while True:
        yield l
        l=[l[x]+l[x+1] for x in range(len(l)-1)]
        l.insert(0,1)
        l.append(1)
        if len(l)>line:
            break

a=yanghuitangle(10)		
for i in a:
    print(i)			
			
			
for k in range(2-1):
    print(k)
-----------------------
'''
		
'''	
-----------------------		
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的，例如：			
	
from collections import Iterator
from collections import Iterable
#print(isinstance([],Iterable))			
#print(isinstance([],Iterator))	
----------------------
'''
#高阶函数：函数中调用函数，传入函数名
#高阶函数之map ,reduce，filter
'''
------------------------------------
def add(x,y,func):
    return func(x)+func(y)
t=add(-3,4,abs)
print (t)
#作用于列表每一个元素			

#map(函数名,列表) 
#reduce(函数名,列表)
#filter(函数名,列表)
#strip(rm) 删除s字符串中开头、结尾处，位于 rm删除序列的字符
ls=[1,3,5,7,9]
def f(x):
    return x*x
ls2=map(f,ls)

ls3=map(str,ls)

from functools import reduce			
def add(x,y):
    return x+y
r=reduce(add,[1,2,3,4,5,6])
print(r)

lj=["","","des","","hahha"]
 def not_enpty(lj):
     return lj and lj.strip()
	 
ss=filter(not_enpty,lj)
print(ss)
--------------------------------------	 
'''
#filter(函数名,范围或者列表)
#回文的处理输出
'''
def ispaderome(r):
    t=str(r)
    count=0;
    for i in range(len(t)//2):
        if(t[i]==t[len(t)-i-1]):
            count=count+1
        else:
            break;
    if count==len(t)//2:
        return True
    else:
        return False
lll=[234,434,12312,12321]
output = filter(ispaderome,lll)
for x in output:
    print(x)
'''

	
    

	 