#!/usr/bin/env python3
# =================================================
# edited WHS, OJ , 14.1.2022 #
#
# line_detection_sw01_get_picture_from_ros.py
# Ein Bild der raspicam vom ROS raspicam_node holen
# und ausgeben
# -------------------------------------------------------
import rospy
from sensor_msgs.msg import CompressedImage

# raspicam_node => sensor_msgs/CompressedImage
# hier =>  raspicam_node/image/compressed
import cv2
import cv_bridge
import numpy
from matplotlib import pyplot as plt


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
        # zeige Region of Interest an
        # cv2.imshow("ROI", roi_img)
        # warte auf Tastendruck (wichtig, sonst sieht man das Fenster nicht)
        # cv2.waitKey(0)
        # cv2.circle(roi_img, (136, 40), 10, (10, 10, 255), 5)
        # (x, y), radius, (bgr), thickness
        # cv2.imshow("ROI", roi_img)
        # cv2.waitKey(0)

        # konvertiere das Bild in Graustufen
        roi_gray_img = cv2.cvtColor(roi_img, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("ROI gray", roi_gray_img)
        # cv2.waitKey(0)

        # https://docs.opencv.org/4.x/d1/db7/tutorial_py_histogram_begins.html
        hist = cv2.calcHist([roi_gray_img], [0], None, [256], [0, 256])

        # https://stackoverflow.com/questions/47085909/find-the-centre-value-of-the-two-highest-peaks-in-a-histogram-python
        # Convert histogram to simple list
        hist_list = [val[0] for val in hist]
        # Generate a list of indices
        indices = list(range(0, 256))
        # Descending sort-by-key with histogram value as key
        s = [(x, y) for y, x in sorted(zip(hist_list, indices), reverse=True)]

        # Achtung: Histogramm gibt die VErteilung der Grauwerte 0..255 an,
        # aber nicht den Ort wo die Grauwerte liegen
        # => weiße Linie ist nicht am highest peak zu finden

        # Index of highest peak in histogram
        index_of_highest_peak = s[0][0]
        print(index_of_highest_peak)

        # Index of second highest peak in histogram
        index_of_second_highest_peak = s[1][0]
        print(index_of_second_highest_peak)

        # red line
        # Zeichne rote Linie (im BGR-Farbraum)
        # roi_gray_img[50, index_of_highest_peak] = (0, 0, 255)
        # roi_gray_img[50, index_of_second_highest_peak] = (0, 255, 0)

        cv2.circle(roi_gray_img, (185, 20), 10, (10, 10, 255), 5)
        # (x, y), radius, (bgr), thickness
        cv2.imshow("ROI gray", roi_gray_img)
        cv2.waitKey(3)

        plt.plot(hist)
        plt.show()


rospy.init_node('follower')
follower = PiCam()
rospy.spin()
