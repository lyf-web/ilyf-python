#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Author:lyf
#Datetime:2020-8-16
#Filename:main.py

import urllib.request
import re
import pymysql
import time
from movie_db_ctl import movie_db
from get_movie_url import get_movie_url
from setting import web_site, web_site_dir

'''
简易电影天堂最新电影爬虫
可以从第二页开始自动翻页爬取
待解决问题：1,补充下载链接类型
           2,抽取常量字符串
           3,需要改为多线程版本增加效率 
           4,爬取下一页时应改为正则表达式匹配下一页！
'''

def main():
    start = time.time()
    i = 2 #设置开始页数

    while True:
        website_url = f'{web_site}{web_site_dir}/index_{i}.html'
        # print(website_url)
        print(f'第{i}页开始。。。')
        #获取字典
        movie_info_dict = get_movie_url(website_url)
        mb = movie_db()
        
        #循环插入数据库
        for k in movie_info_dict:
            if not mb.is_exist(k, movie_info_dict[k]):
                mb.movie_insert(k, movie_info_dict[k])
            else:
                continue
        print(f'已完成第{i}页')
        print('*'*100)
        print('\n')
        i += 1
        if i > 312:
            break
            print(f'总共{i}页已完成')
    mb.db_close()
    end = time.time()
    print(str(end - start))

if __name__ == "__main__":
    main()
