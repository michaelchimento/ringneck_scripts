#!/bin/sh
# download_video_launcher.sh
# launches correct python scripts with directory management

cd /home/shared_projects/ringneck_scripts/tower_scripts
sleep 10
python3 -u check_all_OK.py >> ../logs/logs&
exit 0
