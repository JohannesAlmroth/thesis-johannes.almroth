# pylint: disable=no-member
# pylint: disable=import-error
# pylint: disable=undefined-variable

import pycom
import time
import os
import ure
from network import WLAN


def blink():
    """Loud and clear heartbeat function
    """
    pycom.heartbeat(False)
    for _ in range(100):  # stop after 100 cycles
        pycom.rgbled(0x007F00)  # green
        time.sleep(1)
        pycom.rgbled(0x7F7F00)  # yellow
        time.sleep(1)
        pycom.rgbled(0x7F0000)  # red
        time.sleep(1)


def wifi():
    """Connects to a Wifi-network

    Uses ssid-key value pairs stored in .env file in root
    """
    # Extract ssid-key pairs from file
    list_of_logons = extract_logon()

    # Attempt to connect to each one individually
    connect(list_of_logons)


def extract_logon():
    f = open("env.txt", "r")
    lines = f.readlines()
    is_wifi = ure.compile('^(.+)_WIFI="(.+)"')
    list_of_logons = []

    # Find a given ssid in the list
    for i in range(0, len(lines) - 1):
        result = is_wifi.search(lines[i])

        if result is not None:
            ssid = result.group(2)
            key = extract_key(result.group(1), lines[i + 1:])
            list_of_logons.append((ssid, key))

    return list_of_logons


def extract_key(var, lines):
    extract_key = ure.compile("^" + var + '_KEY="(.+)"')
    for line in lines:
        result = extract_key.search(line)
        if result is not None:
            return result.group(1)


def connect(list_of_logons):
    wlan = WLAN(mode=WLAN.STA)
    nets = wlan.scan()

    for entry in list_of_logons:
        ssid, key = entry
        for net in nets:
            if net.ssid == ssid:
                print('Network found!')
                wlan.connect(net.ssid, auth=(
                    net.sec, key), timeout=5000)
                print('WLAN connection succeeded!')
                break


# Import what is necessary to create a thread
from time import sleep

# Increment index used to scan each point from vector sensors_data
def inc(index, vector):
    if index < len(vector)-1:
        return index+1
    else:
        return 0

# Define your thread's behaviour, here it's a loop sending sensors data every 5 seconds
def pybytes_test():
    idx = 0
    sensors_data = [0, -0.2, -0.5, -0.7, -0.8, -0.9, -0.9, -0.9, -0.8, -0.6, -0.4, -0.2, 0, 0.3, 0.5, 0.7, 0.8, 0.9, 0.9, 0.9, 0.8, 0.6, 0.4, 0.1]

    while True:
        # send one element from array `sensors_data` as signal 1
        pybytes.send_signal(1, sensors_data[idx])
        idx = inc(idx, sensors_data)
        sleep(5)