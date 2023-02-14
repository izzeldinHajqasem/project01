# Write your code here :-)
# Add your Python code here. E.g.
from microbit import *
import radio
radio.config(group=10)
radio.on()

while True:
    receive = radio.receive()
    if receive == "warning":
        display.scroll("warning")
