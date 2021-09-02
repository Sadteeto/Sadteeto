import rclpy
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

cap = cv2.VideoCapture(0) # cv2 captures video from your default video input
bridge = CvBridge() 

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Image, 'topic', 10)
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        
    

    def timer_callback(self): # this function loops the code inside
        ret,frame = cap.read() # cv2 captures the current image frame
        if ret: # if there is image coming out from default cam
            cap2 = bridge.cv2_to_imgmsg(frame, 'passthrough') # converts cv2 image to ros message
            self.publisher_.publish(cap2) # publishes the image that just got converted
        
        else: # if there is NO image coming out from default cam
            print("No camera device connected")
            return




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