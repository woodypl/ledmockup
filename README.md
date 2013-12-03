ledmockup
=========

A simple Python tool to generate visualisations of LED matrices
This is a very simple script. Look into the sources to find out what it does.


    usage: draw.py [-h] [--rows ROWS] [--cols COLS] [--radius RADIUS]
                   [--hdist HDIST] [--vdist VDIST]
                   filename

    Project a mockup of a LED matrix display.

    positional arguments:
      filename         filename of the image to display

    optional arguments:
      -h, --help       show this help message and exit
      --rows ROWS      number of rows (default: 32)
      --cols COLS      number of columns (default: 32)
      --radius RADIUS  radius of each LED in pixels (default: 5)
      --hdist HDIST    horizontal distance between LEDs in pixels (default: 27)
      --vdist VDIST    vertical distance between LEDs in pixels (default: 15)

Application
-----------

This script can be used to see what output of clustered LED strips might look like.
Specifically, the strip available on AdaFruit: http://www.adafruit.com/products/306 was measured and the default values for the script were chosen to match the strip size.

### Strip measurements

* Height: 16.5mm
* Width: 1000mm
* 32 LEDs per strip
* 2 LEDs per 62.5mm segment
* LED display component radius: 3mm
* LEDs spaced out evenly

This amounts to 31.25mm between LEDs horizontally and 16.5mm vertically.

### Projection
Using a Microvision ShowWX picoprojector at 848x480, 97cm from the wall, the values of 27px between LEDs horizontally and 15px vertically gave expected results.
However, the LED radius was not taken into account due to the brightness and dispersion the lights give, thus the dots projected are slightly bigger.
A sample projection on the wall is available in the repository (`ledmockup.jpg`, trapezoid skew uncorrected). However, more realistic results could be obtained when projecting through glass.
