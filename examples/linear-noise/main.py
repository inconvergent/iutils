#!/usr/bin/env python3
# -*- coding: utf-8 -*-


BACK = [0,0,0,1]
FRONT = [1,1,1,0.5]
SIZE = 1000

def show(render, l, grains):

  from numpy import column_stack

  render.set_front([1,1,1,0.05])

  render.set_line_width(render.pix)

  sandstroke = render.sandstroke

  points = column_stack([
    l.xy[:l.itt,0] - l.w[:l.itt],
    l.xy[:l.itt,1] - 0,
    l.xy[:l.itt,0] + l.w[:l.itt],
    l.xy[:l.itt,1] - 0,
  ])

  sandstroke(points, grains)



def main():

  from numpy.random import random
  from numpy.random import randint

  from iutils.render import Render
  from modules.linear import Linear

  render = Render(SIZE, BACK, FRONT)
  render.clear_canvas()

  nsteps = 500
  height = 1.0

  for i in range(20):

    start = random(size=(1,2))
    start_w = 0
    grains = randint(20,150)
    scale = 0.005 + random()*0.02
    L = Linear(SIZE, height, start, start_w)
    L.steps(nsteps, scale=scale)
    show(render, L, grains)

  render.write_to_png('./linear.png')


if __name__ == '__main__':

  main()

