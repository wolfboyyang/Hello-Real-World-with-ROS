from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hrwros_week1',
            executable='template_publisher_script',
            name='simple_publisher',
        ),
        Node(
            package='hrwros_week1',
            executable='template_subscriber_script',
            name='simple_subscriber',
        ),
    ])