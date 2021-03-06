#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Medidor de distancia com ultrasom
#
# Author: Gilson Giuriatti
#
# Email Address: gilson@gmail.com
#
# Created: 2010
#
# Modified: Maio 2011
#

from pylab import *
import time, serial

ser = serial.Serial('/dev/ttyUSB0', 115200)
time.sleep(2)

ion()

fig = figure(1)
sub = subplot(111)

i = 0
t = []
h = []

line = plot(t, h, 'ro-')

xlabel('')
ylabel('Distancia (cm)')
title('Exemplo usando arduino + python')

while True:
  try:
    ser.write('d')
    s = float(ser.readline().replace('\r\n',''))
    print s
    if (s < 100):
      i = i+1
      t.append(i)
      h.append(s)
      line[0].set_data(t,h)
      x0 = 0
      x1 = i
      if (i > 100):
        x0 = i - 100
      sub.set_xlim(x0,x1)
      sub.set_ylim(0,100)
      draw()
  except KeyboardInterrupt:
    break

