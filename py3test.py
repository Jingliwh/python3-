#py3 测试学习
#2017-7-3
#廖雪峰 python3 
#链接地址 http://www.liaoxuefeng.com/wiki/


#1.错误处理 设置错误返回值（pass）

#2.错误捕获语句 try catch
#2.1)python:  try except  finally
#          ZeroDivisionError 除0异常
#如果没有错误，python可以执行else语句
#python 异常基类 BaseException
#以下为异常继承结构
#https://docs.python.org/3/library/exceptions.html#exception-hierarchy
'''
try:
    print("start")
    t=10/0
    print("interrupt",r)
except ValueError as e:
    print(e,"异常")
except ZeroDivisionError as e:
    print(e,"异常")
else:
    print('no error!')
finally:
    print("end")
'''
#2.2)记录错误 logging
'''
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
'''
#2.3)抛出异常
'''
class FooError(ValueError):
    pass

def foo(s):
    n=int(s)
    if n==0:
        raise FooError("invalid value: %s" %s)
    return 10/n

n=foo("2")
print(n)	
#t=foo("0")#抛出异常   	
#print(t)
try:
    print("start")
    foo("0")
    print("no problem")
except FooError as e: #捕获异常
    print(e)
finally:
    print("end")
'''
#3.错误调试
#3.1) print("输出结果")
#3.2)assert断言,也会抛出断言异常 例：AssertionError: n is zero!
'''
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

main()
'''
#3.3)logging运行日志输出
#日志输出级别debug，info，warning，error
'''
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
'''
#3.4)python 调试桥 pdb
# 调试命令 python3 -m pdb err.py
#pdb.set_trace() 设置断点
#p查看变量 ，c继续运行
'''
import pdb
s='0'
n=int(s)
pdb.set_trace()
print(10/n)
'''
#3.5)IDE调试
#推荐工具及链接
#http://www.jetbrains.com/pycharm/


#4.单元测试
#import unittest
#5.文档测试
#import doctest
'''
def fact(n):
    if(n<1):
        raise ValueError()
    if n==1:
        return 1
    return n*fact(n-1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
'''

















