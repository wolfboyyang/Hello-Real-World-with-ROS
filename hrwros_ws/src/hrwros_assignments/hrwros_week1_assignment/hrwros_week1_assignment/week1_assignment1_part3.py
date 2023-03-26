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

# Assignment 1 for Week1: In this assignment you will subscribe to the topic
# that publishes sensor information. Then, you will transform the sensor
# reading from the reference frame of the sensor to compute the height of a
# box based on the illustration shown in the assignment document. Then, you
# will publish the box height on a new message type ONLY if the height of the
# box is more than 10cm.

# All necessary python imports go here.
import rclpy
# Copy the code from Part1 here
from hrwros_msgs.msg import <write-your-code-here-Part1>
# Import the correct message type for part 3
from hrwros_week1_assignment_interfaces.msg import <write-your-code-here-Part3>

g_node = None


def sensor_info_callback(data, bhi_publisher):

    # Copy the code from Part1 here
    height_box = <write-your-code-here-Part1>

    # Compute the height of the box.
    # Boxes that are detected to be shorter than 10cm are due to sensor noise.
    # Do not publish information about them.
    # Copy the code from Part1 here
    if <write-your-code-here-Part1>:
        pass
    else:
        # Declare a message object for publishing the box height information.
        box_height_info = <write-your-code-here-Part3>
        # Update height of box.
        <write-your-code-here-Part3>
        # Publish box height using the publisher argument passed to the
        # callback function.
        <write-your-code-here-Part3>


def main(args=None):
    rclpy.init(args=args)

    # Initialize the ROS node here.
    g_node = rclpy.create_node('compute_box_height')

    # Copy the code from Part1 here
    g_node.get_logger.info('Waiting for topic %s to be published...', <use the correct topic name here>)
    rclpy.wait_for_message(<use the correct message type here>, node, '<use the correct topic name here>')
    g_node.get_logger.info('%s topic is now available!', <use the correct topic name here>)

    # Create the publisher for Part3 here
    bhi_publisher = node.create_publisher(<use correct message type here>, '<use correct topic name here>', 10)

    # Note here that an ADDITIONAL ARGUMENT (bhi_publisher) is passed to the
    # subscriber. This is a way to pass ONE additional argument to the
    # subscriber callback. If you want to pass multiple arguments, you can use
    # a python dictionary. And if you don't want to use multiple arguments to
    # the subscriber callback then you can also consider using a Class
    # Implementation like we saw in the action server code illustration.

    # Copy the subscriber from Part1 here
    subscription = node.create_subscription(<use correct message type here>, '<use correct topic name here>', <use the correct callback name here>, bhi_publisher)
    subscription

    # Prevent this code from exiting until Ctrl+C is pressed.
    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
