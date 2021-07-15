#本模块需要安装  serial  指令  pip3 install pyserial
from ast import Try
import threading

import serial
import serial.tools.list_ports
class CHelper_Serial(object):
    def __init__(self): 
        pass 
    '''打开串口'''
    def  GetPortName(self):
         list0 = []
         list1 = []
         PortInfo = serial.tools.list_ports.comports()
         for i in range(len(PortInfo)):
             list0.append(PortInfo[i][0])
             list1.append(PortInfo[i][1])
         return list0,list1


    '''读取数据，在线程中调用'''
    def ReadData(self,ser,buff):
        try:
            while ser.is_open:
                if ser.in_waiting:
                    rev = ser.read(ser.in_waiting)#.decode("gbk")
                    self.fifoWrite(buff,rev)
                    #print(buff)
        except Exception as e:
           # print(e)
            pass

    '''打开串口'''
    def openCom(self,comName,comBaud):
        ret=False
        buff = []
        try:
            # 打开串口，并得到串口对象
            ser = serial.Serial(comName, comBaud)
            #判断是否打开成功
            if(ser.is_open):
                ret=True
            threading.Thread(target=self.ReadData, args=(ser,buff)).start()
        except Exception as e:
            return None,False
            pass
        return ser,ret,buff

    '''关闭串口'''
    def closeSerial(self,ser):
        try:
            ser.close()
        except Exception as e:
            #print('异常：',e)
            pass

    '''发送字符串数据'''
    def sendString(self, ser,text):
        try:
            result = ser.write(text.encode("gbk"))  # 写数据
        except Exception as e:
            result = False
            #print('异常：', e)
        #print('发送结果',result)
        return result
    '''发送字节数据'''
    def sendBytes(self, ser,buff):
        try:
            result = ser.write(buff)  # 写数据
        except Exception as e:
            result = False
            #print('异常：', e)
        #print('发送结果',result)
        return result
    '''读取FIFO内容'''
    def fifoRead(self,buff):
        cRet = 1
        dat = 0
        if len(buff) == 0:
            cRet = 0
        else:
            dat = buff.pop(0)
        return cRet,dat
    '''写FIFO内容'''
    def fifoWrite(self,buff,dat):
        cRet = 1
        for i in range(len(dat)):
            buff.append(dat[i])
        return cRet

