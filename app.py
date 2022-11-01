import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
import zipfile

path = "#####"# 此处填写存照片的文件夹路径
todaypath = path
todayfile = path + '.zip'


# 压缩文件夹函数
def zip_ya(startdir):
    file_news = startdir + '.zip'
    zp = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            zp.write(os.path.join(dirpath, filename), fpath + filename)
    zp.close()


# 发送邮件函数
def sendmail(path):
    host_server = 'smtp.qq.com'  # 使用qq邮箱smtp服务器
    sender_qq = '#########'  # sender_qq为发件人的qq号
    pwd = '########'  # pwd为qq邮箱的授权码
    sender_qq_mail = '######@qq.com'  # 发件人的邮箱
    receiver = ['#######@qq.com', '#######@qq.com']  # 收件人邮箱,'######@qq.com'
    mail_title = '今日份照片'  # 邮件标题

    smtp = smtplib.SMTP_SSL(host_server)  # ssl登录邮箱客户端
    smtp.set_debuglevel(0)  # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    ##定义邮箱内容
    msg = MIMEMultipart()  # 生成一个邮箱对象
    msg["Subject"] = Header(mail_title, 'utf-8')  # 添加邮箱主题
    msg["From"] = "##########@qq.com"  # 添加邮箱发送方
    msg["To"] = ";".join(receiver)  # 添加邮箱接收方

    ##添加正文
    text = "你好！这是今天的邮件！请查收！"
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)

    # 添加附件，这里以zip文件为例
    att = MIMEText(open(path, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename = {}'.format(path)

    msg.attach(att)
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    # 压缩今天的文件夹
    zip_ya(todaypath)
    # 发送邮件
    sendmail(todayfile)

    if os.path.exists("photos.zip"):  # 如果文件存在
        os.remove("photos.zip")
    else:
        print('no such file:%s' % "photos.zip")

