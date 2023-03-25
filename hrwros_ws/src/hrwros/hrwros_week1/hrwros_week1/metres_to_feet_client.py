#!/usr/bin/env python3
# This code has been adapted from the ROS Wiki ROS Service tutorials to the context
# of this course.
# (http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29)

import sys

import rclpy

from hrwros_msgs.srv import ConvertMetresToFeet, ConvertMetresToFeetRequest, ConvertMetresToFeetResponse

g_node = None

def metres_to_feet_client(x):
    cli = g_node.create_client(ConvertMetresToFeet, 'metres_to_feet')
    # First wait for the service to become available.
    while not cli.wait_for_service(timeout_sec=1.0):
        g_node.get_logger().info('Waiting for service...')
    
    # Create a service request.
    req = ConvertMetresToFeet.Request()
    req.distance_metres = x
    # Call the service here.
    future = cli.call_async(req)
    rclpy.spin_until_future_complete(g_node, future)

    service_response = future.result()
    # Return the response to the calling function.
    return service_response


def main(args=None):
    # Initialize the client ROS node.
    rclpy.init(args=args)
    g_node = rclpy.create_node('metres_to_feet_client')

    # The distance to be converted to feet.
    dist_metres = 0.25

    g_node.get_logger().info("Requesting conversion of %4.2f m to feet" % (dist_metres))

    # Call the service client function.
    service_response = metres_to_feet_client(dist_metres)

    # Process the service response and display log messages accordingly.
    if(not service_response.success):
         g_node.get_logger().err("Conversion unsuccessful! Requested distance in metres should be a positive real number.")
    else:
        g_node.get_logger().info("%4.2f m = %4.2f feet"%(dist_metres, service_response.distance_feet))
        g_node.get_logger().info("Conversion successful!")


if __name__ == '__main__':
    main()