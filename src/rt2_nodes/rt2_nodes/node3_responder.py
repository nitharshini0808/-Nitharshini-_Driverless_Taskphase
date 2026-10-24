import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from rt2_msgs.msg import RT2String


class Responder(Node):
    def __init__(self):
        super().__init__('rt2_node3_responder')

        # to Node 2: "Yes" or "No"
        self.pub = self.create_publisher(RT2String, '/rt2_answer', 10)

        # from Node 2: 1 or 0
        self.sub = self.create_subscription(
            Int32, '/rt2_check', self.on_check, 10)

    def on_check(self, msg):
        reply = RT2String()
        reply.data = 'Yes' if msg.data == 1 else 'No'
        self.pub.publish(reply)
        self.get_logger().info(f'Received {msg.data}, replied: {reply.data}')


def main(args=None):
    rclpy.init(args=args)
    node = Responder()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    if rclpy.ok():
        rclpy.shutdown()


if __name__ == '__main__':
    main()
