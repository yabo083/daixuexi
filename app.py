import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
import zipfile

path = "D:\Code\daixuexi\photos"
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
    sender_qq = '2657455842'  # sender_qq为发件人的qq号
    pwd = 'xbetfxykhvxvebee'  # pwd为qq邮箱的授权码
    sender_qq_mail = '2657455842@qq.com'  # 发件人的邮箱
    receiver = ['2657455842@qq.com', '2674180551@qq.com']  # 收件人邮箱,'2534096833@qq.com'
    mail_title = '今日份照片'  # 邮件标题

    smtp = smtplib.SMTP_SSL(host_server)  # ssl登录邮箱客户端
    smtp.set_debuglevel(0)  # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    ##定义邮箱内容
    msg = MIMEMultipart()  # 生成一个邮箱对象
    msg["Subject"] = Header(mail_title, 'utf-8')  # 添加邮箱主题
    msg["From"] = "2657455842@qq.com"  # 添加邮箱发送方
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

# # 创建文件夹函数
# def mkdir(path):
#     folder = os.path.exists(path)
#     if not folder:
#         os.makedirs(path)
#         print("创建文件夹成功")
#     else:
#         print("文件夹已存在")


# 获取今天明天昨天的日期
# today = datetime.date.today().strftime("%Y%m%d")
# tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y%m%d")
# yesterday = (datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y%m%d")

# 定义文件路径


# # 定义昨天的压缩文件
# yesterdayfile = path + yesterday + '.zip'
# uyesterdayfile = yesterdayfile

# # 计算今天文件夹下的文件个数
# filenum = 0
# for filename in os.listdir(utodaypath):
#     filenum += 1

# 创建明天的文件夹
# mkdir(utomorrowpath)

# 删除昨天的压缩文件
# if os.path.exists(uyesterdayfile):  # 如果文件存在
#     os.remove(uyesterdayfile)
# else:
#     print('no such file:%s' % uyesterdayfile)

# # 获取今天是周几
# weekoftoday = datetime.date.today().weekday()
# # 节假日列表
# holiday = ['20180924', '20181001', '20181002', '20181003', '20181004', '20181005']
# # 补班列表
# workday = ['20180924', '20180925']
#
# # 是否是周末
# isweekend = (weekoftoday == 5 or weekoftoday == 6)
# # 是否是小长假
# isholiday = today in holiday
# # 是否不要补班
# isworkday = today not in workday
# # 文件夹是否为空
# isnullfile = (filenum == 0)
#
# # 判断是否要压缩文件并发送邮件
# # 周末、工作日放假的节假日、文件夹为空时不执行
# # 补班的周末例外
# if isnullfile:
#     pass
# else:
#     if ((isweekend or isholiday) and isworkday):
#         pass
#     else:
