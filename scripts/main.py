#pylint: disable=import-error
#pylint: disable=undefined-variable

# from network import WLAN
# wlan = WLAN(mode=WLAN.STA)

# nets = wlan.scan()
# print(nets)
# for net in nets:
# 	if net.ssid == 'bbb_net':
# 		print('NETWORK FOUND!')
# 		wlan.connect(net.ssid, auth=(net.sec, 'bbb_net.123'), timeout=5000)
# 		print('WLAN connection succeeded!')
# 		break

from heartbeat import blink
blink()


# from pythonping import ping
# ping('127.0.0.1', verbose=True)