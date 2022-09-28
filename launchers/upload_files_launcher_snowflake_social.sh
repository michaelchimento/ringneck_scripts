#!/bin/sh
# upload_files_launcher.sh
# launches correct python scripts with directory management


cd /home/pi/ringneck_scripts
sleep 10
python3 -u upload_to_server2020_social_video_photo.py > logs/upload_logs&
exit 0
