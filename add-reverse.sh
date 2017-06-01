#!/bin/bash
# add reversed sequence of images

cd vid

# count the number of frames
for ((j=0; j<100000; j++)); do
  printf -v n "%04d" $j
  [[ ! -e "mand$n.png" ]] && break
done
echo $j original images

p=${1:-20}
printf -v s "mand%04d.png" $((j-1))
for ((k=j; k<j+p; k++)); do
  printf -v d "mand%04d.png" $k
  cp $s $d
done
echo "added a $p frame pause, frames $j to $((k-1))"

for ((m=k; m<k+j; m++)); do
  printf -v s "mand%04d.png" $((j+j+p-m-1))
  printf -v d "mand%04d.png" $m
  cp $s $d
done
echo "added a reverse sequence, frames $k to $((m-1))"
