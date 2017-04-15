# coding: utf-8
__author__ = 'gocjy'
__date__ = '2017/4/14 17:29'

import mysql.connector
from lianjia_spider import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
cur = cnx.cursor(buffered=True)


class Sql(object):

    @classmethod
    def insert_data(cls, house_id, title, address, room_type, area, floor, direction, district,
                    shelf_time, community, subway_station, distance, rental, seen_record, details,
                    img_url, housing_price, built_year, tel, scratch_time):
        """
        往数据库中插入数据
        """
        sql = 'INSERT INTO house_info (`house_id`, `title`, `address`, `room_type`, `area`, `floor`, `direction`, ' \
              '`district`, `shelf_time`, `community`, `subway_station`, `distance`, `rental`, `seen_record`, ' \
              '`details`, `img_url`, `housing_price`, `built_year`, `tel`, `scratch_time`) ' \
              'VALUES (%(house_id)s, %(title)s, %(address)s, %(room_type)s, %(area)s, %(floor)s, %(direction)s, ' \
              '%(district)s, %(shelf_time)s, %(community)s, %(subway_station)s, %(distance)s, %(rental)s, ' \
              '%(seen_record)s, %(details)s, %(img_url)s, %(housing_price)s, %(built_year)s, %(tel)s, %(scratch_time)s)'
        value = {
            'house_id': house_id, 'title': title, 'address': address, 'room_type': room_type, 'area': area,
            'floor': floor, 'direction': direction, 'district': district, 'shelf_time': shelf_time,
            'community': community, 'subway_station': subway_station, 'distance': distance, 'rental': rental,
            'seen_record': seen_record, 'details': details, 'img_url': img_url, 'housing_price': housing_price,
            'built_year': built_year, 'tel': tel, 'scratch_time': scratch_time
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def select_house_id(cls, house_id):
        """
        查找house_id，如果已经存在返回 1
        """
        sql = 'SELECT EXISTS(SELECT 1 FROM house_info WHERE house_id=%(house_id)s)'
        value = {
            'house_id': house_id
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]


