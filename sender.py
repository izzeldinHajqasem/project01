# Add your Python code here. E.g.
from microbit import *
import radio

from ultrasonic import Ultrasonic
radio.config(group=10)
radio.on()
ultrasonic_sensor = Ultrasonic()
while True:

    #check the dictance 
    dictance_value =   ultrasonic_sensor.measure_distance_cm()
    #make a variable to see if there is movment
    movment = pin2.read_digital()
    #send a warning to the other microbit
    if movment == 1 and dictance_value <= 30 :
        radio.send("warning")
    sleep(2000)
