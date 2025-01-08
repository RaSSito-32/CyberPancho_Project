import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range

TIME_STEP = 64
MAX_RANGE = 0.15

left_sensor = False
front_sensor = False

class WallFollower(Node):
    def init(self):
        super().__init__('wall_follower')

        self.__publisher = self.create_publiser(Twist, 'cmd_vel', 1)

        self.create_subscription(Range, 'left_sensor', self.__left_sensor_callback, 1)
        self.create_subscription(Range, 'front_sensor', self.__front_sensor_callback, 1)
    
    def __left_sensor_callback(self, message):
        self.__left_sensor_value = message.range

    def __front_sensor_callback(self, message):
        self.__front_sensor_value = message.range

        command_message = Twist()

        command_message.linear.x = 0.1

        #Turn right if a wall exist
        if self.__front_sensor_value < 0.9 * MAX_RANGE:
            command_message.angular.z = -2.0
        else:
            if self.__left_sensor_value < 0.9 * MAX_RANGE:
                command_message.angular.z = 2.0
            else:
                command_message.angular.z = 0.0
        self.__publisher.publish(command_message)

    def main(args = None):
        rclpy.init(args = args)
        follower = WallFollower()
        rclpy.spin(follower)
        follower.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()

