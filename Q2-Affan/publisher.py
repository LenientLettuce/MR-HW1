import rclpy 

from rclpy.node import Node 

from std_msgs.msg import Char 

topic = 'char_topic'

class PublisherNode(Node):
    def __init__(self):

        super().__init__('publisher_node')

        self.pub_char = self.create_publisher(Char, topic, 10)


    def publish_char(self, char):
        char_message = Char()
        char_message.data = ord(char) # AI used for understanding ord

        self.pub_char.publish(char_message)

        self.get_logger().info('publishing: %s' % char)

def main(args=None):
    rclpy.init(args=args)

    publisher_node = PublisherNode()

    while rclpy.ok(): # AI used for figuring out ok method
        text=input('Enter a character: ')
        publisher_node.publish_char(text[0])

    publisher_node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()