# UCF-SST-CitySim-Dataset

The UCF SST team has launched the project of creating an open-source drone video dataset called the “UCF SST CitySim dataset”. Aiming at becoming the leading drone trajectory and co-simulation dataset in terms of diversity, quality and quantity, the dataset currently includes a total 9 locations at USA and overseas, a total recording duration of over 20 hours, with trajectories captured in 10-20 cm precision. The locations cover a wide range of intersections and segments including signalized intersections, non-signalized intersection, mid-block control intersections, continuous intersections, urban expressway weaving segments, and freeway segments. Numerous vehicle conflict events have been observed in the data, and rich driving behaviors such as queueing, yielding, and merging have been recorded. Furthermore, to the best of our knowledge, our dataset is the first to provide signal timing, simulation base map, corresponding crash data compared to other drone video datasets.

<img src="https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainDemo.gif" width="1080">


## Location Example

### Intersection

[University @ Alafaya (Signalized Intersection)](locations/intersection1)  |  [UCF Garage C (Consecutive Signalized Intersections)](locations/intersection2) | [ McCulloch @ Seminole (Non-Signalized Intersection)](locations/intersection3)
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/uni%40gemini030322E01stab-1_final.gif) |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/gargeC031622PM01-1_final.gif) |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/tivoli03302022A01sstabaliened-1_final.gif) 
[University @ McCulloch (Signalized Intersection)](locations/intersection1)  |  | 
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/publix.gif) |  | 

### Freeway

[ Freeway A (Weaving Segment)](locations/freewayA)    |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/tianfu031922AM02-5_final.gif)   
:-------------------------:|:-------------------------:
Freeway B (600m Highway) |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/freewayB.png) 
Freeway C (Highway Merging) |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/FreewayC.png) 

<hr> 


## Other Features

Digital Twin Base Map          |VR Driving Simulation           |  Co-Simulation Demo
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/bandicam%202022-05-05%2021-35-41-187.gif) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/demo4.gif) |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/CoSim2.gif)
Speed Data       | Surrogate Safety Measures           |  10 Years of Crash Data
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/Speed.png) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/SSM2.png) |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/Crash.jpg)
Autonomous Vehicle Simulation      | Sensor Simulation            |  Signal Timing Extraction
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/carlaDemo.gif) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/sensor.gif) |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/phb.gif)

## Trajectory Data

### [University @ Alafaya (Signalized Intersection)](locations/intersection1)

###### Sample Data:  [Google Drive Link](https://drive.google.com/drive/folders/1fHzmDxPHHofIBzQpx75Aol9pYCMX9gx7?usp=sharing) | [Baidu Yun Link](https://pan.baidu.com/s/1M6M7RlDwBUC-VoYVpcwpBQ?pwd=tfde)

### [UCF Garage C (Consecutive Signalized Intersections)](locations/intersection2)

###### Sample Data: [Google Drive Link](https://drive.google.com/drive/folders/1m4eIq4dcbx5olBazagOXqvM6KBgXeCaT?usp=sharing) | [Baidu Yun Link]( https://pan.baidu.com/s/1M-MEC-DeHsBMW9OpltEwbQ?pwd=8eek)

### [ McCulloch @ Seminole (Non-Signalized Intersection)](locations/intersection3)

###### Sample Data [Google Drive Link](https://drive.google.com/drive/folders/1DOPb_EqEwqPwFKlqL9XWoVZrJOqjsntE?usp=sharing) | [Baidu Yun Link]( https://pan.baidu.com/s/1rGTsQJwH-5LyT8I5GwtLCA?pwd=6ujc))

### [ Freeway A (Weaving Segment)](locations/freewayA)

###### Sample Data: TBA

### Freeway B (600m Highway)

###### Sample Data: TBA

### Freeway C (HighWay Merging)

###### Sample Data: TBA

<hr> 

## Data Extraction Tool
[UCF-SST Automated Roadway Conflicts Identify System (A.R.C.I.S)](https://github.com/ozheng1993/A-R-C-I-S)


## Contributing

Contributions to this repository are welcome. Examples of things you can contribute:
-TBD

See [publiction](paper)  built on top of City-Sim and ARCIS.

## Application for Access for Non-Commercial Use

To apply for access to the full dataset, please send us a request to this email: citysim.ucfsst@gmail.com 

Please tell us about yourself, your position, your current (research) project and what exactly you would like to use this dataset for. 


## Citation

If you use CitySim Dataset in your research , please use the following BibTeX entry.
```BibTeX
      @article{,
        title={},
        author={},
        year={},
        publisher={}
      }
```
