#文件操作的演示程序
import csv
'''
------------------------------------------------------------
模式	描述
t	文本模式 (默认)。
x	写模式，新建一个文件，如果该文件已存在则会报错。
b	二进制模式。
+	打开一个文件进行更新(可读可写)。
U	通用换行模式（不推荐）。
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
------------------------------------------------------------
w     以写方式打开，
a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+     以读写模式打开
w+     以读写模式打开 (参见 w )
a+     以读写模式打开 (参见 a )
rb     以二进制读模式打开
wb     以二进制写模式打开 (参见 w )
ab     以二进制追加模式打开 (参见 a )
rb+    以二进制读写模式打开 (参见 r+ )
wb+    以二进制读写模式打开 (参见 w+ )
ab+    以二进制读写模式打开 (参见 a+ )
------------------------------------------------------------
以下是和file对象相关的所有属性的列表
file.closed	返回true如果文件已被关闭，否则返回false。
file.mode	返回被打开文件的访问模式。
file.name	返回文件的名称。
file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true。

# 打开一个文件
fo = open("foo.txt", "w")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
---------------------------------------------------------------
目录操作：
os.mkdir("file")                   创建目录
复制文件：
shutil.copyfile("oldfile","newfile")       oldfile和newfile都只能是文件
shutil.copy("oldfile","newfile")            oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
复制文件夹：
shutil.copytree("olddir","newdir")        olddir和newdir都只能是目录，且newdir必须不存在
重命名文件（目录）
os.rename("oldname","newname")       文件或目录都是使用这条命令
移动文件（目录）
shutil.move("oldpos","newpos")   
删除文件
os.remove("file")
删除目录
os.rmdir("dir")只能删除空目录
shutil.rmtree("dir")    空目录、有内容的目录都可以删
转换目录
os.chdir("path")   换路径
---------------------------------------------------------------
文件操作：
os.mknod("test.txt")        创建空文件
fp = open("test.txt",w)     直接打开一个文件，如果文件不存在则创建文件

关于open 模式：

w     以写方式打开，
a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+     以读写模式打开
w+     以读写模式打开 (参见 w )
a+     以读写模式打开 (参见 a )
rb     以二进制读模式打开
wb     以二进制写模式打开 (参见 w )
ab     以二进制追加模式打开 (参见 a )
rb+    以二进制读写模式打开 (参见 r+ )
wb+    以二进制读写模式打开 (参见 w+ )
ab+    以二进制读写模式打开 (参见 a+ )

 

fp.read([size])                     #size为读取的长度，以byte为单位

fp.readline([size])                 #读一行，如果定义了size，有可能返回的只是一行的一部分

fp.readlines([size])                #把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分。

fp.write(str)                      #把str写到文件中，write()并不会在str后加上一个换行符

fp.writelines(seq)            #把seq的内容全部写到文件中(多行一次性写入)。这个函数也只是忠实地写入，不会在每行后面加上任何东西。

fp.close()                        #关闭文件。python会在一个文件不用后自动关闭文件，不过这一功能没有保证，最好还是养成自己关闭的习惯。  如果一个文件在关闭后还对其进行操作会产生ValueError

fp.flush()                                      #把缓冲区的内容写入硬盘

fp.fileno()                                      #返回一个长整型的”文件标签“

fp.isatty()                                      #文件是否是一个终端设备文件（unix系统中的）

fp.tell()                                         #返回文件操作标记的当前位置，以文件的开头为原点

fp.next()                                       #返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。

fp.seek(offset[,whence])              #将文件打操作标记移到offset的位置。这个offset一般是相对于文件的开头来计算的，一般为正数。但如果提供了whence参数就不一定了，whence可以为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。需要注意，如果文件以a或a+的模式打开，每次进行写操作时，文件操作标记会自动返回到文件末尾。

fp.truncate([size])                       #把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。如果size比文件的大小还要大，依据系统的不同可能是不改变文件，也可能是用0把文件补到相应的大小，也可能是以一些随机的内容加上去。

'''
import threading
import os
class CHelper_File(object):
    def __init__(self): 
        pass 
    #创建文件夹和文件
    def Creat(self,File):
        #获取文件路径
        path=os.path.dirname(File)
        FileName=os.path.basename(File)
        #创建文件夹
        if path!='':
            self.CheckDir(path)
        #创建文件
        if FileName!='':
            fp= open(File, "w+")
            fp.close()

    #没有文件则创建，有的话追加内容
    def FileAdd(self,FileName,text):
        fp= open(FileName, "a+")
        fp.write(text) 
        fp.close()
        return "null"
    #以追加的形式写入csv
    def CsvAdd(self,stu1 = ['marry',26,28]):
        fp = open('d://Stu_csv.csv','a', newline='')
        csv_write = csv.writer(fp,dialect='excel')#设定写入模式
        csv_write.writerow(stu1)
        fp.close()
        return "null"
    #查看文件夹是否存在，不存在就创建一个 'D:/olddata'
    def CheckDir(self,PathName):
        if not os.path.isdir(PathName):
            os.makedirs(PathName) 
    
    #查看文件是否存在
    def CheckFile(self,File):
        return os.path.isdir(File)
    #列出目录下的所有文件   
    def ListFiles(self,filepath):
        files= os.listdir(filepath)
        print(files)