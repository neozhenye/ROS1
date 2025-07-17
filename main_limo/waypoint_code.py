#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# List of waypoints as (position, orientation) tuples
waypoints = [
    [(-0.27503, 0.69391, 0.0), (0.0, 0.0, -0.64, 0.76)],    # arena 5 enter/4 exit
    [(-0.16645, -0.00994, 0.0), (0.0, 0.0, -0.65, 0.75)],   # arena 5 center
    [(-0.87194, -0.05966, 0.0), (0.0, 0.0, -0.996, 0.088)]  # arena 5 exit/6 enter
]

def goal_pose(pose):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()

    # Set position
    goal.target_pose.pose.position.x = pose[0][0]
    goal.target_pose.pose.position.y = pose[0][1]
    goal.target_pose.pose.position.z = pose[0][2]

    # Set orientation (quaternion)
    goal.target_pose.pose.orientation.x = pose[1][0]
    goal.target_pose.pose.orientation.y = pose[1][1]
    goal.target_pose.pose.orientation.z = pose[1][2]
    goal.target_pose.pose.orientation.w = pose[1][3]

    return goal

if __name__ == '__main__':
    rospy.init_node('simple_waypoint_navigator')

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    rospy.loginfo("Waiting for move_base action server...")
    client.wait_for_server()
    rospy.loginfo("Connected to move_base!")

    # Go through each waypoint once
    for pose in waypoints:
        if rospy.is_shutdown():
            break
        goal = goal_pose(pose)
        client.send_goal(goal)
        client.wait_for_result()
        rospy.loginfo("Goal reached or failed. Moving to next...")

    rospy.loginfo("All waypoints processed.")
