import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoveListener(Node):
    def __init__(self):
        super().__init__('move_listener')
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # Previne warning de variável não usada

    def listener_callback(self, msg):
        if msg.linear.x > 0.0:
            self.get_logger().info('Hey João, estou indo pra frente ok!')
        elif msg.linear.x < 0.0:
            self.get_logger().info('Hey João, estou indo para trás ok!')
        elif msg.angular.z != 0.0:
            self.get_logger().info('Hey João, estou girando!')
        else:
            self.get_logger().info('Parado!')

def main(args=None):
    rclpy.init(args=args)
    node = MoveListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
