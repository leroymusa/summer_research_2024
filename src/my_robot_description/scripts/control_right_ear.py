# src/my_robot_description/scripts/control_right_ear.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class RightEarController(Node):
    def __init__(self):
        super().__init__('right_ear_controller')
        self.publisher_ = self.create_publisher(Float64, '/right_ear_joint/command', 10)
        self.timer = self.create_timer(0.5, self.publish_command)
        self.angle = 0.0
        self.increment = 0.1

    def publish_command(self):
        msg = Float64()
        msg.data = self.angle
        self.publisher_.publish(msg)
        self.angle += self.increment
        if self.angle > 1.57 or self.angle < -1.57:
            self.increment = -self.increment

def main(args=None):
    rclpy.init(args=args)
    node = RightEarController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
