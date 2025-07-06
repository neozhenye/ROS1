#!/usr/bin/env python2
import rospy
from turtlesim.srv import TeleportAbsolute

def abs_teleport_tutlesim(x, y, theta):
    try:
        set_teleport = rospy.ServiceProxy("/turtle1/teleport_absolute", TeleportAbsolute)
        response = set_teleport(x, y, theta)
    except rospy.ServiceException as e:
        rospy.logwarn(e)
    
if __name__ == '__main__':
    rospy.init_node("Teleport_node")
    rospy.wait_for_service("/turtle1/teleport_absolute")
    rospy.loginfo("Node has started")
    abs_teleport_tutlesim(5.0, 5.0, 0.0)

    rospy.spin