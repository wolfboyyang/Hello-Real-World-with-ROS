#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
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
#  * Neither the name of Willow Garage, Inc. nor the names of its
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
# Revision $Id$

## Node to publish to a string topic.

# this code is based on
# https://github.com/ros2/examples/
# rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/
# publisher_local_function.py

import rclpy

from hrwros_msgs.msg import SensorInformation
from hrwros_utilities.sim_sensor_data import distSensorData as getSensorData


def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('sensor_info_publisher')
    si_publisher = node.create_publisher(SensorInformation, '/sensor_info', 10)

    # Create a new SensorInformation object and fill in its contents.
    sensor_info = SensorInformation()

    # Fill in the header information.
    sensor_info.sensor_data.header.stamp = node.get_clock().now().to_msg()
    sensor_info.sensor_data.header.frame_id = 'distance_sensor_frame'

    # Fill in the sensor data information.
    sensor_info.sensor_data.radiation_type = sensor_info.sensor_data.ULTRASOUND
    sensor_info.sensor_data.field_of_view = 0.5 # Field of view of the sensor in rad.
    sensor_info.sensor_data.min_range = 0.02 # Minimum distance range of the sensor in m.
    sensor_info.sensor_data.max_range = 2.0 # Maximum distance range of the sensor in m.

    # Fill in the manufacturer name and part number.
    sensor_info.maker_name = 'The Ultrasound Company'
    sensor_info.part_number = 123456

    def timer_callback():
        # Read the sensor data from a simulated sensor.
        sensor_info.sensor_data.range = getSensorData(sensor_info.sensor_data.radiation_type,
            sensor_info.sensor_data.min_range, sensor_info.sensor_data.max_range)

        # Publish the sensor information on the /sensor_info topic.
        si_publisher.publish(sensor_info)
        # Print log message if all went well.
        node.get_logger().info('All went well. Publishing topic')

    timer_period = 0.1  # seconds
    timer = node.create_timer(timer_period, timer_callback)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('KeyboardInterrupt, shutting down.\n')

    # Destroy the timer attached to the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_timer(timer)
    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
