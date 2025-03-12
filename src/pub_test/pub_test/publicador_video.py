import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class PublicadorVideo(Node):

    def __init__(self):
        super().__init__('publicador_video')
        self.publisher_ = self.create_publisher(Image, 'video_topic', 10)
        self.bridge = CvBridge()

        # Caminho para o vídeo
        self.video_path = '/home/evangelista/videos/meu_jogo.mp4'  
        self.cap = cv2.VideoCapture(self.video_path)

        if not self.cap.isOpened():
            self.get_logger().error(f"Não foi possível abrir o vídeo: {self.video_path}")
            raise RuntimeError("Erro ao abrir o vídeo")

       
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        if self.fps <= 0:
            self.get_logger().warn("Não foi possível obter o FPS do vídeo. Usando 30 FPS como padrão.")
            self.fps = 30 

     
        self.timer = self.create_timer(1.0 / self.fps, self.timer_callback)
        self.get_logger().info(f"Publicando vídeo a {self.fps} FPS")

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
        
            msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            self.publisher_.publish(msg)
            self.get_logger().info('Publicando frame do vídeo')
        else:
            self.get_logger().info('Fim do vídeo')
            self.cap.release()

    def destroy_node(self):
        self.cap.release()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    publicador_video = PublicadorVideo()
    rclpy.spin(publicador_video)
    publicador_video.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
