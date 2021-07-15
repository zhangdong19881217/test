#数据可视化处理 
# #折线图/散点图 plot
#直方图 hist
import matplotlib.pylab as pyl
import numpy as npy
import numpy
import os
import pandas as pda

class CHelper_DigitaMap(object):
    def __init__(self): 
        pass 
    #简单折线图演示
    def test0(self):
        x=[1,2,3,4,5]
        y=[5,7,2,1,5]
        pyl.plot(x,y)#x数据  y数据 展现形式（默认折现图 “o”散点图）（可有可无折线图/散点图）
        pyl.show()
        pass
    #简单散点图演示
    def test1(self):
        x=[1,2,3,4,5]
        y=[5,7,2,1,5]
        pyl.plot(x,y,"o")
        pyl.show()
        pass
    #简单散点图演示 颜色演示
    '''
    选项 	意义
c 	cyan -青色
r 	red 红色
m 	magente 品红
g 	green 绿色
b 	blue 蓝色

选项 	意义
- 	普通的直线
-- 	虚线
-. 	一杠一点
: 	细小的虚线

选项 	意义
s 	方形
h 	六角形
H 	六角形
* 	星形
+ 	加号的形式
x 	x形
d 	菱形
D 	菱形
p 	五角形状
    '''
    def test2(self):
        x=[1,2,3,4,5]
        y=[5,7,2,1,5]
        pyl.plot(x,y,"ro--")
        pyl.title("Title")#标题
        pyl.xlabel("x-name")#x 名称
        pyl.ylabel("y-name")#y 名称
        #pyl.xlim(0,20)#x 范围
        #pyl.ylim(5,18)#y 范围
        #添加第二条线段
        x2=[0,1,6,8,9]
        y2=[0,3,4,6,9]
        pyl.plot(x2,y2,"ro--")
        pyl.show()
        pass
    #普通直方图
    def test3(self):
        data = npy.random.normal(10.0,1.0,10000)#平均值10 陡峭度1.0 生成10000个    
        pyl.hist(data)
        sty=npy.arange(2,17,4)#范围2~17 步长4（宽度）
        pyl.show() 
    #直方图
    def test4(self):
        data = npy.random.random_integers(1,25,1000)
        sty=npy.arange(2,30,1)#范围  步长 （宽度）
       # pyl.hist(data,sty)#str指形式
        pyl.hist(data,sty,histtype='stepfilled')#str指形式 stepfilled取消轮廓
        pyl.show()
    #多个直方图
    def test5(self):
        data = npy.random.random_integers(1,25,1000)
        sty=npy.arange(2,30,1)#范围  步长 （宽度）
        pyl.subplot(2,2,3) #两行两列第三个位置
        pyl.hist(data,sty,histtype='stepfilled')#str指形式 stepfilled取消轮廓
        pyl.show()
    #简单绘制股票数据
    # code 股票代码
    # 图片需要保存的路径  "D:/pic/"
    def GetOnePng(self,csvFile="D:/olddata/1.csv",pngFile="D:/pic/1.png"):
        data = pda.read_csv(csvFile,encoding='gbk')
        data.values#获取所有的数据
        data2 = data.T#数据xy交换，为了得到y
        xdata=[]
        ydata=[]
        #清除0数据
        for m in range(len(data2.values[3])):
            if data2.values[3][m]!=0:
                xdata.append(data2.values[0][m])
                ydata.append(data2.values[3][m])
        if len(xdata)==0:
            return
        pyl.figure(figsize=(24, 26)) #窗口大小 600 * 650
        pyl.plot(xdata,ydata)
        pyl.savefig(pngFile)#保存图片
        pyl.close()
        pyl.clf()
        #pyl.show()
        pass
    #分析所有的股票得到所有的图片
    def GetAll(self,csvFilePath="D:/olddata/",pngFilePath="D:/pic/"):
        files= os.listdir(csvFilePath)
        for file in files:
            name =file[:-4]
            myCsvFile=csvFilePath+file
            myPngFile=pngFilePath+name+".png"
            print(name)
            try:
                self.GetOnePng(csvFile=myCsvFile,pngFile=myPngFile)
                pass
            except BaseException as err:
                print(err)
                pass
        pass