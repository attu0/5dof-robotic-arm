# 5DOF Robotic Arm

A 5 degree-of-freedom (5DOF) robotic arm project covering mechanical design, 3D printing, URDF modelling, and ROS integration.

---

## Project Roadmap

- [x] Repository setup
- [ ] CAD design files (joint geometry, links, gripper)
- [ ] 3D-printable STL files
- [ ] URDF description (kinematics & visual/collision meshes)
- [ ] ROS 2 package (MoveIt! integration, controllers, demos)

---

## Directory Structure

```
5dof-robotic-arm/
├── cad/          # Source CAD files (Fusion 360 / FreeCAD / SolidWorks)
├── stl/          # 3D-printable STL files exported from CAD
├── urdf/         # URDF robot description files
│   └── 5dof_arm.urdf
└── ros/          # Future ROS 2 package
```

---

## Robot Description

The arm has **5 revolute joints** arranged in a typical anthropomorphic configuration:

| Joint | Name          | Axis | Range          |
|-------|---------------|------|----------------|
| 1     | base_rotation | Z    | ±180°          |
| 2     | shoulder      | Y    | −90° to +90°   |
| 3     | elbow         | Y    | −135° to +135° |
| 4     | wrist_pitch   | Y    | −90° to +90°   |
| 5     | wrist_roll    | X    | ±180°          |

A fixed **gripper** is attached at the end-effector.

---

## Getting Started

### Visualise the URDF (ROS)

```bash
# Install dependencies (ROS 2 Humble example)
sudo apt install ros-humble-urdf-tutorial

# Launch the URDF viewer
ros2 launch urdf_tutorial display.launch.py model:=$(pwd)/urdf/5dof_arm.urdf
```

### Print the Parts

1. Open the STL files from the `stl/` folder in your slicer (e.g. Cura, PrusaSlicer).
2. Recommended settings: 0.2 mm layer height, 40 % infill, PLA or PETG.
3. Print supports are required for overhanging link bodies.

---

## Contributing

Pull requests are welcome. Please open an issue first to discuss proposed changes.

## License

This project is licensed under the [MIT License](LICENSE).
