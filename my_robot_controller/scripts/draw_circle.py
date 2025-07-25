#!/usr/bin/env python2
import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node("draw_circle")
    rospy.loginfo("Node has started")

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        # pub cmd_vel
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        pub.publish(msg)
        rate.sleep()
