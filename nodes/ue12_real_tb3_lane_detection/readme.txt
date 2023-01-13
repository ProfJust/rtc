TB3 per SSH (2x) rspicam_node und bringup starten

	ubuntu@ubuntu:~$ roslaunch turtlebot3_bringup turtlebot3_robot.launch

	ubuntu@ubuntu:~$ roslaunch raspicam_node camerav2_1280x960_10fps.launch enable_raw:=true
	
Remote PC

# Erkennen zweier weißer Linien => Mitte senden  topic   /lane
rosrun rtc lane_detect_sw1_line_detect_with_mask.py

# PD-Regler für das folgen der /lane
rosrun lane_detect_sw2_control_cmd_vel.py
