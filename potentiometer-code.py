# Imports necessary modules for the code.
from gpiozero import PWMLED, MCP3008
from time import sleep

# Variables for the potentiometer, and the different LEDs. The numbers next to the "PWMLED" refer to the GPIO Pins.
pot = MCP3008(0)
led1 = PWMLED(17)
led2 = PWMLED(27)
led3 = PWMLED(22)


while True:
#   Lights up the first LED if potentiometer value is less than 0.30.
    if (pot.value <0.30):
        led1.value = 0.5
        led2.value = 0
        led3.value = 0
#    Lights up the second LED if potentiomter value is between 0.30 and 0.60.
    elif (0.30 <= pot.value < 0.60):
        led1.value = 0
        led2.value = 0.5
        led3.value = 0
#    Lights up the second LED if potentiomter value is between 0.60 and 1.00. 
    elif (0.60 <= pot.value < 1.00):
        led1.value = 0
        led2.value = 0
        led3.value = 0.5
        
#   Prints the values of the LEDs and tells if they are on or off. 0.5 means on and 0.0 means off.
    print(pot.value, led1.value, led2.value, led3.value)
    sleep(0.1)
