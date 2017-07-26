#python-IO学习
#open("路径","r/w")
#读写字符注意编码错误
#绝对路径与相对路径
#1读文件
#1.1文件打开
'''
f1=open("c:/Users/Administrator/Desktop/python_stydy/py3test/py3test.py","r")
str1=f1.read()
print(str1)
f1.close()
'''
#1.2打开文件捕获异常
'''
try:
    f = open("py3test/py3test.py","r")
    print(f.read())
except Exception as e:
    print("file not found")
finally:
    print("finally")
    if f:
        f.close()
'''
#1.3with语句来自动调用close()方法
'''
with open("py3test/py3test.py","r") as f:
    print(f.read())
#f.read()一次性读取完
#f.readlines()按行读取，可用于读取配置文件
#f.read(size) 按固定size读取文件，在不知道文件具体大小的情况下
'''
#1.4读二进制文件
'''
f = open('mode/haha.jpg', 'rb')
print(f.read())
'''
#2写文件
#2.1写入文件
'''
with open('py3test/py3test.py', 'w') as f:
    f.write('Hello, world!---')
    print("写入成功")
'''
#按某种编码读取，有错就忽略
'''
f1 = open('minmax.py', 'r', encoding='UTF-8', errors='ignore')
print(f1.read())
'''
#3StringIO and BytesIO
#3.1StringIO 读取内存中的字符串
'''
from io import StringIO
f=StringIO()
f.write("hello")
f.write("hehe")
f.write("000000")
print(f.getvalue())
'''
#3.2BytesIO 读取内存中的二进制数据
'''
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
'''
#4操作文件和目录
#4.1判断操作系统
#nt 表示windows  posix表示Linux Unix macos
'''
import os
print(os.name)#操作系统名
#print(os.uname())#操作系统详情，只在Linux等上提供
print(os.environ) #环境变量
print(os.environ.get('path'))
'''
#4.2操作文件和目录
'''
import os
print(os.path.abspath('.')) #当前绝对路径
cdir=os.path.abspath('.')
#os.mkdir(os.path.join(cdir, 'testdir'))#在此路径下创建dir,存在会报错 FileExistsError:
#os.rmdir(os.path.join(cdir, 'testdir'))#在此路径下删除dir
#os.path.split('/Users/michael/testdir/file.txt')拆分路径
#os.path.splitext('/path/to/file.txt')#直接获取文件名
f0=os.path.split('/Users/michael/testdir/file.txt')
print(f0[1])#file.txt
f1=os.path.splitext('/path/to/file.txt')
print(f1[1])#.txt
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])#输出当前目录下所有的.py文件
'''
#4.3序列化
#Python提供了pickle模块来实现序列化。
#4.3.1保存到文件
'''
import pickle
d = dict(name="lijing",age=24,addres="cq")
f = open('dump.txt', 'wb')
pickle.dump(d,f)
f.close()
'''
#4.3.2从文件读取
'''
import pickle
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
'''
#4.4 json数据
#对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON
import json
d = dict(name="hello",age=24,addres="cq")
e = {"name":"hello","age":24,"addres":"cq"}
f = open('dump.txt', 'wb')
json.dump(e,f)
f.close()

