#!/bin/sh

cd /home/pi/Desktop/auss

python3 data_handler/send_to_pd.py &
P1=$!
pd audio_handler/_init_.pd &
P2=$!
wait $P1 $P2
