#! /usr/bin/env python3
"""
Description:
    This ros2 2 node periodicaly publish a temperature readingt to a topic
------------
Publishing Topics:
    The channel containg the "Temperature" reading /room_temperature_topics-std_msgs/Float64
Subsriction Topics:
    None
------------
Anshpreet Singh
1 July 2026
"""
import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import Float64

class FakeTempSensor(Node):
    """
        Creating a simple publishing Node
    """
    def __init__ (self):
        super().__init__('fake_temp_sensor')
        self.publisher_1=self.create_publisher(Float64,'/room_temperature',10)
        time_period = 0.5
        self.timer = self.create_timer(time_period,self.timer_callback)

    def timer_callback(self):
        """
        A callback function
        """
        msg = Float64()
        msg.data = random.uniform(20,30)
        self.publisher_1.publish(msg)
        self.get_logger().info('Publishing : "%f"' % msg.data)

def main(args=None):
    """
    Make function to start the ros2 node
    """
    rclpy.init(args=args)
    fake_temp_sensor = FakeTempSensor()
    rclpy.spin(fake_temp_sensor)
    fake_temp_sensor.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()