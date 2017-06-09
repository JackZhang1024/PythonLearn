# -*- coding:utf-8 -*-
"""
演示如何连接Mysql服务器的test数据库
"""

import mysql.connector

conn=mysql.connector.connect(user='root',password='123456',database='test')
# cursor=conn.cursor()
# #创建User表
# cursor.execute('create table user (id VARCHAR (20) PRIMARY KEY ,name VARCHAR (20))')
# #插入一条纪录
# cursor.execute('insert into user (id,name) values(%s,%s)',['1','Michael'])
# cursor.rowcount
#
# #提交事务
# conn.commit()
# cursor.close()

#进行查询操作
#注意：查询后面的 '1'后面有个,号
cursor=conn.cursor()
cursor.execute('select * from user where id=%s',('1',))
values=cursor.fetchall()
print('result %s ' % values)
#关闭cursor和connection
cursor.close()
conn.close()