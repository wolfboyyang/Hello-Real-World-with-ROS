#! /usr/bin/env python3

from action_msgs.msg import GoalStatus
from hrwros_msgs.action import CounterWithDelay

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

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

        num_counts = 10

        # Creates a goal to send to the action server.
        goal_msg = CounterWithDelay.Goal()
        goal_msg.num_counts = num_counts

        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

        self.get_logger().info("Goal has been sent to the action server.")


def main(args=None):
    # Initializes a rospy node so that the SimpleActionClient can
    # publish and subscribe over ROS.
    rclpy.init(args=args)

    action_client = CounterWithDelayActionClient()

    action_client.send_goal()

    rclpy.spin(action_client)

    
if __name__ == '__main__':
    main()