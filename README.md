# Hello-Real-World-with-ROS
DelftX ROS1x edx course with ROS1: https://learning.edx.org/course/course-v1:DelftX+ROS1x+1T2023/home

# ROS Setup
## Option #0 with singularity
Please follow the cource instructions.

## Option #1 with multipass
Install following instructions on https://multipass.run/
```sh
    multipass launch ros-noetic
    multipass shell ros-noetic
    source /opt/ros/noetic/setup.bash
    mkdir -p ~/hrwros_ws/src
    cd ~/hrwros_ws/src
    wget https://courses.edx.org/assets/courseware/v1/a88adc0595bea37bef1bd99f748368c8/asset-v1:DelftX+ROS1x+1T2023+type@asset+block/hrwros_week1_v21.zip
    unzip hrwros_week1_v21.zip
    cd ..
    sudo rosdep init
    rosdep update
    rosdep install --from-paths src --ignore-src -r -y
    catkin build
    source devel/setup.bash
    roslaunch hrwros_week1 hrwros_welcome.launch
```

If everything is OK, you've done!
## Option #2 with RoboStack & Conda
Another solution could be [RoboStack with Conda](https://robostack.github.io/GettingStarted.html)

1. Install [micromamba or mamba](https://mamba.readthedocs.io/en/latest/installation.html)

```sh
    micromamba config append channels robostack-staging
    micromamba create -n ros_noetic python=3.9 -c conda-forge
    micromamba activate ros_noetic
    micromamba config append channels conda-forge
    micromamba config append channels robostack-staging
    micromamba install ros-noetic-desktop
    micromamba install compilers cmake pkg-config make ninja colcon-common-extensions
    micromamba install catkin_tools
```

2. you also need to install deps for week 1:

```sh
    micromamba install ros-noetic-moveit-msgs ros-noetic-object-recognition-msgs ros-noetic-octomap-msgs
```

3. Then you could create hrwros_ws/src, add week1 contents, and build it.

## Known Issues:
- Fish Shell is Unsupported!

    One issue I found is with as fish shell is not supported officially by ROS yet, I could not build successfully with robostack-conda solution in fish shell. Better stick to zsh or bash for ROS.