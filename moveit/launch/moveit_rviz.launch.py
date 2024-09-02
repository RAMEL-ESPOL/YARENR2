import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_moveit_rviz_launch

def generate_launch_description():
    # Definir robot_description utilizando Xacro
    robot_description = Command([
        'xacro ', 
        os.path.join(
            get_package_share_directory('yaren_description'), 
            'urdf', 
            'yaren_description.urdf.xacro'
        )
    ])

    # Construir la configuración de MoveIt
    moveit_config = MoveItConfigsBuilder(
        "yaren_description", 
        package_name="moveit"
    ).to_moveit_configs()

    # Incorporar robot_description en la configuración de MoveIt
    moveit_config.robot_description = robot_description

    # Añadir el nodo de robot_state_publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description}],
    )

    # Devolver la descripción del lanzamiento con RViz configurado para MoveIt
    return LaunchDescription([
        robot_state_publisher_node,
        generate_moveit_rviz_launch(moveit_config)
    ])

