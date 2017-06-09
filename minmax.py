#coding:utf-8
#1.字典取最大最小指
'''
price = {
	"pen": 12.5,
	"penceil": 16.7,
	"computer": 1111.1,
	"dark": 17.8
}
minprice=min(zip(price.values(),price.keys()))
maxprice=max(zip(price.values(),price.keys()))
print "minprice is %f %r" % minprice
print "minprice is %f %r" % maxprice
'''

#2.统计出现次数最多的前三个单词,和最少的三个单词
words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
down_three = word_counts.most_common()[-4:-1]
print(top_three)
print(down_three)
# outputs [('eyes', 8), ('the', 5), ('look', 4)]
# Example of merging in more words

morewords = ['why','are','you','not','looking','in','my','eyes']
word_counts.update(morewords)
print(word_counts.most_common(3))