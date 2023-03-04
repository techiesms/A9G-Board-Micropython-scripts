import cellular
import machine
import time 

cellular.gprs("www", "", "") # ("apn_name","username","password")

led_topic = "  "
sensor_topic = "  "

led = machine.Pin(27,machine.Pin.OUT)

time_period = 6

# Import mqtt (download client if necessary)
try:
    from umqtt import simple
except ImportError:
    import upip
    upip.install("micropython-umqtt.simple")
    from umqtt import simple
    
def cb(led_topic, msg):                             # Callback function
    print('Received Data:  Topic = {}, Msg = {}'.format(led_topic, msg))
    recieved_data = str(msg,'utf-8')            #   Recieving Data
    if recieved_data=="0":
        led.value(0)
    if recieved_data=="1":
        led.value(1)

# Report location
name = "a9g-micropython-board"
server = "io.adafruit.com"
port = 1883
username = "  "
password = "  "


client = simple.MQTTClient(name, server, port, username, password )
client.connect()

client.set_callback(cb)      # Callback function               
client.subscribe(led_topic) # Subscribing to particular topic

def send_sensor():
    msg = "100"
    print('Sending Data:  Topic = {}, Msg = {}'.format(sensor_topic, msg))
    client.publish(sensor_topic, msg)

while True:
    for x in range(time_period):
        for x in range(10):
            client.check_msg()
            time.sleep(0.1)
    send_sensor()
    
    