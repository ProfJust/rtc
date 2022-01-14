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
        cv2.imshow("window", cv2_img)
        cv2.waitKey(1)

        """# converts compressed image to opencv image
        # deprecated fromstring
        # DeprecationWarning:
        # The binary mode of fromstring is deprecated,
        #  as it behaves surprisingly on unicode inputs. Use frombuffer instead
        # np_image_original = numpy.fromstring(msg_img.data, numpy.uint8)

        np_image_original = np.fromstring(msg.data, np.uint8)
        image = cv2.imdecode(np_image_original, cv2.IMREAD_COLOR)

        # image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        cv2.imshow("window", image)
        cv2.waitKey(3)
        """


rospy.init_node('follower')
follower = PiCam()
rospy.spin()
