#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import Twist

def square_movement():
    rospy.init_node('turtlebot_squaremover', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10) # set up publisher to send velocity cmd
    rate = rospy.Rate(10) #freq of 10hz

    move_cmd = Twist()

    for _ in range(4):
        # Move forward
        move_cmd.linear.x = 0.4 #in m/s
        move_cmd.angular.z = 0.0
        for _ in range(50):  #5 seconds for 2m
            pub.publish(move_cmd)
            rate.sleep()

        # Stop
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 0.0
        for _ in range(10):  # 1 seconds stop
            pub.publish(move_cmd)
            rate.sleep()

        # Turn
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 0.83 #edit to acheive 90 degs
        for _ in range(21):  # 2 seconds at 0.8 rad/s
            pub.publish(move_cmd)
            rate.sleep()

        # Stop
	move_cmd.linear.x = 0.0
        move_cmd.angular.z = 0.0
        for _ in range(10):
            pub.publish(move_cmd)
            rate.sleep()

if __name__ == '__main__': 
    try:
        square_movement()
    except rospy.ROSInterruptException:
        pass

