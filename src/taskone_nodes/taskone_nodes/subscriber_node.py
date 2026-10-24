import rclpy
from rclpy.node import Node
from taskone_msgs.msg import TaskOne


class TaskOneSubscriber(Node):
    def __init__(self):
        super().__init__('taskone_subscriber')
        self.sub = self.create_subscription(
            TaskOne, '/taskone', self.callback, 10)

    def callback(self, msg):
        speed = msg.ang_vel * msg.radius  # v = omega * r
        self.get_logger().info(
            f'ang_vel={msg.ang_vel:.3f} rad/s, radius={msg.radius:.3f} m '
            f'-> longitudinal speed = {speed:.3f} m/s')


def main(args=None):
    rclpy.init(args=args)
    node = TaskOneSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    if rclpy.ok():
        rclpy.shutdown()


if __name__ == '__main__':
    main()
