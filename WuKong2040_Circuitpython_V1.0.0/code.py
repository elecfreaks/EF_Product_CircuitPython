from WuKong2040 import *

wk = WuKong2040()
while True:
    if wk.buttonA_ispressed():		#如果按键按下返回True
        wk.motor("M1", 100)			# 设置M3速度为100，  参数1为电机序号   参数2为速度
        wk.rainbow_all(0, 10 ,0)
        #music.play(music.DADADADUM) # 同picoed用法
        
    if wk.buttonB_ispressed(): # 如果按键B按下返回True
        wk.motor("M1", -100)			# 设置M3速度为100，  参数1为电机序号   参数2为速度
        wk.rainbow_led(0, 0, 0 ,0)	#设置彩虹灯， 参数1为灯号，参数2为红色 ，参数三为绿色 参数四为蓝色 范围均为0-255
        wk.rainbow_led(1, 0, 0 ,0)
        
    if wk.buttonAB_ispressed(): # 如果按键A和B一起按下返回True
        wk.motorStop("M3")


