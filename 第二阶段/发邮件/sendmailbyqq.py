#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: sendmailbyqq.py
@time: 2017/6/1 10:18

QQ邮箱 POP3 和 SMTP 服务器地址设置如下：
邮箱 POP3服务器（端口110） SMTP服务器（端口25） qq.com pop.qq.com smtp.qq.com SMTP服务器需要身份验证。

"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_mail_qq():
    try:
        sender = '1120335370@qq.com'
        receivers = ['1120335370@qq.com', '1239401141@qq.com']
        mail_host = 'smtp.qq.com'
        port = 25
        user = '1120335370@qq.com'
        pwd = 'zxcasdqwe123'
        create_receivers()
        message = MIMEText('Hello World! Nice to meet you', 'plain', 'utf-8')
        message['From'] = Header('1120335370@qq.com', 'utf-8')
        message['To'] = Header('1120335370@qq.com', 'utf-8')
        message['subject'] = Header('TestEmail', 'utf-8')
        s = smtplib.SMTP()
        s.connect(mail_host, port)
        s.login(user, pwd)
        s.sendmail(sender, receivers, message.as_string())
        print('Success')
    except smtplib.SMTPException as e:
        print('Fail', e)


def create_receivers():
    receivers = ['1120335370@qq.com', '1239401141@qq.com']
    receivers_list = ','.join(receivers)
    print(receivers_list)
    return receivers_list


if __name__ == '__main__':
    send_mail_qq()
