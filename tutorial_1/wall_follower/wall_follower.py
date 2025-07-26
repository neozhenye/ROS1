#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class WallFollower: 
    def __init__(self):
        rospy.init_node('wall_follower', anonymous=True)
        self.cmd_pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        rospy.Subscriber('/scan', LaserScan,self.scan_callback)
        self.rate = rospy.Rate(10)
        self.cmd = Twist()

    def scan_callback(self,data):
        front = min(min(data.ranges[0:15]+data.ranges[-15:]),10)
        right = min(min(data.ranges[270-10:270+10]),10)

        #wall following logic
        if front < 0.5:
            self.cmd.linear.x=0.0
            self.cmd.angular.z=0.5
        elif right > 0.5:
            self.cmd.linear.x=0.1
            self.cmd.angular.z=-0.3
        else:
            self.cmd.linear.x=0.15
            self.cmd.angular.z=-0

        self.cmd_pub.publish(self.cmd)
    
    def run(self):
        while not rospy.is_shutdown():
            self.rate.sleep()

if __name__ == '__main__':
    try:
        node = WallFollower()
        node.run()
    except rospy.ROSInterruptException:
        pass
    
