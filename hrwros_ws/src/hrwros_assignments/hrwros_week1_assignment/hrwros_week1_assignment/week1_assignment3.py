#! /usr/bin/env python3

# This code has been adapted from the ROS Wiki actionlib tutorials
# to the context of this course.
# (http://wiki.ros.org/hrwros_msgs/Tutorials)

from hrwros_msgs.action import CounterWithDelay

import rclpy
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node

class CounterWithDelayActionServer(Node):

    def __init__(self):
        # This will be the name of the action server which clients can use to connect to.
        super().__init__('counter_with_delay_action_server')

        self.declare_parameter("counter_delay", 1.0)

        # Create a simple action server of the newly defined action type and
        # specify the execute callback where the goal will be processed.
        self._action_server = ActionServer(
            self,
            CounterWithDelay,
            'counter_with_delay',
            execute_callback=self.execute_callback,
            callback_group=ReentrantCallbackGroup(),
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback)

        # Start the action server.
        self.get_logger().info("Action server started...")

    def destroy(self):
        self._action_server.destroy()
        super().destroy_node()

    def goal_callback(self, goal_request):
        """Accept or reject a client request to begin an action."""
        # This server allows multiple goals in parallel
        self.get_logger().info('Received goal request')
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        """Accept or reject a client request to cancel an action."""
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT
    
    async def execute_callback(self, goal_handle):
        counter_delay_value = 1.0

        #####################################################################
        #  Assignment 3 - Part3                                             #
        #  modify counter delay using "counter_delay" a private parameter.  #

        if self.has_parameter("counter_delay"):
            counter_delay_value = self.get_parameter("counter_delay").value
            self.get_logger().info("Parameter found on the parameter server "
                          " Using %.1fs for counter delay." %
                          (counter_delay_value))
        else:
            self.get_logger().info("Parameter not found on the parameter server "
                          "Using default value of 1.0s for counter delay.")

        # End of Assignment 3 - Part3                                       #
        #####################################################################

        # Variable for delay
        # Keep in mind a rate is in units 1/sec or Hz
        # We convert the counter_delay_value from seconds to Hz
        delay_rate = self.create_rate(1 / counter_delay_value)

        # publish info to the console for the user
        self.get_logger().info('%s action server is counting up to %i '
                      'with %.1fs delay between each count' %
                      (self.get_name(), goal_handle.request.num_counts,
                       counter_delay_value))

        feedback_msg = CounterWithDelay.Feedback()

        # Start executing the action
        for i in range(1, goal_handle.request.num_counts):
            # Check that preempt has not been requested by the client
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled')
                return CounterWithDelay.Result()

            # Update counts
            feedback_msg.counts_elapsed = i

            # Publish the feedback
            goal_handle.publish_feedback(feedback_msg)
            # Wait for counter_delay seconds before incrementing the counter.
            # If the rate is 5Hz, this will sleep for 1/5=0.2 seconds.
            delay_rate.sleep()

        goal_handle.succeed()

        # Populate result message
        result = CounterWithDelay.Result()
        result.result_message = f'Successfully completed counting: {feedback_msg.counts_elapsed}'
        self.get_logger().info('%s: Succeeded' % self.get_name())

        return result


def main(args=None):
    rclpy.init(args=args)

    # Create an instance of the action server here.
    server = CounterWithDelayActionServer()

    # Use a MultiThreadedExecutor to enable processing goals concurrently
    executor = MultiThreadedExecutor()

    try:
        rclpy.spin(server, executor=executor)
    except KeyboardInterrupt:
        server.get_logger().info('KeyboardInterrupt, shutting down.\n')

    server.destroy()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()