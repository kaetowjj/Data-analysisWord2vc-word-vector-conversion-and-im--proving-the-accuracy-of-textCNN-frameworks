import gensim
from gensim.models import word2vec


# 对.sava保存的模型的加载：
model = gensim.models.Word2Vec.load("model\\all_comments.model")


# 获取词向量
print("新冠的词向量是：")
print(model['新冠'])
print("\n")
print("疫情的词向量是：")
print(model['疫情'])
print("\n")
