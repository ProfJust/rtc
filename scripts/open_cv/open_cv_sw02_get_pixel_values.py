#!/usr/bin/env python3
# ################################################################################
# edited WHS, OJ , 7.1.2022 #

import cv2
print(cv2.__version__)

# lese Bild von Festplatte
image = cv2.imread('/home/oj/catkin_ws/src/rtc/scripts/open_cv/test.png')

# lese Farbwerte an Position y, x
y = 100
x = 50
(b, g, r) = image[y, x]

# gib Farbwerte auf Bildschirm aus
print(b, g, r)

# Zeichne rote Linie (im BGR-Farbraum)
for x in range(1, 100):
    image[y, x] = (0, 0, 255)


# zeige Bild in Fenster an
cv2.imshow("Bild", image)

# warte auf Tastendruck (wichtig, sonst sieht man das Fenster nicht)
cv2.waitKey(0)
