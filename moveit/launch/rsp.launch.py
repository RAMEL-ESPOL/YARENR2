from launch import LaunchDescription
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("yaren_description", package_name="moveit").to_moveit_configs()

    # Asignar valores de tipo cadena (str) a los parámetros
    robot_description = ParameterValue(moveit_config.robot_description, value_type=str)
    robot_description_semantic = ParameterValue(moveit_config.robot_description_semantic, value_type=str)

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}],
        ),
        Node(
            package='moveit_ros_move_group',
            executable='move_group',
            output='screen',
            parameters=[
                {'robot_description': robot_description},
                {'robot_description_semantic': robot_description_semantic},
                {'robot_description_planning': moveit_config.robot_description_planning}
            ],
        ),
    ])
