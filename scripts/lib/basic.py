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

class FIFO:
    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.queue = []
    
    def add(self, value):
        self.queue.append(value)
        if len(self.queue) > self.maxlen:
            self.queue = self.queue[-self.maxlen:]