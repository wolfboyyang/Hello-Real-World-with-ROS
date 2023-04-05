from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node

def generate_launch_description():
    counter_delay_parameter = 2.0

    return LaunchDescription([
        DeclareLaunchArgument(
            'counter_delay_parameter', default_value='2.0',
            description='counter delay in seconds.'
        ),
        Node(
            package='hrwros_week1',
            executable='metres_to_feet_server',
            name='metres_to_feet',
        ),
        Node(
            package='hrwros_week1_assignment',
            executable='week1_assignment3',
            name='counter_with_delay',
            parameters=[
                {'counter_delay': LaunchConfiguration('counter_delay_parameter')}
            ]
        ),
    ])