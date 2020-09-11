'''
此爬虫项目只为自学自乐，因不懂股票分析，不知道需要爬取哪些数据，所以只爬取了一些基本的股票相关资料，
如果想进入个股页面爬取更多的内容信息，可以其中凭"f13"属性的股票secid码来进入个股页面，
例如："http://19.push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery112404349382729095952_
1599806589652&secid=0.300126&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2
Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt
=101&fqt=0&end=20500101&lmt=120&_=1599806589681"
这个连接可以打开个股页面时通过抓包工具抓取，经过分析，后面一大串参数，其中secid=0.300126是secid码加上股票代码就可以得到
该股票的一些列数据，因此利用secid码就可以替换这个连接里面secid参数的小数点前面部分的0或者1再加上后面的股票代码就可以访问到
任何一只股票的详细数据，从而经过json处理后就可以解析爬取下来。
后续利用这个数据源，django+mysql来建立一套基本的股票分析系统。
'''




import requests
import json
import re
import datetime
import csv


class stock_spider(object):
    def __init__(self, page):
        #伪造请求头，应对最基本的反爬策略
        self.headers = {
            'Accept': '* / *',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;',
            'Connection': 'keep - alive',
            'Host': '91.push2.eastmoney.com',
            'Referer':'http://quote.eastmoney.com/center/gridlist.html',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/85.0.4183.83 Safari/537.36'
        }
        # 设置URL
        self.url = f'http://91.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124018577022529111842_1599733993448&pn={page}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1599733993449'

    #返回一页的数据
    def get_stock_list(self):
        #简单做个try来捕获未知的异常
        try:
            # 获取response对象
            response = requests.get(self.url, headers=self.headers)
        except Exception as e:
            print(e)

        re_text = re.search('\((.+)\)', response.text) #正则表达式获取json数据

        json_text1 = re_text.group().lstrip('(')    #因直接使用response.json()会报错，提示该字符串不是标准的json格式

        json_text2 = json_text1.rstrip(')') #所以要经过几步愚蠢的字符串操作获取符合json格式的字符串

        j = json.loads(json_text2)  #以上四获行代码是将字符串转换为取json格式数据

        #编列数据获取分类数据
        for num in range(len(j['data']['diff'])):
            stock_name = j['data']['diff'][num]['f14'] #股票名称
            stock_num = j['data']['diff'][num]['f12']   #股票代码
            stock_secid = j['data']['diff'][num]['f13'] #股票secid码
            stock_new_price = j['data']['diff'][num]['f2']  #股票最新价
            stock_high_price = j['data']['diff'][num]['f15']    #股票当日最高价
            stock_low_price = j['data']['diff'][num]['f16'] #股票当日最低价
            stock_start_price = j['data']['diff'][num]['f17']   #股票当日开盘价
            stock_last_price = j['data']['diff'][num]['f18']    #股票昨收价
            stock_extent = j['data']['diff'][num]['f3'] #股票涨跌幅
            stock_extent_price = j['data']['diff'][num]['f4']   #股票涨跌额
            stock_change = j['data']['diff'][num]['f8'] #股票换手率
            stock_macket = j['data']['diff'][num]['f9'] #股票市盈率
            stock_vibration = j['data']['diff'][num]['f7'] #股票振幅
            stock_book_ratio = j['data']['diff'][num]['f23']    #股票市净率

            #定义列表临时存放数据
            stock_info = [
                stock_name,
                stock_num,
                stock_secid,
                stock_new_price,
                stock_high_price,
                stock_low_price,
                stock_start_price,
                stock_last_price,
                stock_extent,
                stock_extent_price,
                stock_change,
                stock_macket,
                stock_vibration,
                stock_book_ratio
            ]
            print(stock_info)
            #使用yield就可以没循环一页就保存一次数据，return的话是循环一次保存一次内容，这样就会造成一行标题一行数据的尴尬显示
            yield stock_info

    #保存数据到csv文件的函数
    def save_csv(self, stock_info):
        #定义每列数据的名称
        header = [
            '股票名称',
            '股票代码',
            '股票secid码',
            '股票最新价',
            '股票当日最高价',
            '股票当日最低价',
            '股票当日开盘价',
            '股票昨收价',
            '股票涨跌幅',
            '股票涨跌额',
            '股票换手率',
            '股票市盈率',
            '股票振幅',
            '股票市净率'
        ]

        #创建csv文件保存爬虫数据，这里文件名加个日期上去方便区分每天的数据
        with open(f'爬取东方财富网所有个股的基本数据{datetime.date.today()}.csv', 'a', encoding='gbk', newline='') as f:
            stock_writer = csv.writer(f)
            stock_writer.writerow(header)
            stock_writer.writerows(stock_info)

    #定义一个运行方法调用以上两个方法来时爬虫工作
    def run(self):
        stock_info = self.get_stock_list()
        self.save_csv(stock_info)


if __name__ == '__main__':
    #页数是从第一页开始，到209页
    for i in range(1,210):
        ss = stock_spider(i)
        ss.run()
