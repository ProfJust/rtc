#!/bin/bash

# -- my_first_shell_script.sh -----
# by OJ at 29.01.2020
#
# usage 
# $ cd catkin_ws/src/turtle_sim_demo/
# $ ./my_first_shell_script.sh
#
# don't forget to make it executable
# install xterm -package
# sudo apt install xterm
#----------------------------------

# Starting ROS-Node in new Shell
#xterm -hold -e rosrun turtlesim turtle_teleop_key
gnome-terminal -e 'rosrun turtlesim turtle_teleop_key'
