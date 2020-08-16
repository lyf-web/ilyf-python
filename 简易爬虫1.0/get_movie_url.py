#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Author:lyf
#Datetime:2020-8-16
#Filename:get_movie_url.py

import re
import urllib.request
from downlaod_link import is_download

def get_movie_url(website_url):
    
    #定义headers内容
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    request_url = urllib.request.Request(website_url,headers=headers)
    #获取网页数据
    request_url_data = urllib.request.urlopen(request_url).read()
    #转换网页数据字符串
    request_url_text = request_url_data.decode('GBK')
    #匹配网页内的电影页面链接
    re_url_list = re.findall(r'<a href="(?P<url>.*?)" class="ulink" title="(?P<name>.*?)">(?P=name)</a>', request_url_text)
    #定义空字典用于临时存放数据
    movie_dict = {}
    #解包列表
    for movie_link, movie_name in re_url_list:
        #生成完整网页连接
        movie_link = 'https://www.dy2018.com/' + movie_link
        #添加请求头
        movie_link_url = urllib.request.Request(movie_link,headers = headers)
        #创建并读取网页数据
        movie_link_url_data = urllib.request.urlopen(movie_link_url).read()
        #解码
        movie_link_url_text = movie_link_url_data.decode('GBK')
        #正则匹配下载链接+
        re_movie_link = re.search(r'(magnet:\?xt=urn:btih|ftp://d|ftp://j|ftp://z|ftp://2|ftp://y):(.*?).(mp4|mkv|rm|rmvb|avi|wmv)', movie_link_url_text)
        #下载链接拼接
        print(re_movie_link)
        # print(re_movie_link.group(1))
        print(re_movie_link.group(2))
        #判断下载链接的类型
        movie_download = is_download(re_movie_link.group(1),re_movie_link.group(2),re_movie_link.group(3))
        # print(movie_download)
        # print('+'*100)
        #临时保存到字典
        movie_dict[movie_name] = movie_download
    return movie_dict
