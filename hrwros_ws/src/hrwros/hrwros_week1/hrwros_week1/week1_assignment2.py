#! /usr/bin/env python

# Assignment 2 for Week1: In this assignment you will subscribe to the topic that
# publishes information on the box height in metres and use the metres_to_feet
# service to convert this height in metres to height in feet.

import rclpy

from hrwros_msgs.srv import ConvertMetresToFeet

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
    global g_node

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
