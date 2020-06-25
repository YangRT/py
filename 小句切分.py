# -*- coding: utf-8 -*-
import re
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import  OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
import numpy as np
import collections

train_sentences = []
test_sentences = []
for i in range(1,26):
    if len(str(i)) == 2:
        with open("data/chtb_00" + str(i) + ".fid", 'r') as f:
            text = f.read()
            content = re.findall("<S .*?>((.|\n)*?)</S>", text)
            if i >= 21:
                for sentence in content[2:]:
                    sentence = str(sentence)
                    sentence = re.sub(r"[\\n\\t]", '', sentence)
                    test_sentences.append(sentence)
            else:
                for sentence in content[2:]:
                    sentence = str(sentence)
                    sentence = re.sub(r"[\\n\\t]", '', sentence)
                    train_sentences.append(sentence)
    else:
        with open("data/chtb_000" + str(i) + ".fid", 'r') as f:
            text = f.read()
            content = re.findall("<S .*?>((.|\n)*?)</S>", text)
        for sentence in content[2:]:
            sentence = str(sentence)
            sentence = re.sub(r"[\\n\\t]",'',sentence)
            train_sentences.append(sentence)

x_train = []
for train_sentence in train_sentences:
    Tuples = re.findall('([A-Z]+ [\u4e00-\u9fa5|，|。|、|“|”|（|）|—|《|》]+)',train_sentence)
    for i in range(len(Tuples)):
        if i == len(Tuples) - 1:
            break
        if Tuples[i+1].split(' ')[1] == ('，' or '：'):
            pos1 = Tuples[i].split(' ')[0]
            pos2 = Tuples[i+2].split(' ')[0]
        else:
            continue
        print(pos1," ",pos2)
        x_train.append([pos1,pos2])

x_test = []
for test_sentence in test_sentences:
    Tuples = re.findall('([A-Z]+ [\u4e00-\u9fa5|，|。|、|“|”|（|）|—|《|》]+)',test_sentence)
    for i in range(len(Tuples)):
        if i == len(Tuples) - 1:
            break
        if Tuples[i+1].split(' ')[1] == ('，' or '：'):
            pos1 = Tuples[i].split(' ')[0]
            pos2 = Tuples[i+2].split(' ')[0]
        else:
            continue
        x_test.append([pos1,pos2])


y_train = [1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,1,0,1,1,0,
           1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,0,0,0,1,1,0,1,0,1,0,1,0,0,1,1,1,0,0,
           1,0,1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,0,
           1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,
           1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,
           1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1,1,
           1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1]
y_test = [1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,
          1,0,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1]


#对词性进行one-hot编码
enc = OneHotEncoder()
enc.fit(x_train)
x_train = enc.transform(x_train).toarray()
x_test = enc.transform(x_test).toarray()

#贝叶斯准确率
print("贝叶斯模型：")
model = MultinomialNB()
accuracy = np.mean(cross_val_score(model, x_train, y_train, cv=10, scoring="accuracy"))
print("正确率", accuracy)
precision = np.mean(cross_val_score(model, x_train, y_train, cv=10, scoring="precision"))
print("精确率", precision)
recall = np.mean(cross_val_score(model, x_train, y_train, cv=10, scoring="recall"))
print("召回率", recall)
f1 = np.mean(cross_val_score(model, x_train, y_train, cv=10, scoring="f1"))
print("F1值", f1)

print("决策树模型：")
model = DecisionTreeClassifier()
accuracy = np.mean(cross_val_score(model, x_train, y_train, cv=10, scoring="accuracy"))
print("正确率", accuracy)
precision = np.mean(cross_val_score(model, x_train, y_train, cv=10, scoring="precision"))
print("精确率", precision)
recall = np.mean(cross_val_score(model, x_train, y_train, cv=10, scoring="recall"))
print("召回率", recall)
f1 = np.mean(cross_val_score(model, x_train, y_train, cv=10, scoring="f1"))
print("F1值", f1)

print("逻辑回归模型：")
model = LogisticRegression(penalty='l2', solver='liblinear')
accuracy = np.mean(cross_val_score(model, x_train, y_train, cv=10, scoring="accuracy"))
print("正确率", accuracy)
precision = np.mean(cross_val_score(model, x_train, y_train, cv=10, scoring="precision"))
print("精确率", precision)
recall = np.mean(cross_val_score(model, x_train, y_train, cv=10, scoring="recall"))
print("召回率", recall)
f1 = np.mean(cross_val_score(model, x_train, y_train, cv=10, scoring="f1"))
print("F1值", f1)