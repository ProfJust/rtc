#!/usr/bin/env python3
# ################################################################################
# edited WHS, OJ , 7.1.2022 #
# sudo apt-get install python3-opencv

import cv2
print(cv2.__version__)

# lese Bild von Festplatte
image = cv2.imread('/home/oj/catkin_ws/src/rtc/scripts/open_cv/test.png')

# zeige Bild in Fenster an
cv2.imshow("Bild", image)

# warte auf Tastendruck (wichtig, sonst sieht man das Fenster nicht)
cv2.waitKey(0)
