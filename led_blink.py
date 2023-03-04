import machine
import time

# Built-in blue LED on the pudding board
led = machine.Pin(27, machine.Pin.OUT, 0)
value = 1

while(1):
 led.value(value)
 time.sleep(1)
 value = not value