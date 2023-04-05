from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hrwros_week1',
            executable='sensor_info_publisher',
            name='sensor_info_publisher',
        ),
        Node(
            package='hrwros_week1_assignment',
            executable='sensor_info_publisher',
            name='assignment1',
        ),
        Node(
            package='hrwros_week1',
            executable='metres_to_feet_server',
            name='metres_to_feet',
        ),
        Node(
            package='hrwros_week1_assignment',
            executable='week1_assignment2',
            name='assignment2',
        ),
    ])