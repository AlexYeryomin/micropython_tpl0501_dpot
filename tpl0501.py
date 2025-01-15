# Copyright (c) 2025 Alex Yeryomin
#
# A library for MicroPython to control digital potentiometer
# (DPOT) TPL0501, a single-channel, linear-taper, with 256 wiper
# positions. This device can be used as a three-terminal potentiometer
# or as a two-terminal rheostat. The TPL0501 is currently offered
# with end-to-end resistance of 100 kΩ. The internal registers
# of the TPL0501 can be accessed using a SPI-compatible interface.
#
# See TPL0501 datasheet:
# https://www.ti.com/lit/ds/symlink/tpl0501-100.pdf?ts=1736053555929
#
# Note, as for the mechanical potentiometer, there is no interface
# to read the current wiper's position. According to the datasheet,
# section 9.2 Wiper Position Upon Power Up, when DPOT is powered off,
# the impedance of the device is not known. Upon power up, the device
# will reset to 0x80 code (middle position) because this device does
# not contain non-volatile memory.

from micropython import const
from machine import Pin, SPI
from time import sleep_us

class TPL0501:
    
    MAX_POSITION = const(255)
    
    def __init__(self, spi, csPin, position=None):
        self.spi = spi
        self.csPin = csPin
        self.csPin.init(Pin.OUT, value=1) # Disabled.
        self.data = bytearray(1)
        self._position = position if position else 0x80
        self.waperPosition = self._position
    
    @property
    def waperPosition(self):
        return self._position
    
    @waperPosition.setter
    def waperPosition(self, position):
        self._position = TPL0501.constrain(position, 0, TPL0501.MAX_POSITION)
        self.csPin(0) # Actived.
        self.data[0] = self._position
        self.spi.write(self.data)
        self.csPin(1) # Disabled.

    def increase(self, amount=1):
        self.waperPosition(self._position + amount)

    def decrease(self, amount=1):
        self.waperPosition(self._position - amount)

    @staticmethod
    def constrain(x, out_min, out_max):
        return max(out_min, min(x, out_max))
