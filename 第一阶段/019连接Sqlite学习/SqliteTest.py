# -*- coding:utf-8 -*-
#导入SQLite驱动
import sqlite3

"""
Python 数据库学习
"""
# conn=sqlite3.connect('test.db')
# #创建一个Cursor
# cursor=conn.cursor()
# #创建user表
# create_user_table='create table user(id VARCHAR (20) PRIMARY key,name VARCHAR (20))'
# try:
#  cursor.execute(create_user_table)
# except Exception as e:
#     print(e)
# finally:
# #继续执行一条sql语句，插入一条纪录
#   cursor.execute('insert into user (id,name) values (\'1\',\'Michael\')')
#   print(cursor.rowcount)
# #关闭cursor
#   cursor.close()
# #提交事务
#   conn.commit()
# #关闭连接
#   conn.close()

#查询纪录
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
cursor.execute('select * from user where id=?',('1'))
#获取查询结果
values=cursor.fetchall()
print('values %s' % values)
print('value id %s name %s'% (values[0][0],values[0][1]))
