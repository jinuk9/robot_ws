import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan

class Move_turtle(Node):
  def __init__(self):
    super().__init__('move_turtle')
    self.qos_profile = QoSProfile(depth = 10)
    self.move_turtle = self.create_publisher(Twist, '/cmd_vel', self.qos_profile)

    self.scan_ranges = []
    self.scan_sub = self.create_subscription(
      LaserScan,
      'scan',
      self.scan_callback,
      qos_profile= qos_profile_sensor_data)

    self.timer = self.create_timer(1, self.turtle_move)
    self.velocity = 0.0
    self.rad = 0.0
    self.timer = self.create_timer(1, self.input_key)

  def input_key(self):
    try:
      key = input('key: w a s d 입력:')
      if key == 'w':
        self.velocity += 0.1
      elif key == 'a':
        self.rad += 0.1
      elif key == 'd':
        self.rad += -0.1
      elif key == 's':
        self.velocity += -0.1
      elif key == 'p':
        self.velocity = 0.0
        self.rad = 0.0
      else:
        self.get_logger().info('key - w a d s 만 입력 가능합니다.')
    except:
      self.get_logger().info('어딘가 문제 발생')

  def turtle_move(self):
    msg = Twist()
    msg.linear.x = self.velocity
    msg.linear.y = 0.0
    msg.linear.z = 0.0

    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = self.rad
    self.move_turtle.publish(msg)
    self.get_logger().info(f'Published mesage: {msg.linear}, {msg.angular}')
    # self.velocity += 0.08
    # if self.velocity > 2:
    #   self.velocity = 0.0

  def scan_callback(self, msg):
    self.scan_ranges = msg.ranges
    self.has_scan_received = True
    self.get_logger().info(f'scanData: {self.scan_ranges[0]}', throttle_duration_sec = 2)

def main(args=None):
  rclpy.init(args=args)
  node = Move_turtle()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    node.get_logger().info('Keyboard interrupt!!!!')
  finally:
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main':
  main()
