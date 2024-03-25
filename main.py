from boot import connection
from machine import Pin, ADC
from time import sleep

led2 = Pin(32, Pin.OUT)  # gewijzigd pinnummer

led2.on()
sleep(1)
led2.off()

while connection.isconnected():
    # read temperature
    tmp36 = Pin(34, Pin.IN)
    adc = ADC(tmp36)
    prop = 1100 / 65535
    v_out = adc.read_u16() * prop
    temp = (v_out - 500) / 10
    
    print(f"de temperatuur is {temp}")
    
    # send temperature to server
    import config
    import urequests as requests

    url = f"http://{config.SERVER}:{config.PORT}{config.ENDPOINT}"

    # POST data
    response = requests.post(url, json=temp)
    # Answer recieved
    answer = response.json()

    # flash blue LED indicating temperature was sent
    led1 = Pin(2, Pin.OUT)

    led1.on()
    sleep(1)
    led1.off()
    # read server response

    # set or unset red LED if server tells us to do so

    led2 = Pin(32, Pin.OUT)  # gewijzigd pinnummer

    led2.on()
    sleep(1)
    led2.off()


    # sleep a little until next temperature reading
    print("Sleep time 20")
    sleep(20)