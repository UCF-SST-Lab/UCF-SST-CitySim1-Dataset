# CitySim: A Drone-Based Vehicle Trajectory Dataset for Safety Oriented Research and Digital Twins

The development of safety-oriented research ideas and applications requires fine-grained vehicle trajectory data that not only has high accuracy but also captures a substantial number of critical safety events. This paper introduces the CitySim Dataset, which was devised with a core objective of facilitating safety-based research and applications. CitySim  currently has vehicle trajectories extracted from 1140-minutes of drone videos@30 FPS recorded at 12 different locations and we are adding more location. It covers a variety of road geometries including freeway basic segments, weaving segments, expressway merge/diverge segments, signalized intersections, stop-controlled intersections, and intersections without sign/signal control. CitySim trajectories were generated through a five-step procedure which ensured the trajectory accuracy. Furthermore, the dataset provides vehicle rotated bounding box information which is demonstrated to improve safety evaluation. Compared to other video-based trajectory datasets, the CitySim Dataset has significantly more critical safety events with higher severity including cut-in, merge, and diverge events. In addition, CitySim facilitates research towards digital twin applications by providing relevant assets like the recording locations'3D base maps and signal timings. These features enable more comprehensive conditions for safety research and applications such as autonomous vehicle safety and location-based safety analysis. 


[Read More](https://www.researchgate.net/publication/362887363_CitySim_A_Drone-Based_Vehicle_Trajectory_Dataset_for_Safety_Oriented_Research_and_Digital_Twins) 



#### 


 Full Data Access
:-------------------------:
The data are not publicly available due to privacy.<br /> Please send us a request form ([Download form here](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/Data_Request_Form.pdf) ) to this email: citysim.ucfsst@gmail.com 


## Documentation

The dataset documentation and file format description can be found [here](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/wiki/Home).


## Location Example

### Intersection

[Intersection A<br /><sub><sup>Signalized Intersection-USA</sup></sub>](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/University%40Alafaya)  |  [ Intersection B <br /><sub><sup>Non-Signalized Intersection-USA</sup></sub>](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/McCulloch%40Seminole%20)
:-------------------------:|:-------------------------:
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/uni%40gemini030322E01stab-1_final.jpg) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/tivoli03302022A01sstabaliened-1_final.jpg)  
[**Intersection C <br /> <sub><sup>Signalized Intersection-USA</sup></sub>**](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/University%40McCulloch)  |  [**Intersection D <br /><sub><sup>Consecutive Signalized Intersections-USA</sup></sub>**](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/GarageC)
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/publix.jpg) |   ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/gargeC031622PM01-1_final.jpg) 
[**Intersection E <br /> <sub><sup>Signalized Intersection-USA</sup></sub>**](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/GarageCV2) |  [**Intersection F <br /> <sub><sup>Non-Signalized Intersection-USA</sup></sub> TBD**](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/IntersectionF)
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/IntersectionEBaseMap.png) |   ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/intersectionFBaseMap.png) 



### Roundabout

[Roundabout A <br /><sub><sup>One lane roundabout-USA</sup></sub>](https://drive.google.com/drive/folders/1XW10wnNg0_gfsRHCZcVWECkDE6OgDEpV?usp=share_link)  |  [ Roundabout B <br /> <sub><sup>Two lane roundabout-USA</sup></sub>]()
:-------------------------:|:-------------------------:
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/RoundAboutA/roundaboutA.png) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/RoundaboutB/RoundaboutB.png)  



### Segment

[ Expressway A <br />Weaving Segment<br />Asia<br/> <sub><sup>In associate with <br /> Southwest Jiaotong University<br />  Data Science and Traffic Safety Lab</sup></sub> ](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/ExpresswayA)    |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/expresswayA.png)   
:-------------------------:|:-------------------------:
[**Freeway B <br />Basic Segment<br /> Asia <br /> <sub><sup>Highway-Asia</sup></sub>**](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/FreewayB) |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/freewayB.png) 
[**Freeway C <br />Merge/Diverge Segment<br /> Asia<br /> <sub><sup>Highway-Asia</sup></sub>**](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/FreewayC) |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/freewayC.png) 
[**Freeway D (TBA)<br /> Merge/Diverge Segment<br /> Asia <br /> <sub><sup>In associate with <br /> Hong Kong PolyU<br />  Dr.Tony Sez</sup></sub>**](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/FreewayD) |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/freewayD.png) 


<hr> 


## Features
Digital Twin Base Map      | Sumo Carla Co-Simulation           |  Signal Timing Extraction  
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/bandicam%202022-05-05%2021-35-41-187.jpg) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/CoSim2.jpg) |![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/phb.jpg) 

## Use Cases

VR Driving Simulation      |Autonomous Vehicle Simulation   |   Sensor Simulation
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/demo4.jpg) |![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/carlaDemo.jpg)| ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/sensor.jpg)
 **Speed Analysis**   | **Surrogate Safety Measures** | **Crash Analysis**    
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/Speed.png) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/SSM2.png) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/Crash.jpg) 





## Data Extraction Tool
[UCF-SST Automated Roadway Conflicts Identify System (A.R.C.I.S)](https://github.com/ozheng1993/A-R-C-I-S)

## Active Project Team

<img src="https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/projectTeam.png" width="100%">

## Pervious Contributor

[Lishengsa Yue](https://www.researchgate.net/profile/Lishengsa-Yue-2) |
[Amr Abdelraouf](https://scholar.google.com/citations?user=kWR3NRUAAAAJ&hl=en) |
[Nada Mahmoud](https://scholar.google.com/citations?user=QH_gttgAAAAJ&hl=en)


## Citation

If you use CitySim Dataset in your research , please use the following BibTeX entry.

```BibTeX
@misc{https://doi.org/10.48550/arxiv.2208.11036,
  doi = {10.48550/ARXIV.2208.11036},
  url = {https://arxiv.org/abs/2208.11036},
  author = {Zheng, Ou and Abdel-Aty, Mohamed and Yue, Lishengsa and Abdelraouf, Amr and Wang, Zijin and Mahmoud, Nada},  
  title = {CitySim: A Drone-Based Vehicle Trajectory Dataset for Safety Oriented Research and Digital Twins},
  publisher = {arXiv},
  year = {2022}
}
```

## Related Publication

See [publication](paper)  built on top of CitySim and ARCIS.
