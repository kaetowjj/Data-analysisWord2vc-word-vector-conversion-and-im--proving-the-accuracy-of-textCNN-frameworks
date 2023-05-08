from gensim.models import word2vec
import logging
 
 
# 主程序
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
sentences =word2vec.Text8Corpus("cut\\comments\\all_comments.txt")  # 加载语料
model = word2vec.Word2Vec(sentences, size=200)  #训练skip-gram模型，默认window=5
 
print(model)

# 计算两个词的相似度/相关程度
try:
    y1 = model.similarity("疫情", "新冠")
except KeyError:
    y1 = 0
print("【疫情】和【新冠】的相似度为：", y1)
print("-----\n")
#
# 计算某个词的相关词列表
y2 = model.most_similar("疫情", topn=20)  # 20个最相关的
print("和【疫情】最相关的词有：\n")
for item in y2:
    print(item[0], item[1])
print("-----\n")
 
# 寻找对应关系
print("医护人员-加油，疫情-")
y3 =model.most_similar(['疫情', '加油'], ['医护人员'], topn=3)
for item in y3:
    print(item[0], item[1])
print("----\n")
 
# 寻找不合群的词
y4 =model.doesnt_match("医护人员 疫情 新冠 口罩".split())
print("不合群的词：", y4)
print("-----\n")
 
# 保存模型，以便重用
model.save("model\\all_comments.model")
# 对应的加载方式
# model_2 =word2vec.Word2Vec.load("xxx.model")
 
# 以一种c语言可以解析的形式存储词向量
#model.save_word2vec_format("comments_2".model.bin", binary=True)
# 对应的加载方式
# model_3 =word2vec.Word2Vec.load_word2vec_format("xxx.model.bin",binary=True)
