# UCF-SST-CitySim-Dataset

The UCF SST dataset is an open-source drone video trajectory and co-simulation dataset. The dataset aims to become the leading drone-video-based trajectory and co-simulation dataset in terms of diversity, quality and quantity. The dataset currently includes various locations in the USA and other countries, a total recording duration of over 20 hours, with trajectories captured in 10-20 cm precision. The locations cover a wide range of road types including signalized intersections, non-signalized intersection, mid-block control intersections, continuous intersections, urban expressway weaving segments, and freeway segments. Numerous vehicle conflict events have been observed in the dataset, and rich driving behaviors such as queueing, yielding, and merging have been recorded. Furthermore, to the best of our knowledge, our dataset is the first to provide 4 point rotation-aware vehicle bounding boxes, signal timing, and simulation base maps.

<img src="https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/MainDemo.gif" width="100%">


## Location Example

### Intersection

[University @ Alafaya (Signalized Intersection)](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/University%40Alafaya)  |  [ McCulloch @ Seminole (Non-Signalized Intersection)](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/McCulloch%40Seminole%20)
:-------------------------:|:-------------------------:
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/uni%40gemini030322E01stab-1_final.jpg) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/tivoli03302022A01sstabaliened-1_final.jpg)  
[**University @ McCulloch (Signalized Intersection)**](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/University%40McCulloch)  |  [**UCF Garage C (Consecutive Signalized Intersections)**](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/GarageC)
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/publix.jpg) |   ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/gargeC031622PM01-1_final.jpg) 

### Segment

[ Expressway A (Weaving Segment)](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/ExpresswayA)    |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/tianfu031922AM02-5_final.jpg)   
:-------------------------:|:-------------------------:
[**Freeway B (Basic Segment)**](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/FreewayB) |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/freewayB.png) 
[**Freeway C (Merge/Diverge Segment)**](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/tree/main/asset/FreewayC) |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/freewayC.png) 

<hr> 


## Features
Digital Twin Base Map      | Co-Simulation           |  Signal Timing Extraction  
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/bandicam%202022-05-05%2021-35-41-187.jpg) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/CoSim2.jpg) |![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/phb.jpg) 

## Use Cases

VR Driving Simulation      |Autonomous Vehicle Simulation   |   Sensor Simulation
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/demo4.jpg) |![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/carlaDemo.jpg)| ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/sensor.jpg)
 **Speed Analysis**   | **Surrogate Safety Measures** | **Crash Analysis**    
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/Speed.png) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/SSM2.png) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/Crash.jpg) 


## Sample Data
Download sample data  [here](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/data/README.md)

## Full Dataset Access 

To apply for access to the full dataset for non-commercial use, please send us a request [form](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/Data_Request_Form.pdf) to this email: citysim.ucfsst@gmail.com 

## Documentation

The dataset documentation and file format description can be found [here](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/wiki/Home).

## Data Extraction Tool
[UCF-SST Automated Roadway Conflicts Identify System (A.R.C.I.S)](https://github.com/ozheng1993/A-R-C-I-S)

## Project Team

<img src="https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainPage/projectTeam.png" width="100%">

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

## Contributing

Contributions to this repository are welcome. Examples of things you can contribute:
-TBD

See [publication](paper)  built on top of CitySim and ARCIS.
