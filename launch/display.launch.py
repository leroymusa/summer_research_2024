import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import Command, LaunchConfiguration

def generate_launch_description():
    pkg_share = get_package_share_directory('my_robot_description')
    default_model_path = os.path.join(pkg_share, 'urdf/expressive_robot.urdf.xacro')
    default_rviz_config_path = os.path.join(pkg_share, 'launch/urdf_config.rviz')

    return LaunchDescription([
        DeclareLaunchArgument(
            name='model',
            default_value=default_model_path,
            description='Absolute path to robot urdf file'
        ),
        DeclareLaunchArgument(
            name='rvizconfig',
            default_value=default_rviz_config_path,
            description='Absolute path to rviz config file'
        ),
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': Command(['xacro ', LaunchConfiguration('model')])
            }]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', LaunchConfiguration('rvizconfig')]
        )
    ])