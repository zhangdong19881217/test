#NumPy模块的演示   关于数组的一些操作
import numpy
class CHelper_NumPy(object):
    def __init__(self): 
        pass 
    #常规演示
    def test0(self):
        a = numpy.array([1,2,3,4,5])
        print(a[0])
        a[0] = 10
        print(a[0])
        pass
    #数组排序
    def test1(self):
        a = numpy.array([0,7,7,2,5,4,1,9,0,5,3,4,2,6,4,8])
        a.sort()
        print(a)
    #最大值与最小值
    def tes2(self):
        a = numpy.array([0,7,7,2,5,4,1,9,0,5,3,4,2,6,4,8])
        print(a.max())
        print(a.min())
    #切片运算
    def test3(self):
        a = numpy.array([0,7,7,2,5,4,1,9,0,5,3,4,2,6,4,8])
        print(a[1:5])#从第1位开始到第（5-1）个结束
    #生产随机数
    def test4(self):
        data = numpy.random.random_integers(1,20,10) #范围是1-20 生成10个随机数
        pass