#!/usr/bin/env python3
# =================================================
# edited WHS, OJ , 13.1.2023 #
#
# Ein Bild der raspicam vom ROS raspicam_node holen
# -------------------------------------------------------
import rospy
import numpy
from sensor_msgs.msg import CompressedImage
# was from sensor_msgs.msg import Image

# raspicam_node => sensor_msgs/CompressedImage
# hier =>  raspicam_node/image/compressed
import cv2

# import cv_bridge
from cv_bridge import CvBridge


class PiCam:
    def __init__(self):
        self.bridge = CvBridge()
        cv2.namedWindow("window", 1)
        self.image_sub = rospy.Subscriber('/raspicam_node/image/compressed',
                                          CompressedImage, self.image_callback,
                                          queue_size=1)

    def image_callback(self, msg_img):
        # converts compressed image to opencv image
        np_image_original = numpy.frombuffer(msg_img.data, numpy.uint8)
        cv2_img = cv2.imdecode(np_image_original, cv2.IMREAD_COLOR)

        cv2.imshow("window", cv2_img)
        cv2.waitKey(1)
        # cv2.imshow("window", cv2_img)
        # cv2.waitKey(1)


rospy.init_node('follower')
follower = PiCam()
rospy.spin()  # keeps this node from exiting until the node has been shutdown
