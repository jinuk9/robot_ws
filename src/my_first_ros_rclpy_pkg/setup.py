from setuptools import find_packages, setup

package_name = 'my_first_ros_rclpy_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='ubuntu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'helloworld_publisher = my_first_ros_rclpy_pkg.helloworld_publisher:main',
            'helloworld_subscriber = my_first_ros_rclpy_pkg.helloworld_subscriber:main',
            'turtlesim_node = my_first_ros_rclpy.turtlesim_node:main',
        ],
    },
)


'entry_points는 콘솔 커맨드 이름 = 모듈경로:콜러블(함수 또는 클래스)'
'''
my_first_ros_rclpy_pkg/
├── package.xml
├── setup.py
└── my_first_ros_rclpy_pkg/
    ├── __init__.py
    ├── helloworld_publisher.py  ← 이 파일엔 main() 함수가 있어야 함
    └── helloworld_subscriber.py ← 이 파일에도 main() 함수가 있어야 함
'''
