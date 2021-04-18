# Turtlebot3_Gripper
Turtlebot 3 with gripper.

### Configuration
`cd ~/catkin_ws/src`
`git clone https://github.com/TejasPhutane/Turtlebot3_Gripper.git`
`cd ..`
`catkin build`
`source ~/catkin_ws/devel/setup.bash`
`echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc`
`source ~/.bashrc`

### To spawn the robot in gazebo : 

`roslaunch turtlebot3_description display.launch`

### To control the robot using teleop : 

`roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`

