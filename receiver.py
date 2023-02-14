# Write your code here :-)
# Add your Python code here. E.g.
from microbit import *
from ssd1306 import initialize, clear_oled 
from ssd1306_text import add_text
import radio
radio.config(group=10)
radio.on()
initialize()
while True:
    clear_oled()
    receive = radio.receive()
    if receive == "warning":
        add_text(0,3,"warning")
    sleep(2000)
