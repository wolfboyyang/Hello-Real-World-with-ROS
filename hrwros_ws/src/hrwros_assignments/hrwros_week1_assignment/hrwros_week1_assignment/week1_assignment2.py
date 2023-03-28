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
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup

from hrwros_msgs.srv import ConvertMetresToFeet
from hrwros_week1_assignment_interfaces.msg import BoxHeightInformation


class BoxHeightInFeetNode(Node):

    def __init__(self):
        super().__init__('box_height_in_feet')

        self.callback_group = ReentrantCallbackGroup()

        self.subscription = self.create_subscription(
            BoxHeightInformation, 'box_height_info',
            self.box_height_info_callback, 10, callback_group=self.callback_group)

        # Create a proxy for the service to convert metres to feet.
        self.cli = self.create_client(ConvertMetresToFeet, 'metres_to_feet',
            callback_group=self.callback_group)
        
        # First wait for the service to become available.
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')
        
    async def box_height_info_callback(self, data):
        # Create a service request.
        request = ConvertMetresToFeet.Request()
        request.distance_metres = data.box_height
        
        response = await self.cli.call_async(request)

        # Process the service response and display log messages accordingly.
        if(not response.success):
            self.get_logger().err("Conversion unsuccessful! Requested distance in metres should be a positive real number.")
        else:
            # Write a log message here to print the height of this box in feet.
            self.get_logger().info('The height of this box (%.3fm) in feet is %.3fft'
                % (data.box_height, response.distance_feet))


def main(args=None):
    rclpy.init(args=args)

    # Initialize the ROS node here.
    node = BoxHeightInFeetNode()

    # Prevent this code from exiting until Ctrl+C is pressed.
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('KeyboardInterrupt, shutting down.\n')

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
