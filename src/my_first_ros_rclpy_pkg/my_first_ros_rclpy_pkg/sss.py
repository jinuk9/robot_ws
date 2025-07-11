
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
from datetime import datetime

class HelloworldPublisher(Node):

    def __init__(self): # 생성자
        super().__init__('helloworld_publisher')
        # 1) QoS 프로필(depth=10) 생성
        qos_profile = QoSProfile(depth=10)
        # 2) String 타입의 퍼블리셔 생성 (토픽명 'hello')
        self.helloworld_publisher = self.create_publisher(
            String, 'hello', qos_profile
        )
        # 3) 1초 주기의 타이머 생성 → publish_helloworld_msg 콜백 호출
        self.timer = self.create_timer(1.0, self.publish_helloworld_msg)
        # 4) 마지막으로 메시지를 퍼블리시한 “분”을 저장할 변수
        self.last_published_minute = None

    def publish_helloworld_msg(self):
        """
        매초 호출된다.
        현재 시각의 초(second)가 0이고, 같은 “분”에 아직 보내지 않았다면
        메시지를 퍼블리시한다.
        """
        now = datetime.now()

        # (A) now.second == 0 → xx:xx:00 일 때만
        # (B) now.minute != self.last_published_minute →
        #     이 분에 한 번도 보내지 않았을 때만
        if now.second == 0 and now.minute != self.last_published_minute:
            # 5) 메시지 생성 및 데이터 설정
            msg = String()
            msg.data = now.strftime('[%Y년 %m월 %d일 %H시 %M분 %S초] 현재 시각 전송')

            # 6) 퍼블리시
            self.helloworld_publisher.publish(msg)
            # 7) 로그에 출력
            self.get_logger().info(f'보낼 메시지: {msg.data}')

            # 8) “마지막 퍼블리시 분” 업데이트
            self.last_published_minute = now.minute

def main(args=None):
    # 9) rclpy 초기화
    rclpy.init(args=args)
    # 10) 노드 인스턴스화
    node = HelloworldPublisher()
    try:
        # 11) 노드 스핀 → 콜백 반복 실행
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        # 12) 노드 정리 및 shutdown
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
