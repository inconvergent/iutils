# -*- coding: utf-8 -*-

def get_colors(f, do_shuffle=True):
  try:
    import Image
  except Exception:
    from PIL import Image

  scale = 1./255.
  im = Image.open(f)
  data = list(im.convert('RGB').getdata())

  res = []
  for r,g,b in data:
    res.append([r*scale,g*scale,b*scale])

  if do_shuffle:
    from numpy.random import shuffle
    shuffle(res)

  return res

