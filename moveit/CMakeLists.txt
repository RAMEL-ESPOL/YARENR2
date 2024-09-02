cmake_minimum_required(VERSION 3.22)
project(moveit)

# Encuentra los paquetes necesarios
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)

# Incluir directorios de encabezados (si es necesario)
include_directories(
  include
  ${rclcpp_INCLUDE_DIRS}
  ${moveit_ros_planning_interface_INCLUDE_DIRS}
  ${geometry_msgs_INCLUDE_DIRS}
  ${std_msgs_INCLUDE_DIRS}
)

# Crear un ejecutable a partir del archivo fuente
add_executable(move_yaren src/move_yaren.cpp)

# Establecer las dependencias del objetivo
ament_target_dependencies(move_yaren
  rclcpp
  moveit_ros_planning_interface
  geometry_msgs
  std_msgs
)

# Instalar el ejecutable en el directorio lib/${PROJECT_NAME}
install(TARGETS
  move_yaren
  DESTINATION lib/${PROJECT_NAME}
)

# Instalar archivos de configuración, lanzamiento, y otros relevantes
install(
  DIRECTORY config launch urdf
  DESTINATION share/${PROJECT_NAME}/
  FILES_MATCHING PATTERN "*.yaml" PATTERN "*.srdf" PATTERN "*.xacro" PATTERN "*.urdf"
)

# Declarar que este proyecto es un paquete de ament
ament_package()
