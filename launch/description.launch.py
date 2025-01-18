from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare 

def generate_launch_description():
    xacro_file = PathJoinSubstitution([
        FindPackageShare("peacetolero_description"),
        "urdf",
        "peacetolero_alpha.config.xacro"
    ])

    return LaunchDescription([
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            parameters=[{
                "robot_description": Command(["xacro ", xacro_file])
            }]
        ),

        # Nodo joint_state_publisher_gui (si prefieres una interfaz gráfica)
        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
            name="joint_state_publisher_gui",
            parameters=[{"use_sim_time": False}],
            condition=None  # Ajusta si quieres habilitarlo opcionalmente
        )
    ])