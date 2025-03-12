import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublicadorURDF(Node):
    def __init__(self):
        super().__init__('publicador_urdf')
        self.pub = self.create_publisher(String, '/robot_description', 10)
        self.timer = self.create_timer(1.0, self.publicar_urdf)

    def publicar_urdf(self):
        with open('/home/evangelista/ros2_ws/src/meu_robo/urdf/meu_robo.urdf', 'r') as f:
            urdf = f.read()
        msg = String()
        msg.data = urdf
        self.pub.publish(msg)
        self.get_logger().info('Publicando URDF do robô.')

def main(args=None):
    rclpy.init(args=args)
    nodo = PublicadorURDF()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

