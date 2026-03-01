import board
import usb_hid
from adafruit_hid.mouse import Mouse
import time

import storage
storage.disable_usb_drive()

# Inicializar el mouse
mouse = Mouse(usb_hid.devices)

# Configurar el patrón de movimiento
MOVE_DISTANCE = 5  # píxeles
DELAY = 10  # segundos

while True:
    # Mover el mouse en un patrón cuadrado
    mouse.move(x=MOVE_DISTANCE, y=0)
    time.sleep(DELAY)
    mouse.move(x=0, y=MOVE_DISTANCE)
    time.sleep(DELAY)
    mouse.move(x=-MOVE_DISTANCE, y=0)
    time.sleep(DELAY)
    mouse.move(x=0, y=-MOVE_DISTANCE)
    time.sleep(DELAY)