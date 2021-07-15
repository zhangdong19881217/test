#配置文件
import os
class CHelper_config(object):
    IsServer=True  #False---pc   True----Server
    ShareThreadNum=5  #采集股票历史数据的线程个数 
    ShareBasePath='D:\\share\\' #
    def __init__(self): 
        if self.IsServer:
            self.ShareBasePath='c:\\share\\'
            pass
        else:
            self.ShareBasePath='d:\\share\\'
            pass
