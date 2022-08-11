# UCF-SST-CitySim-Dataset

The UCF SST dataset is an open-source drone video trajectory and co-simulation dataset. The dataset aims to become the leading drone-video-based trajectory and co-simulation dataset in terms of diversity, quality and quantity. The dataset currently includes various locations in the USA and other countries, a total recording duration of over 20 hours, with trajectories captured in 10-20 cm precision. The locations cover a wide range of road types including signalized intersections, non-signalized intersection, mid-block control intersections, continuous intersections, urban expressway weaving segments, and freeway segments. Numerous vehicle conflict events have been observed in the dataset, and rich driving behaviors such as queueing, yielding, and merging have been recorded. Furthermore, to the best of our knowledge, our dataset is the first to provide 4 point rotation-aware vehicle bounding boxes, signal timing, and simulation base maps.

<img src="https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/MainDemo.gif" width="100%">


## Location Example

### Intersection

[University @ Alafaya (Signalized Intersection)](locations/intersection1)  |  [ McCulloch @ Seminole (Non-Signalized Intersection)](locations/intersection3)
:-------------------------:|:-------------------------:
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/uni%40gemini030322E01stab-1_final.jpg) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/tivoli03302022A01sstabaliened-1_final.jpg)  
[**University @ McCulloch (Signalized Intersection)**](locations/intersection4)  |  [**UCF Garage C (Consecutive Signalized Intersections)**](locations/intersection2)
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/publix.jpg) |   ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/gargeC031622PM01-1_final.jpg) 

### Segment

[ Expressway A (Weaving Segment)](locations/freewayA)    |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/tianfu031922AM02-5_final.jpg)   
:-------------------------:|:-------------------------:
**Freeway B (Basic Segment)** |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/freewayB.png) 
**Freeway C (Merge/Diverge Segment)** |  ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/FreewayC.png) 

<hr> 


## Features
Digital Twin Base Map      | Co-Simulation           |  Signal Timing Extraction  
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/bandicam%202022-05-05%2021-35-41-187.jpg) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/CoSim2.jpg) |![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/phb.jpg) 

## Use Cases

VR Driving Simulation      |Autonomous Vehicle Simulation   |   Sensor Simulation
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/demo4.jpg) |![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/carlaDemo.jpg)| ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/sensor.jpg)
 **Speed Analysis**   | **Surrogate Safety Measures** | **Crash Analysis**    
![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/Speed.png) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/SSM2.png) | ![](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/Crash.jpg) 


## Sample Data

### [University @ Alafaya (Signalized Intersection)](locations/intersection1)

###### Sample Data:  [Google Drive Link](https://drive.google.com/drive/folders/1fHzmDxPHHofIBzQpx75Aol9pYCMX9gx7?usp=sharing) | [Baidu Yun Link](https://pan.baidu.com/s/1M6M7RlDwBUC-VoYVpcwpBQ?pwd=tfde)



### [ McCulloch @ Seminole (Non-Signalized Intersection)](locations/intersection3)

###### Sample Data [Google Drive Link](https://drive.google.com/drive/folders/1DOPb_EqEwqPwFKlqL9XWoVZrJOqjsntE?usp=sharing) | [Baidu Yun Link]( https://pan.baidu.com/s/1QAB3eIyR29KnWOMoSoHmyw?pwd=3ddf))




### [ Expressway A (Weaving Segment)](locations/freewayA)

###### Sample Data: [Google Drive Link](https://drive.google.com/drive/folders/1t0RNw0I3k06rPchSvgkQvzKU_2P-mbhV?usp=sharing) | [Baidu Yun Link]( https://pan.baidu.com/s/1mF423Onhbgt7wVZdyxOqvA?pwd=r6f5 ))



### Freeway B (Basic Segment)


###### Sample Data [Google Drive Link](https://drive.google.com/drive/folders/1wVRBDhHkSRNDrqEEEwQft3qKWCbaBDxh?usp=sharing) | [Baidu Yun Link](https://pan.baidu.com/s/1Dq64PNY6OS1WfABDhkKvMA?pwd=csja))

### Freeway C (Merge/Diverge Segment)

###### Sample Data: [Google Drive Link](https://drive.google.com/drive/folders/1BbOfB86a1Lzef8rTHWzd6a_jvruJIH2L?usp=sharing) | [Baidu Yun Link](https://pan.baidu.com/s/1eTrq0OTsubOAi7v9kLzCEQ?pwd=o331))



### [UCF Garage C (Consecutive Signalized Intersections)](locations/intersection2)

###### Sample Data: TBA

### University @ McCulloch (Signalized Intersection)

###### Sample Data: TBA


## Request Access for Non-Commercial Use

To apply for access to the full dataset, please send us a request [form](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/Data_Request_Form.pdf) to this email: citysim.ucfsst@gmail.com 

## Documentation

The dataset documentation and file format description can be found [here](https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/wiki/Home).



## Data Extraction Tool
[UCF-SST Automated Roadway Conflicts Identify System (A.R.C.I.S)](https://github.com/ozheng1993/A-R-C-I-S)


## Contributing

Contributions to this repository are welcome. Examples of things you can contribute:
-TBD

See [publication](paper)  built on top of CitySim and ARCIS.

## Project Team

<img src="https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/projectTeam.png" width="100%">

## Citation

If you use CitySim Dataset in your research , please use the following BibTeX entry. (TBA)
```BibTeX
      @article{,
        title={},
        author={},
        year={},
        publisher={}
      }
```
