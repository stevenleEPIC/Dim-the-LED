# UNFINISHED CODE


from gpiozero import RotaryEncoder, LED
from time import sleep

rotor = RotaryEncoder(18, 17, wrap=True, max_steps=180) # DT goes to 16, CLK goes to 20
rotor.steps = -180



def dimLED():
    led = LED(24)
    while True:
        led.value = rotor.steps / 180 # the value of led. value will change as you rotate the device
        sleep(0.1) # sleep time is turn the led off but it off fast enough that blinking is unnoticeable

while True:
	print(rotor.steps) # the value of rotor.steps will change as you rotate the device