from wordcloud import WordCloud
import pandas
import re
import jieba
import jieba.analyse
from collections import Counter
import matplotlib.pyplot as plt


# 获取评论
def get_comment():
    df = pandas.read_csv('Data_Product_Comment.csv', encoding='gbk', index_col=False)
    df.drop_duplicates()
    comments = list(df['comments'])
    for i in range(len(comments)):
        comments[i] = re.sub('\\n', "", comments[i])
    return comments


# 获取好评
def get_good_comments():
    comments = []
    df = pandas.read_csv('Data_Product_Comment.csv', encoding='gbk')
    df.drop_duplicates()
    for index, row in df.iterrows():
        if row[1] > 3:
            row[0] = re.sub('\\n', "", row[0])
            comments.append(row[0])
    return comments


# 获取中评
def get_general_comments():
    comments = []
    df = pandas.read_csv('Data_Product_Comment.csv', encoding='gbk')
    df.drop_duplicates()
    for index, row in df.iterrows():
        if 1 < row[1] < 4:
            row[0] = re.sub('\\n', "", row[0])
            comments.append(row[0])
    return comments


# 获取差评
def get_low_comments():
    comments = []
    df = pandas.read_csv('Data_Product_Comment.csv', encoding='gbk')
    df.drop_duplicates()
    for index, row in df.iterrows():
        if row[1] == 1:
            row[0] = re.sub('\\n', "", row[0])
            comments.append(row[0])
    return comments


# 获取停用词
def stopwords_list(file_path):
    stopwords = [line.strip() for line in open(file_path, 'r', encoding='gbk').readlines()]
    return stopwords


# 分词
def participle(data):
    sentence_data = jieba.cut(data.strip())
    stopwords = stopwords_list('chineseStopWords.txt')  # 这里加载停用词的路径
    out_str = ''
    for word in sentence_data:
        if word not in stopwords:
            if word != '\t' and word != 'hellip' and bool(1-word.isdigit()):
                out_str += word
                out_str += " "
    return out_str


# 词频统计
def count_words(file_name, from_file):
    with open(from_file, 'r', encoding='utf-8') as f:
        data = jieba.cut(f.read())
    data = dict(Counter(data))
    data.pop(' ')
    data.pop('\n')
    print(data)
    with open(file_name, 'a', encoding='utf-8') as fw:  # 读入存储wordcount的文件路径
        for k, v in data.items():
            fw.write('%s, %d\n' % (k, v))


# 生成词云
def words_cloud(file_name):
    with open(file_name, encoding='utf-8') as f:
        data = f.read()
        keyword = jieba.analyse.extract_tags(data, topK=100, withWeight=False)
        keyword2 = jieba.analyse.textrank(data, withWeight=True)
        i = 0
        for item in keyword2:
            i = i + 1
            print(item[0], item[1], end=' ')
            if i % 3 == 0:
                i = 0
                print("")
        wl = " ".join(keyword)
        # 设置词云
        wc = WordCloud(
            background_color="white",
            max_words=2000,
            height=1200,
            font_path='C:/Windows/Fonts/simfang.ttf',
            width=1600,
            max_font_size=500,
            random_state=30,
        )
        my_word = wc.generate(wl)  # 生成词云
        # 展示词云图
        plt.imshow(my_word)
        plt.axis("off")
        plt.colorbar()
        plt.show()


# 形容词词云
def words_cloud2(file_name):
    with open(file_name, encoding='utf-8') as f:
        data = f.read()
        keyword = jieba.analyse.extract_tags(data, topK=100, withWeight=False, allowPOS='a')
        keyword2 = jieba.analyse.textrank(data, withWeight=True, allowPOS='a')
        i = 0
        for item in keyword2:
            i = i + 1
            print(item[0], item[1], end='')
            if i % 3 == 0:
                i = 0
                print("")
        wl = " ".join(keyword)
        # 设置词云
        wc = WordCloud(
            background_color="white",
            max_words=2000,
            height=1200,
            font_path='C:/Windows/Fonts/simfang.ttf',
            width=1600,
            max_font_size=500,
            random_state=30,
        )
        my_word = wc.generate(wl)  # 生成词云
        # 展示词云图
        plt.imshow(my_word)
        plt.axis("off")
        plt.colorbar()
        plt.show()


# 名词词云
def words_cloud3(file_name):
    with open(file_name, encoding='utf-8') as f:
        data = f.read()
        keyword = jieba.analyse.extract_tags(data, topK=100, withWeight=False, allowPOS='n')
        keyword2 = jieba.analyse.textrank(data, withWeight=True, allowPOS='n')
        i = 0
        for item in keyword2:
            i = i + 1
            print(item[0], item[1], end='')
            if i % 3 == 0:
                i = 0
                print("")
        wl = " ".join(keyword)
        # 设置词云
        wc = WordCloud(
            background_color="white",
            max_words=2000,
            height=1200,
            font_path='C:/Windows/Fonts/simfang.ttf',
            width=1600,
            max_font_size=500,
            random_state=30,
        )
        my_word = wc.generate(wl)  # 生成词云
        # 展示词云图
        plt.imshow(my_word)
        plt.axis("off")
        plt.colorbar()
        plt.show()


# 处理所有评论
def dispose_all_comments():
    f = open('comments_participle.txt', mode='a', encoding='utf-8')
    # 获取评论
    comments_data = get_comment()
    # 分词
    for i in comments_data:
        result = participle(i)
        f.write(result + '\n')
    f.close()
    # 词频统计，词云展示
    count_words('words_count.txt', 'comments_participle.txt')
    words_cloud('comments_participle.txt')
    words_cloud2('comments_participle.txt')
    words_cloud3('comments_participle.txt')


# 处理好评
def dispose_good_comments():
    f = open('good_comments_participle.txt', mode='a', encoding='utf-8')
    # 获取评论
    good_comments_data = get_good_comments()
    # 分词
    for i in good_comments_data:
        result = participle(i)
        f.write(result+'\n')
    f.close()
    # 词频统计，词云展示
    count_words('good_words_count.txt', 'good_comments_participle.txt')
    words_cloud('good_comments_participle.txt')
    words_cloud2('good_comments_participle.txt')
    words_cloud3('good_comments_participle.txt')


# 处理中评
def dispose_general_comments():
    f = open('general_comments_participle.txt', mode='a', encoding='utf-8')
    # 获取评论
    general_comments_data = get_general_comments()
    # 分词
    for i in general_comments_data:
        result = participle(i)
        f.write(result + '\n')
    f.close()
    # 词频统计，词云展示
    count_words('general_words_count.txt', 'general_comments_participle.txt')
    words_cloud('general_comments_participle.txt')
    words_cloud2('general_comments_participle.txt')
    words_cloud3('general_comments_participle.txt')


# 处理差评
def dispose_low_comments():
    f = open('low_comments_participle.txt', mode='a', encoding='utf-8')
    # 获取评论
    low_comments_data = get_low_comments()
    # 分词
    for i in low_comments_data:
        result = participle(i)
        f.write(result + '\n')
    f.close()
    # 词频统计，词云展示
    count_words('low_words_count.txt', 'low_comments_participle.txt')
    words_cloud('low_comments_participle.txt')
    words_cloud2('low_comments_participle.txt')
    words_cloud3('low_comments_participle.txt')


if __name__ == '__main__':
    # 对不同评论进行关键词提取并词云展示
    dispose_all_comments()
    dispose_good_comments()
    dispose_general_comments()
    dispose_low_comments()
