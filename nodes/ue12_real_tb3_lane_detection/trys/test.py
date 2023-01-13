#!/usr/bin/env python

from __future__ import print_function

import roslib
# roslib.load_manifest('comp_vision')
import sys
import rospy
import cv2
# from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError


class ImageConverter:

    def __init__(self):
        self.image_pub = rospy.Publisher("modified_image",
                                         CompressedImage, queue_size=10)
        self.brige = CvBridge()
        self.image_sub = rospy.Subscriber("/raspicam_node/image/compressed",
                                          CompressedImage, self.callback)

    def callback(self, data):
        try:
            cv_image = self.brige.compressed_imgmsg_to_cv2(data, "passthrough")
        except CvBridgeError as e:
            print(e)

        """(rows, cols, channels) = cv_image.shape
        if cols > 60 and rows > 60:
            cv2.circle(cv_image, (50, 50), 10, 255)
        """
        cv2.imshow("Image Window", cv_image)
        cv2.waitKey(3)

        try:
            self.image_pub.publish(self.brige.cv2_to_compressed_imgmsg(cv_image))
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
