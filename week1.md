# Week1 - Practical Assignment

## Practical Assignment 1

**ROS Publishers and Subscribers:**

Your goal in this assignment is to publish to and subscribe to a topic. Now, what is new about doing this when you already saw me do this in the lectures? Well, in the lecture I used two ROS nodes, one for publisher and one for subscriber. But in this assignment, you will use only ONE ROS node for both publisher and subscriber.

To achieve this, the assignment is divided in three parts:

In the first part you will only subscribe to the topic.
Then you will create the new type of ROS message.
Finally, you will complete everything in part 3.

The ultrasound sensor always reports the distance to the closer surface. If there is a box on the conveyor belt, the sensor reports the distance to the top surface of that box. If not, the ultrasound sensor publishes a value corresponding to the distance to the belt, which in this case is also the maximum range of the sensor (i.e 2.0 m).

However, there is also an indication in the technical specifications of the sensor:

* Although the advertised maximum range is 2.0 m, the usable range is only 1.9 m and any value above that is consider sensor noise.

* This means that those readings should be discarded because they can correspond to false positives.

### Week 1 - Assignment 1 - part 1 (of 3) 

The objective of part 1 of this assignment is to subscribe to the sensor information and to filter out false positives. 

To achieve this, you will MODIFY the week1_assignment1_part_1.py script, by changing the <write-your-code-here-Part1> bits with the correct code. 

The tasks you need to complete in this part are the following:

1. Subscribe to the /sensor_info topic.
2. Compute the height of the box from the sensor reading.
3. Filter out the false positives from the sensor due to sensor noise.

To check whether you implemented the subscriber and filter correctly, you can follow these steps: 

**Step 1**: Start up a terminal, source your setup files, start the sensor info publisher we developed in the videos.

```sh
ros2 run hrwros_week1 sensor_info_publisher
```

**Step 2**: In a new terminal, run the week1_assignment1_part1.py script with

```
ros2 run hrwros_week1_assignment week1_assignment1_part1
```

If you implemented everything correctly, you should now see a series of messages printed in your third terminal (where the assignment is running), which are in the correct height of the box.

### Week 1 - Assignment 1 - part 2 (of 3)

Now that you have successfully created a subscriber. In the part 2 of the assignment, you will create a new ROS message type, which you can use later to publish the box height into a new a topic.

You will create a new message type called BoxHeightInformation, it contains only a place holder called “box_height” which is a floating point number. This way you can share detected box height information with other ROS nodes in your application.

The tasks you need to complete in this part are the following:

Edit the BoxHeightInformation.msg file, found in the msg sub-folder, to add the “box_height” placeholder.
Edit the CMakeList.txt file, to add BoxHeightInformation.msg to the list of messages.
Generate the new message type as instructed in the lecture
You can check if you implemented this correctly by running:  

```sh
ros2 interface show hrwros_week1_assignment_interfaces/msg/BoxHeightInformation
```

### Week 1 - Assignment 1 - part 3 (of 3)

The objective of part 3 of this assignment is to subscribe and publish in the same script.

Note: In this part you will repeat the steps of Part 1, so you can have both subscriber and publisher in the same script. However, this time you will only MODIFY the week1_assignment1_part3.py script.

Now, you are ready to publish a new ROS topic “/box_height_info” ONLY when a valid box is detected. Also, just as in part 1 of this assignment, you are not supposed to publish anything when the detected box height was invalidated due to sensor noise. You can complete this part by making the next changes on the week1_assignment1_part_3.py script: 

1. Create an object of the custom message type you just created ONLY when you need it, that is, only when the detected box height is valid.
2. Create a publisher for the new message type in the main python module.
3. Publish the box height information on the /box_height_info topic ONLY when the detected box has a valid height.  

Once you have finished this, and the previous two parts of the assignment, you can run the full system.  To run it follow this steps: 

**Step 1**: Start up a terminal, start the sensor info publisher

```sh
ros2 run hrwros_week1 sensor_info_publisher
```

**Step 2**: In a new terminal, run the week1_assignment1_part3.py script with

```sh
ros2 run hrwros_week1_assignment week1_assignment1_part3
```
**Step 3**: In a new terminal, run the command

```
ros2 topic list
```

**Step 4**: If you see the topic /box_height_info listed, verify that it has a publisher with the command

```sh
ros2 topic info /box_height_info
```

**Step 5**: Finally, use the command

```sh
ros2 topic echo /box_height_info  
```

And wait until you see at least 5 messages, you should see different values for the box height.

## Practical Assignment 2

Your goal in this assignment is to call a ROS service via a service client similar to what you saw in the lecture. You will also see that the same service can also be called via the command line, provided that the service server is running.

### Week 1 - Assignment 2 - part 1 (of 2)

In Assignment 1, you created a publisher for a new topic to publish box height information. In this part the task is small, just subscribe to that new topic.

To achieve this, you will MODIFY the week1_assignment2.py script, by changing the <write-your-code-here-Part1> bits with the correct code. 

The tasks you need to complete in this part are the following:

Import the new message type.
Create a subscriber to the new topic, i.e, ”/box_height_info”

The script will remain incomplete at this point, so you will not be able to check your code yet,  just continue to part 2.

### Week 1 - Assignment 2 - part 2 (of 2)

The box height information in the topic ”/box_height_info” is published in metres ("m") but we want to convert this measurement to feet ("ft").

The objective of this part is to call the the ”metres_to_feet” ROS service created in the videos to convert the distance information from this topic from metres to feet. The service should be called in the subscriber callback of the ”/box_height_info” topic.

You can follow the same steps as was shown in the code illustration on ROS Service clients, with the necessary modifications to accomplish this assignment. Also, you are free to re-use the code of the ROS service client for this assignment.

Your tasks are to modify the week1_assignment2.py script in order to:

Add a call to the ”metres_to_feet” service in the subscriber callback.
Use a rospy.loginfo log message to display the converted information in feet with a meaningful log message.
Once you complete part 1 and part 2 all the relevant sections of the week1_assignment2.py script will be completed and you can tests this assignment with the following steps:

**Step 1**: Have assignment 1 part 3 running. 

If you did not close the terminals after completing assignment 1, you will have 2 programs running:

1. sensor_info_publisher
2. week1_assignment1_part3 (ROS node for publishing and subscribing)
Then you can continue to step 2.

If you DID close these terminals, you have to restart everything, as instructed in assignment1 part 3, to continue.

**Step 2**: In a new terminal, run the meter_to_feet server with

```sh
ros2 run hrwros_week1 metres_to_feet_server
```

Step 3: In a new terminal, Run the assignment 2 script

```sh
ros2 run hrwros_week1_assignment week1_assignment2
```

To check if it works, wait till you see the log messages with the converted information, appear in your terminal.

## Practical Assignment 3

**ROS Launch Files: Arguments and Node parameters**

In this assignment you will work with launch files. In the lectures, you learned that launch files can be used to start multiple nodes at once. Also, you were told that you can pass arguments to launch files and define node specific parameters. In this 3rd assignment you will explore these ideas further.

## Week 1 - Assignment 3 - part 1 (of 3)

As you may have noticed, running all the nodes one by one can be very tiring, so the goal of this part of the assignment is to run the two previous assignments together, and obtain the same result as you obtained at the end of assignment 2, launching only one file.

To achieve this goal, you need to complete the <add-node-name> and  <add-node-type> sections of the hrwros_week1_assignments1_2.launch file, which you can find in the hrwros_week1_assignment/launch folder.

Please use the correct node types and the following node names to start the all the ROS nodes of assignments 1 and 2.

The name of the first node (sensor info publisher node) should be 'sensor_info_publisher'
The name of the second node (Assignment 1 Part 3) should be 'assignment1'
The name of the last node (Assignment 2) should be 'assignment2'
Important Note: Make sure the node names are exactly those, as automated testing will fail if a different name is used.

You can test this part of the assignment with the following steps:

**Step 1**: Make sure you close all programs that may be running from previous assignments.

**Step 2**: Open a new terminal and run the command:

```sh
ros2 launch hrwros_week1_assignment hrwros_week1_assignments1_2.launch
```

Step 3: Start a new terminal and run the command:

```sh
ros2 node list
```

You should see all the 4 nodes running - Remember to double-check the node names!

### Week 1 - Assignment 3 - part 2 (of 3)

The goal of this part of the assignment is to learn how to use arguments and parameters with launch files.

Using arguments with launch files allows us to change values within launch files by specifying them along with the launch command. Uses of parameters allows us to configure some of the functionalities of our ROS nodes. In this part, you will learn how to use these two features of launch files.

To achieve this goal, you can follow the steps below:

**Step 1**: Make sure you close all programs that may be running from previous assignments.

**Step 2**: Open a new terminal and run the command:

```sh
ros2 launch hrwros_week1_assignment hrwros_week1_assignment3.launch counter_delay_parameter:=2
```

Notice the ”:=” (colon equals) after the counter_delay_parameter. That is how we can pass an argument value to a launch file, provided we have defined the same argument within the <arg> tag in the launch file. In the hrwros_week1_assignment3.launch, this is done in line 5.

**Step 3**:  After running this command, you can see a lot of text output from the command and within that text output, you will see a section called SUMMARY which has two subsections namely PARAMETERS and NODES. If done correctly, you will see the parameter /counter_with_delay/counter_delay with a value of 2. You can also experiment what will happens if you do not give any arguments, or if you use another value.

Now we will make that change permanent by modifying the default value in the hrwros_week1_assignment3.launch file. To do that, just change the default value of the delay to 2.0.

To test this, repeat the previous steps, but skip the counter_delay_parameter:=2 argument in Step 2, you should see the same values on the SUMMARY.

### Week 1 - Assignment 3 - part 3 (of 3)

In this part, you will learn how to read and use ROS parameter inside a ROS node.

In part 2, you observed that in the parameters subsection there is a parameter which is called /counter_with_delay/counter_delay: 2.0.  The value of this parameter is what you passed as the argument to the launch file. And if you look on line 13 of the hrwros_week1_assignment3.launch, the  parameter counter_delay (defined by the <param> tag) takes the value of the argument you just passed.

Defining a parameter inside the <node> tags of a launch file, makes this parameter a private parameter. Hence, the parameter in the parameter list is also prefixed with the node name, that is /counter_with_delay.

Parameters can be accessed inside a node using the rospy.get_param() function. Use the ROS wiki to learn more about how to use parameters with rospy, or just google, ”rospy get param”.

After doing this, you will modify week1_assignment3.py script. You need to figure out what goes in the place of <write your code here> (Lines 40 - 54) so it can read the delay parameter.

Check if the ”counter_delay” parameter has been set using the rospy.has_param() function.
Read the private parameters ”counter_delay” using the and rospy.get_param() function.
Note: week1_assignment3.py is a copy of the counter_with_delay_as.py file, which you used earlier. The only difference is that the old file does not use the parameters, and the new one does.

To test that the code is correctly implemented, follow these steps.

**Step 1**: Make sure you close all programs that may be running from previous assignments.

**Step 2**: Start a new terminal and run the command

```sh
ros2 launch hrwros_week1_assignment hrwros_week1_assignment3.launch
```



**Step 3**: Start a new terminal and run the command:

NOTE: In ROS 2 actions are now a combination of asynchronous service requests and have the optional status and feedback topics for monitoring progress. I could monitor the feedback with the hidden topic but not with rqt_plot.

```sh
ros2 topic list --include-hidden-topics
ros2 topic echo /counter_with_delay/_action/feedback
```

To open rqt_plot GUI:

```sh
ros2 run rqt_plot rqt_plot
```
This will start a plot window.

**Step 4**: In another terminal, run the action client ROS node, counter_with_delay_ac.py with the command:

```sh
ros2 run hrwros_week1 counter_with_delay_ac
```

**Step 5**: Wait for the action client to display the message that the counting was successful. Run the command in step 4 again, and then go to the plot window.

First click on the pause button on the plot window in the right top corner.

Then click on the Pan/Zoom button of this window in the panel just above the plot, and use the right mouse click to zoom out of the default view until you see a ”saw-tooth or right angled triangle” waveform.

