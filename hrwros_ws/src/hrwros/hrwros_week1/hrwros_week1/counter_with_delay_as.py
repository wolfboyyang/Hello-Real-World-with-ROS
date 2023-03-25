#! /usr/bin/env python3

# This code has been adapted from the ROS Wiki actionlib tutorials to the context
# of this course.
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
        self._as.start()
        rospy.loginfo("Action server started...")

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
        # OPTIONAL: NOT GRADED Check if the parameter for the counter delay is available on the parameter server.
        # if not self.has_param("<write your code here>"):
        #     self.get_logger().info("Parameter %s not found on the parameter server. Using default value of 1.0s for counter delay.","counter_delay")
        #     counter_delay_value = 1.0
        # else:
        # Get the parameter for delay between counts.
        counter_delay_value = self.get_param("<write your code here>")
        self.get_logger().info("Parameter %s was found on the parameter server. Using %fs for counter delay."%("counter_delay", counter_delay_value))

        # Variable for delay
        # Keep in mind a rate is in units 1/sec or Hz
        # We convert the counter_delay_value from seconds to Hz
        delay_rate = self.create_rate(1/counter_delay_value)

        # publish info to the console for the user
        self.get_logger().info('%s action server is counting up to  %i with %fs delay between each count' % (self.get_name(), goal_handle.num_counts, counter_delay_value))

        feedback_msg = CounterWithDelay.Feedback()

        # Start executing the action
        for i in range(1, goal_handle.request.order):
            # Check that preempt has not been requested by the client
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled')
                return CounterWithDelay.Result()
            if self._as.is_preempt_requested():
                rospy.loginfo('%s: Preempted' % self._action_name)
                self._as.set_preempted()
                success = False
                break
            # Publish the feedback
            feedback_msg.counts_elapsed = i
            goal_handle.publish_feedback(feedback_msg)
            # Wait for counter_delay seconds before incrementing the counter.
            # If the rate is 5Hz, this will sleep for 1/5=0.2 seconds.
            delay_rate.sleep()

        goal_handle.succeed()

        # Populate result message
        result = CounterWithDelay.Result()
        #reslut.result_message = feedback_msg.result_message
        reslut.result_message = "Successfully completed counting."
        self.get_logger().info('%s: Succeeded' % self.get_name())
        #self.get_logger().info('Returning result: {0}'.format(result.result_message))

        return result


def main(args=None):
    rclpy.init(args=args)

    # Create an instance of the action server here.
    server = CounterWithDelayActionServer()

    # Use a MultiThreadedExecutor to enable processing goals concurrently
    executor = MultiThreadedExecutor()

    rclpy.spin(server, executor=executor)

    server.destroy()
    rclpy.shutdown()


if __name__ == '__main__':
    main()