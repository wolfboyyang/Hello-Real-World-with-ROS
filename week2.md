# Week2 - Practical Assignment

Note: new dependency: ros-humble-ur-description, ros-humble-joint-state-publisher, ros-humble-joint-state-publisher-gui

could also get from https://github.com/UniversalRobots/Universal_Robots_ROS2_Description


## Practical Assignment 1

**Add a new model to the factory.**
In this assignment you are going to add a new model to the factory: one of the bins that we already used and saw in the first few videos (Changing Worlds).

The second bin should be placed on the opposite side of the conveyor, right in front of Robot 1.

The only file that needs to be changed is hrwros_assignment1.xacro in hrwros_week2_assignment/urdf.

To verify your solution, you can use the visualize_hrwros_assignment1.launch file in the hrwros_week2_assignment package to start RViz while you're editing the XACRO file.

Correct implementations will show:

1. An extra bin in the factory
2. The bin must be on the floor, not in the floor or slightly above it
3. Located opposite Robot 1 (i.e.: on the other side of the conveyor,as indicated by the red arrows in the two illustrations above)
4. Not touching anything other than the floor (this also means not touching the yellow lines on the floor)

## Practical Assignment 2

**Add a new object to the factory**

In this assignment you are going to add a new object to the factory: a green sphere.

The sphere should be placed on the opposite side of the conveyor, underneath the stairs at the far end of the factory.

The only file that needs to be changed is hrwros_assignment2.xacro in hrwros_week2_assignment/urdf.

As explained before, you don't need to upload anything at this point. You will be asked to upload the entire hrwros_week2_assignment package folder, after completing all 3 assignments of this week.

To verify your solution, you can use the visualize_hrwros_assignment2.launch file in the hrwros_week2_assignment package to start RViz while you're editing the XACRO file.

Correct implementations will show:

1. A new, green sphere in the factory
2. Radius: 40 centimeters
3. The sphere must be on the floor, not in the floor or slightly above it
4. Located under the stairs, behind the yellow line (as indicated by the red arrows in the two illustrations above)
5. Not touching anything other than the floor

## Practical Assignment 3

**Replace a model in the factory**

In this assignment you will need to replace Robot 2 (the UR5) with a different robot from another ROS package.

The package is provided to you in the Week 2 assignment materials that you've downloaded earlier.  The hrwros_week2_assignment package which provides support for a single new robot model: the Fanuc LR Mate 200iC.

You will have to update the hrwros_assignment3.xacro file to use this new model and place it on the pedestal behind the pallet with the boxes, which now supports Robot 2 (i.e.: the UR5).

The hrwros_week2_assignment package provides the required files and the xacro macro for the robot, which is located in the urdf subdirectory.

The name of the xacro macro of the new robot is fanuc_lrmate200ic. Be sure to import the correct file with the macro definition inside it.

The hrwros_week2_assignment package also provides a launch file you can use to view the new robot in RViz, it's called view_week2_replacement_robot.launch.

Be sure to check the relevant videos (2.4 and others). You can also run check_urdf to make sure your  implementation is correct.

**Solution requirements:**

The only file that needs to be changed is hrwros_assignment3.xacro in hrwros_week2_assignment/urdf.

To verify your solution, you can use the visualize_hrwros_assignment3.launch file in the hrwros_week2_assignment package to start RViz while you're editing the XACRO file.

Correct implementations will show:

1. The new robot model properly mounted on the pedestal where Robot 2 is now
2. The new robot with an identical orientation (i.e.: rotation) as Robot 2: in its startup pose, the replacement robot should point in the same direction as the UR5. The replacement robot does not need to completely mimic the position of all joints and links of the UR5.
3. The robot must be on the pedestal, not in the pedestal or slightly above it
4. The robot should not be touching anything other than the pedestal