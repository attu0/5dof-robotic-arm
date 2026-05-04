# 5DOF Robotic Arm – ROS Package (Planned)

This directory will contain the ROS 2 package for the 5DOF robotic arm.

## Planned Contents

```
ros/
└── arm_description/          # ROS 2 package
    ├── package.xml
    ├── CMakeLists.txt
    ├── launch/
    │   └── display.launch.py
    ├── urdf/                  # symlink or copy of ../urdf/
    └── rviz/
        └── arm.rviz
```

## Planned Features

- [ ] `arm_description` package – URDF + RViz launch
- [ ] `arm_moveit_config` – MoveIt 2 configuration
- [ ] `arm_controllers` – ros2_control hardware interface
- [ ] `arm_bringup` – launch files for full system bring-up
- [ ] `arm_teleop` – keyboard / joystick teleoperation node

## Prerequisites (ROS 2 Humble)

```bash
sudo apt install \
  ros-humble-urdf-tutorial \
  ros-humble-robot-state-publisher \
  ros-humble-joint-state-publisher-gui \
  ros-humble-rviz2
```
