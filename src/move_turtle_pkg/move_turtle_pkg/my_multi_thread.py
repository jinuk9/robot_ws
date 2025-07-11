import rclpy as rp
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node

from move_turtle_pkg.move_turtle_pub import Move_turtle
from move_turtle_pkg.turtle_cmd_and_pose import CmdAndPose


def main(args=None):
    rp.init()

    sub = Move_turtle()
    pub = CmdAndPose()

    executor = MultiThreadedExecutor()

    executor.add_node(sub)
    executor.add_node(pub)
    # add_node로 멀티 쓰레드 작업할 노드 넣어줌
    #import 하고 add 하면 같이 실행됨
    try:
        executor.spin()

    finally:
        executor.shutdown()
        sub.destroy_node()
        pub.destroy_node()
        rp.shutdown()


if __name__ == '__main__':
    main()
