#!/bin/bash
# add end credits

txt='Graphics by Dave Farrance  (CC BY 3.0)\n\n
Music "Frozen Star" by Kevin MacLeod  (CC BY 3.0)\n\n
Creative Commons Attribution 3.0 Unported license'

cd vid

# count the number of frames
for ((j=0; j<100000; j++)); do
  printf -v n "mand%04d.png" $j
  [[ ! -e "$n" ]] && break
done
echo $j original images

echo "new image: $n"

read w h < <(identify -format "%w %h" mand0000.png)

echo "width: $w   height: $h"

# create credit frame
convert -size "${w}x${h}" -pointsize $(( w / 35 )) \
  -background black -fill white -gravity center \
  -font Verdana-Regular caption:"$txt" "$n"

p=75 # copy to create p credit frames
for ((k=j+1; k<j+p; k++)); do
  printf -v d "mand%04d.png" $k
  cp $n $d
done
echo "added $p frame credits, frames $j to $((k-1))"
