A library for MicroPython to control digital potentiometer
(DPOT) TPL0501, a single-channel, linear-taper, with 256 wiper
positions. This device can be used as a three-terminal potentiometer
or as a two-terminal rheostat. The TPL0501 is currently offered
with end-to-end resistance of 100 kΩ. The internal registers
of the TPL0501 can be accessed using a SPI-compatible interface.

See TPL0501 datasheet:
https://www.ti.com/lit/ds/symlink/tpl0501-100.pdf?ts=1736053555929

Note, as for the mechanical potentiometer, there is no interface
to read the current wiper's position. According to the datasheet,
section 9.2 Wiper Position Upon Power Up, when DPOT is powered off,
the impedance of the device is not known. Upon power up, the device
will reset to 0x80 code (middle position) because this device does
not contain non-volatile memory.

The library should work for any microcontroller that supports MicroPython. As an example, let's use Raspberry Pi Pico. Connect TPL0501 module to a microcontroller as shown below. You don't need the level shifter, the module works with 3.3V directly from the microcontroller, however, it is better to provide 5V. Upload the file 'tpl0501.py' to a microcontroller and run the test program 'test_tpl5001.py'.

![schematics](rp2040_tpl0501_schematics.png)
