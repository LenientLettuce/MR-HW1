#Note Used AI for setting up VS codium with distrobox, as I use debian
#and had to install ROS2 through distrobox

#Also use AI to understand how to generate boilerplate files, ran this command:
#ros2 pkg create --build-type ament_python char_pkg --dependencies rclpy std_msgs
#(provided by AI)

import rclpy
from rclpy.node import Node
from std_msgs.msg import Char

topic1 = 'char_topic'

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.pub_char = self.create_publisher(Char, topic1, 10)

    def send_input(self, user_char):
        message1 = Char()
        
        #used AI to figure out ord function
        message1.data = ord(user_char)
        
        self.pub_char.publish(message1)
        self.get_logger().info(f"Published: '{user_char}'")

def main(args=None):
    rclpy.init(args=args)
    publisher_node = PublisherNode()
    
    publisher_node.get_logger().info('Type a character and press Enter.')
    
    #used AI to learn about rclpy.ok and rcl spin once, cos normal spin was not working
    while rclpy.ok():
        user_input = input("Enter a single character: ")
        char_to_send = user_input[0]
        publisher_node.send_input(char_to_send)
        
    rclpy.spin_once(publisher_node, timeout_sec=0.1)
    publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
