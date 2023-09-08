"""
Publishing ROS messages using python
"""
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Header
from geometry_msgs.msg import Point
6
class SendMessagesNode(Node):
    def __init__(self):
        super().__init__('send_message_node')
        # create 10hz timer
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.run_loop)
        # create publisher
        self.publisher = self.create_publisher(PointStamped, 'my_point', 10)

    def run_loop(self):
        my_header = Header(stamp=self.get_clock().now().to_msg(), frame_id='odom')
        my_point = Point(x=1.0, y=2.0, z=0.0)
        my_point_stamped = PointStamped(header=my_header, point=my_point)
        print(my_point_stamped)
        print('Hi from in_class_day02 Rajivs code')
        self.publisher.publish(my_point_stamped)

def main(args=None):
    rclpy.init(args = args)      # initialize communication with ROS
    node = SendMessagesNode()   # create our node
    rclpy.spin(node)            # run the Node: blocks until context shutdown 
    rclpy.shutdown()            # cleanup


if __name__ == '__main__':
    main()
