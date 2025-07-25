#!/usr/bin/env python2
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen

previous_x = 0

def call_set_pen_service(r, g, b, width, off):
    try:
        set_pen = rospy.ServiceProxy("/turtle1/set_pen", SetPen)
        response = set_pen(r, g, b, width, off)
        # rospy.loginfo(response)
    except rospy.ServiceException as e:
        rospy.logwarn(e)

def pose_callback(msg):
    cmd = Twist()
    if msg.x > 9.0 or msg.x < 2 or msg.y > 9.0 or msg.y < 2.0:
        cmd.linear.x = 1.0
        cmd.angular.z =1.4
    else:
        cmd.linear.x = 5.0
        cmd.angular.z =0.0

    pub.publish(cmd)

    global previous_x
    if msg.x >= 5.5 and previous_x <5.5:
        previous_x = msg.x
        rospy.loginfo("Set color to red")
        call_set_pen_service(255, 0, 0, 3, 0)
    elif msg.x <5.5 and previous_x >= 5.5 : 
        previous_x = msg.x
        rospy.loginfo("set color to green")
        call_set_pen_service(0, 255, 0, 3, 0)

if __name__ == '__main__':
    rospy.init_node("turtle_controller")
    rospy.wait_for_service("/turtle1/set_pen")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback = pose_callback)
    rospy.loginfo("Node has been started")

    rospy.spin()