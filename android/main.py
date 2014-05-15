#!/usr/bin/env python
import sys
import pygame
import threading
import socket
import time
from PIL import Image
from StringIO import StringIO
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

class Mockup(object):

    def __init__(self):
        self.rows = 32
        self.cols = 32
        self.radius = 5
        self.hdist = 27
        self.vdist = 15
    
    def draw_row(self, window, row, matrix, start):
        for idx in range(self.cols):
            pygame.draw.circle(window, matrix[idx,row], (start[0]+self.hdist*idx, start[1]), self.radius, 0)
    
    def draw_matrix(self, window, matrix, start=(0,0)):
        for idx in range(self.rows):
            self.draw_row(window, idx, matrix, (start[0], start[1]+self.vdist*idx))

    def load_image(self, data):
        im = Image.open(StringIO(data))
        return im.resize((self.rows,self.cols), Image.ANTIALIAS).load()

    def draw_progress(self, window, percentage, colour=(255,0,0)):
        start=(5,5)
        for idx in range(self.cols):
            if idx > (percentage*self.cols/100):
                colour=(119,136,153)
            pygame.draw.circle(window, colour, (start[0]+self.hdist*idx, start[1]), self.radius, 0)


class ServerHandler(SimpleHTTPRequestHandler):

    def __init__(self,request,client_address,server):
        self.mockup = Mockup()
        self.window = pygame.display.set_mode((848, 480), pygame.FULLSCREEN)
        SimpleHTTPRequestHandler.__init__(self, request,client_address,server)

    def do_POST(self):
        self.send_response(200, "OK")
        self.end_headers()

        length = int(self.headers.get('Content-Length', 0))
        if length > 0:
            data = self.rfile.read(length)
            matrix = self.mockup.load_image(data)
            self.mockup.draw_matrix(self.window, matrix, (self.mockup.radius, self.mockup.radius))
            pygame.display.flip()

def bcastpresence(alive):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 0))
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    while alive.is_set():
        data = 'Android LedMockup ready'
        sock.sendto(data, ('<broadcast>', 55555))
        time.sleep(30)

def main():
    pygame.init()

    HandlerClass = ServerHandler
    ServerClass  = HTTPServer
    Protocol     = "HTTP/1.0"

    port = 8000
    server_address = ('0.0.0.0', port)

    HandlerClass.protocol_version = Protocol
    httpd = ServerClass(server_address, HandlerClass)
    sa = httpd.socket.getsockname()

    alive = threading.Event()
    alive.set()
    keepalive = threading.Thread(target=bcastpresence, args=(alive,))
    keepalive.start()

    print ("Serving HTTP on", sa[0], "port", sa[1], "...")
    try:
        httpd.serve_forever()
    except:
        alive.clear()
        keepalive.join()


if __name__ == "__main__":
        main()
