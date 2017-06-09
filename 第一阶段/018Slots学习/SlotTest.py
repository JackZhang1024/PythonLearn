# -*- coding:utf-8 -*-

class MyLimeter(object):
    __slots='myname','myage','myhobby'

if __name__=='__main__':
    x=MyLimeter()
    x.myname='lisi'
    x.myage=20
    x.myhobby='song'
    x.girlfriend='lili'
    print(x.myname,x.myhobby,x.myage,x.girlfriend)

