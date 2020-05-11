import matplotlib
from jieba import posseg
import re
import pandas
from matplotlib import pyplot


def auto_label(rects):
    for rect in rects:
        height = rect.get_height()
        pyplot.text(rect.get_x()+rect.get_width()/2 - 0.2, 1.03*height, '%s' % int(height))


#  所有评论名词
def find_all_n():
    comments = []
    df = pandas.read_csv('Data_Product_Comment.csv', encoding='gbk')
    df.drop_duplicates()
    for index, row in df.iterrows():
        row[0] = re.sub('\\n', "", row[0])
        comments.append(row[0])
    df = open("all_words", "w", encoding='utf-8')
    counts = {}
    for comment in comments:
        # 词性标注
        words = posseg.cut(comment)
        for i in words:
            # 词频统计
            if i.flag == "n":
                counts[i] = counts.get(i, 0) + 1
            df.write(str(i) + ' ')
        df.write('\n')
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    print(items[:20])
    word_list = []
    count_list = []
    for i in range(len(items)):
        word, pos = items[i][0]
        count = items[i][1]
        word_list.append(word)
        count_list.append(count)
        if i == 20:
            break
    font = {'family': 'MicroSoft Yahei',
            'weight': 'light',
            'size': 8}
    matplotlib.rc("font", **font)
    auto_label(pyplot.bar(range(len(count_list)), count_list, color='rgb', tick_label=word_list))
    pyplot.xticks(rotation=45)
    pyplot.title("高频名词")
    pyplot.ylabel("次数")
    pyplot.show()


#  好评名词
def find_good_n():
    comments = []
    df = pandas.read_csv('Data_Product_Comment.csv', encoding='gbk')
    df.drop_duplicates()
    for index, row in df.iterrows():
        if row[1] > 3:
            row[0] = re.sub('\\n', "", row[0])
            comments.append(row[0])
    df = open("good_words", "w", encoding='utf-8')
    counts = {}
    for comment in comments:
        # 词性标注
        words = posseg.cut(comment)
        for i in words:
            if i.flag == "n":
                # 词频统计
                counts[i] = counts.get(i, 0) + 1
            df.write(str(i) + ' ')
        df.write('\n')
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    print(items[:20])
    word_list = []
    count_list = []
    for i in range(len(items)):
        word, pos = items[i][0]
        count = items[i][1]
        word_list.append(word)
        count_list.append(count)
        if i == 20:
            break
    font = {'family': 'MicroSoft Yahei',
            'weight': 'light',
            'size': 8}
    matplotlib.rc("font", **font)
    auto_label(pyplot.bar(range(len(count_list)), count_list, color='rgb', tick_label=word_list))
    pyplot.xticks(rotation=45)
    pyplot.title("好评高频名词")
    pyplot.ylabel("次数")
    pyplot.show()


#  中评名词
def find_general_n():
    comments = []
    df = pandas.read_csv('Data_Product_Comment.csv', encoding='gbk')
    df.drop_duplicates()
    for index, row in df.iterrows():
        if 1 < row[1] < 4:
            row[0] = re.sub('\\n', "", row[0])
            comments.append(row[0])
    df = open("general_words", "w", encoding='utf-8')
    counts = {}
    for comment in comments:
        # 词性标注
        words = posseg.cut(comment)
        for i in words:
            # 词频统计
            if i.flag == "n":
                counts[i] = counts.get(i, 0) + 1
            df.write(str(i) + ' ')
        df.write('\n')
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    print(items[:20])
    word_list = []
    count_list = []
    for i in range(len(items)):
        word, pos = items[i][0]
        count = items[i][1]
        word_list.append(word)
        count_list.append(count)
        if i == 20:
            break
    font = {'family': 'MicroSoft Yahei',
            'weight': 'light',
            'size': 8}
    matplotlib.rc("font", **font)
    auto_label(pyplot.bar(range(len(count_list)), count_list, color='rgb', tick_label=word_list))
    pyplot.xticks(rotation=45)
    pyplot.title("中评高频名词")
    pyplot.ylabel("次数")
    pyplot.show()


#  差评名词
def find_low_n():
    comments = []
    df = pandas.read_csv('Data_Product_Comment.csv', encoding='gbk')
    df.drop_duplicates()
    for index, row in df.iterrows():
        if row[1] == 1:
            row[0] = re.sub('\\n', "", row[0])
            comments.append(row[0])
    df = open("low_words", "w", encoding='utf-8')
    counts = {}
    for comment in comments:
        # 词性标注
        words = posseg.cut(comment)
        for i in words:
            # 词频统计
            if i.flag == "n":
                counts[i] = counts.get(i, 0) + 1
            df.write(str(i) + ' ')
        df.write('\n')
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    print(items[:20])
    word_list = []
    count_list = []
    for i in range(len(items)):
        word, pos = items[i][0]
        count = items[i][1]
        word_list.append(word)
        count_list.append(count)
        if i == 20:
            break
    font = {'family': 'MicroSoft Yahei',
            'weight': 'light',
            'size': 8}
    matplotlib.rc("font", **font)
    auto_label(pyplot.bar(range(len(count_list)), count_list, color='rgb', tick_label=word_list))
    pyplot.xticks(rotation=45)
    pyplot.title("差评高频名词")
    pyplot.ylabel("次数")
    pyplot.show()


# 所有评论形容词
def find_all_a():
    comments = []
    df = pandas.read_csv('Data_Product_Comment.csv', encoding='gbk')
    df.drop_duplicates()
    for index, row in df.iterrows():
        row[0] = re.sub('\\n', "", row[0])
        comments.append(row[0])
    counts = {}
    for comment in comments:
        # 词性标注
        words = posseg.cut(comment)
        for i in words:
            if i.flag == "a":
                # 词频统计
                counts[i] = counts.get(i, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    print(items[:20])
    word_list = []
    count_list = []
    for i in range(len(items)):
        word, pos = items[i][0]
        count = items[i][1]
        word_list.append(word)
        count_list.append(count)
        if i == 20:
            break
    font = {'family': 'MicroSoft Yahei',
            'weight': 'light',
            'size': 8}
    matplotlib.rc("font", **font)
    auto_label(pyplot.bar(range(len(count_list)), count_list, color='rgb', tick_label=word_list))
    pyplot.xticks(rotation=45)
    pyplot.title("高频形容词")
    pyplot.ylabel("次数")
    pyplot.show()


# 好评形容词
def find_good_a():
    comments = []
    df = pandas.read_csv('Data_Product_Comment.csv', encoding='gbk')
    df.drop_duplicates()
    for index, row in df.iterrows():
        if row[1] > 3:
            row[0] = re.sub('\\n', "", row[0])
            comments.append(row[0])
    counts = {}
    for comment in comments:
        # 词性标注
        words = posseg.cut(comment)
        for i in words:
            # 词频统计
            if i.flag == "a":
                counts[i] = counts.get(i, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    print(items[:20])
    word_list = []
    count_list = []
    for i in range(len(items)):
        word, pos = items[i][0]
        count = items[i][1]
        word_list.append(word)
        count_list.append(count)
        if i == 20:
            break
    font = {'family': 'MicroSoft Yahei',
            'weight': 'light',
            'size': 8}
    matplotlib.rc("font", **font)
    auto_label(pyplot.bar(range(len(count_list)), count_list, color='rgb', tick_label=word_list))
    pyplot.xticks(rotation=45)
    pyplot.title("好评高频形容词")
    pyplot.ylabel("次数")
    pyplot.show()


# 中评形容词
def find_general_a():
    comments = []
    df = pandas.read_csv('Data_Product_Comment.csv', encoding='gbk')
    df.drop_duplicates()
    for index, row in df.iterrows():
        if 1 < row[1] < 4:
            row[0] = re.sub('\\n', "", row[0])
            comments.append(row[0])
    counts = {}
    for comment in comments:
        # 词性标注
        words = posseg.cut(comment)
        for i in words:
            if i.flag == "a":
                # 词频统计
                counts[i] = counts.get(i, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    print(items[:20])
    word_list = []
    count_list = []
    for i in range(len(items)):
        word, pos = items[i][0]
        count = items[i][1]
        word_list.append(word)
        count_list.append(count)
        if i == 20:
            break
    font = {'family': 'MicroSoft Yahei',
            'weight': 'light',
            'size': 8}
    matplotlib.rc("font", **font)
    auto_label(pyplot.bar(range(len(count_list)), count_list, color='rgb', tick_label=word_list))
    pyplot.xticks(rotation=45)
    pyplot.title("中评高频形容词")
    pyplot.ylabel("次数")
    pyplot.show()


# 差评形容词
def find_low_a():
    comments = []
    df = pandas.read_csv('Data_Product_Comment.csv', encoding='gbk')
    df.drop_duplicates()
    for index, row in df.iterrows():
        if row[1] == 1:
            row[0] = re.sub('\\n', "", row[0])
            comments.append(row[0])
    counts = {}
    for comment in comments:
        # 词性标注
        words = posseg.cut(comment)
        for i in words:
            if i.flag == "a":
                # 词频统计
                counts[i] = counts.get(i, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    print(items[:20])
    word_list = []
    count_list = []
    for i in range(len(items)):
        word, pos = items[i][0]
        count = items[i][1]
        word_list.append(word)
        count_list.append(count)
        if i == 20:
            break
    font = {'family': 'MicroSoft Yahei',
            'weight': 'light',
            'size': 8}
    matplotlib.rc("font", **font)
    auto_label(pyplot.bar(range(len(count_list)), count_list, color='rgb', tick_label=word_list))
    pyplot.xticks(rotation=45)
    pyplot.title("差评高频形容词")
    pyplot.ylabel("次数")
    pyplot.show()


if __name__ == '__main__':
    # 对不同评论进行词性标注，统计词频，柱状图表示
    find_good_n()
    find_general_n()
    find_low_n()
    find_good_a()
    find_general_a()
    find_low_a()
    find_all_a()
    find_all_n()