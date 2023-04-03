# Hello-Real-World-with-ROS
ROS2 Migration for DelftX ROS1x edx course with ROS1: https://learning.edx.org/course/course-v1:DelftX+ROS1x+1T2023/home

# ROS Setup
## Option #0 with singularity
Please follow the cource instructions.

## Option #1 with multipass
Install following instructions on https://multipass.run/
```sh
    multipass launch ros-humble
    multipass shell ros-humble
    source /opt/ros/humble/setup.bash
    git clone https://github.com/wolfboyyang/Hello-Real-World-with-ROS.git -b ros2
    cd Hello-Real-World-with-ROS/hrwros_ws/
    
    sudo rosdep init
    rosdep update
    rosdep install --from-paths src --ignore-src -r -y
    colcon build --symlink-install
    source devel/setup.bash
    ros2 launch hrwros_week1 hrwros_welcome.launch
```

If everything is OK, you've done!
## Option #2 with RoboStack & Conda
Another solution could be [RoboStack with Conda](https://robostack.github.io/GettingStarted.html)

1. Install [micromamba or mamba](https://mamba.readthedocs.io/en/latest/installation.html)

```sh
    micromamba config append channels robostack-staging
    micromamba create -n ros_humble python=3.10 -c conda-forge
    micromamba activate ros_humble
    micromamba config append channels conda-forge
    micromamba config append channels robostack-staging
    micromamba install ros-humble-desktop
    micromamba install compilers cmake pkg-config make ninja colcon-common-extensions
```

2. you also need to install deps for week 1:

```sh
    micromamba install ros-humble-moveit-msgs
```

3. Then you could clone the repo, and build it.

## Option #3 WSL
For wsl, make sure you upgrade to win11 to enable the GUI integration. And for humble, install Ubuntu 22.04 from Microsoft Store. Then follow ROS humble install instructions for Ubuntu. (I didn't try it)

```sh
    sudo apt update && sudo apt install curl -y
    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
    sudo apt update
    sudo apt upgrade
    
    sudo apt install ros-humble-desktop
    sudo apt install ros-dev-tools

    source /opt/ros/humble/setup.bash

    sudo rosdep init
    rosdep update
```

in your hrwros_ws folder,
```sh
    rosdep install --from-paths src --ignore-src -r -y
    colcon build --symlink-install
    source devel/setup.bash
    ros2 launch hrwros_week1 hrwros_welcome.launch
```


## Known Issues:
- Link Errors on Mac:
```sh
export CMAKE_OSX_SYSROOT=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk
```

- Unable to found Python with Numpy when Python 3.11 is installed
    add `find_package (Python3 3.10 EXACT)` to CMakefiles.txt
    and add `export Python3_ROOT_DIR=$HOME/micromamba/envs/ros_humble` to .bashrc or .zshrc

- Setuptools or Easyinstall deprecated warning
    add the following to .bashrc or .zshrc
```sh
# for bash/zsh
 export PYTHONWARNINGS=ignore:::setuptools.command.install,ignore:::setuptools.command.easy_install,ignore:::pkg_resources
```

```sh
# for fishshell
set -x PYTHONWARNINGS ignore:::setuptools.command.install,ignore:::setuptools.command.easy_install,ignore:::pkg_resources
```
- Fish Shell is Unsupported!

    if you want to use fish shell, one choice is using [bass](https://github.com/edc/bass), then then, you could source ros env with:

```sh
fisher install edc/bass
bass source /opt/ros/humble/setup.bash
```