TB3 per SSH (2x) rspicam_node und bringup starten

	ubuntu@ubuntu:~$ roslaunch turtlebot3_bringup turtlebot3_robot.launch

	ubuntu@ubuntu:~$ roslaunch raspicam_node camerav2_1280x960_10fps.launch 
	
	ohne: enable_raw:=true  sonst kommen nur 5fps
	rostopic hz /raspicam_node/image/compressed
	
	?? Regelt der Raspberry Pi die Leistung runter (bei Wärme?)

Remote PC

# Erkennen zweier weißer Linien => Mitte senden  topic   /lane
rosrun rtc lane_detect_sw1_line_detect_with_mask.py

# PD-Regler für das folgen der /lane
rosrun rtc lane_detect_sw2_control_cmd_vel.py


Problem 16.1.23. Lenkt zu früh ein => Kamerausschnit mölichst tief
Gegenproblem: Wenn Kameraausschnitt zu tief, 
gibt es rechts und links kaum Toleranz, bis die Kontur aus dem Bild verschwindet

?Lösung Streifen in der Mitte?

Lösung Kamera tiefer montieren und steiler => uoside Down Bild
# Bild umdrehen, da Camera am TB3 upside down montiert
cv_image = cv2.rotate(cv_image2 , cv2.ROTATE_180)

Besser lenkt zu früh ein, Bild mit kleinerer Brennweite??
