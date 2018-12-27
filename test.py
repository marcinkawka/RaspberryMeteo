#!/usr/bin/python3

import sys
import Adafruit_DHT
from db import DBInterface

sensor = Adafruit_DHT.DHT22
pin =27

db=DBInterface("config.ini")


humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

db.storeData(temperature,humidity)
db=None

# print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
 