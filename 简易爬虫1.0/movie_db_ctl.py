#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Author:lyf
#Datetime:2020-8-16
#Filename:movie_db_ctl.py

'''
movie_db类是操作数据库的类，因现阶段项目需求只设有innsert方法，和close方法,
以后可根据需求增数据库操作的其他方法
'''

import pymysql

#定义电影数据库类
class movie_db(object):
    #初始化数据库操作
    def __init__(self):
        
        self.conn = pymysql.connect(host = 'localhost', user = 'root', password = 'zy051201230', database = 'movie_db')
        self.cur = self.conn.cursor()
   
    #定义添加方法 
    def movie_insert(self,movie_name,movie_download):
        self.movie_name = movie_name
        self.movie_download = movie_download
        #定义execute函数
        params = [self.movie_name,self.movie_download]
        #定义sql语句
        sql_insert = 'insert into movie_info value(null, %s, %s)'
        result = self.cur.execute(sql_insert, params)
        #插入一条数据，提交一次
        self.conn.commit()
        print('数据插入成功！')
    
    #定义数据库连接关闭方法
    def db_close(self):
        self.cur.close()
        self.conn.close() 
        print('已完成')           
