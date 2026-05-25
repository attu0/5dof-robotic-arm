from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

import xacro
import os

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    share_dir = get_package_share_directory('robotic_arm')

    # Xacro file
    xacro_file = os.path.join(
        share_dir,
        'description',
        'robot.urdf.xacro'
    )

    # Process xacro
    robot_description_config = xacro.process_file(xacro_file)

    robot_urdf = robot_description_config.toxml()

    # Robot State Publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[
            {'robot_description': robot_urdf}
        ]
    )

    # Joint State Publisher GUI
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    # Gazebo Harmonic
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            )
        ),
        launch_arguments={
            'gz_args': '-r empty.sdf'
        }.items()
    )

    # Spawn robot into Gazebo
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-topic', 'robot_description',
            '-name', 'robotic_arm'
        ],
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        gazebo,
        spawn_robot
    ])