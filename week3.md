# Week3 - Practical Assignment

Note: new dependency:

[turtlebot_gazebo](https://github.com/turtlebot/turtlebot_simulator)
[turtlebot_description](https://github.com/turtlebot/turtlebot)
[kobuki_desktop](https://github.com/yujinrobot/kobuki_desktop)
[kobuki_description](https://github.com/yujinrobot/kobuki)
[kobuki_msgs](https://github.com/yujinrobot/kobuki_msgs)
[yocs_controllers](https://github.com/yujinrobot/yujin_ocs)
[ecl_core](https://github.com/stonier/ecl_core)
[ecl_tools](https://github.com/stonier/ecl_tools)
[yocs_msgs](https://github.com/yujinrobot/yocs_msgs)
[depthimage_to_laserscan](https://github.com/ros-perception/depthimage_to_laserscan)
ros-noetic-gazebo-ros-pkgs
ros-noetic-image-geometry
ros-noetic-joy
ros-noetic-gazebo-ros

## Practical Assignment 1

**Localization - Knowing where the robot is on a map**

In this first assignment, we will work on helping the robot to find it's own position on a map. So we will use the Adaptive Monte Carlo Localization (AMCL) to help localize the robot in our factory floor.

This first assignment is divided in three parts:

Visualize the robot in the factory floor map.
Provide a good estimation of the robot's initial position.
Improve the quality of the localization with the AMCL algorithm.

### Week 3 - Assignment 1 - part 1 (of 3)

In this first is very short,  you will prepare for navigation in our factory world by visualizing the robot on the factory floor.

To do this you need to modify the configuration of RVIZ to visualize the robot, You can do this with the following steps:

**Step 1**: Launch the hrwros factory simulation with:

```sh
roslaunch hrwros_week3 hrwros_turtlebot_navigation.launch
```

Note:  This might not succeed at the first attempt or it may take a while to start.

The factory environment has quite a lot of graphics to be rendered on Gazebo and depending on the processing power on your computer, it might take a few tries before you can see everything like it is shown in the picture of the previous unit. For example, you might see that the Turtlebot may not show up after multiple launch attempts. But, this is expected behavior. Normally, it should not require more than 5 re-starts.

**Step 2**: Launch AMCL with a map of the factory we created:

```sh
roslaunch hrwros_week3_assignment amcl_navigation.launch map_file:=$HOME/hrwros_ws/src/hrwros_week3/config/map_factory_v1.yaml
```

**Step 3**: Next, start the RViz navigation visualization:

```sh
roslaunch hrwros_week3_assignment view_navigation.launch
```

In RViz, you will see there are red mark in the RobotModel display tab to the left. Let's fix this!

It appeared in red because RViz is missing the Robot Description parameter. This was to be expected, because there are actually three robots present in the factory!

So let's tell RViz which one is the TurtleBot.

**Step 4**: Change the Robot Description field to turtlebot_description.

You should now see a green cloud of arrows where AMCL thinks the TurtleBot is.

This position estimation clearly is incorrect! However, we will solve that in Part 2 of this assignment.

Remember to save the RVIZ configuration with File -> Save config  or  Ctrl+S

### Week 3 - Assignment 1 - part 2 (of 3)

In this part, you will define the correct initial position of the robot in the map.

At the end of the first part, we noted that the pose of the TurtleBot in RViz is incorrect, it's further away  from the obstacles in Gazebo than in RViz (it looks like it is in front of the conveyor belt).

This is because when we launch AMCL, it assumes a default initial pose at the origin, but the TurtleBot is actually spawned in a different position in Gazebo and the localization can't correct the pose estimation from that initial pose.

We can fix this by giving AMCL a better estimation of the initial pose, which can be obtained from the TurtleBot's position on Gazebo.  The pose can be given, by passing two arguments to the amcl_navigation.launch:

* initial_pose_x
* initial_pose_y

The assignment is as follows:

**Step 1**:  Find the pose of the TurtleBot in Gazebo from the World tab.

In the Hands-on practice 1 of the Recap module of this Week, you learned how to do this.

**Step 2**: Use the relevant coordinates from that pose to tell AMCL where the initial pose is using the command below.

Make sure you need terminate the amcl_navigation.launch launched previously (if it was still running).

```sh
roslaunch hrwros_week3_assignment amcl_navigation.launch map_file:=$HOME/hrwros_ws/src/hrwros_week3/config/map_factory_v1.yaml initial_pose_x:=<XCOORD> initial_pose_y:=<YCOORD>
```
You should now see the 'green arrow cloud' and the TurtleBot shifted to the correct location.

**Step 3**: Now that you have found the correct initial position, you can set those changes on the amcl_navigation.launch file.

Edit the relevant parts of the amcl_navigation.launch to change the default arguments <arg>  tags.

Set the correct map and initial pose values.

**Step 4**: Relaunch the AMCL localization without the parameters to check that they have been set correctly.

```sh
roslaunch hrwros_week3_assignment amcl_navigation.launch
```

Keep both Gazebo and RViz simulations running as you move on to the next part.

### Week 3 - Assignment 1 - part 3 (of 3) 

Now that everything is fixed, that is, RViz knows the robot description, and AMCL also has a good estimation of the initial position of the TurtleBot, let's take it for a spin!

We will use the teleoperation for this, open another CCS and launch the teleoperation (as we did on the first part of this week).

```sh
roslaunch turtlebot_teleop keyboard_teleop.launch
```

Move the turtlebot around. You should see that, as the robot moves, the cloud of green arrows around it becomes less disperse and more dense centered in the robot. This means that the AMCL is improving the robot's estimation of its position.

This completes Assignment 1. Keep the Gazebo and RViz simulations, and the amcl launch running.

## Practical Assignment 2

Pathing - Knowing where your robot is going

In the previous assignment, we got to move the TurtleBot around the factory. If you got everything to work, this should have been fun to watch!

In this next assignment, we will start using the autonomous navigation stack and see the robot moving by itself and we will visualize the plans that the TurtleBot is using to navigate.

It is assumed here that Gazebo Simulations are still running, as the RViz and and the AMCL navigation. If you closed them, just relaunch them with the instructions of assignment 1.

### Week 3 - Assignment 2 - part 1 (of 2)

In this part you will visualize the Full Path planned by the Navigation stack in RViz by adding so-called path elements.

You can do that with the following steps:

**Step1**: At the bottom of the left panel in RViz, you can see a button marked 'Add'.

**Step2**: After clicking on the Add button, select the Path display type like in the screenshot below, and change the display name to _Full Path_.

**Step 3**: Point the Path display to the topic it will use to get the full path. Navigate to the topic field, and select /move_base/NavfnROS/plan.

This topic will visualize the overall global path planned by the navigation stack using Dijkstra's algorithm.

If you set a new navigation goal in RViz, a green line will appear, showing you the path the Turtlebot intends to take.

**Step 4**: To visualize this path, give the robot a goal with a long path, for example from near robot 1 to near robot 2, so it is clearly visible.

Remember to save the RVIZ configuration with File -> Save config  or  Ctrl+S

### Week 3 - Assignment 2 - part 2 (of 2)

We can now see the Full Path  planned by toward the goal. But ROS navigation stack also provides more than just the 'pre-planned' full path.

The ROS navigation stack also provides two more plans: the first one, called Global Plan, is an implementation of the DWA local planner for planning around unknown and dynamic obstacles! That is, the path can also be dynamically modified, when previously unknown obstacles appear. For example, there is a new crate blocking its path, it will attempt to drive around it. The second one is called Local Plan, and it's a very short plan that corresponds to the path that the TurtleBot will follow in the next couple of seconds, and is used to actually compute the motion control of the wheels in that short period.

In this part of the assignment, you will visualize also create new path displays for those two plans, just follow these steps.

**Step 1**: Add a new path display and subscribe it to /move_base/DWAPlannerROS/global_plan. Change the color from green to blue (0; 0; 255), and the name to Global Plan.

Notice how this Global Plan is different from the overall Full Path when the TurtleBot starts navigating.

**Step 2**:  Add another path display, in this case for the /move_base/DWAPlannerROS/local_plan,  Set its color to red (255; 0; 0) and name it Local Plan.

**Step 3**. Give the robot a new navigation goal and look at the displayed paths.

You should now be able to visualize all three paths, full, global and local.
You might need to zoom in a little to view the local plan, as it is very short.

Remember to save the RVIZ configuration with File -> Save config  or  Ctrl+S

This completes assignment 2. And only one last assignment to go!

## Practical Assignment 3

**Navigating using a ROS Node - Simple Action Client**

So far, we've had a lot of fun racing the TurtleBot around the factory, but when we think of (real world) ROS applications, having to use the RVIZ UI to set new navigation goals every time is not desirable.

In this assignment, we will learn how to command navigation goals to the TurtleBot using a ROS node that implements a simple action client interface that can send goals the move_base action server. In fact, the move_base action server that has so far been servicing all our navigation goals, only they were sent via RVIZ.

In the last part of this assignment, we will also work with a new challenge, when previously unknown obstacles start showing up along a path that has already been planned. Will the TurtleBot be able to avoid unknown obstacles as well? Jump in and start playing with the scripts! You will find out soon!!

### Week 3 - Assignment 3 - part 1 (of 2)

The goal of this part of the assignment is to update two files: week3_assignment3_part1.py and week3_assignment3_part1.launch.

The goal is to have the TurtleBot navigate to its first target location for the factory operation.

You will work towards this goal using the following steps:

Make sure you close all previous CCSs, if you have any open from previous assignments.

**Step 1**: Start the Factory simulation with:

```sh
roslaunch hrwros_week3 hrwros_turtlebot_navigation.launch
```

**Step 2**: Start the amcl_localization.launch file, it should now have the correct arguments for the map and the initial pose estimate of the TurtleBot.

```sh
roslaunch hrwros_week3_assignment amcl_navigation.launch
```

**Step 3**: Next, in another CCS, start the RViz visualization with:

```sh
roslaunch hrwros_week3_assignment view_navigation.launch
```

If you follow the steps from Assignment 1, you should visualize the TurtleBot in the green cloud of arrows indicating its potential initial position.

**Step 4**: In RViz, enable the TF display by clicking on the checkbox next to it.

**Step 5**:  If you expand the TF display by clicking on the black triangle to the left of the letters TF, you will see several elements with a check mark against them under the category Frames.

If you scroll down a bit, you will be able to see a frame called turtlebot_target1.

The tasks for completing this assignment are:

**Task 1**: Update the relevant information to complete the missing parts of the script and add the first goal in the week3_assignment3_part1.py. (Hint: you only have to change four lines of code in this file)

You can get the exact location from the turtlebot_target1 frame display by clicking on the small triangle to its left.

**Task 2**: Update week3_assignment3_part1.launch so that we can actually start the ROS node that will move the TurtleBot to the first target location as shown at the beginning of this assignment.

To check if everything is correct, just launch the file you just edited with:

```sh
roslaunch hrwros_week3_assignment week3_assignment3_part1.launch
```

If everything is good, when you launch this, the TurtleBot will autonomously navigate to the first target location, wait until the Turtlebot arrives to its goal. It may take some time, and the TurtleBot may struggle to reach it, if it fails, just re-launch it. Once the TurleBot has arrived at its goal, you should get the following messages: "Goal sent to move_base action server.",  "Goal position x: <>  y: <>",  "Hooray! Successfully reached the desired goal".

### Week 3 - Assignment 3 - part 2 (of 2)

In this part, the goal is to navigate the TurtleBot to its second target location, following similar steps as you followed in the first part, but with an added difficulty: To visualize and become aware of the "unknown obstacle avoidance" feature of the ROS autonomous navigation package which we have learned this week.

For this part, you will need to update two files: week3_assignment3_part2.py and week3_assignment3_part2.launch.

You will work towards this goal using the following steps:

**Step 1**: Following the same steps as in the Part 1, update the week3_assignment3_part2.py script.

Complete the missing parts of the script and add the second target location for the TurtleBot.

You will find the information under the turtlebot_target2 frame, also in the TF Display in RViz.

**Step 2**:  Update the week3_assignment3_part2.launch with the corresponding type of node, but don't launch it yet.

**Step 3**:  Make sure you have all the Three Path Displays enabled:

One for the overall global plan topic /move_base/NavfnROS/plan.
One for the global plan of the Dynamic Window Approach (DWA) planner which is used for obstacle avoidance (topic: /move_base/DWAPlannerROS/global_plan)
One for the local plan of the DWA planner (topic:  /move_base/DWAPlannerROS/local_plan).

**Step 4**:  To better visualize the obstacle avoidance (the modified global path around the obstacle), you need to retain the global path.

Change the "Buffer length" entry of the Full Path display to 20.

**Step 5**: Assuming you did not close or stop any ROS nodes from the previous part, you can start the week3_assignment3_part2.launch file in a new CCS with:

```sh
roslaunch hrwros_week3_assignment week3_assignment3_part2.launch.
```

If you did close or terminate the previous part, then make sure re-run the steps in Part 1, so the TurtleBot is at the first target location.

**Step 6**: A couple of seconds after the robot starts moving, you will notice that two new obstacles pop on Gazebo.

These obstacles were not known to the global planner at the time of planning.
So the initial path might actually collide with or go very close to the obstacles, however, as the TurtleBot approaches (one or both of) these obstacles, the global path gets modified.
You should see the changes on the Full Path as it avoids the obstacles, depending on which way the global planner plans the overall path.
Remember, the solution that the global planner finds can approach the target2 position either side of the obstacles, also the TurtleBot may have a hard time avoiding them, and take a few turns, but it's OK.

Remember to save the RVIZ configuration with File -> Save config  or  Ctrl+S

You have completed all the assignments of week 3!