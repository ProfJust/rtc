# ros_noetic_install_skript.sh
# ROS Noetic auf einem Rechner mit Ubuntu 20.04 Focal Fossa  installieren
# OJ fuer robotik.bocholt@w-hs.de
# WS2020
# geaendert am 2.11.2020 source devel/setup.bash
# erst nach catkin_make, da es sonst den Ordner noch nicht gibt

#!/bin/bash
# script to setup your catkin_ws-Workspace

echo -e "\033[34m ---------- robotik.bocholt@w-hs.de -- WS20 - ROS installieren und Workspace einrichten  ------------ \033[0m "

sudo apt-get dist-upgrade

echo -e "\033[34m ---------- Installiere ROS-Noetic  http://wiki.ros.org/noeticic/Installation/Ubuntu  ------------ \033[0m "
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-noetic-desktop-full


echo -e "\033[34m ---------- Konfiguriere .bashrc ------------ \033[0m "

echo "export LC_NUMERIC="en_US.UTF-8"" >> ~/.bashrc
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
echo "export ROS_PACKAGE_PATH=~/catkin_ws/src:/opt/ros/noetic/share" >> ~/.bashrc
echo "export ROS_MASTER_URI=http://localhost:11311" >> ~/.bashrc
echo "export ROS_HOSTNAME=127.0.0.1" >> ~/.bashrc
source ~/.bashrc

echo -e "\033[34m ---------- Dependencies for building packages ------------ \033[0m "
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
sudo rosdep init
rosdep update


echo -e "\033[34m ---------- Erstelle catkin_ws  ------------ \033[0m "
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/ProfJust/rtc.git

cd ~/catkin_ws/
catkin_make
source devel/setup.bash

# echo -e "\033[34m  Falls Fehlermeldung nach Erstinstallation von ROS, bitte einmal das Terminal schliessen und wieder öffnen  \033[0m"

echo -e "\033[34m  catkin_ws is installed - now install your packages  \033[0m"
