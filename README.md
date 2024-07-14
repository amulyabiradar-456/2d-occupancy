# TechMate Presentation

**Presented by:** TechMate  
**Name:** Amulya  
**Date:** 14-07-24

# Robotics : Develop a 2D Occupancy Grid Map of a Room using Overhead Cameras [INT 2]

The primary objective of this project is to develop a 2D occupancy grid map of a room using overhead cameras, similar to the map created by a ROS2-based SLAM algorithm typically used by autonomous mobile robots (AMRs).

<img src="./img/cam.png" width=47%> <img src="./img/dsg.png" width=51%>

Description:
+ In the initial phase, you will need to equip a room or area with four overhead RGB cameras
arranged in a 2x2 pattern, ensuring some overlap in their fields of view. The room should contain
static objects such as chairs, tables, stools, and boxes. Using the images from these cameras, and
by stitching the views together, you will create a 2D occupancy grid map of the room. The goal is
to demonstrate that this map can be effectively used by AMRs for path-planning and navigation.

+ In the second phase, the room environment will become dynamic, meaning objects like tables and
chairs can be moved around. The 2D occupancy grid map should be able to dynamically update
itself to reflect these changes, providing a new, accurate map for AMRs to navigate. Additionally,
you will add semantic labels to the map (e.g., "table", "chair", "other AMR") to provide further
context for the AMRs. This will likely require the implementation of simple object detection.

Motivation:
+ Map entire environment in one shot 
+ Map moving obstacles in real-time 
+ Reduce AMR cost – don’t need expensive LiDAR or depth cams
+ Provide non line of sight to AMRs
+ Better multi-robot path planning and coordination

Project Scope
+ Add the 4 RGB cameras in Gazebo simulation environment [[infraCam](./infraCam/)] in a 2x2 matrix (birds eye view) covering the environment 
with marginal overlap of FoVs at a height of ~ 8 meters.
+ Use 640x480 image resolution and acquire images from the simulated cameras
+ Explore techniques for multi-camera calibration to automatically calibrate and align FoVs or all overhead cameras
+ Create a composite 2D occupancy grid map with accurate physical dimensions by fusing images from 4 cameras. The map 
should be in a form (.pgm and 512x512 pixel resolution) such that it can be used in ROS navigation stack.
+ Benchmark accuracy/error of infra-cam derived (dimensionally accurate) composite map v/s the Gazebo environment (refer 
slides 12-14) and Measure the computing latency to run the algorithm.

Outcomes:

Initially, you can model and simulate the room environment, objects, and overhead cameras in the
Gazebo simulator. Gazebo will also support the addition of an AMR equipped with an on-board camera
or LiDAR for SLAM map generation and navigation using the ROS2 navigation stack. This will allow for a comparison between the map generated from the overhead cameras and the map created by the AMR
using SLAM.

Expected deliverables :

+ Word document describing your solution, approach, novelty, pros/cons/limitations of your approach and comparison to 
state-of –the-art. Detailed block diagram and writeup describing your algorithm and approach.
+ Fused map of the environment with detailed dimensions (derived via your infra-cam fusion algorithm) v/s the ground truth 
map from Gazebo (provided)
+ Error estimates: Measure positions/distances between various key points in the composite map and identify % absolute 
avg, min and max errors. Provide details on how the algorithm was rigorously tested and the map accuracy results.
+ Computing latency: Characterize computing latency of the algorithm on an Intel i5 (10th Gen) computer. Provide 
measurement procedure and detailed test results.
+ Source code and algos to be shared for evaluation.

Evaluation criteria :

+ Accuracy (absolute avg, min, max error) of generated fused map v/s distances of key￾point in simulation. The expectation is that the avg error should be < 10% (lesser the 
better). 
    + The algo and code will be tested on a modified map to verify accuracy of the algorithm

+ Computational Complexity (Computational latency in milliseconds to process each 
set of images from camera and convert them to a composite map) as measured on 
an Intel Core i5 (10th gen CPU, iGPU can be used). The expectation it that the overall 
computational latency should be < 1000ms (lesser the better).
