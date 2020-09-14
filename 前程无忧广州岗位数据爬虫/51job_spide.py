import requests
from lxml import etree
import re
import json
import csv
import datetime
import time

class job_spide(object):
    #初始化url链接，获取responsed对象
    def __init__(self, kw, page):
        #经过前期的url分析，构造初始搜索结果的链接
        self.kw = kw
        url = f'https://search.51job.com/list/030200,000000,0000,00,9,99,{kw},2,{page}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
        #构造请求头，避开最基础的反爬策略
        headers = {
            'Host': 'search.51job.com',

            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 85.0.4183.102 Safari / 537.36',
        }
        try:
            #获取response对象
            self.response = requests.get(url=url, headers=headers)
        except Exception as e:
            print(e)

    #获取一页的json数据
    def get_one_page(self):
        #利用xpath找到含有json数据的字符串
        html = etree.HTML(self.response.text)
        result = html.xpath('/html/body/script[2]/text()')
        #将字符串无用的部分去除掉
        str_result_json = re.sub(r'\r\nwindow.__SEARCH_RESULT__ = ', '', result[0])
        #转换成Json格式
        result_json = json.loads(str_result_json)
        return result_json

    #解析json数据返回数据储存到列表
    def parse_position(self):
        result_json = self.get_one_page()
        #经过分析，json数据里的engine_search_result字段就是搜索结果的各个数据
        data = result_json['engine_search_result']
        if len(data) > 0:
            for num in range(len(data)):
                job_name = data[num]["job_name"] #职位名称
                company_href = data[num]["company_href"]    #公司连接
                company_name = data[num]["company_name"]    #公司名称
                providesalary_text = data[num]["providesalary_text"]    #薪水范围
                workarea_text = data[num]["workarea_text"]  #工作地点
                updatedate = data[num]["updatedate"]    #发布时间
                companytype_text = data[num]["companytype_text"]    #公司类别
                jobwelf = data[num]["jobwelf"]  #福利待遇
                companysize_text = data[num]["companysize_text"]    #公司规模
                companyind_text = data[num]["companyind_text"]  #公司行业
                job_href = data[num]["job_href"]    #职位连接
                attribute_text = ','.join(data[num]["attribute_text"])    #基本要求
                job_base_info = [job_name,company_href,company_name,providesalary_text,workarea_text,updatedate,companyind_text,companytype_text,jobwelf,companysize_text,job_href,attribute_text]
                # print(job_base_info)
                yield job_base_info

        else:
            return

    #判断json数据是否为空
    def if_true(self):
        json_data = self.get_one_page()
        if len(json_data['engine_search_result']) > 0:
            return True
        else:
            return False


    #储存为csv格式保存数据
    def save_csv(self,job_base_info):
        jobs_title = ['岗位名称', '公司链接', '公司名称', '薪水范围', '工作地点', '发布时间', '公司类别', '福利待遇', '公司规模', '公司行业', '职位连接', '基本要求']
        with open(f'{self.kw}jobs{datetime.date.today()}.csv', 'a', newline="", encoding='gbk') as f:
            job_writer = csv.writer(f)
            job_writer.writerow(jobs_title)
            job_writer.writerows(job_base_info)

    #运行函数
    def run(self):
        job_base_info = self.parse_position()
        self.save_csv(job_base_info)

if __name__ == '__main__':
    kw = input('请输入查询职位的关键词：')
    start = time.time()
    i = 1
    while True:
        job = job_spide(kw, str(i))
        if job.if_true():
            job.run()
            print(f'第{i}页完成')
        else:
            break
        i += 1
    print(time.time()-start)