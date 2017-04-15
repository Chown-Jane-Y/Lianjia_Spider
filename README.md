# [量锐科技笔试题]链家数据爬取与简单分析


## 数据采集

### 技术选择
方案：Scarpy + BeautifulSoup + Selenium + Mysql

### 数据表定义
本次一共采集了20个字段，`Item`定义如下图所示：
![item](http://i1.piimg.com/588729/e57e9d0060a0669f.png)




















### 动态数据

因为经纬度调用的是百度地图API，涉及到动态数据，所以把Selenium和Scrapy结合，作为中间件，`middlewares`定义如下：
![selenium](http://i1.piimg.com/588729/88f39e9ff0d04af9.png)












## 数据分析

### 房源关键词分析

用结巴分词和`wordcloud`对房源的标题进行分析，生成词云

![wordcloud](http://i1.piimg.com/588729/b90bd42413c50ca5.png)

















可以从中大致了解用户找房所关注的点，比如楼层、真实度、交通等因素。




### 地铁距离与租房价格



### 
