import nltk
from nltk.corpus import gutenberg as gb
from nltk.corpus import brown as br, PlaintextCorpusReader
from nltk.corpus import names
from nltk.corpus import inaugural as ina
import numpy
import re
import jieba

# print(len(br.categories()))
# print(len(br.fileids()))
# print(len(br.fileids('news')))
# print(len(br.words('ca01')), len(br.sents('ca01')))
# print(br.raw('ca02'))

# print(gb.fileids())
# words = gb.words('austen-persuasion.txt')
# print("word num:", len(words))
# print("unique word num:", len(set(words)))

# emma_words = gb.words('austen-emma.txt')
# fd = nltk.FreqDist(emma_words)
# # fd.plot(30, cumulative=False)
# print(list(fd.items())[100:150])
#
# cfd = nltk.ConditionalFreqDist(
#     (genre, word)
#     for genre in br.categories()
#     for word in br.words(categories=genre)
#     )
# genre = ['news', 'religion']
# word = []
#
# male_name = names.words('male.txt')
# female_name = names.words('female.txt')
# d = nltk.ConditionalFreqDist(
#     (file, name[-1])
#     for file in names.fileids()
#     for name in names.words(file)
# )
# d.plot()


# print(len(ina.fileids()), ina.fileids())
# for file in ina.fileids():
#     if file[0:4] == '1797':
#         print(ina.raw(file))
#
# fd = nltk.ConditionalFreqDist(
#     (word, file[0:4])
#     for file in ina.fileids()[0:20]
#     for w in ina.words(file)
#     for word in ['america', 'citizen']
#     if (w.lower()).startswith(word)
# )
# fd.plot()

# corpus_root = "C:/Users/Administrator/Desktop/test-corpus"
# corpus = PlaintextCorpusReader(corpus_root, ".*")
# print(corpus.fileids())
# for file in corpus.fileids():
#     print(file, ":words-", len(corpus.words(file)), "sents-", len(corpus.sents(file)), "paras-", len(corpus.paras(file)) )
#
# chars = corpus.raw('14843.txt')
# words = corpus.words('14843.txt')
# sent = corpus.sents('14843.txt')
#
# print(len(chars))
# print(len(words))
# print(len(sent))
# print(len(set(words)))

# emma = gb.words('austen-emma.txt')
# words = [w for w in emma if re.search('^sh',w) and len(w) >= 4]
# print(len(words))
# print(words)

# with open('article',encoding='utf-8') as file_object:
#     contents = file_object.read()
#     result = jieba.lcut(contents)
#     print(result)
# with open("result.txt", "w",encoding='utf-8') as f:
#     f.write(str(result))
#
# import codecs
# from jieba import posseg
# import json
# f = open("test.json", encoding='utf-8')
# news = json.load(f)
# words = posseg.cut(news['news'][0]['content'])
# with open("words", "w", encoding='utf-8') as f:
#     for i in words:
#         f.write(str(i)+'\n')
# https://item.jd.com/100012241196.html#comment
# https://item.jd.com/100012241196.html#comment
# from nltk.grammar import CFG
# # g = CFG.fromstring("""
# #                     S -> NP VP
# #                     NP -> ART N
# #                     NP -> ART ADJ N
# #                     VP -> V
# #                     VP -> V NP
# #                     ART -> "the"
# #                     ADJ -> "old"
# #                     N -> "old"|"man"
# #                     V -> "cried"|"man"
# #                     """)
# # sent = "the old man cried".split()
# # rd_parser = nltk.RecursiveDescentParser(g)
# # for tree in rd_parser.parse(sent):
# #     print(tree)
# import numpy
# import numpy.linalg
# result = numpy.arange(0,50,3)
# print(result.sum())
# print(result.mean())
# print(result.std())
# print(result)
# a = numpy.array([[1,0,-1,2],[-1,1,3,0],[0,5,-1,4]])
# b = numpy.array([[0,3,4],[1,2,1],[3,1,-1],[-1,2,1]])
# c = a.dot(b)
# f = numpy.linalg.det(c)
# e = numpy.linalg.inv(c)
# print(c)
# print(f)
# print(e)
# from matplotlib import pyplot
# import math
# from random import *
# x = []
# for i in range(100):
#     x .append(random())
# y = []
# z = []
# for i in x:
#     y.append(math.cos(i*i)+1)
#     z.append(math.sin(i)+1)
# pyplot.plot(x,y,label='y=cos(x**2)+1',color='red',lineWidth=2)
# pyplot.plot(x,z,label='z=sin(x)+1',color='blue')
# pyplot.xlabel('x')
# pyplot.ylabel('y')
# pyplot.ylim(0,2)
# pyplot.xlim(0,1)
# pyplot.legend()
# pyplot.show()
# from sklearn.impute import SimpleImputer
# import numpy
# X = [[numpy.nan,2,10,5],[6,10,8,numpy.nan],[7,2,8,6]]
# imp = SimpleImputer(missing_values=numpy.nan,strategy='mean')
# imp.fit(X)
# print(imp.transform(X))
from sklearn.cluster import KMeans
import numpy
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
f = open("three_ring.txt", 'r',encoding='utf-8')
data = []
for line in f.readlines():
    item = line.split(',')
    x = float(item[0])
    y = float(item[1])
    t = [x, y]
    data.append(t)
X = numpy.array(data)
k = KMeans(n_clusters=3,).fit(X)
label = k.labels_
print(label)
colors = ListedColormap(['#FF0000','#00FF00','#0000FF'])
plt.scatter(X[:,0:1],X[:,1:2],c=label,cmap=colors)
plt.show()
