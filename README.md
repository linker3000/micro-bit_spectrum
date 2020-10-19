# micro-bit_spectrum
Code to display an audio spectrum bar chart on the BBC micro:bit using the MSGEQ7 spectrum analyser chip - circuit schematic as shown.

The prototype was breadboarded and then transferred to a zbit:builder board (kindly supplied by http://zbit-connect.co.uk/). Due to the limited prototyping space on the zbit:builder, less experienced constructors might find it easier to use regular stripboard.

Video here: https://youtu.be/wQXjX3phBOo

The MSGEQ7 chip is available from Sparkfun and regional/global agents. 

* https://www.sparkfun.com/products/10468
* https://www.sparkfun.com/datasheets/Components/General/MSGEQ7.pdf

Beware of buying the MSGEQ7 chip on ebay - some/many have turned out to be faulty and it's suspected that they are manufacturing rejects. 

*Schematic*
![Image](MSGEQ7_Breakout_Board.png)


*On zbit:builder*
![Image](zbit01.jpg)


(That's some mighty [fine/scary - insert as appropriate] circuit squishing going on there.)

*How it works*

The circuit built around Operational Amplifier U1 amplifies the signal received from the electret microphone and this signal is fed into the MSGEQ7 chip (U2) for sampling. The micro:bit program first resets U2 and the chip evaluates (samples) the amount of the input signal that corresponds to its first sampling frequency of 63Hz. A voltage proportional to the sample is output on U2 pin 3 and this is fed into the micro:bit and used to display a suitably-sized LED bar on its display. The micro:bit then sends a pulse ('strobe signal') to U2 pin 4, which causes the chip to assess the microphone input at its next sampling frequency of 160Hz and output an approporiate voltage on pin 3 again, which is used for the next LED bar on the micro:bit. This "sample - display - strobe' cycle is repeated for a total of 5 frequency bands, after which the micro:bit resets U2 to start over. 

Notes:

* The MSGEQ7 chip sample frequencies are: 63Hz, 160Hz, 400Hz, 1KHz, 2.5KHz, 6.25KHz and 16KHz. 
* The MSGEQ7 chip can perform total of 7 frequency samples, but since there are only 5 columns / bars on the micro:bit display only the first 5 frequencies are used.
* There's additional comments in the Python program file.
