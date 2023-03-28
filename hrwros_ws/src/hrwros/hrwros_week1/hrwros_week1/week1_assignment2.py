#! /usr/bin/env python

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
            '<write your code here:Type>', '<write your code here>:Topic',
            '<write your code here>:Callback', 10, callback_group=self.callback_group)

        # Create a proxy for the service to convert metres to feet.
        self.cli = self.create_client('<write your code here>:Type', '<write your code here>:Name',
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
