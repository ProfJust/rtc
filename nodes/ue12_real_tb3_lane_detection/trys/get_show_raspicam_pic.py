#!/usr/bin/env python3
# =================================================
# edited WHS, OJ , 13.1.2023 #
#
# Ein Bild der raspicam vom ROS raspicam_node holen
# rostopic hz /raspicam_node/image muss < 1.0 sein

# -------------------------------------------------------
import rospy
import numpy as np
# from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image

# raspicam_node => sensor_msgs/CompressedImage
# hier =>  raspicam_node/image/compressed
import cv2

# import cv_bridge
from cv_bridge import CvBridge


###### NO WORX NO WORX ######################################

class PiCam:
    def __init__(self):
        self.bridge = CvBridge()
        cv2.namedWindow("window", 1)
        # self.image_sub = rospy.Subscriber('/raspicam_node/image/compressed',
        #                                 CompressedImage, self.image_callback,
        #                                  queue_size=1)
        self.image_sub = rospy.Subscriber('/raspicam_node/image',
                                          Image, self.image_callback,
                                          queue_size=2)
        # If the number of messages that arrive on the
        # /raspicam_node/image topics in a single ros::spin()
        # is greater than the queue_size, the extra messages
        #  will be discarded. => perfomance improvement

    def image_callback(self, msg_img):
        # converting image to opencv image
        # interpret a buffer as a 1-dimensional array
        np_image = np.frombuffer(msg_img.data, np.uint8)
        # print(np_image)  # =>  [ 27  24  41 ... 255 254 255]

        # Reads an image from a buffer in memory
        # IMREAD_COLOR: convert image to the 3 channel BGR color image
        # https://docs.opencv.org/3.4/d8/d6a/group__imgcodecs__flags.html#ga61d9b0126a3e57d9277ac48327799c80
        # IMREAD_COLOR IMREAD_GRAYSCALE
        cv2_img = cv2.imdecode(np_image, cv2.IMREAD_COLOR)
        # print(cv2_img) => None  %%% WHY ??????
        
        if cv2_img is not None:
            rospy.loginfo("=> show in window")
            cv2.imshow("window", cv2_img)
            cv2.waitKey(0)
        else:
            rospy.loginfo(" no image to show")
        """
        No Image in cv2_img --> imshow():
        cv2.error: OpenCV(4.6.0) /io/opencv/modules/highgui/src/window.cpp:967:
        error: (-215:Assertion failed)
        size.width>0 && size.height>0 in function 'imshow'
        """


rospy.init_node('follower')
follower = PiCam()
rospy.spin()  # keeps this node from exiting until the node has been shutdown
