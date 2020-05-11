import re
import pandas
import jieba
import numpy


# 读取数据
def read_text():
    with open('news.txt') as file_object:
        contents = file_object.read()
    sentences = re.split('[。]', contents)
    for i in range(len(sentences)):
        # 去除标点符号及数字
        sentences[i] = re.sub(r"[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+", "", sentences[i])
    return sentences


# 分词
def participle(data):
    for i in range(len(data)):
        data[i] = jieba.lcut(data[i])
    return data


# 构建词字典
def build_dic(data):
    word_dic = {}  # 把所有词语的列表转化为字典
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in word_dic.keys():
                word_dic[data[i][j]] += 1
            else:
                word_dic[data[i][j]] = 1
    return word_dic


# 选取词频超过2的词构建矩阵
def get_set_key(word_dic, threshold):
    wf = {k: v for k, v in word_dic.items() if threshold <= v}
    set_key_list = []
    for a in sorted(wf.items(), key=lambda item: item[1], reverse=True):
        set_key_list.append(a[0])  # 把排序的关键词语写入集合当中
    return set_key_list


#  处理需要计算的数据
def format_data(data, set_key_list):
    final_data = []  # 存储所有句子的列表，没有重复词语
    for i in range(len(data)):
        temp = []
        for j in range(len(data[i])): # 筛选出format_data中属于关键词集合的词语
            if data[i][j] in set_key_list:
                temp.append(data[i][j])
        data[i] = temp
        data[i] = list(set(filter(lambda x: x!='',data[i]))) # 去重
        final_data.append(data[i])
    return final_data


# 建立矩阵,并初始化
def build_matrix(set_key_list):
    edge = len(set_key_list)+1
    matrix = [[0 for j in range(edge)] for i in range(edge)]
    matrix[0][1:] = numpy.array(set_key_list)
    for i in range(1,len(set_key_list)+1):
        matrix[i][0] = set_key_list[i-1]
    return matrix


# 构建共现矩阵
def calculate(matrix, final_data):
    keywordlist = matrix[0][1:]                 # 列出所有关键词
    print(keywordlist)
    appeardict={}                             # 每个关键词与[出现在的行(final_data)的list] 组成的dictionary
    for w in keywordlist:
        appearlist = []
        i = 0
        for each_line in final_data:       # final_data每条数据组成的列表,遍历每一条数据
            if w in each_line:
                appearlist.append(i)
            i += 1
        appeardict[w] = appearlist             # 关键词列表中的每个词出现在哪些文本中

    for column in range(1, len(matrix)):        # 遍历矩阵第一行，跳过下标为0的元素
        for row in range(1, len(matrix)):    # 遍历矩阵第一列，跳过下标为0的元素
            if row >= column:                   # 仅计算上半个矩阵
                if matrix[0][column] == matrix[row][0]:        # 如果取出的行关键词和取出的列关键词相同，则其对应的共现次数为0，即矩阵对角线为0
                    matrix[row][column] = str(0)
                else:
                    # 计算两个集合共现的次数
                    counter = len(list((set(appeardict[matrix[0][column]]).union(set(appeardict[matrix[row][0]])))^(set(appeardict[matrix[0][column]])^set(appeardict[matrix[row][0]]))))
                    if counter == 0:
                        matrix[row][column] = 0
                    else:
                        matrix[row][column] = counter
                        #matrix[row][column] = str(math.log2((counter*8)/word_dic[matrix[0][column]]/word_dic[matrix[row][0]]))

            else:
                matrix[row][column] = 0
    return matrix


# 计算互信息
def count(word_dic,word_list,word_matrix):
    sum = 0
    word_num = []
    result = []
    # 计算词总数 各词出现次数
    for i in range(len(word_list)):
        word_num.append(word_dic[word_list[i]])
        sum += word_num[i]
    # 计算互信息
    for i in range(len(word_list)-1):
        for j in range(i+1,len(word_list)):
            # 以字典形式存储
            dic = {}
            dic['word1'] = word_list[i]
            dic['word2'] = word_list[j]
            dic['result'] = word_matrix[j+1][i+1]*sum/(word_num[i]*word_num[j])
            result.append(dic)
    # 将结果排序
    result.sort(key=lambda k: (k.get('result',0)),reverse=True)
    # # 写入文件
    # with open("result.txt", "w", encoding='utf-8') as f:
    #     for i in result:
    #         f.write(str(i)+'\n')
    print(result[0:10])


if __name__ == '__main__':
    # 获取文本 分句
    text = read_text()
    # 分词
    words = participle(text)
    # 构建词字典
    words_dic = build_dic(words)
    #  选择出现次数超过 2 的词
    matrix_list = get_set_key(words_dic,2)
    #  处理数据，删除部分词
    words_list = format_data(words,matrix_list)
    # 构建共现矩阵
    matrix_result = build_matrix(matrix_list)
    # 计算共现次数
    matrix_result = calculate(matrix_result,words_list)
    df = pandas.DataFrame(matrix_result)
    # # 将矩阵输出为 csv 文件
    # df.to_csv('C:/Users/Administrator/Desktop/a.csv', header=None, encoding='utf-8_sig', index=None)
    # 计算互信息
    count(words_dic,matrix_list,matrix_result)
