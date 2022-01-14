#!/usr/bin/env python3
# ################################################################################
# edited WHS, OJ , 14.1.2022 #
#
# line_detection_sw01_get_picture_from_ros.py
# Ein Bild der raspicam vom raspicam_node holen und ausgeben
# -------------------------------------------------------
import rospy
from sensor_msgs.msg import Image

import cv2
import cv_bridge


class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        cv2.namedWindow("window", 1)
        self.image_sub = rospy.Subscriber('/raspicam_node/image/compressed',
                                          Image, self.image_callback)

    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        cv2.imshow("window", image)
        cv2.waitKey(3)


rospy.init_node('follower')
follower = Follower()
rospy.spin()
