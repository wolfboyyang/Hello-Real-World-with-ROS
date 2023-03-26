#! /usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, Delft University of Technology
# TU Delft Robotics Institute.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of SRI International nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Authors: the HRWROS mooc instructors

# Assignment 2 for Week1: In this assignment you will subscribe to the topic that
# publishes information on the box height in metres and use the metres_to_feet
# service to convert this height in metres to height in feet.

import rclpy

from hrwros_msgs.srv import ConvertMetresToFeet, ConvertMetresToFeetRequest, ConvertMetresToFeetResponse

g_node = None


def box_height_info(data):
    cli = g_node.create_client(use the correct message type here>, '<use the correct service name here>')
    # First wait for the service to become available.
    while not cli.wait_for_service(timeout_sec=1.0):
        g_node.get_logger().info('Waiting for service...')
    
    # Create a proxy for the service to convert metres to feet.
    box_height_info = rospy.ServiceProxy(<update the correct details here>)

    # Call the service here.
    service_response = <write your code here>

    # Write a log message here to print the height of this box in feet.
    <write your code here>
    return service_response


def main(args=None):
    rclpy.init(args=args)

    # Initialize the ROS node here.
    g_node = rclpy.create_node('box_height_in_feet')

    # Call the service client function to get to the box height.
    service_response = box_height_info(dist_metres)

    # Process the service response and display log messages accordingly.
    if(not service_response.success):
         g_node.get_logger().err("Conversion unsuccessful! Requested distance in metres should be a positive real number.")
    else:
        g_node.get_logger().info("Conversion successful!")


if __name__ == '__main__':
    main()
