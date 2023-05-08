import jieba.analyse
import  jieba
import  pandas as pd


#  去掉中英文状态下的逗号、句号
def clearSen(comment):
    comment = comment.strip(' ')
    comment = comment.replace('、','')
    comment = comment.replace('~','。')
    comment = comment.replace('～','')
    comment = comment.replace('…','')
    comment = comment.replace('\r', '')
    comment = comment.replace('\t', ' ')
    comment = comment.replace('\f', ' ')
    comment = comment.replace('/', '')
    comment = comment.replace('、', ' ')
    comment = comment.replace('/', '')
    comment = comment.replace(' ', '')
    comment = comment.replace(' ', '')
    comment = comment.replace('_', '')
    comment = comment.replace('?', ' ')
    comment = comment.replace('？', ' ')
    comment = comment.replace('了', '')
    comment = comment.replace('➕', '')
    comment = comment.replace('：', '')
    return comment


# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='UTF-8').readlines()]
    return stopwords


# 停用词list
# stopwords = pd.read_table('dict\\stopwords.txt',header = None).iloc[:,:].values
stopwords = stopwordslist('dict\\stopwords.txt')

# 加载要处理的文件的路径
fR=pd.read_table('comments\\comments.txt',sep=',',encoding='UTF-8',error_bad_lines=False).astype(str)

# 加载处理后的文件路径
fW = open('cut\\comments\\all_comments.txt', 'a+',encoding="UTF-8")

# 数据重命名
fR.columns=['content']


for word in fR['content']:
    # 清除标点符号
    kk = clearSen(word)
    # 精确模式切词
    seg_list = jieba.cut(kk)
    # 停用词过滤
    if word not in stopwords:
        if word != '\t':
            comment=" ".join(seg_list)
            print(comment)
    # 写出数据
    fW.write(comment + '\n')

# 关闭文件
fW.close()
