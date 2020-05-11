import re
from nltk.corpus import wordnet

# 第 38 题
# 1. 识别连字符连接的跨行处的词汇
pattern = '(.+?-\\n.+)'
# 测试
words = ["long-\nterm","hello","long-term"]
for i in words:
    res = re.findall(pattern,i)
    print(res)
# 2.使用re.sub()从这些词中删除\n字符
word = "long-\nterm"
final = re.sub(r'\n+','', word)
print(final)
# 3.确定换行符被删除后是否保留连字符
word_list = ['long-\nterm','encyclo-\npedia']
# 删除 换行
for i in range(len(word_list)):
    word_list[i] = re.sub(r'\n+','', word_list[i])
# 使用 wordNet 判断
for i in word_list:
    if not wordnet.synsets(i):
        # 不是英语单词 去除 -
        i = re.sub('-','',i)
    print(i)


# 第39题
def soundex(name, len=4):
    # 26个英文字母的映射
    digits = '01230120022455012623010202'
    result = ''
    first_char = ''
    # 将名字中的字母转换成soundex数字
    for c in name.upper():
        if c.isalpha():
            if not first_char:
                first_char = c  # 保存第一个字符
            d = digits[ord(c) - ord('A')]
            # 去重，重复连续数字保留一个
            if not result or (d != result[-1]):
                result += d
    print(result)
    # 第一个字母替换第一个数字
    result = first_char + result[1:]
    # 删除所有0
    result = result.replace('0', '')
    # 返回前4个字符，不足4位以0补足
    return (result + (len * '0'))[:len]


if __name__ == '__main__':
    print(soundex('sungzhaoheng'))
    print(soundex('sonzhaoheng'))