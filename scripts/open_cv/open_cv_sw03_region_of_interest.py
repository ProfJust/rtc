#!/usr/bin/env python3
# ################################################################################
# edited WHS, OJ , 7.1.2022 #

import cv2 as cv

# lese Bild von Festplatte
image = cv.imread('/home/oj/catkin_ws/src/rtc/scripts/open_cv/test.png')

# Position y, x
y = 100
x = 50

# waehle eine Region of Interest an Punkt:
# (y, x) mit Dimension 50x50 Pixel
region_of_interest = image[y:y+50, x:x+50]

# zeige Region of Interest an
cv.imshow("ROI", region_of_interest)

# warte auf Tastendruck (wichtig, sonst sieht man das Fenster nicht)
cv.waitKey(0)

# setze ROI auf Gruen
region_of_interest[:, :] = (0, 255, 0)

# die ROI ist ein "Zeiger" auf das urspruenglich geladene Image.
# Es enthaelt nun eine gruene Box!
cv.imshow("Bild modifiziert", image)

# warte auf Tastendruck
cv.waitKey(0)
