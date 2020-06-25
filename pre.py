import re
import numpy as np
import pandas as pd
import json
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer as TF
from sklearn.model_selection import cross_val_score
from sklearn.svm import LinearSVC
from sklearn.svm import SVC


def clean_text(origin_text):
    # 去掉html标签
    text = BeautifulSoup(origin_text,features="html.parser").get_text()
    # 去掉标点符号和非法字符
    text = re.sub("[^a-zA-Z]", " ", text)
    # 将字符全部转化为小写，并通过空格符进行分词处理
    words = text.lower().split()
    # 去停用词
    stop_words = set(stopwords.words("english"))
    meaningful_words = [w for w in words if w not in stop_words]
    # 将剩下的词还原成str类型
    cleaned_text = " ".join(meaningful_words)
    return cleaned_text


# 读取数据
f1 = open("IMDB/train.json", encoding='utf-8')
f2 = open("IMDB/test.json", encoding='utf-8')
train = json.load(f1)
test = json.load(f2)
print(train[0])
print(test[0])
# 评论清洗
train_df = []
test_df = []
for i in range(len(train)):
    t = clean_text(train[i]['review_text'])
    train_df.append(t)
for j in range(len(test)):
    t = clean_text(test[j]['review_text'])
    test_df.append(t)
print(train_df[0])
print(test_df[0])


# 读取标签
train_is = []
for i in range(len(train)):
    if train[i]['is_spoiler']:
        train_is.append(1)
    else:
        train_is.append(0)

train = []
test = []


tfidf = TF(
    analyzer="word",
    tokenizer=None,
    preprocessor=None,
    stop_words=None,
    max_features=200)

# 数据向量化
print("Creating the tfidf vector...\n")
tfidf.fit(train_df)
x_train = tfidf.transform(train_df)
x_train = x_train.toarray()

x_test = tfidf.transform(test_df)
x_test = x_test.toarray()

print(x_train.shape)
print(x_test.shape)

# 读取标签
y_train = train_is
# 线性
clf = LinearSVC(max_iter=5000)
clf.fit(x_train,y_train)


print("10折交叉验证：")
accuracy = np.mean(cross_val_score(clf, x_train, y_train, cv=10, scoring="accuracy"))
print("正确率：",accuracy)  # 0.7471582339500099
precision = np.mean(cross_val_score(clf, x_train, y_train, cv=10, scoring="precision"))
print("精确率：",precision)  # 0.6081359874173097
recall = np.mean(cross_val_score(clf, x_train, y_train, cv=10, scoring="recall"))
print("召回率：",recall)  # 0.10849976434177115
f1 = np.mean(cross_val_score(clf, x_train, y_train, cv=10, scoring="f1"))
print("F1分数：",f1)  # 0.18413581066117626
preds = clf.predict(x_test)
submission = pd.DataFrame({'id': range(len(preds)), 'pred': preds})
submission['id'] = submission['id']
submission.to_csv("submission.csv", index=False, header=False)
submission.head()

