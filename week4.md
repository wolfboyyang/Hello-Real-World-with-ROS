# Week4 - Practical Assignment

## Practical Assignment 1

**Modifying an existing MoveIt configuration package**

In Module 4.3, the MoveIt Setup Assistant was introduced as a tool to setup everything we need to be able to use with MoveIt. We hope you succeeded in generating a MoveIt configuration package and experimented with it.

For this assignment, we want to have a common starting point for all learners, therefore we have created an assignment-specific MoveIt configuration package, it's called week4_moveit_config.

You can find this configuration package as part of your week 4 assignment packages, please download it from the weekly downloads page, if you haven't done so.

The goal of this assignment, is to learn how to use and modify an existing MoveIt configuration package.

### Week 4 - Assignment 1

The goal for this assignment is to add four new Robot Poses to the MoveIt configuration.

You can reach this goal by following the steps below.

**Step 1**: Launch the week4_moveit_config setup assistant:

```sh
roslaunch week4_moveit_config setup_assistant.launch
```
Make sure that: "Edit Existing MoveIt Configuration Package" is selected and that the Configuration Package reads "week4_moveit_config".

**Step 2**: Click on the "Load Files" button in the setup assistant GUI.

You should be able to see the factory on the right pane, and the elements on Self-Collisions and Planning Groups should be ready.

**Step 3**: Click on the "Robot Poses" entity on the left navigation pane. You should be able to see 4 Robot Poses there (R1Up, R2Up, R1Home, R2Home).

**Step 4**: Add four new poses (two for each robot) with the following names and joint values:

robot1 group:

R1PreGrasp:
```xml
        <joint name="robot1_elbow_joint" value="1.57" />
        <joint name="robot1_shoulder_lift_joint" value="-1.57" />
        <joint name="robot1_shoulder_pan_joint" value="0.4143" />
        <joint name="robot1_wrist_1_joint" value="-1.57" />
        <joint name="robot1_wrist_2_joint" value="-1.57" />
        <joint name="robot1_wrist_3_joint" value="0" />
```
R1Place:
```xml
        <joint name="robot1_elbow_joint" value="1.57" />
        <joint name="robot1_shoulder_lift_joint" value="-1.57" />
        <joint name="robot1_shoulder_pan_joint" value="2.87" />
        <joint name="robot1_wrist_1_joint" value="-1.57" />
        <joint name="robot1_wrist_2_joint" value="-1.57" />
        <joint name="robot1_wrist_3_joint" value="0" />
```
robot2 group:

R2PreGrasp:
```xml
        <joint name="robot2_elbow_joint" value="1.3809" />
        <joint name="robot2_shoulder_lift_joint" value="-0.8976" />
        <joint name="robot2_shoulder_pan_joint" value="0.7" />
        <joint name="robot2_wrist_1_joint" value="-2.0023" />
        <joint name="robot2_wrist_2_joint" value="-1.6225" />
        <joint name="robot2_wrist_3_joint" value="0" />
```
R2Place:
```xml
        <joint name="robot2_elbow_joint" value="1.3364" />
        <joint name="robot2_shoulder_lift_joint" value="-1.3017" />
        <joint name="robot2_shoulder_pan_joint" value="2.6902" />
        <joint name="robot2_wrist_1_joint" value="-1.6489" />
        <joint name="robot2_wrist_2_joint" value="-1.6225" />
        <joint name="robot2_wrist_3_joint" value="0" />
```
To test that the poses are correctly created, change the visualization on the right pane to show both robots and click on "MoveIt"

You should see the robot moving to all the poses in the list.

**Step 5**: Click on the "Author Information" entity and update it with your own information.

**Step 6**: Click on the "Configuration Files" entity, you will get a pop-up window warning message about some files being modified outside the Setup Assistant, Just click OK:

**Step 7**: Ensure that you have the correct items marked/unmarked on the "Files to be generated panel"

1. The config/hrwros.srdf file should have a "check" mark against it.

2. The launch/move_group.launch file should NOT have a check mark against it.

3. The launch/hrwros_moveit_controller_manager.launch.xml should NOT have a check mark against it.

4. The launch/trajectory_execution.launch.xml should NOT have a check mark against it.

**Step 8**: Click on "Generate Package", confirm that No end effectors have been added, and then confirm that you want to overwrite this existing package.

This completes the first assignment of this week, You can now exit the setup assistant!

Important Note:

**If you accidentally modify the package by using different settings for the check-marks (Step 7), you will get errors in the next assignments as some important files have been modified. In that case the best solution would be to remove the entire package, download / extract it again, and repeat all the steps.**

## Practical Assignment 2

**Use the MoveIt commander cmdline** 

In Module 4.4, we learned how to send commands and how to write a script for the MoveIt commander command line tool.

In this assignment, you will write a script, called week4_assignment2_script, to make robot2 execute a sequence using this tool.

You can find the empty file in the week4_assignment package, included in the download files of this week, and you should just complete it.

For this assignment to work, you need to have completed Assignment 1, where you defined the robot poses that are going to be used here.

### Week 4 - Assignment 2

To complete the assignment follow this steps:

**Step 1**: Start the factory simulation for week 4 with:
```sh
roslaunch hrwros_week4_assignment hrwros_week4_environment.launch
```
**Step 2**: In your favorite editor, edit the file week4_assignment2_script that you will find on the hrwros_week4_assignment/scripts folder.

**Step 3**: Using the instructions of Module 4.4, add a sequence of MoveIt Commander instructions such that the robot2 executes the following motions:

1. The robot2 goes to the R2Home configuration.

2. The robot2 goes to the R2PreGrasp configuration.

3. The end effector of robot2 moves linearly down by 0.1m.

4. The robot2 goes to the R2Place configuration.

5. The end effector of robot2 moves linearly down by 0.2m.

**Step 4**:  In a new CCS, Move to the same file path of the script.
```sh
roscd hrwros_week4_assignment/scripts
```
**Step 5**:  In that CCS, start the MoveIt commander with the following command:
```sh
rosrun hrwros_week4 hrwros_moveit_commander_cmdline
```
**Step 6**: Run the script you just created on the MoveIt! commander prompt that shows up.

> load week4_assignment2_script

This completes the second assignment of this week!

### Practical Assignment 3

**Use the MoveIt MoveGroup Interface**

The last assignment of this week requires you to implementing a simple pick and place pipeline for robot2.  Using the same process as we did for robot1 in the Module 4.5

To achieve this, we will use a python script called week4_assignment3.py that sends commands to the robot2 using the moveit_commander API studied during the week. You can find this script in the week4_assignment package, included in the download files of this week.

For this assignment to work, you need to have completed Assignment 1, where you defined the robot poses that are going to be used here.

### Week 4 - Assignment 3

To complete the last assignment of the week, you need to follow this steps.

**Step 1**: Complete the script week4_assignment3.py located on the scripts folder of the hrwros_week4_assignment package.

You only need to change wherever you are instructed with <write your code here>.

**Step 2**: After you have completed the script, start the factory simulation in a new CCS with:
```sh
roslaunch hrwros_week4_assignment hrwros_week4_environment.launch
```
**Step 3**: Make sure to adjust the perspective of the Gazebo Simulation to have a clear view of Robot2.

**Step 4**: In another CCS, first navigate to the hrwros_week4_assignment/scripts folder with roscd. Make sure the week4_assignment3.py script is executable.

**Step 4**: Finally, run the command:
```sh
roslaunch hrwros_week4_assignment week4_assignment3.launch.
```
You should see the robot2 execute simple pick and place motions, in both RViz and Gazebo!!

This completes all the assignments for week 4.