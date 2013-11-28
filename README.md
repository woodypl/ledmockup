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
  --hdist HDIST    horizontal distance between LEDs in pixels (default: 15)
  --vdist VDIST    vertical distance between LEDs in pixels (default: 15)
