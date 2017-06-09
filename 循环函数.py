#-*-coding:utf-8-*-
hairs=["brown","blond","red"]
eyes = ['brown','blue','black','green']
weights=[1,2,3,4]
fruits=['apples','oranges','pears','apricots']
the_count=[1,2,3,4,5]
'''
#this first kind of for-loop goes through a list 
for number in the_count:
    print "this is count %d" %number
# same as above
for fruit in fruits:
    print "the fruit type  is %s" %fruit
'''
"""
elements = []
for i in range(1,6):
    print "Adding %d to the list." %i
    elements.append(i)

#print elements
for i in elements:
    print "element was %d" %i 
"""
#习题33，while循环
'''
i = 0
numbers=[]
while i<6:
    print "at the top i is %d" %i
    numbers.append(i)
    
    i=i+1
    print "numbers now:", numbers
    print "at the bottom i is %d" %i


print "The numbers:"
for num in numbers:
    print num
'''
#习题34,访问列表的元素
'''
f1=fruits[0]
print f1
'''
#习题35,分支和函数
'''
from sys import exit

def gold_room():
    print "how much do you take?"
    next = raw_input("edit:")
    if("0" in next or "1" in next):
        how_much = int (next)
    else:
        dead("man,learn to type a number.")
    if(how_much<50):
        print "nice ,you are good,you win."
        exit(0)
    else:
        dead("you  are so greedy!")
def dead(why):
   print why,"good job!"
   exit(0)
def start():
    print "you are in a dark room"
    print "there is a door to right and left."
    print "which one do you take?"
    next = raw_input("r or l：")
    if next=="left":
        bear_room()
    elif next=="right":
        gold_room()
    else:
        dead("new come，game over!")
def bear_room():
    print "just so so."	

start()
'''
#列表操作
'''
states={
    "bj":"beijing",
	"sh":"shanghai",
    "sichuan":"chengdu",
    "jiangsu":"nanjing"
}
# create dict city
cites={
    "beijing":"chaoyangqu",
    "shanghai":"pudong",
    "chengdu":"shuangliu"
}
#add  more city
cites["chongqing"]="wanzhouqu"
cites["guangdong"]="shenzhen"

#print out some cites
print '-' * 10
print "chongqing has :",cites["chongqing"]
print "shanghai has :",cites["shanghai"]
print '-' * 10
print "bj,s abb  is:",states["bj"]
'''
#38 test join, stuff
'''
str1="www.baidu.com"
str2=str1[3:7]
print str2
str3=" ".join(str2)
str4=":".join(str1)
print str1
print str2
print str3
print str4
'''
#可爱的字典
'''
class Song(object):
    def __init__(self,lyrice):
        self.lyrice=lyrice
    def sing_me_a_song(self):
        for line in self.lyrice:
            print line

happy_bday = Song(["happy birthday to you",
                    "I don't want to sued",
		            "so i stop right there"])
bulls_on_parde=Song(["will be okay!",
                    "you are so good"])
happy_bday.sing_me_a_song()
bulls_on_parde.sing_me_a_song()
'''
#习题40：模块，类，对象
'''
import test
test.apple()
strr={'haha':"goaxiao"}
print strr['haha']

class MyStuff(object):

    def __init__(self,ly):
        self.tting=ly

    def apple(self):
        print "I am a apple"

#things=MyStuff()
#things.apple()
#print things.tting
thing2=MyStuff("hahaha")
print thing2.tting
'''
#习题41：物以类聚
'''
stuff=["test",'this',"out"]
print ' '.join(stuff)
'''
#习题42 继承和合成
#1.隐式继承
'''
class Parent(object):

    def implicit(self):
        print "parent implicit()"

class Child(Parent):
    pass

dad=Parent()
son=Child()
dad.implicit()
son.implicit()
'''
#2.显示继承
'''
class Parent(object):

    def implicit(self):
        print "parent implicit()"

class Child(Parent):
    def implicit(self):
        print "son implicit()"

dad=Parent()
son=Child()
dad.implicit()
son.implicit()
'''
#3.运行前后复写
class Parent(object):

    def implicit(self):
        print "parent implicit()"

class Child(Parent):
    def implicit(self):
        print "son implicit()"
        super(Child,self).implicit()
        print "child after"

dad=Parent()
son=Child()
dad.implicit()
son.implicit()
















