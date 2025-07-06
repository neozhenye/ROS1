#!/usr/bin/env python2
import rospy
from my_robot_controller.srv import AddTwoInt, AddTwoIntResponse

def handle_add_two_ints(req):
    rospy.loginfo("Adding %d + %d", req.a, req.b)
    return AddTwoIntResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    service = rospy.Service('add_two_ints', AddTwoInt, handle_add_two_ints)
    rospy.loginfo("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
