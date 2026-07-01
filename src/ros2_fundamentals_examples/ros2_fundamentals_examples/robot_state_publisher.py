#! /usr/bin/env python3

"""
Description:
    This node publishes "robot status" and "battery level" messages.

------------
Publishing Topics:
    The channel containing "Robot status" messages /robot_status.
    The channel containing "Battery status" messages /battery_level

------------
Subscription Topics
    None

------------
Anshpreet Singh
2nd July 2026
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String,Int32

class RobotStatePublisher(Node):
    def __init__(self):
        super().__init__('Robot_Status_Publisher')

        self.publisher_1 = self.create_publisher(String,'/robot_status',10)
        self.publisher_2 = self.create_publisher(Int32,'/battery_level',10)

        self.timer1 = self.create_timer(2,self.robot_status_callback)
        self.timer2 = self.create_timer(5,self.battery_status_callback)

        self.batterylevel = 100

    def robot_status_callback(self):
        status = String()
        status.data = 'Robot is operational'
        self.publisher_1.publish(status)
        self.get_logger().info(f'Robot-Status :"{status.data}"')

    def battery_status_callback(self):
        msg = Int32()
        msg.data = self.batterylevel
        self.publisher_2.publish(msg)
        self.get_logger().info(f'Battery-Level :"{msg.data}"')
        self.batterylevel -= 1

def main(args=None):
    rclpy.init(args=args)
    robot_state = RobotStatePublisher()
    rclpy.spin(robot_state)
    robot_state.destroy_node()
    rclpy.shutdown()
if __name__=="__main__":
    main()
