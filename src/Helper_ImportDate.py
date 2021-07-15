#数据导入
import os
import numpy
import csv
import pandas as pds #取别名
from Helper_File import *
from Helper_MySql import *
from Helper_config import *
from datetime import datetime
from sqlalchemy.types import NVARCHAR, Float, Integer
from sqlalchemy import create_engine
class CHelper_ImportDate(object):
    def __init__(self): 
        pass 
    #------------------------------------------
    #导入csv并做简单分析 D:/olddata/000001.csv
    def test0(self,file=""):
        mCHelper_File = CHelper_File()
        if not mCHelper_File.CheckFile(file):
            print("不存在文件：",file)
        a = pds.read_csv(file,encoding='gbk')
        #print(a.describe())#输出简单的分析
        #print(a.sort_values(by="收盘价"))#按照收盘价进行排序
    #------------------------------------------
    #导入excel并做简单分析 D:/olddata/000001.xlsx
    def test1(self,file=""):
        mCHelper_File = CHelper_File()
        if not mCHelper_File.CheckFile(file):
            print("不存在文件：",file)
        a = pds.read_excel(file,encoding='gbk')
    #------------------------------------------ 
    #将采集的数据导入到数据库
    '''
    调用方法：
    mCHelper_shares.GetAllCsv(path="D:/olddata/",mystarttime="",myendtime="20190111")
    mCHelper_ImportDate.ImportAllCvs('D:/olddata/')
    '''
    # pandas类型和sql类型转换 
    def map_types(self,df):
        dtypedict = {}
        for i,j in zip(df.columns,df.dtypes):
            if "object" in str(j): 
                dtypedict.update({i: NVARCHAR(length=255)}) 
            if "float" in str(j): 
                dtypedict.update({i: Float(precision=2, asdecimal=True)}) 
            if "int" in str(j): 
                dtypedict.update({i: Integer()}) 
        return dtypedict

    #将一个csv文件导入数据库 D:/olddata/000001.csv   usecols 为读取的列
    #tushare 中  encoding='utf_8_sig'
    #其他    encoding='gbk'    
    def ImportOneCvs(self,file,TableName,usecols=[0, 3, 4, 5, 6, 11],my_encoding='gbk'):
        # 连接设置 连接mysql 用户名ffzs 密码666 地址localhost：3306 database：stock
        mCHelper_config=CHelper_config()
        if mCHelper_config.IsServer:
            engine = create_engine('mysql+pymysql://root:zhangdong1217@localhost:3306/zhangdong')
        else:
            engine = create_engine('mysql+pymysql://root:zhangdong1217@111.230.25.95:3306/zhangdong')
        # 建立连接
        con = engine.connect()
        #读取数据
        df = pds.read_csv(file, encoding=my_encoding,usecols=usecols)
        dtypedict = self.map_types(df) 
        # 通过dtype设置类型 为dict格式{“col_name”:type} 
        df.to_sql(name=TableName, con=con, if_exists='replace', index=False, dtype=dtypedict)
        
        pass
    def ImportAllCvs(self,FilePath):
        files= os.listdir(FilePath)
        for file in files:
            name =file[:-4]
            #name = name.encode("UTF-8")
            myfile=FilePath+file
            #myfile = myfile.encode("UTF-8")
            print(name)
            print(myfile)
            try:
                self.ImportOneCvs(file=myfile,TableName=name)
            except BaseException as er:
                print(er)   
        pass
    #------------------------------------------ 
    #从数据库中读取数据 "select * from `000017`"
    def ReadMySql(self,sql):
        mCHelper_MySql=CHelper_MySql(
                host='111.230.25.95',
                port=3306,
                user='root',
                passwd='zhangdong1217',
                db='zhangdong',
                charset='utf8')
        mCHelper_MySql.OpenMysql()
        a=pds.read_sql(sql,mCHelper_MySql.connect)
        print(a.describe())
        pass
    #------------------------------------------ 
    #从网页中读取表格
    def ReadHtml(self):
        a = pds.read_html("http://quote.stockstar.com/stock/szb.shtml")
        print(a)
        pass
    #------------------------------------------ 
    #导入文本
    def ReadText(self):
        a = pds.read_table("d://1.txt")
        a= a.encode("utf-8")
        print(a)
        pass

