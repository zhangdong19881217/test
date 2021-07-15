'''
图片的简单操作
安装环境：
pip install Pillow

'''
from PIL import Image
class CHelper_img(object):
    def __init__(self): 
        pass 
    #显示图片
    def FileShow(self,FileName):
        try: 
            im = Image.open(FileName)
            im.show()
        except BaseException as e: 
            print("打开图片失败,错误码：",e)
            pass
