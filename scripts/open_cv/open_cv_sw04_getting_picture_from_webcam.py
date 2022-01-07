#!/usr/bin/env python3
# ################################################################################
# edited WHS, OJ , 7.1.2022 #

import cv2 as cv

# initialisiere WebCam
cam = cv.VideoCapture(0)

# WebCam braucht einen Moment zum Starten
# und zum Einstellen des Autofokus
# mehrere Bilder holen und die ersten verwerfen

# lese ein Bild von der WebCam
ret, image = cam.read()
ret, image = cam.read()
ret, image = cam.read()

# zeige das Bild an
cv.imshow("WebCam", image)
cv.waitKey(0)

# konvertiere das Bild in Graustufen
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# zeige das Bild an
cv.imshow("Bild modifiziert", image)
cv.waitKey(0)
