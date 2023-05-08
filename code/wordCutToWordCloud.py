#分词
import jieba
import numpy
from PIL import Image
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from wordcloud import WordCloud
from wordcloud.wordcloud import colormap_color_func


#定义一个空字符串
final = ""
#文件夹位置
filename = r"cut\\comments\\all_comments_keywords.txt"

color_mask = numpy.array(Image.open('weiboicon.png'))#词云形状
colormaps = colors.ListedColormap(['#E6162D','#FF9933'])#字体颜色

#打开文件夹，读取内容，并进行分词
with open(filename,'r',encoding = 'UTF-8') as f:
    for line in f.readlines():
        word = jieba.cut(line)
        for i in word:
            final = final + i +" "

word_pic = WordCloud(font_path = r'C:\Windows\Fonts\simkai.ttf',width = 1920,height = 1080,max_words=1000,background_color=(255,255,255),scale=20,mask=color_mask, colormap=colormaps).generate(final)
plt.imshow(word_pic)
#去掉坐标轴
plt.axis('off')
#保存图片到相应文件夹
plt.savefig(r'pic\\comments\\comments_background.png')


