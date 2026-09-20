import rclpy
from rclpy.node import Node
from std_msgs.msg import Char

topic1 = 'char_topic'

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.sub_char = self.create_subscription(Char, topic1, self.listener_callback, 10)
        
    def listener_callback(self, msg):
        #used AI for the chr function
        char_received = chr(msg.data)
        
        self.get_logger().info(f"Received character: '{char_received}'")
        
def main(args=None):
    rclpy.init(args=args)
    subscriber_node = SubscriberNode()
    
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
