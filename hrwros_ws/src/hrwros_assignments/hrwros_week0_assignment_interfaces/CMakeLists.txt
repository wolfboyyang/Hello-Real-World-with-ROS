cmake_minimum_required(VERSION 3.5)
project(hrwros_week0_assignment_interfaces)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

## Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

################################################
## Declare ROS messages, services and actions ##
################################################
## Generate interfaces

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Dummy.msg"
)

## Declare dependencies
ament_export_dependencies(rosidl_default_runtime)

## Package information
ament_package()
