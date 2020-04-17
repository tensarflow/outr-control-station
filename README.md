# control-station

All implementations related to the control station of the OUTR.

TODO:
*  Send cmd_vel messages to robot
*  Find soloution for continous data stream (frequencies, periods, etc.)
*  Make gui
*  Implement control for lifting mechanism
*  Is python ideal for this?

## Purpose
The control station is a tool to manipulate the robot manually. It allows to debug control algorithms of the robot


## Dependencies
- rospy
- Temporarily opencv


## Install
1. Clone this repository to your `../catkin_ws/src` directory:
```
git clone https://gitlab.com/outr1/control-station.git
```

2. Build the package from `catkin_ws/`
```
cd ~/catkin_ws

catkin build

or

catkin_make

```

## Usage
Run in terminal:

```
roscore
```

Then run in seperate terminal:

```
rosrun control-station control.py
```

After that follow the instructions on the terminal.