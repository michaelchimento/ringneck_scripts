#!/bin/sh
# download_video_launcher.sh
# launches correct python scripts with directory management

cd /home/shared_projects/ringneck_scripts/tower_scripts
sleep 10
python3 -u reboot_pis.py >> ../logs/reboot_logs&
exit 0
