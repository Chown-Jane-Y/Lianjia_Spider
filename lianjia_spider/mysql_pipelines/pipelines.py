# -*- coding: utf-8 -*-
from lianjia_spider import settings
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


""" 初始化数据库表语句
DROP TABLE IF EXISTS `house_info`;
CREATE TABLE `house_info` (
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
  `img_url` MESSAGE_TEXT DEFAULT NULL,
  `scratch_time` varchar(40) DEFAULT NULL,
  `housing_price` varchar(10) DEFAULT NULL,
  `tel` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`house_id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4;
"""

class LianjiaSpiderPipeline(object):
    def process_item(self, item, spider):
        return item
