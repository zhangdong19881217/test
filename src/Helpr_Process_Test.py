
#多进程测试
import time
import multiprocessing
from multiprocessing import Process,Queue#用于进程见的数据通信
from multiprocessing import Process,Pipe#  以管道的方式建立数据的通讯
from multiprocessing import Process,Manager# 实现数据的共享
pepo1,pepo2=Pipe()
class CHelp_Threading_Test(object):
    def __init__(self): 
        pass 
    #进程执行程序
    def run(self,str):
        print(str)
    #进程执行程序  设置进程通信的变量
    def run1(self,q):
        q.put(["1122","zhangdong"])
    #进程执行程序  设置进程通信的变量
    def run2(self,q):
        print(q.get())
    #管道的形式通讯，放入数据
    def run3(self,pepo):
        pepo.send(["1111","zhangdong"])
        pepo.close()
        print(pepo.recv())
    #管道的形式通讯，取出数据
    def run4(self,pepo):
        print(pepo.recv())
     #进程数据共享
    def run5(self,pepo):
        pepo[1] = "zhangdong"
     #进程数据共享
    def run6(self,pepo):
        print(pepo[1])
    #简单的启用一个进程
    def test(self):
        p = multiprocessing.Process(target = CHelp_Threading_Test.run, args = ("112233",))
        p.start()
        p.join()
    #演示进程间的通信
    def test1(self):
        q = Queue()
        p1 = multiprocessing.Process(target = CHelp_Threading_Test.run1, args = (q,))
        p2 = multiprocessing.Process(target = CHelp_Threading_Test.run2, args = (q,))
        p1.start()
        p2.start()
        #p.join()
    #演示进程间的通信（以管道的方式）
    def test2(self):
        p1 = multiprocessing.Process(target = CHelp_Threading_Test.run3, args = (pepo1,))
        p2 = multiprocessing.Process(target = CHelp_Threading_Test.run4, args = (pepo2,))
        p1.start()
        p1.join()
        p2.start()
        p2.join()


    #演示进程间数据共享
    def test3(self):
        with Manager() as  manager:
            d = manager.dict()#生成一个字典可以在进程间传递
            d[1] = "112233"
            p1 = Process(target = CHelp_Threading_Test.run5, args = (d,))
            p2 = Process(target = CHelp_Threading_Test.run6, args = (d,))
            p1.start()
            p2.start()
            p1.join()
            p2.join()