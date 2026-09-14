from gpiozero import RotaryEncoder, PWMLED
from time import sleep

rotor = RotaryEncoder(17, 18, wrap=True, max_steps=180) # DT goes to 16, CLK goes to 20


led = PWMLED(24)

while True:
	if rotor.steps<0 and rotor.steps>-25:
		rotor.steps=rotor.steps*0 # makes the value so it can't go below -1
	elif rotor.steps>=-180 and rotor.steps<-50:
		rotor.steps=180 # makes the value so it's can't go to -180
	led.value = rotor.steps / 180 # the value of led. value will change as you rotate the device
	sleep(0.1) 
	print(rotor.steps) # the value of rotor.steps will change as you rotate the device
