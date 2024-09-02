cmake_minimum_required(VERSION 3.5)
project(moveit)

# Encontrar las dependencias necesarias
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(moveit_common REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(std_msgs REQUIRED)

# Agregar el archivo .cpp
add_executable(move_yaren src/move_yaren.cpp)

# Especificar las dependencias para el ejecutable
ament_target_dependencies(move_yaren rclcpp moveit_ros_planning_interface std_msgs)

# Instalar el ejecutable
install(TARGETS move_yaren
  DESTINATION lib/${PROJECT_NAME})

ament_package()
