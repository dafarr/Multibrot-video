**Multibrot video generator**

**multibrot-make-images.py**

  This is the python script for generating the multibrot images
  as a sequence of png files. It is Python 2.7 compatible but
  use a 2.7 compatible version of the Pypy jit-compiler to run
  it so that it completes in a few hours rather than days.
  Tested on Ubuntu -- and uses Ubuntu's location of its fonts.
  
**multibrot-rotate-cut-make-images.py**

  Alternative to the above that creates slightly different images 
  due to the different mathematical method of creating the multibrot.
  
**add-reverse.sh**

  Bash script to add the reversed sequence to the images, created
  from the existing images.
  
**add-credits.sh**

  Bash script uses ImageMagick's "convert" to add credits to the
  end of the image sequence.
  
**Frozen_Star.mp3**

  Not included here. CC by 3.0 licensed music file..
  Find this file by web-searching with something like:
  "Kevin Macleod Frozen Star free mp3 download"
 
**makevid.sh**

  Bash script to convert png image sequence to mp4 video and adds
  music file.  Needs the "real" ffmpeg that's in most very recent
  Linux distros but not the "fake" ffmpeg that's a front-end to
  avconv that was in many distros until just recently.
  

