# coding: utf-8
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import jieba

font = 'C:\Windows\Fonts\SIMHEI.ttf'
text = open('sourceData.txt', 'rb').read().decode('utf-8')

wordlist_after_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)

backgroud_Image = plt.imread('flower.jpg')

my_wordcloud = WordCloud(background_color='white',  # 设置背景颜色
                         mask=backgroud_Image,  # 设置背景图片
                         max_words=2000,  # 设置最大现实的字数
                         stopwords=STOPWORDS,  # 设置停用词
                         font_path=font,  # 设置字体格式，如不设置显示不了中文
                         max_font_size=50,  # 设置字体最大值
                         random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
                         ).generate(wl_space_split)
image_colors = ImageColorGenerator(backgroud_Image)
my_wordcloud.recolor(color_func=image_colors)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
