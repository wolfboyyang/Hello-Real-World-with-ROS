# Week6 - Practical Assignment

## Practical Assignment 1: Modifying an existing behavior

**Modifying an existing behavior**

In Module 6.3, you learned how you can create your robot behavior using FlexBE. We hope you tried playing around with the behavior "Pick part from conveyor", included in the Week 6 downloads.

In this first assignment, you will modify the state machine of the behavior "Final Project" to perform a more sophisticated version of the pick part, it will start by feeding the box to the conveyor belt and finish with the box on the actuator of robot 1.

### Week 6 - Assignment 1

Most of the first part of the behavior is already implemented in the code provided.

The goal for this assignment is to add two new states, so you can use the conveyor belt to bring a part (the white box) to the area where the camera can detect it and where the Robot 1 can pick it up.

To do this you need to modify "Final Project" behavior. You can do this with the following steps:

**Step 1**: Open the flexbe app by using the following command.
```sh
rosrun flexbe_app run_app --offline
```
**Step 2**: Load the Open the "Final Project" behavior in the flexbe app.

Click on load behavior and select "Final Project"

**Note**:  If you don't see the "Final Project" on the behavior list, please make sure you have downloaded files of week 6 and followed the instructions there.

**Step 3**: Add your name to the author tag and set the correct date.

**Step 4**: Edit the state machine by adding and configuring two new states, so that:

* After "Move R1 Home", a new state starts the conveyor belt.
* After "Stop feeder" another new state stops the conveyor belt.

You may revisit videos 6.4.3 part 1 and 6.4.3 part 2 to see what state type to use, how to configure it and if any additional variables are needed.

**Step 5**: Reconnect the states in the state machine so that, if no state results in the "failed" outcome, the last active state is "Move R1 back Home" and, as a result of executing the behavior, robot1 holds the part.

**Step 6**: Save your changes in the behavior, check that no error messages appear, and close the FlexBE App.

**Test your behavior**

You can now test the behavior up to this part, to do so please follow these steps.

**Step 1**: Close the flexbe app and any other CCS  you may have running.

**Step 2**: Launch the final project environment simulation environment using:
```sh
roslaunch hrwros_week6 hrwros_final_project.launch
```
**Step 3**: On another CCS terminal, open the flexbe App for behavior execution using.
```sh
roslaunch flexbe_app flexbe_full.launch
```
**Step 4**: Click on load behavior and select "Final Project"

**Step 5**: Go to the "Runtime Control" Tab, and click on "Start Execution"

You can follow the execution in the flexbe app and see the robots moving in the gazebo simulator!

At this point the behavior should end with the Robot 1 holding the Box in its Home position.

This completes this assignment! You can continue with the next one, where you will include the mobile robot!!

## Practical Assignment 2: Command the Turtlebot

**Command the Turtlebot from your state machine**

In this assignment you will use the "MoveBaseState" implementation to make the Turtlebot navigate in the factory floor.

The assignment consist on two parts, on the first one the Turtlebot should receive the part from Robot 1 and in the second one it should deliver the bot to the Robot 2.

Important note:  You need to have completed the previous assignment to continue and test this one.

### Week 6 - Assignment 2 Part 1 

In this first part of the assignment, you will modify the "Final Project" behavior to control the Turtlebot so that, after robot1 picks the part, it delivers it to the Turtlebot.

To do this you need to open and modify the "Final Project" behavior, same as in the first assignment, and then follow the next steps.

**Step 1**: Add a state to of type "MoveBaseState"  to the state machine. You can name it Navigate to Robot 1.

This new state should become active after "Move R1 back Home" finishes with outcome "reached".

**Step 2**: Configure the input key "waypoint" of the newly added state so that the Turtlebot navigates to a location next to Robot 1.

Hint: check the constant variables in "Private configuration"

**Step 3**: Re-wire (change the transitions between states) to the state machine so that:

When the new state you added in Step 1 outputs "arrived", the states: "Locate Turtlebot", "Compute place Turtlebot", and "Move R1 to place" are executed in that order.

Hint: You need to remove their connection to the "finished" output, and set it to the correct state.

**Step 4**: Add the necessary states in between "Move R1 to place" and the "finished" outcome of the state machine, so that:

* Robot 1 drops the part on top of the Turtlebot
* After dropping the part, Robot 1 returns to its home pose.

**Step 5**: Save your changes in the behavior, check that no error messages appear, and close the FlexBE App.

To test your work, you can follow the same steps as in indicated in the first assignment.  If everything is OK, Robot 1 should be in the home pose, and the white box should be clearly visible on top of the turtlebot.

### Week 6 - Assignment 2 Part 2

In this second part, you will modify the "Final Project" behavior to control the Turtlebot so that, after getting the box from Robot 1, it delivers it to Robot 2.

To do this you need to open and modify the "Final Project" behavior, same as in the first assignment, and then follow the next steps.

**Step 1**: Add another state, between the last state you added in the Part 1 of this assignment and the "finished" outcome of the Final Project state machine, so that The Turtlebot navigates to the position given by

* x = -4.3
* y = -0.9
* theta = 0.0

Hint 1: Check the documentation of  "MoveBaseState"

Hint 2: You may need to add another constant variable in the Private Configuration of the behavior.

**Step 2**: Save your changes in the behavior, check that no error messages appear, and close the FlexBE App.

To test your work, you can follow the same steps as in indicated in the first assignment.  If everything is OK, the Turtlebot and the part (white box) should be next to the Robot 2.

This completes this second assignment! You can continue with the final one, where you will use Robot 2 to pick the part and place it on the bin!

## Practical Assignment 3: Pick and place with Robot 2

**Pick and place with Robot 2**

You have arrive to the last assignment of the course, now you will complete the behavior for the entire factory!!

The assignment consist on two parts, on the first one, the Robot 2 picks the part from the Turtlebot and in the second one, it places the part in the output bin.

Important note:  You need to have completed the previous assignment to continue and test this one

### Week 6 - Assignment 3 Part 1

In this part you will add the necessary states to the "Final Project" behavior so that: after Turtlebot brings the part next to the Robot 2, Robot 2 picks it from the Turtlebot.

To do this you need to open and modify the "Final Project" behavior, same as in assignments 1 and 2, and then follow the next steps.

**Step 1**: Add the necessary states between the state that makes the Turtlebot navigate lo the location next to Robot 2 and "Move R2 back Home", so that Robot 2 picks the part from the Turtlebot.

Hint: See which set of states were used to pick the part with Robot 1, and how they are configured.
Hint: Be aware that over Robot 2 there is another logical camera (logical camera 2) that works analogously to the camera on the conveyor belt (logical camera 1).

Important note:  You may notice that there are two versions of the MoveitToJointsDynState type. One in the package flexbe_manipulation_states, and another one in the hrwros_factory_states. For the assignments, you need to use the one in hrwros_factory_states.

**Step 2**: Save your changes in the behavior, check that no error messages appear, and close the FlexBE App.

To test your work, you can follow the same steps as in indicated in the first assignment.  If everything is OK, the Robot 2 should be on its home pose with the white box should being hold by its actuator.

### Week 6 - Assignment 3 Part 2

In this second part of the assignment,  you will add the necessary states to the "Final Project" behavior so that Robot 2 places the part in the output bin.

Same as with previous assignments and parts of this week, to do this you need to open and modify the "Final Project" behavior, and then follow the next steps.

**Step 1**: Add the necessary states between "Move R2 back Home" and the final "finished" outcome of the state machine, so that:

* Robot 2 moves its gripper above the output bin.
  Hint: to move the robot you can use the state implementation "SrdfStateToMoveit" and the joint configuration "R2Place". See how it is configured in "MoveR2 back Home".

* Robot 2 drops the part on the bin.

**Step 2**: Save your changes in the behavior, check that no error messages appear, and close the FlexBE App.

To test your work, you can follow the same steps as in indicated in the first assignment.  If everything is OK, Robot 2 should be in the R2Place pose, and the white box should be clearly visible on the output bin.

Congratulations!!

You have completed all the assignments of this course!!