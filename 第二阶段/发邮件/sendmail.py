# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "from@aragoncs.com"
receivers =["1120335370@qq.com"]

messages = MIMEText("Python发送邮件测试 ", "plain", "utf-8")
messages['From'] = Header("菜鸟教程", "utf-8")
messages['To'] = Header("测试", "utf-8")
messages['Subject'] = Header("Python SMTP 邮件测试", "utf-8")
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, messages.as_string())
except smtplib.SMTPException:
    print("邮件发送失败")
