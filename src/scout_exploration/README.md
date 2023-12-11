# scout_exploration Package

This package contains ROS (Robot Operating System) launch files and configuration parameters to enable the Silvanus robot to navigate using the explore_lite and move_base package.

## Prerequisites / Installation / Usage

This package should be run only as part of the explorat_module. All requisites are listed in the Dockerfile of this repository. For further instructions, refer to the README of this repository.

## Nodes

There are no custom nodes in this package.

## Launch files

### nav_and_explore.launch

This is the main launch file for the exploration_module for the Silvanus robot. It combines the capabilities to move using move_base as well as receiving 3D coordinates to explore by the explore_lite package.

#### Launched nodes

- **move_base**
  - Please refer to the [official ROS documentation](https://wiki.ros.org/move_base) for more information and input parameter description
  - Loads the costmap_common.yaml, costmap_local.yaml and base_local_planner_params.yaml configuration files of this package
- **explore_lite**

  - Please refer to the [official ROS documentation](https://wiki.ros.org/explore_lite) for more information and input parameter description

- **scout_bringup**
  - For information about the included launch file, please refer to the scout_ros submodule that is also inside the src directory of this repository

### navigation.launch

Exactly the same as nav_and_explore.launch except that explore_lite will not get launched. This means this launch file is used when NavGoals are inputted manually by the user through RViz.

### explore.launch

Only launches the explore_lite package.

## Configuration files

### costmap_common.yaml

Costmap configuration parameters that are shared between the local and global costmap created by move_base.

### costmap_local.yaml

Costmap configuration parameters that are specific to the local costmap of the move_base package.

### costmap_global.yaml

Costmap configuration parameters that are specific to the global costmap of the move_base package.

### base_local_planner_params.yaml

Max velocity configurations used by the move_base package to restrict the robot's speed when moving around.
