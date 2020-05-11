import requests
import json
import csv
import time


# 获取好评
def get_good(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/65.0.3325.181 Safari/537.36'}
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100004323294&' \
          'score=3&sortType=5&page=' + str(
        page) + '&pageSize=10&isShadowSku=0&rid=0&fold=1'
    res = requests.get(url, headers=headers)
    jd = json.loads(res.text.lstrip('fetchJSON_comment98vv12345(').rstrip(');'))
    com_list = jd['comments']
    comments = []
    for i in com_list:
        data = {'comments': i['content'], 'score': i['score'], 'creationTime': i['creationTime']}
        comments.append(data)
    print('评论数：' + str(len(comments)))
    # 写入文件
    with open('Data_Product_Comment.csv', 'a', newline='') as f:
        dict_writer = csv.DictWriter(f, fieldnames=['comments', 'score', 'creationTime'])
        try:
            dict_writer.writerows(comments)
        except EOFError as e:
            print(e)
            pass
    print(str(page) + ": finished")


# 获取中评
def get_mid(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100004323294&score=2&sortType=5&page=' + str(
        page) + '&pageSize=10&isShadowSku=0&rid=0&fold=1'
    res = requests.get(url, headers=headers)
    jd = json.loads(res.text.lstrip('fetchJSON_comment98vv12345(').rstrip(');'))
    com_list = jd['comments']
    comments = []
    for i in com_list:
        data = {'comments': i['content'], 'score': i['score'], 'creationTime': i['creationTime']}
        comments.append(data)
    print('评论数：' + str(len(comments)))
    # 写入文件
    with open('Data_Product_Comment.csv', 'a', newline='') as f:
        dict_writer = csv.DictWriter(f, fieldnames=['comments', 'score', 'creationTime'])
        try:
            dict_writer.writerows(comments)
        except EOFError as e:
            print(e)
            pass
    print(str(page) + ": finished")


# 获取差评
def get_low(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100004323294&score=1&sortType=5&page=' + str(
        page) + '&pageSize=10&isShadowSku=0&rid=0&fold=1'
    res = requests.get(url, headers=headers)
    jd = json.loads(res.text.lstrip('fetchJSON_comment98vv12345(').rstrip(');'))
    com_list = jd['comments']
    comments = []
    for i in com_list:
        data = {'comments': i['content'], 'score': i['score'], 'creationTime': i['creationTime']}
        comments.append(data)
    print('评论数：' + str(len(comments)))
    # 写入文件
    with open('Data_Product_Comment.csv', 'a', newline='') as f:
        dict_writer = csv.DictWriter(f, fieldnames=['comments', 'score', 'creationTime'])
        try:
            dict_writer.writerows(comments)
        except EOFError as e:
            print(e)
            pass
    print(str(page) + ": finished")


# 评论整体信息 如好评率，评论总数等
def total_information():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100004323294&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1'
    res = requests.get(url, headers=headers)
    jd = json.loads(res.text.lstrip('fetchJSON_comment98vv12345(').rstrip(');'))
    com = jd['productCommentSummary']
    print(type(com))
    com_sum = {'averageScore':com['averageScore'],'commentCount':com['commentCount'],'defaultGoodCount':com['defaultGoodCount'],'generalCount':com['generalCount'],'goodCount':com['goodCount'],'poorCount':com['poorCount'],'score1Count':com['score1Count'],'score2Count':com['score2Count'],'score3Count':com['score3Count'],'score4Count':com['score4Count'],'score5Count':com['score5Count']}
    with open('Data_Product.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['averageScore', 'commentCount', 'defaultGoodCount','generalCount','goodCount','poorCount','score1Count','score2Count','score3Count','score4Count','score5Count'])
        writer.writeheader()
        writer.writerow(com_sum)


if __name__ == '__main__':
    with open('Data_Product_Comment.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['comments','score','creationTime'])
        writer.writeheader()
    # 好评 中评 差评 各爬取 100 页
    for i in range(100):
        get_good(i)
        get_low(i)
        get_mid(i)
        if i % 500 == 0:
            time.sleep(1)
    total_information()
