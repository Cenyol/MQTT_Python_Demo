#!/usr/bin/python

import time
import json
from BMP180 import BMP180
import paho.mqtt.publish as publish

bmp = BMP180()
while True:
	temp = bmp.read_temperature()
	pressure = bmp.read_pressure()
	altitude = bmp.read_altitude()
	data = [{'temp':temp,'pressure':pressure,'altitude':altitude,'timestamp':int(time.time())}];
	publish.single("test", json.dumps(data), hostname="121.40.130.184")
	time.sleep(5 * 60)
