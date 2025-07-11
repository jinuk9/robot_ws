from setuptools import find_packages, setup
import os
import glob
package_name = 'move_turtle_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob.glob(os.path.join('launch', '*.launch.py'))),
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
            'turtle_cmd_and_pose = move_turtle_pkg.turtle_cmd_and_pose:main',
            'turtlesim_node = move_turtle_pkg.turtlesim_node:main',
            'move_turtle_pub = move_turtle_pkg.move_turtle_pub:main',
            'my_service_server = move_turtle_pkg.my_service_server:main',
            'dist_turtle_action_server = move_turtle_pkg.dist_turtle_action_server:main',
            'my_subscriber = move_turtle_pkg.my_subscriber:main',
            'my_multi_thread = move_turtle_pkg.my_multi_thread:main',
        ],
    },
)
