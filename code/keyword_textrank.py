from jieba import analyse
textrank = analyse.textrank
 
text = open('cut\\comments\\all_comments.txt', 'rb').read()
# 基于textrank算法关键词提取
keywords = textrank(text, topK = 10, withWeight = True)
print('keywords by tfidf:')
for keyword, val in keywords:
    print(keyword + " " + str(val))
