import requests
import re
import json


def req(url):
    # 获取 HTML
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    return r.text


def find(article):
    result = []
    # 获取新闻列表中各新闻 链接，标题，时间
    link = re.findall('<li id="line_u3_.*?\"><a href=\"(.*?)\" target', article)
    titles = re.findall('<li id="line_u3_.*?\"><a href=\".*?\" target="_blank" title="(.*?)"', article)
    times = re.findall(
        '<li id="line_u3_.*?\"><a href=\".*?\" target="_blank" title=".*?">.*?</a><span>(.*?)</span></li>', article)
    # 将每个新闻信息存储为字典形式 加入列表中
    for i in range(len(link)):
        dic = {'link': link[i], 'title': titles[i], 'time': times[i], 'content': ""}
        result.append(dic)
    return result


def get_data(url):
    # 获取新闻内容
    xml = req(url)
    content = re.findall('<div class="v_news_content">([\s\S]*?)</div>', xml)
    # 列表有某些新闻为公众号文章，需适配
    if len(content) > 0:
        content = re.sub('<.*?>', "", content[0])
        content = re.sub('&nbsp;', "", content)
        content.replace('\n', '').replace('\r', '')
    else:
        content = re.findall('<div class="rich_media_content " id="js_content" style="visibility: hidden;">([\s\S]*?)</div>', xml)
        content = re.sub('<.*?>', "", content[0])
        content.replace('\n', '').replace('\r', '')
    return content


def to_json(data,name):
    # 生成 json文件
    with open(name+".json", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


if __name__ == '__main__':
    # 获取 新闻列表 网页HTML
    r = req("https://yqzt.gdufs.edu.cn/xxbs.htm")
    # 获取新闻列表中各新闻 链接，标题，时间
    # 每个新闻以字典形式保存 最后返回字典列表
    results = find(r)
    print(len(results))
    # 循环访问新闻列表中新闻页面
    for i in range(len(results)):
        print(results[i]['title'])
        # 获取新闻内容
        cont = get_data(results[i]['link'])
        # 将新闻内容赋值
        results[i]['content'] = cont
    # 构建 json
    info = {'news': results}
    # 创建 json 文件保存数据
    to_json(info,'data_10')

    print('------------------------------------------')
    r1 = req("https://yqzt.gdufs.edu.cn/xxbs/9.htm")
    results1 = find(r1)
    print(len(results1))
    for i in range(9,24):
        print(results1[i]['title'])
        # 获取新闻内容
        cont = get_data(results1[i]['link'])
        # 将新闻内容赋值
        results1[i]['content'] = cont
    # 构建 json
    info1 = {'news': results1[9:24]}
    # 创建 json 文件保存数据
    to_json(info1,'data_9')

    print('------------------------------------------')
    r2 = req("https://yqzt.gdufs.edu.cn/xxbs/8.htm")
    results2 = find(r2)
    print(len(results2))
    for i in range(9,24):
        print(results2[i]['title'])
        # 获取新闻内容
        cont = get_data(results2[i]['link'])
        # 将新闻内容赋值
        results2[i]['content'] = cont
    # 构建 json
    info2 = {'news': results2[9:24]}
    to_json(info2,'data_8')

    print('------------------------------------------')
    r3 = req("https://yqzt.gdufs.edu.cn/xxbs/7.htm")
    results3 = find(r3)
    print(len(results3))
    for i in range(9,24):
        print(results3[i]['title'])
        cont = get_data(results3[i]['link'])
        results3[i]['content'] = cont
    info3 = {'news': results3[9:24]}
    to_json(info3,'data_7')