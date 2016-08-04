# Spectrum analyser for the BBC micro:bit
#
# Version 1.0 N. Kendrick 05-Jun-2016
#
# This program is designed to work with the L3K BBC micro:bit audio I/O
# board, which includes an electret microphone & amplifier circuit connected
# to an MSGEQ7 spectrum analyser chip from Mixed Signal Integration.
#
# The program controls the MSGEQ7 by initially resetting it and then
# pulsing its strobe pin to make the chip sample the audio
# frequencies within a specific band. The chip samples 7 bands before starting
# again. Each time the chip samples a frequency band, its output pin sets
# itself to a voltage proportional to the strength of the frequency sample;
# this voltage is fed to the micro:bit and displayed on one of the column
# of LEDs. Because there are only 5 columns of LEDs on the micro:bit, we
# skip over two of the MSGEQ7's sampling bands by resetting the chip after 5
# toggles of its strobe signal.
#
# The audio I/O board is connected to the micro:bit as follows:
#
# Pin 0 = MSGEQ7 Strobe
# Pin 1 = MSGEQ7 Output
# Pin 2 = MSGEQ7 Reset
#
# Also connect 3V and 0V from the micro:bit to the audio I/O board.

from microbit import *

# This value is used to adjust the scaling of the read analogue value, which
# often does not start from zero. 500 is a good start
baseVal = 500

# Start with strobe and reset lines set low and set pin 1 to input by reading it
audioSample = pin1.read_analog()
pin0.write_digital(0)
pin2.write_digital(0)

while True:

    # Reset the MSGEQ7 and wait 1mS for things to settle
    pin2.write_digital(1)
    pin2.write_digital(0)
    sleep(1)

    # Main loop - strobe the MSGEQ7 5 times and then reset it,
    # sampling the MSGEQ7 output each time and writing the value to an
    # LED column. The chip needs a reset after 5 reads because it
    # actually has 7 sample points but we only use 5; (one for each
    # LED column). LEDCol counts from 0 to 4 (up to one before the specified
    # number) - which is a Python thing.

    for LEDCol in range(5):

        # Strobe the chip and then read a value
        pin0.write_digital(1)
        pin0.write_digital(0)

        # Read the analogue value from the MSGEQ7; this will be a number
        # from 0 to 1023 which needs to be scaled for the 5 LEDs in each column.
        audioSample = pin1.read_analog()

        # Bring the analogue value into the 5 LED range...
        audioSample = audioSample - baseVal
        if audioSample < 0:
            audioSample = 0

        audioSample = int(audioSample / ((1023 - baseVal) / 5))

        # Write a bar on the LEDs in the relevant column. Note that the top
        # LED in each column is #0 and the bottom is #4.
        # There are a few ways to do what we want, for example with a loop,
        # but this is the most easy to read - we just turn on/off each LED
        # in the column...

        if audioSample > 4:
            display.set_pixel(LEDCol, 0, 9)
        else:
            display.set_pixel(LEDCol, 0, 0)

        if audioSample > 3:
            display.set_pixel(LEDCol, 1, 9)
        else:
            display.set_pixel(LEDCol, 1, 0)

        if audioSample > 2:
            display.set_pixel(LEDCol, 2, 9)
        else:
            display.set_pixel(LEDCol, 2, 0)

        if audioSample > 1:
            display.set_pixel(LEDCol, 3, 9)
        else:
            display.set_pixel(LEDCol, 3, 0)

        if audioSample > 0:
            display.set_pixel(LEDCol, 4, 9)
        else:
            display.set_pixel(LEDCol, 4, 0)

    # End of for loop

# End of while loop

