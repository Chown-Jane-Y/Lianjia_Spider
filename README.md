# [量锐科技笔试题]链家数据爬取与简单分析

[toc]

## 数据采集

### 技术选择
方案：Scarpy + BeautifulSoup + Selenium + Mysql

### 数据表定义
本次一共采集了20个字段，`Item`定义如下图所示：
![img1](./1492261324302.png)




















### 动态数据

因为经纬度调用的是百度地图API，涉及到动态数据，所以把Selenium和Scrapy结合，作为中间件，`middlewares`定义如下：
![Markdown](http://i1.piimg.com/588729/88f39e9ff0d04af9.png)












## 数据分析

### 技术选择

**pandas + matplotlib**

### 房源关键词分析


用结巴分词和`wordcloud`对房源的标题进行分析
![Markdown](http://i1.piimg.com/588729/7d4f30672bddec0c.png)






















生成词云如下：
![Markdown](http://i1.piimg.com/588729/b90bd42413c50ca5.png)






















可以看到楼层、真实度、交通等高频词汇，能一定程度体现用户找房时关注的点。




### 地图上的房源分布

(注：由于时间关系，以下**地图热力图**都是在BDP个人版进行分析)
![Markdown](http://i1.piimg.com/588729/8cab363595712a09.png)
















将地图放大一些：

![Markdown](http://i1.piimg.com/588729/faba4824e8ef4d4c.png)
















和预想中一样，房源主要集中**徐汇区、长宁区、闵行区和浦东新区**。

自己用程序验证一下（**这里使用的是pandas进行数据统计，matplotlib进行绘图**）：
![Markdown](http://i1.piimg.com/588729/4e32e14004dc5855.png)

















可以看到，房源最多的三个区分别是**浦东、闵行、徐汇**。



### 户型分布

![Markdown](http://i1.piimg.com/588729/561587bc9c336241.png)















1室1厅、2室1厅、2室2厅、3室2厅是最多的户型。可以推测用户需求，1-3个房间、1-2个厅为宜，房间过多或者没有客厅都是没有市场的。


### 住房面积分布

![Markdown](http://i1.piimg.com/588729/ed50ead64eeb6d94.png)




















50-100平米的住房最多，其次是100-150平米，满足绝大多数老百姓需求。


### 租房价格分布

根据租金绘制的热力图：
![Markdown](http://i1.piimg.com/588729/7fbe86f9c0d4cba8.png)























颜色越深，说明房价越高。与现实情况一样，越靠近市中心，租房价格越高。图中有两个大红色，是全图中价格最高的两块地方。于是放大看一看，到底是什么地方。

一个是**闵行区的名都古北住宅区**：
![Markdown](http://i1.piimg.com/588729/5d5b39810d826997.png)











一个是黄浦江边的江景房**世茂滨江花园**，这应该是上海地区价格最高的地儿了：
![Markdown](http://i1.piimg.com/588729/4f9f1f39605af0e5.png)






























### 根据建造年份分布
![Markdown](http://i1.piimg.com/588729/9dcdc5a9d01bd068.png)












颜色越深的代表年代越新，也是市中心的新建楼盘更多。




### 房价租金比

房价租金比，是指“每平方米”的房价与每平方米的“月租金”之间的比值，大致反映了房屋以出租方式取得的投资回报。一般情况下，若要满足5%-6%的投资回报要求，房价租金的比值为196-232，**如果房价租金比超过300，说明该区域房产投资价值变小，房价高估，也就意味着房地产泡沫严重；如果低于200，说明该区域投资潜力较大，房价泡沫不大。**

**计算公式：房价租金比=商品房市价总值/该房出租月收入**

![Markdown](http://i1.piimg.com/588729/0afa9da014d61b20.png)
 
















市中心普遍房价租金比更高，而且经过计算，上海所有地区的平均房价租金比高达989，貌似房价泡沫很大呀（不懂房地产和经济，只是根据概念自娱自乐）。



## 结语

因为水平有限与时间紧迫，这次只做了很简单的分析。由于之前只接触过爬虫，而对于采集的数据没有真正利用起来。通过这次笔试题才第一次接触到一些数据分析的基础知识以及工具，觉得甚是有趣。而且在爬虫的设计上面也有很大的缺陷，比如遇到网络故障不能从断点续爬，没有采取分布式，导致采集速度比较缓慢。深知关于Python和数据挖掘与分析这方面，自己还有很多东西需要学习，就把这个小题目作为一个入口，不断地深入。