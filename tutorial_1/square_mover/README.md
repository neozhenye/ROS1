# TurtleBot Square Movement

This ROS Python script makes a TurtleBot (or any robot that accepts velocity commands via `/cmd_vel`) move in a square trajectory.
It uses the `geometry_msgs/Twist` message type to control the robot's linear and angular velocities.

## 🧠 Overview

The robot:
1. Moves forward for 2 meters (5 seconds at 0.4 m/s),
2. Stops for 1 second,
3. Rotates approximately 90 degrees (2.1 seconds at ~0.83 rad/s),
4. Repeats the process 4 times to complete a square.

## 📁 Files

- `square_movement.py`: Main Python script written for ROS (Python 2).
- `README.md`: Documentation and usage instructions.

## Bash cmd

- source file
  ```bash
  source devel/setup.bash
  ```
- How to open file
  ```bash
  rosrun tutorial_1 square_mover
  
