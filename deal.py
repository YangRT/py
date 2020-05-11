import json
import re


def read_json():
    num = 1

    f = open("data_10.json", encoding='utf-8')
    news = json.load(f)
    for i in range(len(news['news'])):
        with open("new_%d" % num + ".txt", "w", encoding='utf-8') as f:
            f.write(news['news'][i]['title']+ '\n')
            result = re.sub('\\r\\n', "", news['news'][i]['content'])
            result = re.sub('\\n',"",result)
            result = re.sub('\\t',"",result)
            result = result.strip()
            f.write(result)
        num = num + 1

    f2 = open("data_9.json", encoding='utf-8')
    news2 = json.load(f2)
    for i in range(len(news2['news'])):
        with open("new_%d" % num + ".txt", "w", encoding='utf-8') as f:
            f.write(news2['news'][i]['title']+ '\n')
            result = re.sub('\\r\\n', "", news2['news'][i]['content'])
            result = re.sub('\\n', "", result)
            result = re.sub('\\t', "", result)
            result = result.strip()
            f.write(result)
        num = num + 1

    f = open("data_8.json", encoding='utf-8')
    news = json.load(f)
    for i in range(len(news['news'])):
        with open("new_%d" % num + ".txt", "w", encoding='utf-8') as f:
            f.write(news['news'][i]['title'] + '\n')
            result = re.sub('\\r\\n', "", news['news'][i]['content'])
            result = re.sub('\\n', "", result)
            result = re.sub('\\t', "", result)
            result = result.strip()
            f.write(result)
        num = num + 1

    f2 = open("data_7.json", encoding='utf-8')
    news2 = json.load(f2)
    for i in range(len(news2['news'])):
        with open("new_%d" % num + ".txt", "w", encoding='utf-8') as f:
            f.write(news2['news'][i]['title'] + '\n')
            result = re.sub('\\r\\n', "", news2['news'][i]['content'])
            result = re.sub('\\n', "", result)
            result = re.sub('\\t', "", result)
            result = result.strip()
            f.write(result)
        num = num + 1

if __name__ == '__main__':
    read_json()