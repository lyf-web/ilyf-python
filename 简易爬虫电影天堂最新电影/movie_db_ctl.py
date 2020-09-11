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
from setting import sql_host, sql_user, sql_passwd, sql_database

#定义电影数据库类
class movie_db(object):
    #初始化数据库操作
    def __init__(self):
        
        self.conn = pymysql.connect(host = sql_host, user = sql_user, password = sql_passwd, database = sql_database)
        self.cur = self.conn.cursor()
   
    #定义添加方法 
    def movie_insert(self,movie_name,movie_download):
        self.movie_name = movie_name
        self.movie_download = movie_download
        #定义execute函数
        params = [self.movie_name,self.movie_download]
        #定义sql语句
        sql_insert = 'insert into movie_info value(null, %s, %s)'
        res = self.cur.execute(sql_insert, params)
        #判断是否保存数据成功
        if res > 0:
            self.conn.commit()
            print('数据插入成功！')
        
    #定义检查是否有重复数据
    def is_exist(self,movie_name,movie_download):
        self.movie_name = movie_name
        self.movie_download = movie_download
        #定义查询语句,参数
        sql_select = f'select id from movie_info where name = %s and downloak_link = %s limit 1'
        params = [self.movie_name,self.movie_download]
        #执行查询语句
        ret = self.cur.execute(sql_select, params)
        if ret:
            print(f'数据已存在!{self.movie_name}')
            return True
        else:
            return False

    #定义数据库连接关闭方法
    def db_close(self):
        self.cur.close()
        self.conn.close() 
        print('已完成')           
