import gps
import time

gps.on()

while True:
	print("Location", gps.get_location())
	print("Satellites (tracked, visible)", gps.get_satellites())
	time.sleep(1)