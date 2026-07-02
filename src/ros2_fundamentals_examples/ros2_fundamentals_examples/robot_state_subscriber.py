#! /usr/bin/env python3

"""
Description :
    This node subscribes to "Robot Status" and "Battery Level" messages.

------------
Publishing Topics :
    None

------------
Subscribing Topics :
    The channel containing "Robot status" messages /robot_status-std_msgs.String.
    The channel containing "Battery level" messages /battery_level-std_msgs.Int32.

------------
Anshpreet Singh
2nd July 2026
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String , Int32

class RobotStateSubscriber(Node):
    def __init__(self):
        super().__init__('robot_state_subscriber')
        self.subscriber_1 = self.create_subscription(String,'/robot_status',self.robotstatus_callback,10)
        self.subscriber_2 = self.create_subscription(Int32,'/battery_level',self.batterylevel_callback,10)

    def robotstatus_callback(self,msg):
        self.get_logger().info(f'I heared :"{msg.data}"')

    def batterylevel_callback(self,msg):
        self.get_logger().info(f'I heared :"{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    robot_state_subscriber = RobotStateSubscriber()
    rclpy.spin(robot_state_subscriber)
    robot_state_subscriber.destroy_node()
    rclpy.shutdown()
if __name__=="__main__":
    main()