'''
声音的简单操作
安装环境：
    pip install pygame


#CHelper_img.FileShow("C://Users//Administrator//Pictures//1.jpg")
#CHelper_sound.RunSound2("C://Users//Administrator//Music//验证码（女）.mp3")  
CHelper_sound.test("C://Users//Administrator//Music//验证码.mp3", loops=10, start=0.0, value=0.5)
#os.system("C://Users//Administrator//Music//验证码（女）.mp3")  
'''
import time
import pygame
import os
import threading
class CHelper_sound(object):
    def __init__(self): 
        pass 
    def RunSound(self,file):
        pygame.mixer.init()
        track = pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.stop()
    def RunSound1(self,file):#这种调用会弹窗
        os.system(file) 
    def RunSound2(self,file):
        #song = AudioSegment.from_wav("never_gonna_give_you_up.wav")
        #song1 = AudioSegment.from_mp3(enPath)
        pass
    '''
    :param filename: 文件名
    :param loops: 循环次数
    :param start: 从多少秒开始播放
    :param value: 设置播放的音量，音量value的范围为0.0到1.0
    :return:
    '''
    def playMusic(self,filename, loops=0, start=0.0, value=0.5):
        flag = False  # 是否播放过
        pygame.mixer.init()  # 音乐模块初始化
        while 1:
            if flag == 0:
                pygame.mixer.music.load(filename)
                # pygame.mixer.music.play(loops=0, start=0.0) loops和start分别代表重复的次数和开始播放的位置。
                pygame.mixer.music.play(loops=loops, start=start)
                pygame.mixer.music.set_volume(value)  # 来设置播放的音量，音量value的范围为0.0到1.0。
            if pygame.mixer.music.get_busy() == True:
                flag = True
            else:
                if flag:
                    pygame.mixer.music.stop()  # 停止播放
                    break
    def  test(self,filename, loops=0, start=0.0, value=0.5):
         t1 = threading.Thread(target=CHelper_sound.playMusic,args =(filename, loops, start, value))
         t1.setDaemon(True);#将线程设置为守护线程
         t1.start()