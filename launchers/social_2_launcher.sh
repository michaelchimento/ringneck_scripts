#!/bin/sh
# sociallauncher.sh
# launches correct python scripts with directory management

cd /home/pi/ringneck_scripts
sleep 15
python3 social_video_photo.py >> logs/logs&
exit 0
