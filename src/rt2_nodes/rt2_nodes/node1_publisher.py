import threading

import rclpy
from rclpy.node import Node
from rt2_msgs.msg import RT2String


class StringPublisher(Node):
    def __init__(self):
        super().__init__('rt2_node1_publisher')
        self.pub = self.create_publisher(RT2String, '/rt2_input', 10)
        self.current = None  # the string being published

        # publish the current string once every second
        self.timer = self.create_timer(1.0, self.publish_current)

        # read the user's typing in the background
        self.reader = threading.Thread(target=self.read_input, daemon=True)
        self.reader.start()

    def read_input(self):
        while rclpy.ok():
            try:
                text = input('Enter a string: ').strip()
            except EOFError:
                break
            if text:
                self.current = text
                self.get_logger().info(f'Now publishing: {text}')

    def publish_current(self):
        if self.current is None:
            return
        msg = RT2String()
        msg.data = self.current
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    if rclpy.ok():
        rclpy.shutdown()


if __name__ == '__main__':
    main()
