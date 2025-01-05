# RT_Assignment2 (part 2)

# **ROS Package Documentation**

## **Description**

This ROS package consists of one node implemented in python. The purpose of the project is to control a robot in a simulation environment, provided by the assignment. The node allows the user to set the desired velocity of the robot (in terms of linear and angular components); the robot will start moving accoding to the given input. It will move for 5 seconds: then, the robot stops and the user can insert new values. The behaviors is quite similar to the node implemented for the first assignment of the course; nevertheless, since there are no obstacles or buondaries, there is no check about robot position to prevent collisions. 


## **How to Run the Package**

IMPORTANT: in order to be correctly executed, the implemented launch file requires the presence of the package "robot_urdf", provided by the assignment.

To run the simulation first run $ros2 launch robot_urdf gazebo.launch.py
This will open the simulation environment, with the robot spawned in position (2;2)
Open a new terminal and run $ros2 run assignment2_rt_ros2 move_robot

---

