cmake_minimum_required(VERSION 3.8)
project(yaren_description)

# Buscar paquetes necesarios de ROS 2
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(xacro REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Instalar directorios específicos
install(
  DIRECTORY
    config
    launch
    meshes
    urdf
    rviz
    world
  DESTINATION
    share/${PROJECT_NAME}/
)

# Instalar archivos URDF
install(
  DIRECTORY urdf/
  DESTINATION share/${PROJECT_NAME}/config
  FILES_MATCHING PATTERN "*.urdf"
)

# Instalar archivos SRDF desde la nueva ubicación
install(
  FILES
    ${CMAKE_CURRENT_SOURCE_DIR}/../moveit/config/yaren_description.srdf
  DESTINATION share/${PROJECT_NAME}/config
)

# Definir dependencias del paquete
ament_package()
