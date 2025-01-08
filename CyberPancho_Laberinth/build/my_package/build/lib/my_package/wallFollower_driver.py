import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
from example_interfaces.msg import String

MAX_RANGE = 0.06657209992408752
TIME_SPEN = 64

class WallFollower(Node):
    def __init__(self):
        super().__init__('wallFollower_driver')

        self.__publisher = self.create_publisher(Twist, 'cmd_vel', 1)

        self.create_subscription(Range, 'left_sensor', self.__left_sensor_callback, 1)
        self.create_subscription(Range, 'front_sensor', self.__front_sensor_callback, 1)
    
    def __left_sensor_callback(self, message):
        self.__left_sensor_value = message.range

    def __front_sensor_callback(self, message):
        self.__front_sensor_value = message.range

        command_message = Twist()

        command_message.linear.x = 0.1

        #Turn right if the front_sensor detects a wall
        if self.__front_sensor_value <  0.9 * MAX_RANGE:
            command_message.angular.z = -1.5
        else:
            #Follow the wall if the left_sensor detects a wall
            if self.__left_sensor_value <  0.9 * MAX_RANGE:
                command_message.angular.z = 0.0
            #Turn left if the front_sensor and left_sensor doesn't detect the wall
            else:
                command_message.angular.z = 1.5

        self.__publisher.publish(command_message)

def main(args = None):
    rclpy.init(args = args)
    follower = WallFollower()
    rclpy.spin(follower)
    follower.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

