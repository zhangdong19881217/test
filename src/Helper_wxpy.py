#微信模块
#安装方法   pip install -U wxpy
#快速安装方法 pip install -U wxpy -i "https://pypi.doubanio.com/simple/"
# 软件参考地址 https://wxpy.readthedocs.io/zh/latest/index.html

from wxpy import *#导入微信接口
import os
import threading
from Helper_shares import *#导入微信接口
#全局变量
bot = NullHandler;    
class CHelper_wxpy(object):
    def __init__(self): 
        bot = self.LognInit1()
        self.Tip()
        #接收消息
        @bot.register(except_self=False)
        def print_group_msg(self,msg):

            pass
    def Tip(self):
        self.SendMsgToSelf('\
                        1.回复a1 开始更新股票数据\
                        2.查询更新进度\
        ')
    #简单登录--------------------------------------------------------------------
    def LognInit(self):
        global bot
        bot= Bot()# 初始化机器人，扫码登陆
    #标准登录---------------------------------------------------------------------
        '''
    参数:	

        cache_path –
            设置当前会话的缓存路径，并开启缓存功能；为 None (默认) 则不开启缓存功能。
            开启缓存后可在短时间内避免重复扫码，缓存失效时会重新要求登陆。
            设为 True 时，使用默认的缓存路径 ‘wxpy.pkl’。
        console_qr –
            在终端中显示登陆二维码，需要安装 pillow 模块 (pip3 install pillow)。
            可为整数(int)，表示二维码单元格的宽度，通常为 2 (当被设为 True 时，也将在内部当作 2)。
            也可为负数，表示以反色显示二维码，适用于浅底深字的命令行界面。
            例如: 在大部分 Linux 系统中可设为 True 或 2，而在 macOS Terminal 的默认白底配色中，应设为 -2。
        qr_path – 保存二维码的路径
        qr_callback – 获得二维码后的回调，可以用来定义二维码的处理方式，接收参数: uuid, status, qrcode
        login_callback – 登陆成功后的回调，若不指定，将进行清屏操作，并删除二维码文件
        logout_callback – 登出时的回调

        '''
   
    def LognInit1(self):
        bot= Bot(cache_path=True,#缓存位置为当前路径  可以避免每次都扫描
                 #console_qr=True,
                 qr_path=os.getcwd()+"\\1.png",#二维码储存路径为当前目录
               #  qr_callback = CHelper_wxpy.CallBack_qr_callback,
               #  login_callback = CHelper_wxpy.CallBack_login_callback,
               #  logout_callback = CHelper_wxpy.CallBack_logout_callback
                 )# 初始化机器人，扫码登陆
        return bot
    #通过线程的方式登录，不会存在界面卡顿
    def LognInit2(self):
        t = threading.Thread(target=CHelper_wxpy.LognInit1,args =())
        t.setDaemon(True);#将线程设置为守护线程
        t.start()
        #t.join()
#    #获取二维码后的回调
    def CallBack_qr_callback(self,uuid, status, qrcode):
        print("已获取二维码")
    #登陆成功后的回调
    def CallBack_login_callback(self,):
        print("登陆成功")
    #登出时的回调
    def CallBack_logout_callback(self,):
        print("#登出")
    #给自己发送消息
    def SendMsgToSelf(self,str):
        if bot ==NullHandler:
            return
        # 机器人账号自身
        myself = bot.self
        # 向文件传输助手发送消息
        bot.file_helper.send(str)
    #获取所有好友
    def GetAllFriends(self):
        if bot ==NullHandler:
            return
        Friends = bot.friends()
        return Friends
    #获取所有性別好友 男MALE  女FEMALE
    def GetAllFriends1(self,in_sex = MALE):
        if bot ==NullHandler:
            return
        Friends = bot.friends()
        found = bot.friends().search(sex=in_sex)
        return found
    #通过名字查找一个好友，并判断唯一性  返回结果 <Friend: 马长春>
    def SerchFriends(self,name):
        if bot ==NullHandler:
            return
        found = bot.friends().search(name)
        result = ensure_one(found)#判断是否唯一
        return result
    #搜索所有群聊
    def SerchAllGroup(self,):
        if bot ==NullHandler:
            return
        wxpy_groups = bot.groups()
        #found = wxpy_groups[0].search() 获得群0的所有成员
        return wxpy_groups
    #搜索所有群聊
    '''
    参数:	

    user – 用户对象，或 user_name
    verify_content – 验证说明信息

    '''
    def AddFriend(self,):
        if bot ==NullHandler:
            return
        result = bot.add_friend(user="13418663731", verify_content='haha')
        return result
