## ROS 2- HUMBLE

## Clonar el repositorio, rama master:
```bash
git clone -b master https://github.com/RAMEL-ESPOL/YARENR2.git
```
## PASOS PREVIOS (EN CASO DE ERROR):
```bash
sudo apt-get install ros-humble-gazebo-ros-pkgs
```
Revisar los permisos y dependencias:
```bash
sudo apt-get install libgazebo11-dev
```
Actualizar e instalar dependencias faltantes:
```bash
sudo apt-get update
```
```bash
sudo apt-get upgrade
```


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

Para solucionar warning- Poner en Fixed Frame: base_link

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
