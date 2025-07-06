#!/usr/bin/env python2
import rospy
from my_robot_controller.srv import AddTwoInt

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInt)
        resp = add_two_ints(x, y)
        return resp.sum
    except rospy.ServiceException as e:
        rospy.logwarn("Service call failed: %s" % e)

if __name__ == "__main__":
    rospy.init_node("add_two_ints_client")
    result = add_two_ints_client(4, 5)
    rospy.loginfo("Sum is: %d", result)

