# Paper-2026 Stereo YOLO UAV Localization and Tracking
Workspace for 2026 AIAA SciTech paper "Stereo YOLO UAV Localization and Tracking Enabling Autonomous Sensor Deployment on Critical Infrastructure".

This work is completed on the basis of a UAV-deployable sensor package system that can be flown and magnetically attach sensors underneath metal elements of a structure [1,2]. This system uses two cameras for stereo vision to track the movement of the UAV as it docks its magnetic sensors. An object tracking algorithm called You Only Look Once (YOLO) has been trained on images of the UAV flight to translate color images of the drone flight into three-dimensional coordinates, with the help of some additional Python code for this stereo analysis of input images. These three-dimensional coordinates were derived by having the object tracking algorithm draw bounding boxes around the element of interest (the UAV), where the center of the bounding box is considered the coordinate location of the drone.

<p align="center">
<img src="Figures/Experimental_Setup.png" alt="drawing" width="700"/>
</p>
<p align="center">
Figure 1: Complete set-up of UAV flight zone and docking area with associated cameras. 
</p>

<p align="center">
<img src="Figures/cam_position_real.jpg" alt="drawing" width="700"/>
</p>
<p align="center">
Figure 2: Positional placement of cameras that will send visual data to the computer running YOLO. 
</p>

<p align="center">
<img src="Figures/YOLO_drone_detection.png" alt="drawing" width="700"/>
</p>
<p align="center">
Figure 3: YOLO bounding box output of the UAV during flight, with the center representing the coordinate location of the drone. 
</p>

### References

[1] Satme, J. N., Yount, R., Goujevskii, N., Jannazzo, L., and Downey, A. R. J., “Sensor Package Deployment and Recovery Cone with Integrated Video Streaming for Rapid Structural Health Monitoring,” ASME 2024 Conference on Smart Materials, Adaptive Structures and Intelligent Systems, American Society of Mechanical Engineers, 2024. https://doi.org/10.1115/smasis2024-140435.

[2] Smith, C., Satme, J., Martin, J., Downey, A. R., Vitzilaios, N., and Imran, J., “UAV rapidly-deployable stage sensor with electro-permanent magnet docking mechanism for flood monitoring in undersampled watersheds,” HardwareX, Vol. 12, 2022, p.e00325. https://doi.org/10.1016/j.ohx.2022.e00325.


## Licensing and Citation

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License [cc-by-sa 4.0].

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)


Cite this data as: 

#### Bibtex

@Misc{ARTSLab2026Paper2026Stereo,    
  author = {ARTS-Lab},  
  howpublished = {GitHub},  
  title  = {Paper 2026 Stereo YOLO UAV Localization and Tracking},  
  groups = {ARTS-Lab},    
  year = {2026},   
  url    = {https://github.com/ARTS-Laboratory/Paper-2026-Stereo-YOLO-UAV-Localization-and-Tracking/tree/main},   
}




