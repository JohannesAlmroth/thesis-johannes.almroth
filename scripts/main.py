# pylint: disable=import-error
from lopy import HX711
from utime import sleep_us, sleep

hx = HX711('P13', 'P14')
hx.tare()
normal = False
count = 0
while True:
    val = hx.read_average()
    if (val < 100) and normal:
        print("Normal levels")
        flag = False
    if val > 100:
        count += 1
        flag = True
        print("Spike nr " + str(count) + " at: " + str(val))
        
