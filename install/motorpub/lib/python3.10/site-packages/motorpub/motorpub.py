import rclpy
from rclpy.node import Node

class MotorPub(Node):
	def __init__(self):
		super().__init__('motor publisher')
		self.publisher_ = self.create_publisher(int,'motorSND',10)
		timer_period = 0.5
		self.timer = self.create_timer(timer_period, self.timer_callback)
		
	def timer_callback(self):
		msg = int(20)
		self.publisher_.publish(msg)
		
def main(args=None):
	rclpy.init(args = args)
	motorpub = MotorPub()
	
	rclpy.spin(motorpub)
	motorpub_publisher.destroy_node()
	rclpy.shutdown()
	
if __name__ == '__main__':
	main()
	
	
