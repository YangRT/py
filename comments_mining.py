import matplotlib
import re
import pandas
from matplotlib import pyplot


# 手机特征分析
def mining():
    features = ['屏幕', '客服', '外观', '待机时间', '降价', '电池', '系统','音效','耳机','速度',
                '拍照','快递','曲面','手感','功能','赠品','颜色','视频','游戏','性价比']
    comments = []
    comments_dic = []
    # 获取评论
    df = pandas.read_csv('Data_Product_Comment.csv', encoding='gbk')
    df.drop_duplicates()
    for index, row in df.iterrows():
        comment = {}
        row[0] = re.sub('\\n', "", row[0])
        comment['comment'] = row[0]
        comment['score'] = row[1]
        comments_dic.append(comment)
        comments.append(row[0])
    print(comments_dic[:20])
    features_data = []
    # 量化特征
    for j in range(len(features)):
        features_count = {}
        features_count['word'] = features[j]
        for i in range(len(comments_dic)):
            if features[j] in comments_dic[i]['comment']:
                features_count['total'] = features_count.get('total', 0) + 1
                if comments_dic[i]['score'] > 3:
                    features_count['good'] = features_count.get('good', 0) + 1
                if 1< comments_dic[i]['score'] < 4:
                    features_count['general'] = features_count.get('general', 0) + 1
                if comments_dic[i]['score'] == 1:
                    features_count['low'] = features_count.get('low', 0) + 1
        features_data.append(features_count)
    for i in range(len(features_data)):
        print(features_data[i])
    return features_data


# 画饼状图
def paint(data):
    font = {'family': 'MicroSoft Yahei',
            'weight': 'light',
            'size': 8}
    matplotlib.rc("font", **font)
    labels = ['good','general','low']
    sizes = [data['good'],data['general'],data['low']]
    pyplot.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150)
    pyplot.title("饼图示例- \'"+data['word']+'\' 评论占比')
    pyplot.show()


if __name__ == '__main__':
    # 特征分析
    data = mining()
    # 画饼状图
    for i in range(len(data)):
        paint(data[i])
    # 打印结果
    for i in range(len(data)):
        print(data[i]['word'], '   ', data[i]['total'], '   ', data[i]['good'], '     ', data[i]['general'], '   ', data[i]['low'], '    ',data[i]['good']/data[i]['total'] )