import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Obtener la ruta del paquete
    package_share_directory = get_package_share_directory('yaren_description')
    
    # Ruta a los archivos de configuración
    joint_names_config = os.path.join(package_share_directory, 'config', 'joint_names_yaren_description.yaml')
    controllers_config = os.path.join(package_share_directory, 'config', 'controllers.yaml')

    # Nodo para el estado del robot
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[joint_names_config]
    )

    # Nodo para el controlador del robot
    controller_manager_node = Node(
        package='controller_manager',
        executable='ros2_control_node',
        output='screen',
        parameters=[controllers_config]
    )

    # Nodo para cargar los controladores
    load_controllers = []
    controllers = ['robot_arm_controller', 'joint_state_controller']
    for controller in controllers:
        load_controllers.append(Node(
            package='controller_manager',
            executable='spawner',
            arguments=[controller],
            output='screen',
        ))

    return LaunchDescription([
        robot_state_publisher_node,
        controller_manager_node,
        *load_controllers
    ])
