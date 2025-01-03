import rclpy
import time
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DesiredVelocity(Node):

    def __init__(self):
        super().__init__('desired_velocity')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)


    def velocity_publisher(self,x,z):
        input_velocity = Twist()
        input_velocity.linear.x = x
        input_velocity.linear.y = 0.0
        input_velocity.angular.z = z
        self.publisher_.publish(input_velocity)
        #self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    desired_velocity = DesiredVelocity()
    
    while rclpy.ok():
    	while True
    		try:
    			x = float(input("Insert the derired linear velocity: "))
    			break
    		except ValueError:
    			print("Wrong input. Please insert a valid number.")
    	while True
    		try:
    			z = float(input("Insert the derired angular velocity: "))
    			break
    		except ValueError:
    			print("Wrong input. Please insert a valid number.")
    	
    	desired_velocity.velocity_publisher(x,z)
    	time.sleep(5)
    	desired_velocity.velocity_publisher(0.0,0.0)

    #rclpy.spin(velocity_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    desired_velocity.destroy_node()
    #rclpy.shutdown()


if __name__ == '__main__':
    main()

