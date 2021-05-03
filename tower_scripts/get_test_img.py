#!/usr/bin/python3
import datetime as dt
import os
import sys
from all_ipsandnames import pi_data_table
from term_utils import ping_pi, terminal, kill_python, reboot, take_test_img

print("####{} get_test_img.py####".format(dt.datetime.now().strftime('%Y-%m-%d_%H_%M')))

#clear out yesterday's photos
copy_to = "/home/shared_projects/test_images"
copy_from = "APAPORIS/CURRENT"
command = 'rm -rf {}/*.jpg'.format(copy_to)
terminal(command)

for pi in pi_data_table:
    print("Attempting to take picture from {}".format(pi))
    reachable = ping_pi(pi[1])
	
    if not reachable:
        pass
    else:
        if "Puzzle" not in pi[0]:
            #return most recently created image
            command = "ssh pi@{} \"cd {} && ls -t | head -n 1\"".format(pi[1],copy_from)
            try:
                most_recent_folder = terminal(command).strip(" \n")
            except:
                print("error retrieving most recent folder")
                pass
            else:
                print(most_recent_folder)
            command = "ssh pi@{} \"cd {}/{} && ls -t | head -n 2 | tail -n 1\"".format(pi[1],copy_from,most_recent_folder)
            try:
                most_recent_img = terminal(command).strip()
            except:
                print("error getting most recent image")
                pass
            else:
                print(most_recent_img)
            
            #copy to tower
            try:
                command = 'scp pi@{}:{}/{}/{} {}/{}.jpg'.format(pi[1], copy_from,most_recent_folder,most_recent_img, copy_to,pi[0])
                print(command)
                terminal(command)
            except:
                print("nothing in MOVED folder to scp")                
                pass





