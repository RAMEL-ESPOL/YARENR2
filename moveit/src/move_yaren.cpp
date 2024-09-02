#include <rclcpp/rclcpp.hpp>
#include <moveit/move_group_interface/move_group_interface.h>
#include <std_msgs/msg/string.hpp>

class MoveYaren : public rclcpp::Node
{
public:
    MoveYaren() : Node("move_yaren")
    {
        // Crear el grupo de movimiento aquí directamente
        move_group_ = std::make_shared<moveit::planning_interface::MoveGroupInterface>(std::shared_ptr<rclcpp::Node>(this, [](rclcpp::Node*){}), "DERECHO");

        // Suscriptor para comandos
        command_subscriber_ = this->create_subscription<std_msgs::msg::String>(
            "command_topic", 10, std::bind(&MoveYaren::commandCallback, this, std::placeholders::_1));
    }

private:
    void commandCallback(const std_msgs::msg::String::SharedPtr msg)
    {
        if (msg->data == "a")
        {
            moveToPoseA();
        }
    }

    void moveToPoseA()
    {
        std::vector<double> joint_group_positions = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0};
        move_group_->setJointValueTarget(joint_group_positions);

        moveit::planning_interface::MoveGroupInterface::Plan my_plan;
        bool success = (move_group_->plan(my_plan) == moveit::core::MoveItErrorCode::SUCCESS);

        if (success)
        {
            move_group_->move();
            RCLCPP_INFO(this->get_logger(), "Movimiento realizado con éxito.");
        }
        else
        {
            RCLCPP_ERROR(this->get_logger(), "Error en la planificación.");
        }
    }

    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr command_subscriber_;
    std::shared_ptr<moveit::planning_interface::MoveGroupInterface> move_group_;
};

int main(int argc, char** argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MoveYaren>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
