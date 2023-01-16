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
from std_msgs.msg import Int16
from cv_bridge import CvBridge, CvBridgeError
from matplotlib import pyplot as plt


class ImageConverter:

    def __init__(self):
        # self.image_pub = rospy.Publisher("modified_image",
        #                                 CompressedImage, queue_size=10)
        # If the number of messages arriving in a single ros::spin()
        # is greater than the queue_size, the extra messages
        #  will be discarded. => perfomance improvement

        self.lane_pub = rospy.Publisher("lane", Int16, queue_size=10)

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
        roi = cv_image[720:800, 0:1279]  # [y...] [x..]
        # roi_width = 1179-100
        # zeige Region of Interest an
        # cv2.imshow("Image Window", roi)
        # cv2.waitKey(3)

        # konvertiere das Bild in Graustufen
        roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("Image Window", roi_gray)
        # cv2.waitKey(3)

        # Threshold the gray image to get only colors in configured Range
        mask = cv2.inRange(roi_gray, 230, 255)
        # cv2.imshow("Mask roi", mask)
        # cv2.waitKey(3)

        # Erodieren
        mask = cv2.erode(mask, None, iterations=2)
        # cv2.imshow("Mask erode", mask)
        # cv2.waitKey(3)

        # Dilatation
        mask = cv2.dilate(mask, None, iterations=2)
        # cv2.imshow("Mask dilate", mask)
        # cv2.waitKey(3)

        # Konturen finden
        contours = cv2.findContours(mask.copy(),
                                    cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)[-2]
        # print(len(contours))  # Anzahl der Konturen
        self.lane = 0  
        if len(contours) > 1:
            c = max(contours, key=cv2.contourArea)
            (x, y, w, h) = cv2.boundingRect(c)
            # umgebendes Rechteck zeichnen
            cv2.rectangle(roi_gray, (x, y), (x+w, y+h), (0, 255, 0), 2)
            posleft = (x + w)  # linke Contour rechte Ecke
         
            c2 = min(contours, key=cv2.contourArea)
            (x, y, w, h) = cv2.boundingRect(c2)
            # umgebendes Rechteck zeichnen
            cv2.rectangle(roi_gray, (x, y), (x+w, y+h), (0, 255, 0), 4)
            posright = x  # rechte Contour , linke Ecke
            print("Linien erkannt an Positionen "
                  + str(posleft) + " & " + str(posright))

            self.lane = int((posright - posleft) / 2 + posleft)

        print("lane " + str(self.lane))
        cv2.rectangle(roi_gray, (self.lane, 2), (self.lane + 10, 20),
                      (255, 255, 255), 5)  # GrauBild
        cv2.imshow("Contours & Lane", roi_gray)
        cv2.waitKey(3)
        
        try:
            # self.image_pub.publish(self.brige.
            #                       cv2_to_compressed_imgmsg(cv_image))
            self.lane_pub.publish(self.lane)
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
