#!/bin/bash
set -e
source /root/.bashrc

# Add a delay to wait for the ros master to be ready
sleep 2

# setup ros environment
source "/opt/ros/$ROS_DISTRO/setup.bash" --

if [ ! -e "CONTAINER_INITIALIZED_PLACEHOLDER" ]; then
    echo "-- First container startup --"
    catkin build
    touch "CONTAINER_INITIALIZED_PLACEHOLDER" # <== This placeholder file used in the github action to check when colcon build is done, do not remove
fi
    source "/root/ros_ws/devel/setup.bash"
    sleep 5
    if [ -n "$AUTO_EXPLORE" ]; then
        roslaunch scout_exploration nav_and_explore.launch # <== change to your launch file // comment out if you don't want auto launch
    else
        roslaunch scout_exploration navigation.launch
    fi

exec "$@"
