#线程测试  python 多线程只能实现并发，并不能提高执行效率
import threading
import time
num=0
lockA=threading.Lock()
sem = threading.BoundedSemaphore(3)# 信号量 最多允许3个线程访问资源
class CHelp_Threading_Test(object):
    def __init__(self): 
        pass 
    
    #功能函数
    def  run(self,str):
         print(str)
         print(threading.active_count)#打印线程存在的个数
         print(threading.current_thread())#当前活跃的线程
    #功能函数  线程锁演示  
    def  run1(self,str):
        lockA.acquire()
        global num
        num = num+1
       # time.sleep(1)
        lockA.release()
        print("str=",str,"num=",num)
        #print(str)
         #print(threading.active_count)#打印线程存在的个数
         #print(threading.current_thread())#当前活跃的线程
    #信号量的演示
    def  run2(self,str):
        sem.acquire()
        global num
        num = num+1
        # time.sleep(1)
        sem.release()
        print("str=",str,"num=",num)
    #简单演示线程的使用
    def  test(self):
         t1 = threading.Thread(target=CHelp_Threading_Test.run,args =("This is t1",))
         t2 = threading.Thread(target=CHelp_Threading_Test.run,args =("This is t2",))
         t1.start()
         t2.start()
    #开启50个线程
    def test1(self):
        for i in range(50):
            t = threading.Thread(target=CHelp_Threading_Test.run,args =(str(i),))
            t.start()
    #阻塞  这个实例会将线程变成串行（一个一个执行）
    def test2(self):
        for i in range(50):
            t = threading.Thread(target=CHelp_Threading_Test.run,args =(str(i),))
            t.start()
            t.join()#等待结果
    #阻塞  等待所有线程执行完 并行
    def test3(self):
        try:
            t_obj = []
            for i in range(50):
                t = threading.Thread(target=CHelp_Threading_Test.run,args =(str(i),))
                t.start()
                t_obj.append(t)
            for t in t_obj:
                t.join()
        except KeyError as e:
            print(e)
    #守护线程   线程被设置为守护线程后，主线程退出，从线程也会退出
    def test4(self):
        for i in range(50):
            t = threading.Thread(target=CHelp_Threading_Test.run,args =(str(i),))
            t.setDaemon(True);#将线程设置为守护线程
            t.start()
    #线程锁 避免一个资源被多个线程同时调用，从而出现问题
    def test5(self):
        t_obj = []
        for i in range(50):
            t = threading.Thread(target=CHelp_Threading_Test.run1,args =(str(i),))
            t.start()
            t_obj.append(t)
        for t in t_obj:
                t.join()
        print("end_num=",num)
    #线程信号量的演示
    def test6(self):
        t_obj = []
        for i in range(50):
            t = threading.Thread(target=CHelp_Threading_Test.run2,args =(str(i),))
            t.start()
            t_obj.append(t)
        for t in t_obj:
                t.join()
        print("end_num=",num)