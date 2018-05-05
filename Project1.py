import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(3,GPIO.OUT)  #Dimmer
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

GPIO.setup(29,GPIO.OUT) #Relay 1
GPIO.setup(19,GPIO.IN)
GPIO.setup(21,GPIO.IN)

GPIO.setup(31,GPIO.OUT) #Relay 2
GPIO.setup(23,GPIO.IN)
GPIO.setup(32,GPIO.IN)

GPIO.setup(24,GPIO.IN)  #Sensor 1
GPIO.setup(26,GPIO.IN)  #Sensor 2

GPIO.output(3,0)
GPIO.output(5,0)
GPIO.output(7,0)
dimmer_state = 0

sen1_before = GPIO.input(24)
sen2_before = GPIO.input(26)

sen1_after = sen1_before
sen2_after = sen2_before

GPIO.output(29,0)
GPIO.output(31,0)

relay1_state = 0
relay2_state = 0

while 1:

    sen1_after = GPIO.input(24)
    sen2_after = GPIO.input(26)

    relay1_nc2 = GPIO.input(21)
    relay1_no2 = GPIO.input(19)

    relay2_nc2 = GPIO.input(23)
    relay2_no2 = GPIO.input(32)

    if (sen1_before != sen1_after):
        print('Sensor 1 has detected a change')
        sen1_before = sen1_after
        break

    if (sen2_before != sen2_after):
        print('Sensor 2 has detected a change')
        sen2_before = sen2_after
        break
    key_pressed = input()
    if (key_pressed == 1):
        if (dimmer_state == 0):
            GPIO.output(3,0)
            GPIO.output(5,0)
            GPIO.output(7,0)
        elif (dimmer_state == 1):
            GPIO.output(3,0)
            GPIO.output(5,0)
            GPIO.output(7,0)
            dimmer_state = 0
        elif (dimmer_state == 2):
            GPIO.output(3,0)
            GPIO.output(5,0)
            GPIO.output(7,1)
            dimmer_state = 1
        elif (dimmer_state == 3):
            GPIO.output(3,0)
            GPIO.output(5,1)
            GPIO.output(7,0)
            dimmer_state = 2
        elif (dimmer_state == 4):
            GPIO.output(3,0)
            GPIO.output(5,1)
            GPIO.output(7,1)
            dimmer_state = 3
        elif (dimmer_state == 5):
            GPIO.output(3,1)
            GPIO.output(5,0)
            GPIO.output(7,0)
            dimmer_state = 4
        else :
            GPIO.output(3,1)
            GPIO.output(5,0)
            GPIO.output(7,1)
            dimmer_state = 5
            
    elif (key_pressed == 2):
        if (dimmer_state == 6):
            GPIO.output(3,1)
            GPIO.output(5,1)
            GPIO.output(7,0)
        elif (dimmer_state == 5):
            GPIO.output(3,1)
            GPIO.output(5,1)
            GPIO.output(7,0)
            dimmer_state = 6
        elif (dimmer_state == 4):
            GPIO.output(3,1)
            GPIO.output(5,0)
            GPIO.output(7,1)
            dimmer_state = 5
        elif (dimmer_state == 3):
            GPIO.output(3,1)
            GPIO.output(5,0)
            GPIO.output(7,0)
            dimmer_state = 4
        elif (dimmer_state == 2):
            GPIO.output(3,0)
            GPIO.output(5,1)
            GPIO.output(7,1)
            dimmer_state = 3
        elif (dimmer_state == 1):
            GPIO.output(3,0)
            GPIO.output(5,1)
            GPIO.output(7,0)
            dimmer_state = 2
        else :
            GPIO.output(3,0)
            GPIO.output(5,0)
            GPIO.output(7,1)
            dimmer_state = 1
            
    elif (key_pressed == 3):
        if ((relay1_nc2 == 1) and (relay1_no2 == 0)):
            GPIO.output(29,1)
        elif ((relay1_nc2 == 0) and (relay1_no2 == 1)):
            GPIO.output(29,0)
        else :
            sleep(0.01)

    elif (key_pressed == 4):
        if ((relay2_nc2 == 1) and (relay2_no2 == 0)):
            GPIO.output(31,1)
        elif ((relay2_nc2 == 0) and (relay2_no2 == 1)):
            GPIO.output(31,0)
        else :
            sleep(0.01)
        
    else:
        sleep(0.01)
