#!/usr/bin/env python3
# =================================================
# edited WHS, OJ , 13.1.2023 #
#
# Ein unkomprimiertes Bild der raspicam vom ROS raspicam_node holen
# https://stackoverflow.com/questions/55377442/how-to-subscribe-and-publish-images-in-ros
# -------------------------------------------------------
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
# import os
# import numpy as np


class Nodo(object):
    def __init__(self):
        # Params
        self.image = None
        self.bridge = CvBridge()
        # Node cycle rate (in Hz).
        self.loop_rate = rospy.Rate(1)

        # Publishers
        self.pub = rospy.Publisher('image', Image, queue_size=10)

        # Subscribers
        rospy.Subscriber('/raspicam_node/image',
                         Image, self.callback)

    def callback(self, msg):
        rospy.loginfo('Image received...')
        # http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

        # -- convert ROS-Image to OpenCV-Imnage with CvBridge
        cv2_img = self.bridge.imgmsg_to_cv2(msg.data)
        #                                   desired_encoding='passthrough')
        cv2.imshow("window", cv2_img)
        cv2.waitKey(0)
        # self.image = self.br.imgmsg_to_cv2(msg.data)
        # converts compressed image to opencv image
        # np_image = np.frombuffer(msg.data, np.uint8)
        # cv2_img = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

        # ####### cv2.size
        if cv2_img is not None:
            rospy.loginfo("=> show in window")
            cv2.imshow("window", cv2_img)
            cv2.waitKey(0)
        else:
            rospy.loginfo(" no image to show")

    def start(self):
        rospy.loginfo("subscribe and publich image")
        while not rospy.is_shutdown():
            rospy.loginfo('publishing image')
            if self.image is not None:
                self.pub.publish(self.br.cv2_to_imgmsg(self.image))
            self.loop_rate.sleep()


if __name__ == '__main__':
    rospy.init_node("imagetimer", anonymous=True)
    my_node = Nodo()
    my_node.start()
