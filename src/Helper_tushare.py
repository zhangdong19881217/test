#股票模块
#使用该模块的程序用pyinstaller 打包会出现问题  执行不会出现问题
#本模块需要安装
#python中安装tushare及其依赖
#pip install lxml pandas requests bs4 tushare

import tushare as ts
import time
class CHelper_tushare(object):
    token = 'b01dfbe29d9283710cfb09bc1116386340372c495c38b2de04b290c3'
    def __init__(self): 
        ts.set_token(CHelper_tushare.token)
        pass 
    #################################################################################
    #查看当前版本
    #
    #################################################################################
    def  GetVersion(self):
        result = ts.__version__
        return  result
    #################################################################################
    #获取股票码列表
    #is_hs 	        str 	N 	是否沪深港通标的，N否 H沪股通 S深股通
    #list_status 	str 	N 	上市状态： L上市 D退市 P暂停上市
    #exchange 	    str 	N 	交易所 SSE上交所 SZSE深交所 HKEX港交所
    #调用示例
    '''
        data = mCHelper_tushare.GetShareList(my_exchange='SZSE',#交易所 SSE上交所 SZSE深交所 HKEX港交所   默认全部
                                         my_list_status='L', #上市状态： L上市 D退市 P暂停上市
                                         my_fields=
                                         'ts_code,'+ #TS代码
                                         'symbol,'+  #股票代码
                                         'name,'+#股票名称
                                         'area,'+#所在地域
                                         'industry,'+   #所属行业
                                         'fullname,'+#股票全称
                                         'enname,'+#英文全称
                                         'market,'+#市场类型 （主板/中小板/创业板）
                                         'exchange,'+#交易所代码
                                         'curr_type,'+#交易货币
                                         'list_status,'+#上市状态： L上市 D退市 P暂停上市
                                         'list_date,'+#上市日期
                                         'delist_date'#退市日期
                                         )
    data.to_csv('d:/000875.csv',encoding="utf_8_sig") 
    '''
    #################################################################################
    def  GetShareList(self):
        pro = ts.pro_api()
        data = pro.stock_basic(list_status='L')
        return  data
    #################################################################################
    #交易日历  主要是查看是否存在交易
    '''
    mCHelper_tushare = CHelper_tushare()
    data = mCHelper_tushare.IsOpen(my_exchange='', my_start_date='20180101', my_end_date='20181231')
    data.to_csv('d:/1.csv',encoding="utf_8_sig") 
    '''
    #################################################################################
    def  IsOpen(self,my_exchange='', my_start_date='20180101', my_end_date='20181231'):
        pro = ts.pro_api()
        result = pro.trade_cal(exchange=my_exchange, start_date=my_start_date, end_date=my_end_date)
        return  result
    #################################################################################
    #获取沪股通、深股通成分数据
    #
    #################################################################################
    def  Get_hs_const(self):
        pro = ts.pro_api()
        #获取沪股通成分
        df = pro.hs_const(hs_type='SH') 
        print(df)
        #获取深股通成分
        df = pro.hs_const(hs_type='SZ')
        print(df)
        #return  result
    #################################################################################
    #获取上市公司基础信息
    '''
s_code 	str 	Y 	股票代码
exchange 	str 	Y 	交易所代码 ，SSE上交所 SZSE深交所
chairman 	str 	Y 	法人代表
manager 	str 	Y 	总经理
secretary 	str 	Y 	董秘
reg_capital 	float 	Y 	注册资本
setup_date 	str 	Y 	注册日期
province 	str 	Y 	所在省份
city 	str 	Y 	所在城市
introduction 	str 	N 	公司介绍
website 	str 	Y 	公司主页
email 	str 	Y 	电子邮件
office 	str 	N 	办公室
employees 	int 	Y 	员工人数
main_business 	str 	N 	主要业务及产品
business_scope 	str 	N 	经营范围'''
    #################################################################################
    def  GetCompanyInfo(self):
        pro = ts.pro_api()
        #或者
        #pro = ts.pro_api('your token')
        df = pro.stock_company()
        #df = pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
        print(df)
    #################################################################################
    #获取新股上市列表数据
    #
    #################################################################################
    def  Get_new_share(self,my_start_date='20180901', my_end_date='20181018'):
        pro = ts.pro_api()
        df = pro.new_share(start_date=my_start_date, end_date=my_end_date)
        print(df)
    #################################################################################
    #获取上市公司财务利润表数据
    #df = pro.income(ts_code=my_ts_code, start_date=my_start_date, end_date=my_end_date)
    #################################################################################
    def  Get_Report(self,my_ts_code="600000.SH"):
        pro = ts.pro_api()
        df = pro.income(ts_code=my_ts_code)
        return df
    #################################################################################
    #获取上市公司资产负债表
    #
    #################################################################################
    def  Get_balancesheet(self,my_ts_code="600000.SH"):
        pro = ts.pro_api()
        df = pro.balancesheet(ts_code=my_ts_code)
        return df
    #################################################################################
    #获取上市公司现金流量表
    #################################################################################
    def  Get_cashflow(self,my_ts_code="600000.SH"):
        pro = ts.pro_api()
        df = pro.cashflow(ts_code=my_ts_code)
        return df
    #################################################################################
    #获取业绩预告数据
    #################################################################################
    def  Get_forecast(self, my_ann_date='20190131', my_end_date='20180730',path="d:\\1.csv"):
        pro = ts.pro_api()
        df=pro.forecast(ann_date=my_ann_date, fields='ts_code,ann_date,end_date,type,p_change_min,p_change_max,net_profit_min')
        df.to_csv(path,encoding="utf_8_sig") 
    #################################################################################
    #获取上市公司业绩快报
    #################################################################################
    def Get_express(self,my_ts_code="600000.SH"):
        MY_start_date='20180101'
        MY_end_date='20180701'
        pro = ts.pro_api()
        df = pro.express(ts_code=my_ts_code, start_date=MY_start_date, end_date=MY_end_date)
        return df