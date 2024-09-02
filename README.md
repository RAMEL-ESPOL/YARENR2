## ROS 2- HUMBLE

## Al iniciar el proyecto ejecutar los siguientes comandos en su workspace:

```bash
colcon build
```
```bash
source install/setup.bash  
```

## VISUALIZACIÓN de YAREN en Gazebo: 
```bash
ros2 launch yaren_description yaren_gazebo.launch.py
 ```

## VISUALIZACIÓN de YAREN en RVIZ:
```bash
ros2 launch yaren_description yaren_description.launch.py
 ```

## MOVIMIENTOS predefinidos YAREN en Rviz:

En una terminal ejecutar: 

```bash
ros2 launch moveit move_group.launch.py
 ```

En otra terminal: 

```bash
ros2 launch moveit moveit_rviz.launch.py
 ```

## MOVIMIENTOS POR TECLADO:

En una terminal ejecutar: 

```bash
ros2 launch moveit rsp.launch.py
 ```

En otra terminal: 

```bash
ros2 run moveit move_yaren
 ```
