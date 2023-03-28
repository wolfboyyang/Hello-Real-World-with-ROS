#!/usr/bin/env python
# This code has been adapted from the ROS Wiki ROS Service tutorials to the context
# of this course.
# (http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29)

from hrwros_msgs.srv import ConvertMetresToFeet

import rclpy

import numpy as np

_CONVERSION_FACTOR_METRES_TO_FEET = 3.28 # Metres -> Feet conversion factor.

g_node = None

# Service callback function.
def process_service_request(request, response):

    # Perform sanity check. Allow only positive real numbers.
    # Compose the response message accordingly.
    if(request.distance_metres < 0):
        response.success = False
        response.distance_feet = -np.Inf # Default error value.
    else:
        response.distance_feet = _CONVERSION_FACTOR_METRES_TO_FEET * request.distance_metres
        response.success = True

    # Return the response message.
    return response


def main(args=None):
    global g_node
    rclpy.init(args=args)

    # ROS node for the service server.
    g_node = rclpy.create_node('metres_to_feet_server')

    # Create a ROS service type.
    service = g_node.create_service(ConvertMetresToFeet, 'metres_to_feet', process_service_request)

    # Log message about service availability.
    g_node.get_logger().info('Convert metres to feet service is now available.')

    try:
        rclpy.spin(g_node)
    except KeyboardInterrupt:
        g_node.get_logger().info('KeyboardInterrupt, shutting down.\n')

    # Destroy the service attached to the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    g_node.destroy_service(service)
    rclpy.try_shutdown()


if __name__ == "__main__":
    main()
