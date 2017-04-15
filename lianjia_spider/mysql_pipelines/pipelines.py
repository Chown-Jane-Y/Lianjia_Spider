# -*- coding: utf-8 -*-
from .sql import Sql
from lianjia_spider.items import LianjiaSpiderItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


""" 初始化数据库表语句
DROP TABLE IF EXISTS `house_info`;
CREATE TABLE `house_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `house_id` varchar(12) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `district` varchar(20) DEFAULT NULL,
  `community` varchar(20) DEFAULT NULL,
  `area` varchar(10) DEFAULT NULL,
  `details` varchar(255) DEFAULT NULL,
  `room_type` varchar(10) DEFAULT NULL,
  `floor` varchar(10) DEFAULT NULL,
  `direction` varchar(10) DEFAULT NULL,
  `subway_station` varchar(20) DEFAULT NULL,
  `distance` varchar(6) DEFAULT NULL,
  `built_year` varchar(6) DEFAULT NULL,
  `rental` varchar(10) DEFAULT NULL,
  `shelf_time` varchar(20) DEFAULT NULL,
  `seen_record` varchar(6) DEFAULT NULL,
  `img_url` TEXT DEFAULT NULL,
  `scratch_time` varchar(40) DEFAULT NULL,
  `housing_price` varchar(10) DEFAULT NULL,
  `tel` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""


class LianjiaSpiderPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, LianjiaSpiderItem):
            house_id = item['house_id']
            ret = Sql.select_house_id(house_id)
            if ret[0] == 1:
                print(house_id + '该房源已经存在')
                pass
            else:
                house_id = item['house_id']
                title = item['title']
                address = item['address']
                room_type = item['room_type']
                area = item['area']
                floor = item['floor']
                direction = item['direction']
                district = item['district']
                shelf_time = item['shelf_time']
                community = item['community']
                subway_station = item['subway_station']
                distance = item['distance']
                rental = item['rental']
                seen_record = item['seen_record']
                details = item['details']
                img_url = item['img_url']
                housing_price = item['housing_price']
                built_year = item['built_year']
                tel = item['tel']
                scratch_time = item['scratch_time']
                Sql.insert_data(house_id, title, address, room_type, area, floor, direction, district, shelf_time,
                                community, subway_station, distance, rental, seen_record, details, img_url,
                                housing_price, built_year, tel, scratch_time)
                print('开始保存' + house_id)
