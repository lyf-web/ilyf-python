import requests
import re
import datetime
import csv
import time
import random


class taobao_spide(object):
    def __init__(self, page, keyword):
        try:
            #利用https://curl.trillworks.com/来解析获得headers和params
            headers = {
                'authority': 's.taobao.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://s.taobao.com/search?q=%E9%A9%AC%E6%A1%B6&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cookie': 'cna=n/OBF0dV4nECAbRbpBtBqfTz; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; sgcookie=EcG%2BNJnhr0I64yr9fqVn%2B; uc3=nk2=GdFmKlMHnia0XcU%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dCufXF2i4egpOgTAY%3D&id2=UoYekRdcp93Q; lgc=zy051201231; uc4=id4=0%40UO6XcJxslCMHwH7AQig2ypKNSMA%3D&nk4=0%40Gxh%2FMoHkSzWt6rdyRdry%2BS0nrIVCmw%3D%3D; tracknick=zy051201231; _cc_=UIHiLt3xSw%3D%3D; enc=jC5Xz%2FO7NsZuAN%2BBFLuC7Dc%2FI3J5lkSAs851wDKJTVXUflzm6fD8%2FA3ap8PFUwyyR03vcjHOeLMF6qypFoAK7w%3D%3D; t=34d405c558ffa0d6d96cc7d99795c263; UM_distinctid=174803e66aa195-05a0f7e1bff6f2-333769-10ae00-174803e66ab277; mt=ci=-1_0; v=0; _tb_token_=95d3e93ee531; xlly_s=1; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; cookie2=118f58aaf4a0d52f07eb154c93dacc00; _m_h5_tk=6eb5952943c5707a37cd12601b2d5b32_1599900753324; _m_h5_tk_enc=7051216dfec9b74217fd1e958c1b43ef; _samesite_flag_=true; JSESSIONID=F9E46279EA2A71CD0AA7040E717DA672; uc1=cookie14=UoTV5YQOECpBag%3D%3D; tfstk=cxW1BFc2kV0soWNqQGZeu5zpvXJfZ4NMx5TFf16fbGg8RES1iiMyPHoGi2MpwH1..; l=eBQVukSlOUICPx3sBOfahurza779sIRvMuPzaNbMiOCP9KfpfSdVWZyKVc89CnhVh6lvR3uV-FgLBeYBqIv4n5U62j-la_Dmn; isg=BM7OlMssHWWtJKlVWiJIPX3yH6SQT5JJ656QNvgXP1GOW261YN3XWQ4Zkoc3i4ph',
            }

            params = (
                ('q', keyword),
                ('imgfile', ''),
                ('js', '1'),
                ('stats_click', 'search_radio_all:1'),
                ('initiative_id', 'staobaoz_20200912'),
                ('ie', 'utf8'),
                ('s',page),
            )

            self.response = requests.get('https://s.taobao.com/search', headers=headers, params=params)
            self.response.raise_for_status()
            self.response.encoding = self.response.apparent_encoding

        except Exception as e:
            print(e)

    #利用正则表达式获取页面的相关关键数据
    def get_page_list(self):
        one_page_text = self.response.text
        title_list = re.findall(r'"raw_title":"(.*?)"', one_page_text)  #产品名称
        pic_url_list = re.findall(r'"pic_url":"(.*?)"', one_page_text)  #产品图片链接
        price_list = re.findall(r'"view_price":"(.*?)"', one_page_text) #商品价格
        area_list = re.findall(r'"item_loc":"(.*?)"', one_page_text)    #店铺地区
        shop_name_list = re.findall(r'"nick":"(.*?)"', one_page_text)   #店铺名称
        sales_list = re.findall(r'"view_sales":"(.*?)"', one_page_text) #付款人数
        #因为各个列表的数据长度都是相等的，所以随便用其中一个列表的长度来进行遍历
        for i in range(len(title_list)):
            products_base_info = [
                title_list[i],
                pic_url_list[i],
                price_list[i],
                area_list[i],
                shop_name_list[i],
                sales_list[i]
            ]

            print(products_base_info)
            #通过yield关键字将该方法定义为生成器，并返回数据
            yield products_base_info

    #储存数据到csv文件里
    def save_csv(self, product_info_list):
        product_info_title = [
            '产品名称',
            '产品图片连接',
            '产品价格(元)',
            '店铺地区',
            '店铺名称',
            '付款人数'
        ]
        with open(f'淘宝商品搜所基本信息{datetime.date.today()}.csv', 'a', newline='', encoding='gbk') as f:
            f_write = csv.writer(f)
            f_write.writerow(product_info_title)
            f_write.writerows(product_info_list)

    #运行函数
    def run(self):
        product_info_list = self.get_page_list()
        self.save_csv(product_info_list)


if __name__ == '__main__':
    kw = input('请输入关键词：')
    start = time.time()
    #为了防止淘宝封IP，所以只爬取了前十页的数据，增加一页就在range函数的第二个参数加44，而且每趴一页就随机休眠1-20秒
    #第一页为0，第二页为44，第三页为88，每页相隔44
    for i in range(0,440,44):
        ts = taobao_spide(i, kw)
        time.sleep(random.randint(1,20))
        ts.run()
    print(time.time()-start)
