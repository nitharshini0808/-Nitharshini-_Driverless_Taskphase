import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from rt2_msgs.msg import RT2String


class PalindromeChecker(Node):
    def __init__(self):
        super().__init__('rt2_node2_checker')
        self.last = ''  # the last string we checked

        # to Node 3: 1 (palindrome) or 0 (not)
        self.pub = self.create_publisher(Int32, '/rt2_check', 10)

        # from Node 1: the string
        self.sub_in = self.create_subscription(
            RT2String, '/rt2_input', self.on_string, 10)

        # from Node 3: the Yes / No answer
        self.sub_ans = self.create_subscription(
            RT2String, '/rt2_answer', self.on_answer, 10)

    def on_string(self, msg):
        s = msg.data
        self.last = s
        out = Int32()
        out.data = 1 if s == s[::-1] else 0
        self.pub.publish(out)

    def on_answer(self, msg):
        self.get_logger().info(
            f"String '{self.last}' -> Node 3 says: {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    if rclpy.ok():
        rclpy.shutdown()


if __name__ == '__main__':
    main()
