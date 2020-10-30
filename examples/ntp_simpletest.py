import adafruit_ntp
import socket
import time

ntp = adafruit_ntp.NTP(socket)

while True:
    print(ntp.datetime)
    time.sleep(1)
