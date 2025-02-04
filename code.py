import board
import usb_hid
from adafruit_hid.mouse import Mouse
import time

# Initialize the mouse
mouse = Mouse(usb_hid.devices)

# Configure the movement pattern
MOVE_DISTANCE = 5  # pixels
DELAY = 10  # seconds

while True:
    # Move the mouse in a square pattern
    mouse.move(x=MOVE_DISTANCE, y=0)
    time.sleep(DELAY)
    mouse.move(x=0, y=MOVE_DISTANCE)
    time.sleep(DELAY)
    mouse.move(x=-MOVE_DISTANCE, y=0)
    time.sleep(DELAY)
    mouse.move(x=0, y=-MOVE_DISTANCE)
    time.sleep(DELAY)