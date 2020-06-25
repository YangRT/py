# encoding=utf-8
import codecs
import re
import nltk
import jieba
import codecs
from math import *
import numpy as np
from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from time import time

# step0:
# 读入中文停用词
s=codecs.open("chinese_stopwords.txt","r","GBK")
stopwords=s.read().split('\r\n')
print(stopwords[0:20])
s.close()

# step1:
# 打开文件并进行预处理
t0 = time()
f=codecs.open("199801.txt","r","GBK")
sentence_lines=f.readlines()
corpus=[]
for line in sentence_lines:
    sentence = ""
    words=line.split('  ')# ['学习/v','中国/n',...]
    for word in words: #word= '学习/v'
        wpos=word.split('/') # wpos= ['学习','v']
        if len(wpos)==2:
            w=wpos[0]
            pos = wpos[1]
            if w in stopwords:#这里可以补充去停用词操作
                continue
            if pos=='v' or pos=='n':
                sentence=sentence+w+" "
    re.sub(" ","",sentence)
    if len(sentence)>=1:
        corpus.append(sentence)
print(corpus[0:10])
f.close()
print("预处理所花的时间为：%0.3fs." % (time() - t0))

# step2:
# 使用sklearn中的tf,  TF-IDF向量化方法对该数据集中1000个句子建立文档词向量矩阵。
t0 = time()
n_features = 1000
myvectorizer=TfidfVectorizer(max_df=0.95,min_df=2,max_features=n_features,)
vectors=myvectorizer.fit_transform(corpus)
matrixs=vectors.toarray()
# print(matrixs)
data=np.array(matrixs)
print(data)
print("向量化所花的时间为：%0.3fs." % (time() - t0))


# step3:
# 使用LDA模型对文本进行主题建模
print("Fitting LDA models...")
n_components=10
lda = LatentDirichletAllocation(n_components=n_components, max_iter=5,
                                    learning_method='online',
                                    learning_offset=50.,
                                    random_state=0)
t0 = time()
lda.fit(data)
print("LDA建模时间为： %0.3fs." % (time() - t0))


# step4:打印所抽取出的主题的主题词
print("\nTopics in LDA model:")
feature_names = myvectorizer.get_feature_names()
n_top_words=50
for topic_idx, topic in enumerate(lda.components_):
    message = "Topic #%d: " % topic_idx
    message += " ".join([feature_names[i]
                            for i in topic.argsort()[:-n_top_words - 1:-1]])
    print(message)


