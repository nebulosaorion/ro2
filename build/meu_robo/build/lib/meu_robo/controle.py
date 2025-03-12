import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class ControleRobo(Node):
    def __init__(self):
        super().__init__('controle_robo')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.mover)

    def mover(self):
        msg = Twist()
        msg.linear.x = 0.2  # Move para frente
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    nodo = ControleRobo()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
