#!/usr/bin/env python3
# -*- coding: utf-8 -*-


BACK = [0,0,0,1]
FRONT = [1,1,1,1]
SIZE = 2000
N = 40
W = int(SIZE/N)
ONE = 1.0/SIZE

def main():

  from iutils.render import Render

  render = Render(SIZE, BACK, FRONT)
  render.clear_canvas()

  # from iutils.colors import get_colors
  # colors = get_colors('./colors/img.gif') # point to your source image
  # nc = len(colors)

  for i in range(N):
    for j in range(N):

      # random colors
      # rgba = colors[(i*N+j)%nc] + [1]
      # render.set_front(rgba)

      # bw checkers
      if not (i+j)%2:
        continue

      a = (i*W)*ONE
      b = (j*W)*ONE
      print(a,b, W*ONE)
      render.ctx.rectangle(a,b,W*ONE,W*ONE)
      render.ctx.fill()

  render.write_to_png('checkers.png')


if __name__ == '__main__':
  main()

