#软件爬虫
import urllib.request
import re
import os
class CHelper_reptile(object):
    def __init__(self): 
        pass 
    #爬取豆瓣供应商
    def test1(self):
        url = "https://read.douban.com/provider/all"
        headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
        opener = urllib.request.build_opener()
        opener.addheaders=[headers]
        data = opener.open(url).read()
 
        data = data.decode("utf-8")
       
        pat = '<div class="name">(.*?)</div>'
        mydata = re.compile(pat).findall(data)
        print(mydata)
        return mydata
    #爬取网页并保存
    def test(self):
        url = "https://read.douban.com/provider/all"
        data=urllib.request.urlretrieve(url,os.getcwd()+"\\my\\1.html")
        urllib.request.urlcleanup()#清除运行过程中产生的缓存
        print("保存完毕")
        return "null"
    #获取爬取信息
    def test3(self):
        url = "https://read.douban.com/provider/all"
        file=urllib.request.urlopen(url)
        data1 = file.info() #获取网页信息
        data2 = file.getcode()  #打开网页结果  200表示成功  其他失败
        data3 = file.geturl()#当前爬取的地址
        return data3
     #设置爬取超时
    def test4(self):
        url = "https://read.douban.com/provider/all"
        data = ""
        for i in range(100):
            try:
                file=urllib.request.urlopen(url,timeout=1)#正常是5s--10s
                data = file.info() #获取网页信息
            except Exception as e:
                print("出现异常"+str(e))
            print(str(i))
        return data
    #固定搜索 不支持http   https://www.baidu.com/s?wd=python******
    def test5(self):
        url = "http://www.baidu.com/s?wd="
        key = "python"
       # key = urllib.request.quote(key); 中文需要转码
        allurl = url+key
        req=urllib.request.Request(allurl)
        data = urllib.request.urlopen(req).read()
        fh = open(os.getcwd()+"\\my\\1.html","wb")
        fh.write(data)
        fh.close()
        urllib.request.urlcleanup()#清除运行过程中产生的缓存
        return "null"
    #模拟表单post   http://www.iqianyue.com/mypost/
    def test6(self):
        url = "http://www.iqianyue.com/mypost/"
        data = urllib.parse.urlencode({
        "name":"xiaoming",
        "pass" :"123456"
            }).encode("utf-8")
        req = urllib.request.Request(url,data);#请求
        data = urllib.request.urlopen(req).read()#将提交后的网页爬取
        fh = open(os.getcwd()+"\\my\\1.html","wb")
        fh.write(data)
        fh.close()
        urllib.request.urlcleanup()#清除运行过程中产生的缓存
        return "null"
    #模拟浏览器
    def test7(self):
        url = "https://www.qiushibaike.com/text/"
        headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
        opener = urllib.request.build_opener()
        opener.addheaders=[headers]
        data = opener.open(url).read()
        fh = open(os.getcwd()+"\\my\\1.html","wb")
        fh.write(data)
        fh.close()
        urllib.request.urlcleanup()#清除运行过程中产生的缓 存
        return "null"
    #爬取新浪新闻
    def test8(self):
        url = "https://news.sina.com.cn/"
        data = urllib.request.urlopen(url).read()
        data = data.decode("utf-8","ignore")
        pat ='.shtml">(.*?)</a>'
        mydata  = re.compile(pat).findall(data)
        return mydata
    #使用代理IP 模拟浏览器   爬取   防止IP被封   免费代理https://www.xicidaili.com/
    def test9(self):
        #url = "https://blog.csdn.net/go_str/article/details/80844175"
        url = "http://quote.eastmoney.com/center//" 
        proxy_addr = "218.76.253.201:61408"
        headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
        proxy = urllib.request.ProxyHandler({"http":proxy_addr})
        opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        opener.addheaders=[headers]
        urllib.request.install_opener(opener)
        
        data =  urllib.request.urlopen(url).read()
        fh = open(os.getcwd()+"\\my\\1.html","wb")
        fh.write(data)
        fh.close()
        urllib.request.urlcleanup()#清除运行过程中产生的缓 存
        return "null"
    #使用代理IP 模拟浏览器 
    def test10(self):
        #访问网址 
        url = "https://www.xicidaili.com/"
        #这是代理 IP 
        proxy = {'http':"61.135.217.7:80"} 
        #创建ProxyHandler 
        proxy_support = urllib.request.ProxyHandler(proxy) 
        #创建Opener 
        opener = urllib.request.build_opener(proxy_support) 
        #添加User Angent 
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')] 
        #安装OPener 
        urllib.request.install_opener(opener) 
        #使用自己安装好的Opener 
        response = urllib.request.urlopen(url) 
        #读取相应信息并解码 
        html = response.read().decode("utf-8") 
        #打印信息
        print(html)
        return "null"
    #使用代理IP 模拟浏览器 
    def test11(self):
        url = "https://www.taobao.com/"
        #url = "http://www.ip138.com/"
        proxy_ip={'http': '161.135.217.7:80'}  #想验证的代理IP
        proxy_support = urllib.request.ProxyHandler(proxy_ip)
        opener = urllib.request.build_opener(proxy_support)
        opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64)")]
        urllib.request.install_opener(opener)
        print(urllib.request.urlopen(url).read().decode("utf-8") )
        return "null"
    #爬取一张图片
    def test12(self):
        url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1544726458301&di=b54c3b5d47cd3411cabb3aa7bbcb6ab2&imgtype=0&src=http%3A%2F%2Fe.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2Fb151f8198618367afe76969623738bd4b21ce5fa.jpg"
        file = os.getcwd()+"\\my\\1.jpg"
        urllib.request.urlretrieve(url,filename=file)
        return "null"