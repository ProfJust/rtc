#!/usr/bin/env python3
#
# https://stackoverflow.com/questions/51688799/
# ros-melodic-opencv-compressedimage-not-publishing
# =================================================
# edited WHS, OJ , 13.1.2023 #
#
# Ein Bild der raspicam vom ROS raspicam_node holen
# rostopic hz /raspicam_node/image muss < 1.0 sein
# -------------------------------------------------------
import roslib
import sys
import rospy
import cv2
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError
from matplotlib import pyplot as plt


class ImageConverter:

    def __init__(self):
        self.image_pub = rospy.Publisher("modified_image",
                                         CompressedImage, queue_size=10)
        # If the number of messages arriving in a single ros::spin()
        # is greater than the queue_size, the extra messages
        #  will be discarded. => perfomance improvement

        self.brige = CvBridge()
        self.image_sub = rospy.Subscriber("/raspicam_node/image/compressed",
                                          CompressedImage, self.callback)

    def callback(self, data):
        try:
            cv_image = self.brige.compressed_imgmsg_to_cv2(data, "passthrough")
        except CvBridgeError as e:
            print(e)

        # ROI  waehle eine Region of Interest an Punkt:
        # 1280 x 960 Pixel
        roi = cv_image[900:959, 100:1179]  # [y...] [x..]
        roi_width = 1179-100
        # zeige Region of Interest an
        # cv2.imshow("Image Window", roi)
        # cv2.waitKey(3)

        # konvertiere das Bild in Graustufen
        roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("Image Window", roi_gray)
        # cv2.waitKey(3)
        

        # https://docs.opencv.org/4.x/d1/db7/tutorial_py_histogram_begins.html
        hist = cv2.calcHist([roi_gray], [0], None, [256], [0, 256])

        # https://stackoverflow.com/questions/47085909/find-the-centre-value-of-the-two-highest-peaks-in-a-histogram-python
        # Convert histogram to simple list
        hist_list = [val[0] for val in hist]
        # Generate a list of indices
        indices = list(range(0, 256))
        # Descending sort-by-key with histogram value as key
        s = [(x, y) for y, x in sorted(zip(hist_list, indices), reverse=True)]

        # Achtung: Histogramm gibt die Verteilung der Grauwerte 0..255 an,
        # aber nicht den Ort wo die Grauwerte liegen
        # => weiße Linie ist nicht am highest peak zu finden

        # Index of highest peak in histogram
        ind_hi_pk = s[0][0]
        print(ind_hi_pk)

        # Peak sollten nicht zu nah beieinander liegen
        dist = 20
        i = 1
        while True:
            # Index of second highest peak in histogram
            ind_2hi_pk = s[i][0]
            if ind_2hi_pk > (ind_hi_pk + dist) or ind_2hi_pk < (ind_hi_pk - dist):
                break
            else:
                i = i+1

        print(ind_2hi_pk)
        # plt.plot(hist)
        # plt.show()

        # Zeichne rote Linie (im BGR-Farbraum)
        # roi_gray[50, ind_hi_pk] = (0, 0, 255)
        # roi_gray[50, ind_2hi_pk] = (0, 255, 0)

        x1_peak = int(ind_hi_pk * roi_width/256 -130)
        x2_peak = int(ind_2hi_pk * roi_width/256 -170)

        # circle (x, y), radius, (bgr), thickness
        cv2.circle(roi, (x1_peak, 40),
                   10, (10, 10, 255), 5)
        cv2.circle(roi, (x2_peak, 40),
                   10, (10, 10, 255), 5)

        cv2.imshow("ROI ", roi)
        cv2.waitKey(3)

        try:
            self.image_pub.publish(self.brige.
                                   cv2_to_compressed_imgmsg(cv_image))
        except CvBridgeError as e:
            print(e)


def main(args):
    ic = ImageConverter()
    rospy.init_node("image_converter", anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
