# pylint: disable=import-error
# pylint: disable=undefined-variable
from lopy import HX711
from utime import sleep_us, sleep


def main():
    hx = HX711('P13', 'P14')
    hx.tare()
    count = 0
    while True:
        val = hx.read_average()
        print("Value " + str(count) + " is: " + str(val))
        count += 1
        pybytes.send_signal(2, val)
        sleep(2)

main()
