cmake_minimum_required(VERSION 3.5)
project(hrwros_msgs)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

## Find dependencies
find_package (Python3 3.10 EXACT)
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(moveit_msgs REQUIRED)

################################################
## Declare ROS messages, services and actions ##
################################################
## Generate interfaces

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/ObjectDetection.msg"
  "msg/TargetToolPoses.msg"
  "msg/RobotTrajectories.msg"
  "msg/SensorInformation.msg"
  "srv/ConvertMetresToFeet.srv"
  "action/CounterWithDelay.action"
  DEPENDENCIES moveit_msgs
)

## Declare dependencies
ament_export_dependencies(rosidl_default_runtime)

## Package information
ament_package()
