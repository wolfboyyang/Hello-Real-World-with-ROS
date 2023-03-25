#! /usr/bin/env python3
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
from __future__ import print_function

from action_msgs.msg import GoalStatus
from hrwros_msgs.action import CounterWithDelay

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

import sys
# Brings in the SimpleActionClient
import actionlib
# Brings in the messages used by the CounterWithDelay action, including the
# goal message and the result message.
from hrwros_msgs.msg import CounterWithDelayAction, CounterWithDelayGoal


def CounterWithDelayActionClient(Node):

    def __init__(self):
        # Creates the SimpleActionClient, passing the type of the action
        # (CounterWithDelayAction) to the constructor.
        super().__init__('counter_with_delay_action_client')
        self._action_client = ActionClient(self, CounterWithDelay, 'counter_with_delay')

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(self, feedback):
        self.get_logger().info('Received feedback: {0}'.format(feedback.feedback.counts_elapsed))

    def get_result_callback(self, future):
        result = future.result().result
        status = future.result().status
        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info('Goal succeeded! Result: {0}'.format(result.result_message))
        else:
            self.get_logger().info('Goal failed with status: {0}'.format(status))

        # Shutdown after receiving a result
        rclpy.shutdown()

    def send_goal(self):
        # Waits until the action server has started up and started
        # listening for goals.
        self.get_logger().info('Waiting for action server to come up...')
        self._action_client.wait_for_server()

        num_counts = 3

        # Creates a goal to send to the action server.
        goal_msg = CounterWithDelay.Goal()
        goal_msg.num_counts = num_counts

        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

        self.get_logger().info("Goal has been sent to the action server.")


        # Waits for the server to finish performing the action.
        # client.wait_for_result()

        # Does something else while the action is being done:
        rate = self.create_rate(1.2)
        for i in range(0, num_counts):
            rospy.loginfo('I am doing other things while the goal is being serviced by the server')
            rate.sleep()

        # Prints out the result of executing the action
        #return client.get_result()  # A CounterWithDelayResult


def main(args=None):
    # Initializes a rospy node so that the SimpleActionClient can
    # publish and subscribe over ROS.
    rclpy.init(args=args)

    action_client = CounterWithDelayActionClient()

    action_client.send_goal()

    rclpy.spin(action_client)

    
if __name__ == '__main__':
    main()