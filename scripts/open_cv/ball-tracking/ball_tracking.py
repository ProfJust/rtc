# https://github.com/jonathanfoster/ball-tracking
# $ python ball_tracking.py --video ball_tracking_example.mp4
import argparse
import imutils
import cv2
import time

# Lesen des Konsolenbefehls incl. Argumente
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the (optional) video file")
args = vars(ap.parse_args())

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

# Kamera-Input oder gespeicherte Video?
# Video-Datei bei Shellaufruf angegeben, z.B.
# python ball_tracking.py --video ball_tracking_example.mp4
if not args.get("video", False):
    camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])

while True:
    # Ein Bild/Frame des Videos holen
    (grabbed, frame) = camera.read()

    if args.get("video") and not grabbed:
        break

    # Farbraum BGR => HSV wechseln
    frame = imutils.resize(frame, width=600)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # nur grüne Pixel finden => mask-Image
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    # Morphologie Erosion und Dilatation => Rauschen entfernen
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Contouren finden => cnts
    cnts = cv2.findContours(mask.copy(),
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    # Wenn Contouren gefunden wurden
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        # Kleinsten umschliessenden Kreis finden
        # https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        # Ist der Radius groß genug für unseren Ball?
        if radius > 10:
            # Gelben Kreis zeichnen
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
    time.sleep(0.1)

camera.release()
cv2.destroyAllWindows()
