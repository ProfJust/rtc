Konfiguration des Gazebo - TurtleBots für zwei Sonar-Sensoren

=> rostopic sonar_left und sonar_right werden gesendet

 Paket Twist Mux installieren
 
 $ sudo apt-get install ros-noetic-twist-mux

  usage for two sonar sensors
  
  use dir 
   /new urdf with sonar_left and sonar_right

# copy content of turtlebot3.burger.gazebo_sonar.xacro
#              to turtlebot3.burger.gazebo_sonar.xacro
# copy content of turtlebot3.burger.urdf_sonar.xacro
#              to turtlebot3.burger.urdf.xacro
#
#   $1 roslaunch turtlebot3_gazebo turtlebot3_house.launch
#   $2 roslaunch turtlebot3_navigation turtlebot3_navigation.launch
#                map_file:=$HOME/catkin_ws/src/rtc/rtc_maps/gazebo_house_map_2020_12_07.yaml
#   $3 rosrun rtc sonar_obstacle_avoidance.py  
#   $4 roslaunch rtc sonar_twist_mux.launch	
