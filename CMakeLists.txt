cmake_minimum_required(VERSION 3.0.2)
project(rtc)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  rospy
  roscpp
  std_msgs
  sensor_msgs
  diagnostic_msgs
  turtlebot3_msgs
)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)
find_package(PythonLibs 3 REQUIRED)


###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if your package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES rtc
#  CATKIN_DEPENDS rospy std_msgs
#  DEPENDS system_lib
  CATKIN_DEPENDS roscpp std_msgs sensor_msgs diagnostic_msgs turtlebot3_msgs
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
# catkin_install_python(PROGRAMS
#   scripts/my_python_script
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

# Ort wo die Python-Skripte fuer die ROS-Knoten liegen
file(GLOB python_nodes_DIR
    "nodes/*/*.py"
)
# Ort wo die Python-Skripte (ohne ROS.Bezug) liegen
file(GLOB python_scripts_DIR
    "scripts/*/*.py"
)
catkin_install_python(PROGRAMS 
		       ${python_scripts_DIR}
                      ${python_nodes_DIR}
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})


