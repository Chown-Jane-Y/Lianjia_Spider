# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    community = scrapy.Field()        # 小区名字
    rental = scrapy.Field()         # 租金
    distance = scrapy.Field()       # 距地铁站距离
    area = scrapy.Field()           # 面积
    room_num = scrapy.Field()       # 户型
    floor = scrapy.Field()          # 楼层
    direction = scrapy.Field()      # 房屋朝向
    build_year = scrapy.Field()     # 建造时间

    # district = scrapy.Field()       # 区
    # introduction = scrapy.Field()   # 介绍
    # seen_record = scrapy.Field()    # 看房记录
    # img_url = scrapy.Field()        # 图片连接
    # details = scrapy.Field()        # 各房间面积
    # scratch_time = scrapy.Field()   # 抓取时间