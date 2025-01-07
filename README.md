# RT_Assignment2 (part 2)

# **ROS Package Documentation**

## **Description**

This ROS package consists of two nodes implemented in python. The purpose of the project is to control a robot in a simulation environment, provided by the assignment. The first node is called `move_robot` and it is a publisher that allows the user to set the desired velocity of the robot (in terms of linear and angular components); the robot will start moving accoding to the given input. It will move for 5 seconds: then, the robot stops and the user can insert new values. The second node is called `position`: it subcribes to the topic /odom to get information about robot position (x and y coordinates) and simply print them on the terminal.


## **How to Run the Package**

IMPORTANT: in order to be correctly executed, the implemented launch file requires the presence of the package "robot_urdf", provided by the assignment.

To run the simulation first run $ros2 launch robot_urdf gazebo.launch.py
This will open the simulation environment, with the robot spawned in position (2;2)
Open a new terminal and run $ros2 run assignment2_rt_ros2 move_robot
Open a new terminal and run $ros2 run assignment2_rt_ros2 position

---

