import rclpy
from rclpy.node import Node
from geometry_msg.msg import Twist
import math
import time

topic1 = '/turtle1/cmd_vel'
frequency = 20

def main(args = None):
    rclpy.init(args = args)

    controlVel = Twist ()

    controlVel.linear.x = 2.0 
    controlVel.linear.y = 0.0
    controlVel.linear.z = 0.0

    controlVel.angular.x = 0.0
    controlVel.angular.y = 0.0
    controlVel.angular.z = 0.0

    TestNode = Node("test_node")
    publisher = TestNode.create_publisher(Twist , topic1, 1)

    rate = TestNode.create_rate(1/frequency)

    start_time = time.time()
    while rclpy.ok():
        t = time.time() - start_time
        controlVel.angular.z = math.cos(t)
        
        print("Sending Control Message")
        publisher.publish(controlVel)

        rclpy.spin_once(TestNode)
        rate.sleep()

    TestNode.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()