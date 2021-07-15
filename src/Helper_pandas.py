#pandas模块的演示 数据索引 行列操作
import pandas as pds #取别名
class CHelper_pandas(object):
    def __init__(self): 
        pass 
    #常规演示  系统默认索引 情况和数组类似
    def test0(self):
        a = pds.Series([0,7,7,2,5,4,1,9,0,5,3,4,2,6,4,8])
        print(a)
        print(a[3])
        pass
    #指定字段索引
    def test1(self):
        a = pds.Series([8,9,2,1],index=["a","b","c","d"])
        print(a)
        print(a["c"])
        pass
    #数据框的演示  能够进行行列操作
    def test2(self):
        a = pds.DataFrame([[1,2,3,4],[7,5,1,3],[0,5,7,9],[9,8,4,5]])
        print(a)
        b = pds.DataFrame([[1,2,3,4],[7,5,1,3],[0,5,7,9],[9,8,4,5]],columns=["a","b","c","d"])#指定列名
        print(b)
        c=pds.DataFrame({
        "a":4,
        "b":[6,2,3],
        "c":list(str(982))
        })
        print(c)
        m=c.head()#默认显示前5行
        print(m)
        m=c.head(2)#显示前2行
        print(m)
        m=c.tail(2)#显示后2行（无参数默认5行）
        print(m)
        pass
    #数据统计
    '''
   0  1  2  3
0  1  2  3  4
1  7  5  1  3
2  0  5  7  9
3  9  8  4  5
              0        1     2         3
count  4.000000  4.00000  4.00  4.000000
mean   4.250000  5.00000  3.75  5.250000
std    4.425306  2.44949  2.50  2.629956
min    0.000000  2.00000  1.00  3.000000
25%    0.750000  4.25000  2.50  3.750000
50%    4.000000  5.00000  3.50  4.500000
75%    7.500000  5.75000  4.75  6.000000
max    9.000000  8.00000  7.00  9.000000
分位数介绍：https://blog.csdn.net/bitcarmanlee/article/details/71211701
1.按列统计
2.count 表示每列有多少个元素
3.mean 表示平均数
4.std 标准差
5.数据中的最小值
6.25% 50% 75%  分位数  数据区间
7.max 每一列的最大值
'''
    def test3(self):
        a = pds.DataFrame([[1,2,3,4],[7,5,1,3],[0,5,7,9],[9,8,4,5]])
        print(a)
        print(a.describe())
    #数据转置 行和列调换
    def test(self):
        a = pds.DataFrame([[1,2,3,4],[7,5,1,3],[0,5,7,9],[9,8,4,5]])
        print(a)
        b = a.T
        print(b)