from gpiozero import RotaryEncoder, PWMLED
from time import sleep

rotor = RotaryEncoder(17, 18, wrap=True, max_steps=75) # DT goes to 16, CLK goes to 20


led = PWMLED(24)

while True:
	if rotor.steps<0 and rotor.steps>-25:
		rotor.steps=rotor.steps*0 # makes the value so it can't go below -1
	elif rotor.steps>=-75 and rotor.steps<-50:
		rotor.steps=75
	led.value = rotor.steps / 75 # the value of led. value will change as you rotate the device
	sleep(0.1) 
	print(rotor.steps) # the value of rotor.steps will change as you rotate the device
