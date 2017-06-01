#!/bin/bash
# make video from png sequence in vid directory

fr=${1:-25}     # framerate

cd vid

[[ -e _mand.mp4 ]] && mv -f _mand.mp4 _mand.old.mp4

# count the number of frames
for ((j=0; j<100000; j++)); do
  printf -v n "%04d" $j
  [[ ! -e "mand$n.png" ]] && break
done
echo $j images

afd=$(echo "scale=3; $j / $fr - 3.0" | bc) # audio fade 3 secs

ffmpeg -framerate "$fr" -i mand%04d.png -i ../Frozen_Star.mp3 \
  -shortest -af afade=t=out:st=$afd:d=3 -pix_fmt yuv420p _mand.mp4


# Frozen_Star is 3m41s so video shold not be longer than this

