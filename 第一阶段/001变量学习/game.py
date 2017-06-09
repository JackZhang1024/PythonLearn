# -*- coding:utf-8 -*-
print('----------开始小游戏----------')
while True:
    temp = input("请输入你个数字\n")
    number = int(temp)
    if number == 8:
        print("真聪明，你猜对了！")
        print("游戏结束！")
        print("---------------一只小猫喵喵喵------------")
        break
    else:
        print("不好意思，你猜错了！")


