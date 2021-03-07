import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import time
import board
import digitalio

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
time.sleep(5)


while True:
    led.value = True
    keyboard.send(Keycode.GUI, Keycode.R)
    time.sleep(0.1)
    layout.write("chrome\n")
    time.sleep(0.5)
    layout.write("http://www.5z8.info/worm_dvim \n")
    time.sleep(1)
    keyboard.send(Keycode.CONTROL, Keycode.T)
    time.sleep(0.5)
    layout.write("http://www.5z8.info/ip-stealer_fhli \n")
    keyboard.send(Keycode.F11)
    keyboard.send(Keycode.F6)
    time.sleep(1)
    keyboard.send(Keycode.CONTROL, Keycode.T)
    keyboard.send(Keycode.F11)
    keyboard.send(Keycode.F6)
    time.sleep(0.5)
    layout.write("http://www.5z8.info/trojan_zhgr \n")
    keyboard.send(Keycode.ENTER)
    keyboard.send(Keycode.F11)
    keyboard.send(Keycode.THREE)
    time.sleep(0.5)
    keyboard.send(Keycode.THREE)
    time.sleep(0.5)
    keyboard.send(Keycode.THREE)
    time.sleep(0.5)
    count = 100
    while count > 0:
        layout.write("you have been hacked")
        time.sleep(0.5)
        break
        count -= 1
    led.value = False
    break
    time.sleep(100)
