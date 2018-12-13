#!/usr/bin/python
import sys
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin =27

while True:


    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    