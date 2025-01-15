# Copyright (c) 2025 Alex Yeryomin
# The demo program to use a library to control digital
# potentiometer (DPOT) TPL0501.

from machine import ADC, SPI, SoftSPI, Pin, Signal
from time import sleep, time
from tpl0501 import TPL0501

adc = ADC(0)                 # pin 26 for Pi Pico (RP2040).
ADC_TO_V_SCALE = 3.3 / 65535 # The scale for Pi Pico (RP2040). 

# Replace pin's numbers as per your schematics.
TPL0501_SCLK = 6
TPL0501_DIN  = 7
TPL0501_CS   = 8

csPin = Pin(TPL0501_CS)
spi = SPI(0, baudrate=4_000_000, sck=Pin(TPL0501_SCLK), mosi=Pin(TPL0501_DIN), firstbit=SPI.MSB)

# Do not reset the potentiometer, it will be at the middle on power up.
pot = TPL0501(spi, csPin)
print(f"Waper position: {pot.waperPosition}, V={adc.read_u16() * ADC_TO_V_SCALE}")

# Reset the potentiometer to the highest resistance.
pot = TPL0501(spi, csPin, TPL0501.MAX_POSITION)
print(f"Waper position: {pot.waperPosition}, V={adc.read_u16() * ADC_TO_V_SCALE}")

# Wiper sweep test.
direction = None
while True:
    print(f"Waper position: {pot.waperPosition}, V={adc.read_u16() * ADC_TO_V_SCALE}")
    sleep(0.1)

    if pot.waperPosition == 0:
        direction = 1
    elif pot.waperPosition == TPL0501.MAX_POSITION:
        direction = -1
    pot.waperPosition = pot.waperPosition + direction
