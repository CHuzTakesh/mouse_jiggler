# Mouse Jiggler with RP2040-Zero

This project implements a mouse jiggler using an RP2040-Zero and CircuitPython. The device automatically moves the mouse cursor in a square pattern to keep the system active.

## Hardware Requirements

- RP2040-Zero
- USB C Cable 
- Computer with USB port

## Software Requirements

- CircuitPython 9.x
- Adafruit HID Library 9.x
- Compatible operating system (Windows, Linux, MacOS)

## Installation

### 1. Install CircuitPython

1. Download CircuitPython for RP2040 from [circuitpython.org](https://circuitpython.org/board/raspberry_pi_pico/)
2. Connect the RP2040-Zero while holding down the BOOTSEL button
3. Copy the downloaded `.uf2` file to the USB drive that appears

### 2. Install Libraries

1. Download the CircuitPython 9.x bundle from [GitHub Adafruit Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases)
2. Unzip the downloaded file named like `adafruit-circuitpython-bundle-9.x-mpy-YYYYMMDD.zip`
3. Create a `lib` folder if it doesn't exist on your RP2040-Zero
4. Copy the `adafruit_hid` folder from the bundle to the `lib` folder

### 3. Install the Code

1. Copy a `code.py` file to the root of the RP2040-Zero.

## File Structure

```
CIRCUITPY (root unit)
├── code.py
└── lib/
    └── adafruit_hid/
        ├── __init__.mpy
        ├── mouse.mpy
        ├── keyboard.mpy
        └── ... (other files .mpy)
```
## Usage

1. Connect the RP2040-Zero to a USB port
2. The device will start moving the mouse automatically
3. To stop, simply disconnect the device

## Customization

You can modify the following variables in `code.py`:
- `MOVE_DISTANCE`: Distance in pixels that the cursor moves
- `DELAY`: Time in seconds between movements

## Troubleshooting

### Library Version Error
If you see the error "incompatible .mpy file":
1. Check the CircuitPython version in `boot_out.txt`
2. Ensure you are using the library bundle corresponding to your version

### Monitoring Errors
To view error messages on Ubuntu:

```
bash
sudo apt-get install minicom
minicom -D /dev/ttyACM0 -b 115200
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2024 [CHuzTakesh]

## Contributions

Contributions are welcome. Please open an issue or pull request to suggest changes or improvements.