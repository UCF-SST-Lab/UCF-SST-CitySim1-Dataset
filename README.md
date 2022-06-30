# UCF-SST-CitySim-Dataset

The UCF SST CitySim dataset contains vehicle trajectory data collected from drone videos captured at 30 frames per second. The dataset contains variuos location types including signalized intersections, non-signalized intersections, freeway basic segments, and freeway weaving segments. For each detected vehicle, the dataset includes frame number, unique car ID, bouding box X/Y, car center X/Y, bounding box latitude/longitude, car center latitude/longitude, speed, and heading.

<img src="https://github.com/ozheng1993/UCF-SST-CitySim-Dataset/blob/main/asset/uni%40gemini030322E01stab-1_final.gif" width="1080">

## Trajectory Data
### [University @ Alafaya (Signalized Intersection)](locations/intersection1)
:white_check_mark:  55 Mintues Trajectory :white_check_mark:  55 Mintues Signal Timing :white_check_mark:  Carla Base Map :white_check_mark:  Sumo Base Map

The intersection of University Boulevard (9 lanes) and Alafaya Trail (9 lanes) is a large, signalized intersection at the entrance of the University of Central Florida in Orlando, Florida. Due to the large volume of serviced vehicles, the intersection contains numerous vehicle-to-vehicle traffic conflicts including merge conflicts and turning movement conflicts. Between 2011 – 2022, there was a total of 503 crashes in the intersection.

### [UCF Garage C (Consecutive Signalized Intersections)](locations/intersection2)
:white_check_mark: 15 Mintues Trajectory :white_check_mark: 15 Mintues Signal Timing :white_check_mark: Carla Base Map :white_check_mark: Sumo Base Map

This location contains two consecutive signalized intersections as well as their connecting road segment. The two intersections are positioned on both ends of a large student garage at the University of Central Florida in Orlando, Florida. Both intersections have permitted left-turn signal phases which lead to potential conflicts between southbound through traffic on the major road and left-turning vehicles heading for the garage. Furthermore, the connecting road segment contains the queue buildup for vehicles heading to the garage. Between 2011 – 2022, there was a total of 57 crashes in this location.

### [ McCulloch @ Seminole (Non-Signalized Intersection)](locations/intersection3)
:white_check_mark: 60 Mintues Trajectory :white_check_mark: Carla Base Map :white_check_mark: Sumo Base Map

The intersection of McCulloch Road and Seminole Avenue is a non-signalized intersection with a mid-block near the University of Central Florida in Orlando, Florida. Due to the intersection’s non-signalized nature and reliance on driver visibility for movement decision making, the intersection contains numerous turning movement potential conflicts. Conflicts between westbound through traffic on the major road and left-turning vehicles from the minor road as well as left-turning vehicles from the major road are frequently observed, especially when students rush from Seminole Avenue to the major road during school time. Between 2011 – 2022, there was a total of 42 crashes in the intersection.
### [ Freeway A (Weaving Segment)](locations/freewayA)

:white_check_mark: 120 Mintues Trajectory :white_check_mark: Carla Base Map :white_check_mark: Sumo Base Map


<hr> 

## Data Extraction Tool
[UCF-SST Automated Roadway Conflicts Identify System (A.R.C.I.S)](https://github.com/ozheng1993/A-R-C-I-S)


## Contributing

Contributions to this repository are welcome. Examples of things you can contribute:
-TBD

## Application for Access for Non-Commercial Use

To apply for access to the full dataset, please send us a request to this email: citysim.ucfsst@gmail.com 

Please tell us about yourself, your position, your current (research) project and what exactly you would like to use this dataset for. 

## Citation

If you use CitySim Dataset in your research , please use the following BibTeX entry.

      @article{,
        title={},
        author={},
        year={},
        publisher={}
      }
