# ball_tracking_edited.py
# ------------------------------------------
# original from
# https://github.com/jonathanfoster/ball-tracking
# edited by OJ for robotik.bocholt@w-hs.de
# 8.11.2019
# ------------------------------------------
# $ python ball_tracking_edited.py -i Prof_mit_Kugel.jpeg
import argparse
# Parser for command-line options, arguments and sub-commands

import imutils
# convenience functions to make basic image processing
# https://github.com/jrosebr1/imutils
# sudo pip install --upgrade imutils

import cv2  # openCV


# ----- Argumente von der Kommandozeile lesen mit argparse ---
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the (optional) video file")
args = vars(ap.parse_args())

# ----- zu suchende Farbe des Balls einstellen ----
# greenLower = (29, 86, 6)
# HSV-Farbraum (Farbe, Saettigung, Helligkeit)
# greenLower = (50, 150, 50)
# greenUpper = (180, 255, 100)
greenLower = (0, 230, 198)  # H, S, V
greenUpper = (14, 255, 255)

# ---- Capture / Erfassung der Camera ------
# ohne Komandozeilenargumente => aktuelle Kamera
# mit K. => -i Video.mp4
if not args.get("video", False):
    camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])

# ---- Dauerschleife ------
while True:
    # aktuelles Bild/Frame holen
    (grabbed, frame) = camera.read()

    if args.get("video") and not grabbed:
        break

    # auf Breite = 600 Pixel normieren
    frame = imutils.resize(frame, width=600)
    # Farbraum auf HSV anpassen
    #  In HSV, it is more easier to represent a color than RGB color-space.
    # https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only colors in configured Range
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    # Erodieren
    mask = cv2.erode(mask, None, iterations=2)
    # Dilatation
    mask = cv2.dilate(mask, None, iterations=2)

    # Konturen finden
    cnts = cv2.findContours(mask.copy(),
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            print("Objekt erkannt an Position " + str(x) + " " + str(y))

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
