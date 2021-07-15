#数据库操作
# http://www.runoob.com/python3/python3-mysql.html
#  https://www.cnblogs.com/DswCnblog/p/6208726.html
#https://blog.csdn.net/u010746364/article/details/53078550    数据库指令
#http://www.w3school.com.cn/sql/sql_delete.asp      最好的参考资料
'''
安装环境：pip install PyMySQL
------主要函数---------------------------
pymysql.Connect()参数说明
host(str):      MySQL服务器地址
port(int):      MySQL服务器端口号
user(str):      用户名
passwd(str):    密码
db(str):        数据库名称
charset(str):   连接编码

connection对象支持的方法
cursor()        使用该连接创建并返回游标
commit()        提交当前事务
rollback()      回滚当前事务
close()         关闭连接

cursor对象支持的方法
execute(op)     执行一个数据库的查询命令
fetchone()      取得结果集的下一行
fetchmany(size) 获取结果集的下几行
fetchall()      获取结果集中的所有行
rowcount()      返回数据条数或影响行数
close()         关闭游标对象
------------------------------------------
'''
import pymysql
import re
from Helper_config import *
class CHelper_MySql(object):  
    #打开数据库的参数
    my_host='localhost'
    my_port=3306
    my_user='root'
    my_passwd='zhangdong1217'
    my_db='zhangdong'#数据库名称
    my_charset='utf8'#连接编码
    #操作句柄
    connect =None#数据库句柄
    cursor =None#创建一个游标对象
#----------------------------------------------------------------- 
    #初始化数据库信息
    def __init__(self,
                host='111.230.25.95',
                port=3306,
                user='root',
                passwd='zhangdong1217',
                db='zhangdong',
                charset='utf8'):
        mCHelper_config=CHelper_config()
        if mCHelper_config.IsServer:
            self.my_host='localhost'
        else:
            self.my_host=host
        self.my_port=port
        self.my_user=user
        self.my_passwd=passwd
        self.my_db=db
        self.my_charset=charset

#----------------------------------------------------------------- 
    #打开数据库
    def OpenMysql(self):
        try:
            #打开数据库
            self.connect  = pymysql.Connect(host=self.my_host,
                                       port = self.my_port,
                                       user=self.my_user,
                                       passwd=self.my_passwd,
                                       db=self.my_db,
                                       charset=self.my_charset)
            # 使用 cursor() 方法创建一个游标对象 cursor
            self.cursor = self.connect.cursor()
            return True            
        except BaseException as err:
            print("OpenMysql()",err)
            return False
#----------------------------------------------------------------- 
    #关闭数据库
    def CloseMysql(self):
        try:
            # 关闭数据库连接
            self.connect.close()
            self.connect = None
            self.cursor = None
        except BaseException as err:
            print("CloseMysql():",err)
        pass
#----------------------------------------------------------------- 
    #检查数据库打开状况
    def CheckOpen(self,):
        if self.connect == None:
            print("CHelper_MySql.connect = None")
            return False
        if self.cursor == None:
            print("CHelper_MySql.connect = None")
            return False
        return True


#----------------------------------------------------------------- 
    #读取数据库版本
    def ReadVersion(self):
        if self.CheckOpen()==False:
            print("ReadVersion()--CHelper_MySql.CheckOpen()==False")
            return False
        try:
            # 使用 execute()  方法执行 SQL 查询 
            self.cursor.execute("SELECT VERSION()")
            # 使用 fetchone() 方法获取单条数据.
            data = self.cursor.fetchone()
            print ("Database version : %s " % data)
            # 关闭数据库连接
            #self.connect.close()
            return True
        except BaseException as err:
            print("ReadVersion()",err)
            return False
#----------------------------------------------------------------- 
     #向数据库中添加表
#     sql='''
#                create table test2(
#                id int PRIMARY KEY AUTO_INCREMENT,
#                name VARCHAR(20) NOT NULL,
#                sex CHAR(4)
#                )
#            '''
#        CREATE TABLE `trade` (
#          `id` int(4) unsigned NOT NULL AUTO_INCREMENT,
#         `name` varchar(6) NOT NULL COMMENT '用户真实姓名',
#          `account` varchar(11) NOT NULL COMMENT '银行储蓄账号',
#          `saving` decimal(8,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '账户储蓄金额',
#          `expend` decimal(8,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '账户支出总计',
#          `income` decimal(8,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '账户收入总计',
#          PRIMARY KEY (`id`),
#          UNIQUE KEY `name_UNIQUE` (`name`)
 #       ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
 #       INSERT INTO `trade` VALUES (1,'乔布斯','18012345678',0.00,0.00,0.00);
    def AddTable(self,sql):
        if self.CheckOpen()==False:
            print("AddTable(sql)--CHelper_MySql.CheckOpen()==False")
            return False
        try:
            #执行sql语句
            mystr=self.cursor.execute(sql)
            #  获取执行结果
            result=self.cursor.fetchone()
            #关闭
            #self.connect.close()
        except BaseException as err:
            print("AddTable():",err)
            pass
#----------------------------------------------------------------- 
    #添加数据库
    #sql = "CREATE DATABASE test000"
    def AddDatabase(self,sql):
        if self.CheckOpen()==False:
            print("AddDatabase(sql)--CHelper_MySql.CheckOpen()==False")
            return False
        try:
            #执行sql语句
            mystr=self.cursor.execute(sql)
            return True
        except BaseException as err:
            print("AddDatabase(sql)",err)
            return False
#----------------------------------------------------------------- 
    #删除数据库
    #sql="drop database test000"
    def DelDatabase(self,sql):
        if self.CheckOpen()==False:
            print("DelDatabase(sql)--CHelper_MySql.CheckOpen()==False")
            return False
        try:
            #执行sql语句
            self.cursor.execute(sql)
            return True
        except BaseException as err:
            print("DelDatabase(sql)",err)
            return False
    #----------------------------------------------------------------- 
    #删除数据库中的表
    #sql1='use zhangdong2'    选择需要操作的数据库
    # sql2='drop table a'     选择需要删除的数据库名称
    def DelTable(self,sql1,sql2):
        if self.CheckOpen()==False:
            print("DelDatabase(sql)--CHelper_MySql.CheckOpen()==False")
            return False
        try:
            #执行sql语句
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
            return True
        except BaseException as err:
            print("DelDatabase(sql)",err)
            return False
    #----------------------------------------------------------------- 
    #删除表操作
    #sql="use zhangdong2"    选择需要操作的数据库
    #sql="truncate table stu"  删除后以新模板创建
    #sql="delete from stu"    删除表stu中的所有数据  必须有connect.commit()进行执行
    #sql="delete from stu where id>10"
    # 
    # sql1='use zhangdong'    选择需要操作的数据库
    # sql2="delete from stu"  
    def ClearTable(self,sql1,sql2):
        if self.CheckOpen()==False:
            print("DelDatabase(sql)--CHelper_MySql.CheckOpen()==False")
            return False
        try:
            sql3="delete from stu" 
            #执行sql语2句
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
            self.connect.commit()
            return True
        except BaseException as err:
            print("DelDatabase(sql)",err)
            return False
#----------------------------------------------------------------- 
    #查看所有数据库
    def ShowAllDatabase(self):
        if self.CheckOpen()==False:
            print("ShowAllDatabase()--CHelper_MySql.CheckOpen()==False")
            return False
        try:
            sql="show databases"
            #执行sql语句
            mystr=self.cursor.execute(sql)
            restlt = self.cursor.fetchall()
            print(restlt)
            return restlt
        except BaseException as err:
            print("ShowAllDatabase()",err)
            return False
#----------------------------------------------------------------- 
    #查看所有表   显示的是打开的数据库中的表
    def ShowAllTable(self):
        if self.CheckOpen()==False:
            print("DelDatabase(sql)--CHelper_MySql.CheckOpen()==False")
            return False
        try:
            sql="show tables"
            #执行sql语句
            mystr=self.cursor.execute(sql)
            restlt = self.cursor.fetchall()
            print(restlt)
            return restlt
        except BaseException as err:
            print("ShowAllTable()",err)
            return False
    #----------------------------------------------------------------- 
    #显示数据表的结构
    def ShowTableStructure(self):
        if self.CheckOpen()==False:
            print("DelDatabase(sql)--CHelper_MySql.CheckOpen()==False")
            return False
        try:
            sql="describe test2"
            mystr=self.cursor.execute(sql)
            restlt = self.cursor.fetchall()
            print(restlt)
            return restlt
        except BaseException as err:
            print("ShowTableStructure()",err)
            return False
    #----------------------------------------------------------------- 
    #向表中添加数据
    #sql = "insert into stu(id,name, age, sex) values (1, 'zhangdong', 30, '男')"
    def InsertTable(self,sql):
        if self.CheckOpen()==False:
            print("DelDatabase(sql)--CHelper_MySql.CheckOpen()==False")
            return False
        try:
            mystr=self.cursor.execute(sql)
            self.connect.commit() 
            return True
        except BaseException as err:
            print("InsertTable()",err)
            return False
    #----------------------------------------------------------------- 
    #更改表中添加数据
    #sql_update = 'UPDATE infor SET mail = "playstation.com" WHERE user_name = "Peter"'
    def UpdateTable(self):
        if self.CheckOpen()==False:
            print("DelDatabase(sql)--CHelper_MySql.CheckOpen()==False")
            return False
        try:
            sql = 'update stu set name = "hah" where id = 2'
            mystr=self.cursor.execute(sql)
            self.connect.commit() 
            return True
        except BaseException as err:
            print("InsertTable()",err)
            return False

    #检查表是否存在
    def CheckTable(self,table_name):        #这个函数用来判断表是否存在
        if self.CheckOpen()==False:
            print("CheckTable(self,table_name)==False")
            return False
        try:
            sql = "show tables;"
            self.cursor.execute(sql)
            tables = self.cursor.fetchall()#(('name',), ('stu',))
            table_list = []
            for table in tables:
                table_list.append(table[0])
            if table_name in table_list:
                return True
            else:
                return False

        except BaseException as err:
            print("CheckTable(self,table_name)",err)
            