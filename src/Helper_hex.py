#该模块用来解析stm32的hex文件
import re
import os
class CHelper_hex(object):
    hexPath = "c://hex"
    hexPathName = ""
    baseAddr = 0
    hexData = []
    hexLen = 0
    checkSum = 0
    def __init__(self): 
        pass 
    
    #获取Hex版本
    def GetVersion(self):
        dat = 0
        path = os.getcwd()+"\\hex\\"
        hexName =  os.listdir(path)
        if len(hexName) == 1: 
            self.hexPathName = path + hexName[0]
            str =  hexName[0][:-4]
            dat = int(str,10)

        return dat

    #查看软件是否需要更新
    def CheckVersion(self,myHexVersion=""):
        hexName =  os.listdir(self.hexPath)
        for str in hexName:
            if str.find(myHexVersion)>=0:
                self.hexPathName = self.hexPath+"//"+str
                return self.hexPathName
        return ""
    #读取Hex文件
    def getHex(self):
        self.hexData.clear()
        self.hexLen = 0
        self.checkSum = 0
        with open(self.hexPathName,'r') as f:
            print(self.hexPathName+' is opened!')

            for line in f.readlines():
                if(line[0] == ':'):
                    if(line[7:9] == '00'): #获取数据
                        datLen =  int(line[1:3],16)
                        self.hexLen += datLen
                        for len in range(datLen):
                          self.hexData.append(int(line[9+len*2:9+len*2+2],16))
                    elif(line[7:9] == '04'): #获取基地址
                        str = line[9:13]
                        self.baseAddr = int(str,16)<<16

        for i in range(self.hexLen):
            self.checkSum = self.checkSum^self.hexData[i]
        print("基地址:",self.baseAddr)
        print("len:",self.hexLen)
        print("checkSum:",self.checkSum)
        print(self.hexData)


                    