# TurtleBot Wall Follower (ROS Python)

This is a simple **Wall Follower** script for a TurtleBot (or similar robot), written in **Python 2** and using **ROS 1**. It uses LIDAR data from the `/scan` topic to follow the right-hand wall and avoid frontal collisions.

## 🧠 Overview

The robot behaves according to the following rules:
- If there's a wall in front (closer than 0.5 meters), it turns left.
- If the right side is too far from the wall (> 0.5 meters), it steers right to get closer.
- If the right side is close enough, it continues forward.

## How to run file

1. Clone this repository into your ROS workspace:
   ```bash
   rosrun tutorial_1 wall_follower.py
