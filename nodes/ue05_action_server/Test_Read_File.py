#!/usr/bin/env python3

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

path = [[0.0, 0.0]]  # Initial Koordinaten
# fobj = open("path.txt", "r")
fobj = open("/home/oj/catkin_ws/src/rtc/nodes/ue05_action_server/path.txt", 'r')
for line in fobj:
    path.append(eval(line))
fobj.close()
print(path)
print(path[1])
print(path[1][0])
print(path[1][1])




 # rospy.get_param("/path")
        # f = open("/home/oj/catkin_ws/src/rtc/nodes/ue05_action_server/path.txt", 'r')
        # txt = load(f)
        # f.close()
        # rospy.loginfo(str(txt))
        # -----------------------------------------
        # self.path = [[0.0, 0.0]]  # Initiale Koordinaten
        # with open('path.txt', 'r') as filehandle:
        #   filecontents = filehandle.readlines()

        # for line in filecontents:
        #    rospy.loginfo(str(line))
"""with open('path.txt') as fin:
            for line in fin:
                rospy.loginfo(str(line))
"""