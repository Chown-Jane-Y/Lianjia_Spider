# -*- coding: utf-8 -*-
import json

import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from datetime import datetime
from lianjia_spider.items import LianjiaSpiderItem
import requests
import re


class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["sh.lianjia.com"]
    start_urls = ['http://sh.lianjia.com/']

    def start_requests(self):
        yield Request('http://sh.lianjia.com/zufang/')

    def parse(self, response):      # 接收start_requests传来的response
        max_page = 100      # 最多100页
        bashurl = str(response.url)     # 就是http://sh.lianjia.com/zufang/
        for page_num in range(1, int(max_page)+1):
            url = bashurl + 'd' + str(page_num)
            yield Request(url, callback=self.get_house_url)      # 请求每一页的数据，给get_name处理

    def get_house_url(self, response):           # 把每一页中的房源信息的url提取出来
        a_tags = BeautifulSoup(response.text, 'lxml').find_all('a', {'name': 'selectDetail', 'class': 'rent'})
        for a_tag in a_tags:
            each_house_href = a_tag['href']  # 源代码中是相对地址 /zufang/shz3750054.html
            each_house_url = 'http://sh.lianjia.com' + each_house_href       # 需要把前缀http://sh.lianjia.com加上
            yield Request(each_house_url, callback=self.get_house_info)

    def get_house_info(self, response):
        house_id = BeautifulSoup(response.text, 'lxml').find('span', {'class': 'houseNum'}).get_text()[5:]
        title = BeautifulSoup(response.text, 'lxml').find('h1', {'class': 'main'}).get_text()
        scratch_time = datetime.now()
        address = BeautifulSoup(response.text, 'lxml').find_all('p', {'class': 'addrEllipsis'})[1]['title']
        house_type = BeautifulSoup(response.text, 'lxml').find('div', {'class': 'room'}).get_text().strip()
        area = BeautifulSoup(response.text, 'lxml').find('div', {'class': 'area'}).get_text().strip()
        floor = BeautifulSoup(response.text, 'lxml').find('table', {'class': 'aroundInfo'}).find('tr').find_all('td')[1].get_text()
        direction = BeautifulSoup(response.text, 'lxml').find('table', {'class': 'aroundInfo'}).find('tr').find_all('td')[3].get_text().strip()
        district = BeautifulSoup(response.text, 'lxml').find('table', {'class': 'aroundInfo'}).find_all('tr')[1].find_all('td')[1].get_text()
        shelf_time = BeautifulSoup(response.text, 'lxml').find('table', {'class': 'aroundInfo'}).find_all('tr')[1].find_all('td')[3].get_text()
        community = BeautifulSoup(response.text, 'lxml').find_all('p', {'class': 'addrEllipsis'})[0]['title']
        rental = BeautifulSoup(response.text, 'lxml').find('div', {'class': 'price'}).find('div').get_text()[:-3]
        seen_record = BeautifulSoup(response.text, 'lxml').find('div', {'class': 'panel'}).find_all('div')[2].find('span').get_text()
        tel = BeautifulSoup(response.text, 'lxml').find_all('div', {'class': 'phone'})[0].get_text().strip().replace('\n', '').replace(' ','')
        # 爬图片链接 ↓
        img_url_tags = BeautifulSoup(response.text, 'lxml').find('div', {'id': 'album-view-wrap'}).find_all('img')
        img_url = {item['img-title']: item['data-large'] for item in img_url_tags}
        # 爬户型分间 ↓
        json_url = 'http://sh.lianjia.com/api/house/getCells.json?houseId=' + house_id[3:] + '&type=zufang'
        roomtype_json = requests.get(json_url).json()       # 请求户型分间json数据
        roomtype_list = roomtype_json.get('cellInfoList')
        roomtype = None
        if roomtype_list:
            roomtype = {item['name']: item['area'] for item in roomtype_list}       # 取出name和area字段
        # 爬地铁距离，用手机端网页获取↓
        mobile_url = response.url.replace('http://', 'http://m.')       # 换成手机端地址
        subway_info = BeautifulSoup(requests.get(mobile_url).text, 'lxml').find('p', {'class': 'd-value'}).get_text()
        subway = subway_info.split('站')
        distance = subway[1][:-1]
        subway_station = subway[0][2:] + '站'
        # 小区信息页面中爬建造时间和挂牌均价 ↓
        community_href = BeautifulSoup(response.text, 'lxml').find_all('p', {'class': 'addrEllipsis'})[0].find('a')['href']
        community_url = 'http://sh.lianjia.com' + community_href
        built_year = BeautifulSoup(requests.get(community_url).text, 'lxml').find_all('span', {'class': 'other'})[1].get_text().strip()[:-1]
        housing_price_test = BeautifulSoup(requests.get(community_url).text, 'lxml').find('span', {'class': 'p'})
        housing_price = None
        if housing_price_test:
            housing_price = housing_price_test.get_text().strip()

        print('【标    题】' + title)
        print('【房源编号】' + house_id)
        print('【地    址】' + address)
        print('【户    型】' + house_type)
        print('【面    积】' + area)
        print('【楼    层】' + floor)
        print('【朝    向】' + direction)
        print('【区    域】' + district)
        print('【上架时间】' + shelf_time)
        print('【小    区】' + community)
        print('【地 铁 站】' + subway_station)
        print('【距离地铁】' + distance)
        print('【租    金】' + rental + ' 元/每月')
        print('【看房记录】' + seen_record)
        print('【户型分间】' + str(roomtype))
        print('【图片链接】' + str(img_url))
        print('【挂牌均价】' + str(housing_price))
        print('【建造年份】' + built_year)
        print('【联系电话】' + tel)
        print('【采集时间】' + str(scratch_time))


