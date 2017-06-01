#!/usr/bin/env pypy
import time, numpy, os
from PIL import Image, ImageDraw, ImageFont
from math import *
w = 1200; h = 900
t = 1500                # total frames
s = 2.2                 # power if single frame
xc = -0.35; yc = 1.0e-5; m = 0.57
t1 = time.time()
if not os.path.isdir("vid"): os.mkdir("vid")

for f in xrange(t):
  lis=[]
  #asymptotically rising power value over range 1.05 - 10000
  n = 1.05 + 2.0 * f / (1e-9 + t - f - 1.0 + (2.0 * t - 2.0) / (1e4 - 1.05))
  # slow and stop at each whole number by adding sine wave
  p = ((n * 2.0 * pi) + sin((n * 2.0 - 1.0) * pi)) / (2.0 * pi)
  if t == 1: p = s                              # power if 1 frame
  imax = 10 + int((250 / ( p - 0.75)))          # max iterations
  zmax = 1.0 + 20 / ( p - 2.0 + 2.0 / p)        # max escape value

  for y in range(h/2 + 1):
    for x in range(w):
      cr =  xc + (2 * x - w) / (w * m)
      ci = -yc - (2 * y - h) / (w * m)
      cp = atan2(ci, cr)
      zr = zi = za = zp = 0.0
      for i in range(imax):
        zap = za ** p
        zpb = (zp - cp + 3 * pi ) % ( 2 * pi) + cp - pi
        zr = zap * cos(p * zpb) + cr
        zi = zap * sin(p * zpb) + ci
        za = sqrt( zr * zr + zi * zi)
        zp = atan2(zi, zr)
        if za >= zmax: break
      if i >= imax - 1:
        lis += [0, 0, 0]
      else:
        # calc for continuous gradient of background
        zlog = (i - log(log(za)) / log (p)) * log (p);
        # tweak gradient for good contrast at all power values
        v = log(max(1.0, zlog * 1.5 + 1.0)) * (0.3 + 0.02 * log(p));
        if v <= 1.0:
          rgb = (v ** 4, v ** 2.5, v)
        else:
          v = max(0.0, 2.0 - v)
          rgb = (v, v ** 1.5, v ** 3)
        lis += [int(n * 255) for n in rgb]

  for y in range(h/2 - 1):
    s = (h/2 - y - 1) * w * 3
    lis += lis[s: s + w * 3]

  img = Image.frombytes('RGB', (w,h), str(bytearray(lis)))
  draw = ImageDraw.Draw(img)
  ttf = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
  font_a = ImageFont.truetype(ttf, h / 20)
  pow = '%0.2f' % p
  txt = u"Z \u21A6 Z" + ' ' * len(pow) + " + C"
  draw.text((h/18, h - h/10), txt, "white", font=font_a)
  draw.text((h/4.5, h - h/8), pow, "white", font=font_a)
  img.save('vid/mand%04d.png' % f)

print "Elapsed time:", '%7.2f' % (time.time() - t1), "s"


