# coding:utf-8
import smtplib  #加载smtplib模块from email.mime.text import MIMEText
from email.mime.text import MIMEText
from email.utils import formataddr
class SendEmail(object):
    def mail(self,user_list,sub,content):
        my_sender='' #发送邮箱

        msg=MIMEText(content,'plain','utf-8')
        msg['From']=formataddr(["发件人邮箱昵称",my_sender])
        msg['To']=formataddr(["收件人邮箱昵称",user_list])
        msg['Subject']=sub

        server=smtplib.SMTP("smtp.126.com",25)
        server.login(my_sender,"")    #密码
        server.sendmail(my_sender,[user_list],msg.as_string())
        server.quit()

    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num+fail_num

        pass_result = "%.2f%%" %(pass_num/count_num*100)
        fail_result = "%.2f%%" %(fail_num/count_num*100)

        user_list = ''#接收邮箱
        sub = "接口自动化测试报告"
        content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" %(count_num,pass_num,fail_num,pass_result,fail_result )
        self.mail(user_list,sub,content)
if __name__ == '__main__':
    a = [1,2,3,4]
    b = [2,3,4,5,6,7]
    ret = SendEmail()
    data = ret.send_main(a,b)


# from email.mime.text import MIMEText
# from email.header import Header
# from smtplib import SMTP_SSL
#
# #qq邮箱smtp服务器
# host_server = 'smtp.126.com'
# #sender_qq为发件人的qq号码
# sender_qq = 'zl919460849@126.com'
# #pwd为qq邮箱的授权码
# pwd = 'love340827' ## xh**********bdc
# #发件人的邮箱
# sender_qq_mail = 'zl919460849@126.com'
# #收件人邮箱
# receiver = '919460849@qq.com'
#
# #邮件的正文内容
# mail_content = '你好，这是使用python登录qq邮箱发邮件的测试'
# #邮件标题
# mail_title = 'Maxsu的邮件'
#
# #ssl登录
# smtp = SMTP_SSL(host_server)
# #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
# smtp.set_debuglevel(1)
# smtp.ehlo(host_server)
# smtp.login(sender_qq, pwd)
#
# msg = MIMEText(mail_content, "plain", 'utf-8')
# msg["Subject"] = Header(mail_title, 'utf-8')
# msg["From"] = sender_qq_mail
# msg["To"] = receiver
# smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
# smtp.quit()
