#!/bin/bash

# -- rqt_script.sh -----
# by OJ at 29.01.2020
#
# usage 
# $ cd catkin_ws/src/turtle_sim_demo/
# $ ./my_first_shell_script.sh
#
# don't forget to make it executable 
# since ERROR: cannot launch node 
#
# xterm: Befehl nicht gefunden
# install xterm -package
# sudo apt install xterm
#----------------------------------

# Starting ROS-Node in new Shell
# xterm -hold -e rqt
gnome-terminal -e 'rqt'

