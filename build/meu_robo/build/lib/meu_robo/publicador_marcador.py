import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
from std_msgs.msg import ColorRGBA
import time

class PublicadorMarcador(Node):
    def __init__(self):
        super().__init__('publicador_marcador')
        self.pub = self.create_publisher(Marker, '/visualization_marker', 10)
        self.timer = self.create_timer(1.0, self.publicar_marcador)

    def publicar_marcador(self):
        marcador = Marker()
        marcador.header.frame_id = "map"
        marcador.header.stamp = self.get_clock().now().to_msg()
        marcador.ns = "meu_robo"
        marcador.id = 0
        marcador.type = Marker.CUBE
        marcador.action = Marker.ADD
        marcador.pose.position.x = 0.0
        marcador.pose.position.y = 0.0
        marcador.pose.position.z = 0.25
        marcador.pose.orientation.w = 1.0
        marcador.scale.x = 0.5
        marcador.scale.y = 0.5
        marcador.scale.z = 0.5
        marcador.color = ColorRGBA(r=0.0, g=0.0, b=1.0, a=1.0)

        self.pub.publish(marcador)
        self.get_logger().info('Publicando marcador do robô.')

def main(args=None):
    rclpy.init(args=args)
    nodo = PublicadorMarcador()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
