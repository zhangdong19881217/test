#管理获取代理IP   不能频繁调用否则有封IP的可能
import urllib.request
import re
import os
import threading
class CHelper_IP(object):
    def __init__(self): 
        pass 
    #爬取一页IP
    def GetOnePage(self,page="1"):
        #获取网页代码
        url = "https://www.xicidaili.com/nn/"+page
        proxy_addr = "115.46.68.6:8123"
        headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
        proxy = urllib.request.ProxyHandler({"http":proxy_addr})
        opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        opener.addheaders=[headers]
        urllib.request.install_opener(opener)
        data =  urllib.request.urlopen(url).read()
        data = data.decode("utf-8")
        #获取IP
        agency_ip_re = re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b' ,re.S)
        agency_ip = agency_ip_re.findall(data)
        # 获取代理ip的端口号
        agency_port_re = re.compile('<td>([0-9]{2,5})</td>', re.S)
        agency_port = agency_port_re.findall(data)
        #组合成完整的地址
        mAllIp = []
        for i in range(len(agency_port)):
            total_ip = agency_ip[i] + ':' + agency_port[i]
            mAllIp.append(total_ip)
        return mAllIp
    #爬取一页IP
    def GetIP(self,PageNum=10):
        myIp = []
        num=0#统计当前获取的个数
        for i in range(PageNum):
            try:
                myIp += self.GetOnePage(page=str(i+1))
                print("获取的当前页数：",i,"当前获取IP的个数：",len(myIp))
            except Exception as e:
                print(e)
        return myIp
