ROS 2- HUMBLE

Al iniciar el proyecto ejecutar los siguientes comandos en el workspace:

´´´bash
colcon build
´´´
source install/setup.bash 


VISUALIZACIÓN de YAREN en Gazebo: 

ros2 launch yaren_description yaren_gazebo.launch.py 

VISUALIZACIÓN de YAREN en RVIZ:

ros2 launch yaren_description yaren_description.launch.py


MOVIMIENTOS predefinidos YAREN en Rviz:

En una terminal ejecutar: ros2 launch moveit move_group.launch.py

En otra terminal: ros2 launch moveit moveit_rviz.launch.py

MOVIMIENTOS POR TECLADO:

En una terminal ejecutar: ros2 launch moveit rsp.launch.py

En otra terminal: ros2 run moveit move_yaren
