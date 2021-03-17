from machine import Pin, ADC
import time
import pyb

adc = pyb.ADC("A0")


led1 = Pin("D5", Pin.OUT)
led2 = Pin("D13", Pin.OUT)

button1 = Pin("D12", Pin.IN, Pin.PULL_UP)
button2 = Pin("D11", Pin.IN, Pin.PULL_UP)


def buttons():
    while True:
        if not button1.value():
            led1.high()
            time.sleep(0.5)
            led1.low()
            led2.high()
            time.sleep(0.5)
            led2.low()
            led1.high()
            time.sleep(0.5)
            led1.low()
            led2.high()
            time.sleep(0.5)
            led2.low()
            led1.high()
            time.sleep(0.5)
            led1.low()
            led2.high()
            time.sleep(0.5)
            led2.low()
            led1.high()
            time.sleep(0.5)
            led1.low()
            led2.high()
            time.sleep(0.5)
            led2.low()

        if not button2.value():
            for i in range(20):
                led2.high()
                time.sleep(0.1)
                led2.low()
                led1.high()
                time.sleep(0.1)
                led1.low()
        
def READ():
    val = adc.read()
    print(val)
    
    
