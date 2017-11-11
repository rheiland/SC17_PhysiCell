import os
from glob import glob

#kmax = 3696
#for idx in range(0,kmax,10):
#  fname = "snapshot%08d" % idx

count=4
for fname in glob("instance*/snapshot*.png"):
  cmd = "convert " + fname + " -resize 50% " + fname[:-4] + ".png"
  print(cmd)
  os.system(cmd)
  count -= 1
  if (count == 0):
    break

# python svg2png.py
# -- montage of images
# montage -geometry +0+0  -tile 20x20 snapshot*.png  tmp.png
# convert -resize 15% tmp.png out.png
#
# -- animated gif
# convert snap*.png foo.gif
# magick animate foo.gif
