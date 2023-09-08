"""
node to handle stopping robot when it experiences a bump
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from neato2_interfaces.msg import Bump
from geometry_msgs.msg import Twist


class EmergencyStopNode(Node):
    def __init__(self):
        super().__init__('emergency_stop_node')
        self.bumper_active = False
        self.create_timer(0.1, self.run_loop)               # call loop function every .1s
        # create subscriber to monitor bumps and publisher to send resultant vel
        self.sub = self.create_subscription(Bump, 'bump', self.process_bump, 10)
        self.vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
    def run_loop(self):
        """
        send velocity message based on bumper status
        """
        msg = Twist()
        if self.bumper_active:
            msg.linear.x = 0.0
        else:
            msg.linear.x = 0.1
        self.vel_publisher.publish(msg)
        
    def process_bump(self, msg:Bump):
        """
        process bump message and 
        """
        msg_content = [msg.left_front, msg.left_side, msg.right_front, msg.right_side]
        if 1 in msg_content:
            self.bumper_active = True
        else:
            self.bumper_active = False
        print(self.bumper_active)

def main(args=None):
    rclpy.init(args=args)
    node = EmergencyStopNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
