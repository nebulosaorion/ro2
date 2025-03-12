import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublicadorTexto(Node):

    def __init__(self):
        super().__init__('publicador_texto')
        self.publisher_ = self.create_publisher(String, 'texto_topic', 10)
        timer_period = 1.0  # Publica a cada 1 segundo
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hey joão!'
        self.publisher_.publish(msg)
        self.get_logger().info('Publicando: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    publicador_texto = PublicadorTexto()
    rclpy.spin(publicador_texto)
    publicador_texto.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()