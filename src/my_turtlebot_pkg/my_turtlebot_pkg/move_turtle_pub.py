
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile
import time

class MoveTurtle(Node):
    def __init__(self):
        super().__init__('move_turtle')
        qos = QoSProfile(depth=10)
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', qos)
        # 0.1초 주기로 콜백
        self.timer = self.create_timer(0.1, self.turtle_move)
        # 시작 시간 기록
        self.start_time = time.time()

    def turtle_move(self):
        elapsed = time.time() - self.start_time
        msg = Twist()

        if elapsed < 10.0:
            # 10초간 전진s
            msg.linear.x = 0.2
            msg.angular.z = 0.0
        elif elapsed < 12.0:
            # 그 다음 2초간 제자리 회전
            msg.linear.x = 0.0
            msg.angular.z = 0.5
        else:
            # 이후 정지 후 타이머 취소
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.cmd_vel_pub.publish(msg)
            self.timer.cancel()
            self.get_logger().info('Done: stopped')
            return

        self.cmd_vel_pub.publish(msg)
        self.get_logger().info(f'[{elapsed:.1f}s] lin: {msg.linear.x:.2f}, ang: {msg.angular.z:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = MoveTurtle()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
