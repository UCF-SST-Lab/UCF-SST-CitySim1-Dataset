# UCF-SST-CitySim-Dataset

The UCF SST team has launched the project of creating an open-source drone video dataset called the “UCF SST CitySim dataset”. Aiming at becoming the leading drone trajectory and co-simulation dataset in terms of diversity, quality and quantity, the dataset currently includes a total 9 locations at USA and overseas, a total recording duration of over 20 hours, with trajectories captured in 10-20 cm precision. The locations cover a wide range of intersections and segments including signalized intersections, non-signalized intersection, mid-block control intersections, continuous intersections, urban expressway weaving segments, and freeway segments. Numerous vehicle conflict events have been observed in the data, and rich driving behaviors such as queueing, yielding, and merging have been recorded. Furthermore, to the best of our knowledge, our dataset is the first to provide signal timing, simulation base map, corresponding crash data compared to other drone video datasets.

<img src="https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainDemo.gif" width="1080">


## Location Example

### Intersection

[University @ Alafaya (Signalized Intersection)](locations/intersection1)  |  [ McCulloch @ Seminole (Non-Signalized Intersection)](locations/intersection3)
:-------------------------:|:-------------------------:
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/uni%40gemini030322E01stab-1_final.gif) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/tivoli03302022A01sstabaliened-1_final.gif)  
[University @ McCulloch (Signalized Intersection)](locations/intersection4)  |  [UCF Garage C (Consecutive Signalized Intersections)](locations/intersection2)
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/publix.gif) |   ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/gargeC031622PM01-1_final.gif) 

### Segment

[ Expressway A (Weaving Segment)](locations/freewayA)    |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/tianfu031922AM02-5_final.gif)   
:-------------------------:|:-------------------------:
Freeway B (Basic Segment) |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/freewayB.png) 
Freeway C (Merge/Diverge Segment) |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/FreewayC.png) 

<hr> 


## Features
Digital Twin Base Map      | Co-Simulation           |  Signal Timing Extraction  
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/bandicam%202022-05-05%2021-35-41-187.gif) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/CoSim2.gif) |![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/phb.gif) 

## Use Cases

VR Driving Simulation      |Autonomous Vehicle Simulation   |   Sensor Simulation
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/demo4.gif) |![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/carlaDemo.gif)| ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/sensor.gif)
 Speed Analysis   | Surrogate Safety Measures | Crash Analysis    
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/Speed.png) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/SSM2.png) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/Crash.jpg) 


## Sample Data

### [University @ Alafaya (Signalized Intersection)](locations/intersection1)

###### Sample Data:  [Google Drive Link](https://drive.google.com/drive/folders/1fHzmDxPHHofIBzQpx75Aol9pYCMX9gx7?usp=sharing) | [Baidu Yun Link](https://pan.baidu.com/s/1M6M7RlDwBUC-VoYVpcwpBQ?pwd=tfde)

### [UCF Garage C (Consecutive Signalized Intersections)](locations/intersection2)

###### Sample Data: [Google Drive Link](https://drive.google.com/drive/folders/1m4eIq4dcbx5olBazagOXqvM6KBgXeCaT?usp=sharing) | [Baidu Yun Link]( https://pan.baidu.com/s/1M-MEC-DeHsBMW9OpltEwbQ?pwd=8eek)

### [ McCulloch @ Seminole (Non-Signalized Intersection)](locations/intersection3)

###### Sample Data [Google Drive Link](https://drive.google.com/drive/folders/1DOPb_EqEwqPwFKlqL9XWoVZrJOqjsntE?usp=sharing) | [Baidu Yun Link]( https://pan.baidu.com/s/1rGTsQJwH-5LyT8I5GwtLCA?pwd=6ujc))


### University @ McCulloch (Signalized Intersection)

###### Sample Data: TBA

### [ Expressway A (Weaving Segment)](locations/freewayA)

###### Sample Data: [Google Drive Link](https://drive.google.com/drive/folders/1t0RNw0I3k06rPchSvgkQvzKU_2P-mbhV?usp=sharing) | [Baidu Yun Link]( https://pan.baidu.com/s/1mF423Onhbgt7wVZdyxOqvA?pwd=r6f5 ))



### Freeway B (Basic Segment)

###### Sample Data: TBA

### Freeway C (Merge/Diverge Segment)

###### Sample Data: TBA


## Documentation

The dataset documentation and file format description can be found [here](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/wiki/Home).



## Data Extraction Tool
[UCF-SST Automated Roadway Conflicts Identify System (A.R.C.I.S)](https://github.com/ozheng1993/A-R-C-I-S)


## Contributing

Contributions to this repository are welcome. Examples of things you can contribute:
-TBD

See [publiction](paper)  built on top of City-Sim and ARCIS.

## Application for Access for Non-Commercial Use

To apply for access to the full dataset, please send us a request [form](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/Data%20request%20form.docxe) to this email: citysim.ucfsst@gmail.com 



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
