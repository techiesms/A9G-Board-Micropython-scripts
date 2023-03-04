import cellular
import time

global flag
flag = 1

def sms_handler(evt):
    global flag
    if evt == cellular.SMS_SENT:
        print("SMS sent")

    elif evt == cellular.SMS_RECEIVE:
        print("SMS received, attempting to read ...")
        ls = cellular.SMS.list()
        print(ls[-1])
        flag = 0

cellular.on_sms(sms_handler)
cellular.SMS("+91xxxxxxxxxx", "Hello From A9G").send()

print("Doing something important ...")
while flag:
    time.sleep(1)

print("Done!")