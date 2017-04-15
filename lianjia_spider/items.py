# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    house_id = scrapy.Field()       # 房源编号
    title = scrapy.Field()          # 租房信息标题
    address = scrapy.Field()        # 地址
    district = scrapy.Field()       # 区
    community = scrapy.Field()      # 小区名字
    area = scrapy.Field()           # 面积
    details = scrapy.Field()        # 各房间面积
    room_type = scrapy.Field()      # 户型
    floor = scrapy.Field()          # 楼层
    direction = scrapy.Field()      # 房屋朝向
    subway_station = scrapy.Field() # 临近地铁站
    distance = scrapy.Field()       # 距地铁站距离
    built_year = scrapy.Field()     # 建造时间
    rental = scrapy.Field()         # 租金
    shelf_time = scrapy.Field()     # 上架时间
    seen_record = scrapy.Field()    # 看房记录
    img_url = scrapy.Field()        # 图片连接
    scratch_time = scrapy.Field()   # 抓取时间
    housing_price = scrapy.Field()  # 挂牌均价
    tel = scrapy.Field()            # 联系电话