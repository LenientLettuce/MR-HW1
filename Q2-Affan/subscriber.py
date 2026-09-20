import rclpy 

from rclpy.node import Node 

from std_msgs.msg import Char

topic = 'char_topic'


class SubscriberNode(Node):

    def __init__(self):

        super().__init__('subscriber_node')

        self.sub_char = self.create_subscription(
            Char,
            topic,
            self.callback_fun,
            10
        ) 

        
        self.sub_char

    def callback_fun(self, msg):
        rec = chr(msg.data) # AI used for converting integer ascii msg to char using chr method
        self.get_logger().info('Char message received: "%s"' % rec)



def main(args=None):
    rclpy.init(args=args)

    subscriber_node = SubscriberNode()

    rclpy.spin(subscriber_node)

    subscriber_node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()