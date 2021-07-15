#发送邮件
import zmail
class CHelper_Zmail(object):
    def __init__(self): 
        pass 
    #发送一个邮件
    def SendMail(self,tittle='',text=''):
        # 你的邮件内容 
        mail_content = { 'subject': tittle, # 主题
        'content_text': text, #内容
        }
        # 使用你的邮件账户名和密码登录服务器 
        server = zmail.server('kxnlfd@163.com','zhangdong1217')
        # 发送邮件 
        server.send_mail('921201008@qq.com', mail_content)

        pass

