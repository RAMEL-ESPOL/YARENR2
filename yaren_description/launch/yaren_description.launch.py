import os
from ament_index_python import get_package_share_directory
from launch.substitutions import LaunchConfiguration, Command
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.conditions import IfCondition
from launch import LaunchDescription

def generate_launch_description():
    # Arguments
    rviz = LaunchConfiguration('rviz', default='true')
    jsp = LaunchConfiguration('jsp', default='true')
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    namespace = LaunchConfiguration('namespace', default='')

    yaren_description_dir = get_package_share_directory('yaren_description')
    robot_path = os.path.join(yaren_description_dir, 'urdf', 'yaren_description.urdf.xacro')

    robot_desc = ParameterValue(Command(['xacro', ' ', robot_path]), value_type=str)

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': robot_desc,
            'use_sim_time': use_sim_time,
            'publish_frequency': 30.0
        }],
        namespace=namespace
    )

    # Joint state publisher gui
    jsp_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        namespace=namespace,
        name='joint_state_publisher_gui',
        condition=IfCondition(jsp)
    )

    # RViz
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(yaren_description_dir, 'rviz', 'yaren.rviz')],
        condition=IfCondition(rviz),
        namespace=namespace
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'
        ),
        DeclareLaunchArgument(
            'namespace',
            default_value='',
            description='Defines the namespace of the robot'
        ),
        DeclareLaunchArgument(
            'rviz',
            default_value='true',
            description='Open RViz.'
        ),
        DeclareLaunchArgument(
            'jsp',
            default_value='true',
            description='Run joint state publisher node.'
        ),
        jsp_gui,
        rviz_node,
        rsp
    ])


    
