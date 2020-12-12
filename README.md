## Ruhr Master School - RMS:
### Ruhr-TurtleBot-Competition-RTC -  `README.md`
#### ---------------------------------------------------------------
#### Hochschulübergreifender Roboterwettbewerb für den TurtleBot3
##### (PC mit Ubuntu 20.4 - Focal Fossa  notwendig)
### -----------------------------------------------------------------
Installation von ROS Noetic und Konfiguration der `.bashrc` mit dem Shellskript  `ros_noetic_install_skript.sh`
use: 
 >$ chmod +x ros_noetic_install_skript.sh        
 >$ ./ros_noetic_install_skript.sh

Installation der TurtleBot3 - Pakete =>     `turtle_package_install_skript.sh`

#### Simulation in Gazebo mit Haus-Modell - Aufruf der Launch-Files:
##### Gazebo-3D-Simulation:      
    >$ roslaunch turtlebot3_gazebo turtlebot3_house.launch
##### Tastatursteuerung:         
    >$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch    
##### Aufnahme einer Karte (SLAM):
    >$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
##### Speichern der Karte:    
    >$ rosrun map_server map_saver -f /home/oj/catkin_ws/src/rtc/rtc_maps/gazebo_house_map
##### Navigation zum Goal:
    Falls Gazebo noch nicht gestartet:
    >$1 roslaunch turtlebot3_gazebo turtlebot3_house.launch
    >$2 roslaunch turtlebot3_navigation turtlebot3_navigation.launch \
                  map_file:=$HOME/catkin_ws/src/rtc/rtc_maps/gazebo_house_map.yaml    

!!  Navigation und Slammen funktioniert bislang nicht gleichzeitig

roslaunch turtlebot3_gazebo turtlebot3_house.launch
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/catkin_ws/src/rtc/rtc_maps/gazebo_house_map_2020_12_07.yaml



