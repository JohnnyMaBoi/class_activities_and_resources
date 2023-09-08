"""
receiving a message using a callback function
"""
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped

class ReceiveMessageNode(Node):
    def __init__(self):
        super().__init__('receive_message_node')
        self.sub = self.create_subscription(PointStamped, 'my_point', self.process_point, 10)


def main(args=None):
    rclpy.init(args=args)           # initialize communication with ROS
    node = ReceiveMessageNode()     # Create our Node
    rclpy.spin(node)                # run the node and block until shutdown
    rclpy.shutdown()                # cleanup

def process_point(self, msg):
    print(msg.header)

if __name__ == 'main':
    main()