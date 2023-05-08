# encoding=utf-8 
import  jieba

# jieba . enable_paddle () #启动paddle模式。0.40版之后开始支持，早期版本不支持
# strs = [ "我来到北京清华大学" , "乒乓球拍卖完了" , "中国科学技术大学" ]
#  for  str  in  strs :
#      seg_list  =  jieba . cut ( str , use_paddle = True ) #使用paddle模式
#     print ( "Paddle Mode: "  +  '/' . join ( list ( seg_list )))

seg_list  =  jieba . cut ( "加油武汉；希望更多的患者治愈出院！" , cut_all = True )
print ( "Full Mode: "  +  "/ " . join ( seg_list ))   #全模式

seg_list  =  jieba . cut ( "加油武汉；希望更多的患者治愈出院！" , cut_all = False )
print ( "Default Mode: "  +  "/ " . join ( seg_list ))   #精确模式

seg_list  =  jieba . cut ( "加油武汉；希望更多的患者治愈出院！" )   #默认是精确模式
print ( ", " . join ( seg_list ))

seg_list  =  jieba . cut_for_search ( "加油武汉；希望更多的患者治愈出院！" )   #搜索引擎模式
print ( ", " . join ( seg_list ))