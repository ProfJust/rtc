#!/usr/bin/env python3
# ################################################################################
# edited WHS, OJ , 7.1.2022 #

import cv2 as cv
print(cv.__version__)

# lese Bild von Festplatte
image = cv.imread('/home/oj/catkin_ws/src/rtc/scripts/open_cv/test.png')

# zeige Bild in Fenster an
cv.imshow("Bild", image)

# warte auf Tastendruck (wichtig, sonst sieht man das Fenster nicht)
cv.waitKey(0)
