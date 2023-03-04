import machine
import time

# Built-in blue LED on the pudding board
led = machine.Pin(27, machine.Pin.OUT)
but = machine.Pin(26, machine.Pin.IN)
value = 1

while(1):
 but_status = but.value()
 if but_status == 1:
     led.value(1)
 else:
     led.value(1)