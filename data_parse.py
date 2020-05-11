import pandas as pd
import jieba
from gensim import corpora,models
import gensim
import re


# 获取停用词
def stopwords_list(file_path):
    stopwords = [line.strip() for line in open(file_path, 'r', encoding='gbk').readlines()]
    return stopwords


# 分词
def participle(word_list):
    sentences = []
    stopwords = stopwords_list('chineseStopWords.txt')
    # 把一些无关词也进行筛选
    common_words = ['手机', '华为', '喜欢', '特别', '不错', 'hellip', '感觉', '京东', '不好', '500']
    for line in word_list:
        try:
            segs = jieba.lcut(line)
            segs = list(filter(lambda x: len(x) > 1, segs))
            segs = list(filter(lambda x: x not in stopwords, segs))
            segs = list(filter(lambda x: x not in common_words, segs))
            if segs:
                sentences.append(segs)
        except Exception:
            print(line)
            continue
    return sentences


def build_model(sentences):
    dictionary = corpora.Dictionary(sentences)
    corpus = [dictionary.doc2bow(sentence) for sentence in sentences]

    # 基于词袋模型的LDA建模
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=20)  # 最多使用20个关键词表示
    for topic in lda.print_topics(num_topics=3, num_words=10):  # 查看前3个主题，以10个关键字表示
        print(topic)


def build_tfidf_model(sentences):
    dictionary = corpora.Dictionary(sentences)
    corpus = [dictionary.doc2bow(sentence) for sentence in sentences]
    # TF-IDF
    tfidf_model = models.TfidfModel(corpus)
    corpus_tfidf = tfidf_model[corpus]

    # 基于TF-IDF的LDA建模
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=20)  # 最多使用20个关键词表示
    for topic in lda.print_topics(num_topics=3, num_words=10):  # 查看前3个主题，以10个关键字表示
        print(topic)


if __name__ == '__main__':
    # 存储不同评论
    comments = []
    good_list = []
    general_list = []
    low_list = []

    df = pd.read_csv('Data_Product_Comment.csv', encoding='gbk')
    df.drop_duplicates()
    for index, row in df.iterrows():
        row[0] = re.sub('\\n', "", row[0])
        comments.append(row[0])
        if row[1] > 3:
            good_list.append(row[0])
            continue
        if 1 < row[1] < 4:
            general_list.append(row[0])
            continue
        if row[1] == 1:
            low_list.append(row[0])

    # 分词后建模
    comments = participle(comments)
    build_model(comments)
    print('-------------')
    build_tfidf_model(comments)
    good_list = participle(good_list)
    general_list = participle(general_list)
    low_list = participle(low_list)

    build_model(good_list)
    print("---------")
    build_tfidf_model(good_list)
    build_model(general_list)
    print("---------")
    build_tfidf_model(general_list)
    build_model(low_list)
    print("---------")
    build_tfidf_model(low_list)


