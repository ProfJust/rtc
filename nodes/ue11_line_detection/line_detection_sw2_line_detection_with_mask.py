#!/usr/bin/env python3
# =================================================
# edited WHS, OJ , 14.1.2022 #
#
# line_detection_sw2_with mask
# Ein Bild der raspicam vom ROS raspicam_node holen
# und den Ort der weißen Linie bestimmen
# -------------------------------------------------------
import rospy
from sensor_msgs.msg import CompressedImage
import cv2
import cv_bridge
import numpy


class PiCam:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        cv2.namedWindow("window", 1)
        self.image_sub = rospy.Subscriber('/raspicam_node/image/compressed',
                                          CompressedImage, self.image_callback,
                                          queue_size=1)

    def image_callback(self, msg_img):
        # converts compressed image to opencv image
        np_image_original = numpy.frombuffer(msg_img.data, numpy.uint8)
        cv2_img = cv2.imdecode(np_image_original, cv2.IMREAD_COLOR)

        # waehle eine Region of Interest an Punkt:
        # 410x308 Pixel
        roi_img = cv2_img[200:300, 20:390]  # [y...] [x..]

        # konvertiere das Bild in Graustufen
        roi_gray_img = cv2.cvtColor(roi_img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("ROI gray", roi_gray_img)
        cv2.waitKey(3)

        # Threshold the gray image to get only colors in configured Range
        mask = cv2.inRange(roi_gray_img, 230, 255)
        # Erodieren
        mask = cv2.erode(mask, None, iterations=2)
        # Dilatation
        mask = cv2.dilate(mask, None, iterations=2)
        # Konturen finden
        cnts = cv2.findContours(mask.copy(),
                                cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            (x, y, w, h) = cv2.boundingRect(c)
            # umgebendes Rechteck zeichnen
            cv2.rectangle(roi_gray_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            print("Linie erkannt an Position " + str((x+w)/2))

        cv2.imshow("Frame", roi_gray_img)
        cv2.imshow("Mask", mask)


rospy.init_node('follower')
follower = PiCam()
rospy.spin()
