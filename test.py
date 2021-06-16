import requests
import sys
import time
import random
import re
sys.path.append("./")
from utils.http import get_request_headers
from lxml import etree
from domain import Proxy
import base64

# # group_xpath: 分组XPATH, 获取包含代理IP信息标签列表的XPATH
# group_xpath = '//*[@id="scroll"]/table/tbody/tr'
# # detail_xpath: 组内XPATH, 获取代理IP详情的信息XPATH, 格式为: {'ip':'xx', 'port':'xx', 'area':'xx'}
# detail_xpath = {
#     'ip':'./td[1]/text()',
#     'port':'./td[2]/text()',
#     'area':'./td[4]/text()'
# }


# response = requests.get('https://proxy-list.org/chinese/index.php?p={}', headers=get_request_headers())

# element = etree.HTML(response.content)


# ip_list = []
# trs = element.xpath('//*[@id="proxy-table"]/div[2]/div/ul/li[1]/text()')
# for tr in trs:
#     ip_list = tr.split(":")
#     print(ip_list)
#     ip = ip_list[0]
#     port = ip_list[1]
#     print(ip)
#     print(port)


    #             yield base64.b64decode(proxy).decode()


# class Proxy_List():

def freeProxy11():
    urls = ['https://proxy-list.org/chinese/index.php?p=%s' % n for n in range(1, 2)]
    import base64
    for url in urls:
        r = requests.get(url, timeout=10)
        proxies = re.findall(r"Proxy\('(.*?)'\)", r.text)
        for proxy in proxies:
            # print(proxy)
            ip_list = base64.b64decode(proxy).decode().split(":")
            print(ip_list)
            ip = ip_list[0]
            port = ip_list[1]
            # proxy = Proxy(ip, port)
            # yield proxy

# freeProxy11()
# a = freeProxy11()
# for _ in a:
#     print(_)
