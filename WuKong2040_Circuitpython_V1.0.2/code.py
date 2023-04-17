from WuKong2040 import *

wk = WuKong2040()

while True:
    if wk.button_is_pressed():
        wk.motor("M1",100)
        wk.rainbow_led("all")
    if wk.button_is_pressed("ButtonB"):
        wk.motor()
        wk.rainbow_led("all",255,0,0)
    if wk.button_is_pressed("ButtonAB"):
        wk.motor("M1",-100)





