#!/usr/bin/env python3
# ################################################################################
# edited WHS, OJ , 7.1.2022 #
import cv2

# initialisiere WebCam
cam = cv2.VideoCapture(0)

# lese ein Bild von der WebCam
# mehrfach, da Webcam erst hochfahren und fokussieren muss
ret, image = cam.read()
ret, image = cam.read()
ret, image = cam.read()

# zeige das Bild an
cv2.imshow("Bild von Webcam,", image)

# konvertiere das Bild in Graustufen
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.waitKey(0)

# zeige das Bild an
# cv2.imshow("Bild modifiziert", image)

# warte auf Tastendruck (wichtig, sonst sieht man das Fenster nicht)
cv2.waitKey(0)

cv2.imwrite('/home/oj/Bilder/bild_von_webcam.jpg', image)
