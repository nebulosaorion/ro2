import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
        
        launch_ros.actions.Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': LaunchConfiguration('robot_description')}]
        ),
        
        
        launch_ros.actions.Node(
            package='controller_manager',
            executable='ros2_control_node',
            name='controller_manager',
            parameters=[{'config_file': LaunchConfiguration('config_file')}]
        ),

        
        launch_ros.actions.Node(
            package='controller_manager',
            executable='spawner.py',
            arguments=['diff_drive_controller'],
            output='screen'
        ),
    ])
