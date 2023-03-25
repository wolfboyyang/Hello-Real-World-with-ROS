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
    wget https://courses.edx.org/assets/courseware/v1/01b274edcf91f56f8cdd7c56ae05b139/asset-v1:DelftX+ROS1x+3T2018+type@asset+block/week1_contents_new2_fixed.zip
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
    micromamba install ros-noetic-moveit-msgs
```

3. Then you could create hrwros_ws/src, add week1 contents, and build it.

## Option #3 WSL
For wsl, make sure you upgrade to win11 to enable the GUI integration. And for noetic, install Ubuntu 20.04 from Microsoft Store. Then follow ROS noetic install instructions for Ubuntu. (I didn't try it)

```sh
    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
    sudo apt install ros-noetic-desktop-full
    sudo apt install python3-catkin-tools python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential


    source /opt/ros/noetic/setup.bash
    sudo rosdep init
    rosdep update
```

in your hrwros_ws folder,
```sh
    rosdep install --from-paths src --ignore-src -r -y
    catkin build
    source devel/setup.bash
    roslaunch hrwros_week1 hrwros_welcome.launch
```

## Option #4 Docker/Podman
For docker/podman, I tried in raspberry pi 4 with ubuntu server 22.04 for week1:
```sh
    sudo apt install podman
    podman pull docker.io/library/ros:noetic

    podman run -it --rm -v ~/hrwros_ws/:/hrwros_ws docker.io/ros:noetic
    apt update
    apt install python3-catkin-tools
    cd /hrwros_ws
    rosdep install --from-paths src --ignore-src -r -y
    catkin build
    source devel/setup.bash
    roslaunch hrwros_week1 hrwros_welcome.launch
```
But for GUI, you'd better try docker.io/osrf/ros:noetic-desktop-full (only amd64) and vnc or X forwarding.


## Known Issues:
- Fish Shell is Unsupported!

    One issue I found is with as fish shell is not supported officially by ROS yet, I could not build successfully with robostack-conda solution in fish shell. Better stick to zsh or bash for ROS.