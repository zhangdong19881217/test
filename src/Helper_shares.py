#对股票的操作
import urllib
import re
import pandas as pd
import pymysql
import os
from Helper_File import *#文件操作
import multiprocessing#多进程
import threading
from Helper_tushare import* 
from Helper_ImportDate import* 
from Helper_File import* 
from Helper_MySql import* 
import time
import pandas as pda
from Helper_config import *
class CHelper_shares(object):
    path="d:\\1\\"
    starttime=""
    endtime="20190227"
    number=0
    CodeList=[]
    mCHelper_config=CHelper_config()
    Total=list(range(mCHelper_config.ShareThreadNum))
    BasePath=mCHelper_config.ShareBasePath
    def __init__(self): 
        pass
    #获取股票代码
    #爬虫抓取网页函数
    def getHtml(self,url):
        html = urllib.request.urlopen(url).read()
        html = html.decode('gbk')
        return html

    #抓取网页股票代码函数
    def getStackCode(self,html):
        s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'
        pat = re.compile(s)
        code = pat.findall(html)
        return code
    #获取一个CSV  带初始日期
    def GetOneCsv(self,path="d:\\1\\",code="000002",mystarttime="20190226", myendtime="20190227"):
        if code[0] == '6':
            url = "http://quotes.money.163.com/service/chddata.html?code=0"+code\
                +"&start="+mystarttime+"&end="+myendtime+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP" 
        else:
            url = "http://quotes.money.163.com/service/chddata.html?code=1"+code\
                +"&start="+mystarttime+"&end="+myendtime+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP" 
        urllib.request.urlretrieve(url, path + code + '.csv')  # 可以加一个参数dowmback显示下载进度
    #获取一个CSV  不带初始日期
    def GetOneCsv1(self,path="d:\\1\\",code="000001",myendtime="20190227"):
        if code[0] == '6':
            url = "http://quotes.money.163.com/service/chddata.html?code=0"+code\
                +"&end="+myendtime+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP" 
        else:
            url = "http://quotes.money.163.com/service/chddata.html?code=1"+code\
                +"&end="+myendtime+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP" 
        urllib.request.urlretrieve(url, path + code + '.csv')  # 可以加一个参数dowmback显示下载进度
    #线程执行程序
    #number 第几个线程
    #total  线程的总个数
    def ProcessRun(self,number,total):
        i=0
        while((i*total+number)<len(self.CodeList)):
            print(self.CodeList[i*total+number],"\r\n")
            self.GetOneCsv1(path=self.path,code=self.CodeList[i*total+number],myendtime=self.endtime)
            i+=1  
        pass               
    #使用多进程的方式批量下载股票数据    
    def GetAllCsv(self,path="",myendtime=""):
        self.path=path
        self.endtime=myendtime
        Url = 'http://quote.eastmoney.com/stocklist.html'#东方财富网股票数据连接地址
        #实施抓取
        self.CodeList = self.getStackCode(self.getHtml(Url)) 
        #抓取数据并保存到本地csv文件
        j=20 #线程的个数
        t_obj = []
        for i in range(j):
            p = threading.Thread(target=CHelper_shares.ProcessRun,args =(self,i,j,))
            p.start()
            t_obj.append(p)
            i=i+1
        for m in t_obj:
            m.join() 
        pass
    #使用tushare采集所有股票编号,并导入到数据库中
    #CsvPath  为缓存路径
    def MySql_ImportShareNumbers(self):
        CsvPath=self.BasePath+'ShareNumber.csv'
       #查看文件是否存在，不存在就创建
        mCHelper_File=CHelper_File()
        mCHelper_File.Creat(CsvPath)
        #删除数据库中的表
        mCHelper_MySql=CHelper_MySql()
        mCHelper_MySql.OpenMysql()
        mCHelper_MySql.DelTable(sql1='use zhangdong',sql2='drop table ShareNumber')
        mCHelper_MySql.CloseMysql()

        #获取股票代码并保存
        mCHelper_tushare=CHelper_tushare()
        data=mCHelper_tushare.GetShareList()
        data.to_csv(CsvPath,encoding="gbk") 
        
        #将数据导入到Mysql
        mCHelper_ImportDate=CHelper_ImportDate()
        mCHelper_ImportDate.ImportOneCvs(file=CsvPath,TableName='ShareNumber',usecols=[1,2,3,4,5,6,7],my_encoding='gbk')

    #采集单个股票的历史数据并导入到数据库中
    def MySql_ImportOneShareDate(self,ShareNumber='000001'):
        CsvPath=self.BasePath+ShareNumber+'\\d'+ShareNumber+'.csv'
        myendtime=time.strftime("%Y%m%d", time.localtime()) 
        #myendtime= '20181201'
        #创建文件夹及文件
        mCHelper_File=CHelper_File()
        mCHelper_File.Creat(CsvPath)
        #采集历史数据并保存为csv
        if ShareNumber[0] == '6':
            url = "http://quotes.money.163.com/service/chddata.html?code=0"+ShareNumber\
                +"&end="+myendtime+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP" 
        else:
            url = "http://quotes.money.163.com/service/chddata.html?code=1"+ShareNumber\
                +"&end="+myendtime+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP" 
        urllib.request.urlretrieve(url, CsvPath)  # 可以加一个参数dowmback显示下载进度

        #将数据导入到Mysql
        mCHelper_ImportDate=CHelper_ImportDate()
        mCHelper_ImportDate.ImportOneCvs(file=CsvPath,TableName='d'+ShareNumber,usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
        pass 
    #线程
    #number 第几个线程
    #total  线程的总个数
    def MySql_ProcessRun(self,number,total):
        i=0
        while((i*total+number)<len(self.CodeList)):
           # self.Total[number]=(i*total+number)/len(self.CodeList)
           # print(self.Total[number],"\r\n")
            print(self.CodeList[i*total+number],"\r\n")
            code=self.CodeList[i*total+number][0:6]
            try:
                self.MySql_ImportOneShareDate(ShareNumber=code)
            except BaseException as ex:
                print(ex)
            i+=1    
        pass
    #更新所有股票历史数据
    def MySql_ImportAllShareDate(self):
        mCHelper_config=CHelper_config()
        ThreadNum=mCHelper_config.ShareThreadNum
        #更新股票编号
        self.MySql_ImportShareNumbers()
        #获取所有编号并生成一个列表
        data = pda.read_csv(self.BasePath+'ShareNumber.csv',encoding='gbk')
        data.values#获取所有的数据
        data2 = data.T#数据xy交换，为了得到y
        self.CodeList=data2.values[1]
        #开启线程
        t_obj = []
        for i in range(ThreadNum):
            p = threading.Thread(target=CHelper_shares.MySql_ProcessRun,args =(self,i,ThreadNum,))
            p.start()
            t_obj.append(p)
            i=i+1
        for m in t_obj:
            m.join() 
        pass
    #获取一个公司的财务报表
    def MySql_ImportOneIncome(self,ShareNumber="000002.SZ"):
        #生成路径
        code=ShareNumber[0:6]
        CsvPath=self.BasePath+code+'\\i'+code+'.csv'
        MyTableName='i'+code
        #检查路径
        mCHelper_File=CHelper_File()
        mCHelper_File.Creat(CsvPath)
        #获取财务数据
        mCHelper_tushare=CHelper_tushare()
        data=mCHelper_tushare.Get_Report(my_ts_code=ShareNumber)
        data.to_csv(CsvPath,encoding="gbk") 
        #将数据导入到Mysql
        mCHelper_ImportDate=CHelper_ImportDate()
        mCHelper_ImportDate.ImportOneCvs(file=CsvPath,TableName=MyTableName,usecols=range(65),my_encoding='gbk')
        pass
    #获取一个公司的资产负债表
    def MySql_ImportOneBalancesheet(self,ShareNumber="000001.SZ"):
        #生成路径
        code=ShareNumber[0:6]
        CsvPath=self.BasePath+code+'\\b'+code+'.csv'
        MyTableName='b'+code
        #检查路径
        mCHelper_File=CHelper_File()
        mCHelper_File.Creat(CsvPath)
        #获取数据
        mCHelper_tushare=CHelper_tushare()
        data=mCHelper_tushare.Get_balancesheet(my_ts_code=ShareNumber)
        data.to_csv(CsvPath,encoding="gbk") 
        #将数据导入到Mysql
        mCHelper_ImportDate=CHelper_ImportDate()
        mCHelper_ImportDate.ImportOneCvs(file=CsvPath,TableName=MyTableName,usecols=range(137),my_encoding='gbk')
        pass
    #获取一个公司的现金流量
    def MySql_ImportOneCashflow(self,ShareNumber="000001.SZ"):
        #生成路径
        code=ShareNumber[0:6]
        CsvPath=self.BasePath+code+'\\c'+code+'.csv'
        MyTableName='c'+code
        #检查路径
        mCHelper_File=CHelper_File()
        mCHelper_File.Creat(CsvPath)
        #获取数据
        mCHelper_tushare=CHelper_tushare()
        data=mCHelper_tushare.Get_cashflow(my_ts_code=ShareNumber)
        data.to_csv(CsvPath,encoding="gbk") 
        #将数据导入到Mysql
        mCHelper_ImportDate=CHelper_ImportDate()
        mCHelper_ImportDate.ImportOneCvs(file=CsvPath,TableName=MyTableName,usecols=range(90),my_encoding='gbk')
        pass
    #更新所有公司的财务数据
    def MySql_ImportAllIncome(self):
        #获取所有编号并生成一个列表
        data = pda.read_csv(self.BasePath+'ShareNumber.csv',encoding='gbk')
        data.values#获取所有的数据
        data2 = data.T#数据xy交换，为了得到y
        self.CodeList=data2.values[1]
        #开始采集 速度 1个/s
        for i in range(len(self.CodeList)):
            print(self.CodeList[i])
            try:
                self.MySql_ImportOneIncome(self.CodeList[i])
                self.MySql_ImportOneBalancesheet(self.CodeList[i])
                self.MySql_ImportOneCashflow(self.CodeList[i])
            except BaseException as ex:
                print(ex) 
            #time.sleep(0.8)
        pass

