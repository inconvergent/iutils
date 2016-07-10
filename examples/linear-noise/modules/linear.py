#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import pi
from numpy.random import random
from numpy import zeros
from numpy import array

from numpy import sqrt


TWOPI = pi*2
HPI = pi*0.5


class Linear(object):

  def __init__(
      self,
      size,
      height,
      start,
      start_w,
      nmax=1000000
    ):

    self.size = size
    self.one = 1.0/size
    self.start = start
    self.start_w = start_w
    self.xy = zeros((nmax,2), 'float')
    self.itt = 0

    self.xy[0,:] = start
    self.w = zeros(nmax, 'float')
    self.w[0] = start_w

  def steps(self, nsteps=500, scale=0.01):

    xy = self.xy
    w = self.w
    one = self.one

    wstp = 0

    for i in range(1, nsteps):

      stp = array([[0,one]])*random()
      newxy = xy[i-1, :] - stp
      # neww = w[i-1] - (1.0-2.0*random())*one

      wstp += random()*one*scale
      neww = w[i-1] + wstp*random()

      xy[i,:] = newxy
      w[i] = neww
      self.itt += 1

      # neww = w[i-1] - random()*sqrt(i/100.0)*one


    return self.itt

