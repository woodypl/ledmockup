#!/usr/bin/env python
import argparse
import sys
import pygame
from PIL import Image

class Mockup(object):

    def draw_row(self, window, row, matrix, start):
        for idx in range(self.cols):
            pygame.draw.circle(window, matrix[idx,row], (start[0]+self.hdist*idx, start[1]), self.radius, 0)
    
    def draw_matrix(self, window, matrix, start=(0,0)):
        for idx in range(self.rows):
            self.draw_row(window, idx, matrix, (start[0], start[1]+self.vdist*idx))

    def load_image(self):
        im = Image.open(self.filename)
        return im.resize((self.rows,self.cols), Image.ANTIALIAS).load()

parser = argparse.ArgumentParser(description='Project a mockup of a LED matrix display.')
parser.add_argument('filename', type=argparse.FileType('r'),
                           help='filename of the image to display')
parser.add_argument('--rows', default=32, type=int,
        help='number of rows (default: 32)')
parser.add_argument('--cols', default=32, type=int,
        help='number of columns (default: 32)')
parser.add_argument('--radius', default=5, type=int,
        help='radius of each LED in pixels (default: 5)')
parser.add_argument('--hdist', default=27, type=int,
        help='horizontal distance between LEDs in pixels (default: 27)')
parser.add_argument('--vdist', default=15, type=int,
        help='vertical distance between LEDs in pixels (default: 15)')



mockup = Mockup()

parser.parse_args(namespace=mockup)

pygame.init()

#create the screen
window = pygame.display.set_mode((848, 480), pygame.FULLSCREEN) 

matrix = mockup.load_image()
mockup.draw_matrix(window, matrix, (mockup.radius, mockup.radius))

#draw it to the screen
pygame.display.flip() 

#input handling (somewhat boilerplate code):
while True:
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      elif event.type == pygame.KEYUP:
          if event.key == pygame.K_ESCAPE:
              sys.exit(0)
      else: 
          print event 
   pygame.time.wait(10)
