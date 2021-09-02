import rclpy
from rclpy.node import Node
import cv2
import numpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
cap = cv2.VideoCapture(0)
bridge = CvBridge()

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Image, 'topic', 10)
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        
    

    def timer_callback(self):
        ret,frame = cap.read()
        cap2 = bridge.cv2_to_imgmsg(frame, 'passthrough')
        # msg = cap2
        # msg.data = msg
        self.publisher_.publish(cap2)
        # self.get_logger().info('Publishing: "%s"' % msg)
        # self.i += 1


def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()