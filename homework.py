import nltk
from nltk.corpus import inaugural
from nltk.corpus import wordnet
import random
import re
import math

# 23题_a
# 导入数据
inaugural_words = inaugural.words()
# 创建字典
a = nltk.FreqDist()
# 遍历列表,将词转成小写
fd = nltk.FreqDist([w.lower() for w in inaugural_words])
# 遍历列表,统计对数词频
for key in fd:
    t = math.log10(fd[key])
    a[key] = t

fd2 = dict(fd)
# 将dict 根据词频排序 转成list
voc = sorted(fd2.items(), key=lambda item: item[1], reverse=True)
# 计算 倍数
result = voc[49][1]/voc[149][1]
print(voc[49][0],' ', voc[149][0])
print("r_a="+str(result))
# 第一个 与 最后一个
print(voc[0]," ",voc[149])
# 画图
a.plot(150)

# 23题_b
b = nltk.FreqDist()
text = ""
# 构建文本
for i in range(1000000):
    text += random.choice("abcdefg ")
# 分词
text_p = re.split(u"\s+", text)
fd_1 = nltk.FreqDist(text_p)
# 统计对数词频
for k in fd_1:
    n = math.log10(fd_1[k])
    b[k] = n
fd3 = dict(fd_1)
# 排序转成 list
vocl = sorted(fd3.items(), key=lambda item: item[1], reverse=True)
# 计算倍数
result_b = vocl[49][1]/vocl[149][1]
print(vocl[49][0]," ",vocl[149][0])
print("r_b="+str(result_b))
print(vocl[0]," ",vocl[149])
# 画图
b.plot(150)

# 27题

types = [('n', '名词'), ('v', '动词'), ('a', '形容词'), ('r', '副词')]
for type in types:
    # 获取指定 类型 所有同义词集
    synsets = wordnet.all_synsets(type[0])
    lemmas = []
    # 遍历 同义词集
    for s in synsets:
        # 遍历收集词条
        for lemma in s.lemmas():
            lemmas.append(lemma.name())
    # 去重
    lemmas = set(lemmas)
    print(type[1], '的词条有:', len(lemmas), '条')
    count = 0
    # 计算词条含义数
    for lemma in lemmas:
        count = count + len(wordnet.synsets(lemma, type[0]))
    print('词条的含义总数为:',count)
    print(type[1], '的平均多义性为：', count/ len(lemmas))
    print('------------------------------')
