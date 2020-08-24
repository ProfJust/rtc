# turtle_package_install_skript.sh
# Installation der TurtleBot 3 Pakete auf dem Remote-PC
# https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/
# OJ fuer robotik.bocholt@w-hs.de
# WS2020

#!/bin/bash
# script to setup youbot-Workspace

echo -e "\033[34m ---------- RTC WS20 - TurtleBot Workspace einrichten  ------------ \033[0m "

echo "Shellskript zur Installation der Treiber-Pakete" 

sudo apt-get dist-upgrade -y
pwd
cd ~/catkin_ws/src/

sudo apt-get install ros-noetic-joy  -y
sudo apt-get install ros-noetic-teleop-twist-joy -y
sudo apt-get install ros-noetic-teleop-twist-keyboard -y
sudo apt-get install ros-noetic-laser-proc -y
sudo apt-get install ros-noetic-rgbd-launch -y
sudo apt-get install ros-noetic-depthimage-to-laserscan -y
sudo apt-get install ros-noetic-rosserial-arduino -y
sudo apt-get install ros-noetic-rosserial-python -y
sudo apt-get install ros-noetic-rosserial-server -y
sudo apt-get install ros-noetic-rosserial-client -y
sudo apt-get install ros-noetic-rosserial-msgs -y
sudo apt-get install ros-noetic-amcl -y
sudo apt-get install ros-noetic-map-server -y
sudo apt-get install ros-noetic-move-base -y
sudo apt-get install ros-noetic-urdf -y
sudo apt-get install ros-noetic-xacro -y
sudo apt-get install ros-noetic-compressed-image-transport -y
sudo apt-get install ros-noetic-rqt-image-view -y
sudo apt-get install ros-noetic-gmapping -y
sudo apt-get install ros-noetic-navigation -y
sudo apt-get install ros-noetic-interactive-markers -y


cd ~/catkin_ws/src

echo -e "\033[34m Aktualisiere alle Abhaengigkeiten der ROS-Pakete \033[0m"
rosdep update
rosdep install --from-paths src --ignore-src -r -y

#echo -e "\033[34m to do:   $ cd ~/catkin_ws/  ...   catkin_make \033[0m"
cd ~/catkin_ws/
catkin_make

echo -e "\033[34m RTC - WS20 - Workspace is installed - have fun!  \033[0m"
echo -e "\033[32m $ roslaunch rtc turtle.launch \033[0m"

