# Crowd Navigation based on GCNs and Deep RL
Forked from the repository [ChanganVR/RelationalGraphLearning](https://github.com/ChanganVR/RelationalGraphLearning), this github repository utilizie its simulation envrionment and training code. This repository realize a new algorithm which combine graph learning and self-attention module, having deeper understanding of the environment. Some supplements are in [R_CrowdNav](https://jasonz5.github.io/projects/R_CrowdNav/).


## Abstract
In certain scenarios, robots need navigate through crowds to complete specific tasks. This environment poses great challenges as it requires robots to avoid collisions with surrounding individuals. To address this challenge, this graduation project mainly designs and implements algorithm for robot navigation in crowds.
The algorithm utilizes graph structure to model the scenario, and uses graph convolutional networks(GCNs) to calculate deeper interactive features between agents. 
Based on the importance of human for robot, the interaction features are merged for movement planning.
Additionally, the model also incorporates human dynamics, to  provide more comprehensive considerations and improve the navigation strategy.
The algorithm model is trained by deep reinforcement learning algorithm, and compared with other classical methods in a simulation environment. Through simulation experiments, it is demonstrated that the model can generate more efficient and safer movement paths, with shorter navigation time and higher success rate.
The algorithm will improve the efficiency and safety of robots in crowded environments.



## Method Overview
<img src="https://jasonz5.github.io/assets/projects/crowd_nav/frame.png" width="1000" />


## Setup
Disclaimer: This part is just a reference for my system.

1. Choose linux/WSL2, the code can't run successful due to [Python-RVO2](https://github.com/sybrenstuvel/Python-RVO2) in Windows.
2. Install [Python-RVO2](https://github.com/sybrenstuvel/Python-RVO2) library
     ```python
    # Recommend no newest version of Python. Current test version: 3.8.10
    # 安装CMake和Cython
    sudo apt install cmake # cmake==3.16.3，不要用最新版，直接apt安装即为旧版
    sudo pip3 install Cython # ubuntu下：pip安装的不能被使用到

    python3 setup.py build # build
    # 如果cmake编译报错可能需要将build文件夹删除重新编译
    sudo python3 setup.py install # install
    python3 example.py # test
    ```
    + tips: no newest version of *setuptools*, the version should < 66.0.0 for python3.8
3. Install [socialforce](https://github.com/ChanganVR/socialforce) library
    ```python
    # install from source
    pip install -e '.[test,plot]'

    # run linting and tests
    sudo apt install pylint
    pylint socialforce
    sudo apt install python3-pytest
    # pytest可能调用的是python2，需要改为pytest-3
    pytest-3 tests/*.py 
    ```
4. Install crowd_sim and crowd_nav into pip
   + some possible errors
     + About 'AssertionError: You must specify a action space.'
       + Solution: degrade *gym*, *gym==0.13.0*
    ```python
    # 首先更改setup.py里各个库的版本号
    gym>=0.15.7
    # 不用改成这俩个版本torch==1.4.0, torchvision==0.5.0,  之前bug是将H+=改为H=H+

    # 开始下载
    pip install -e .
    # ERROR: pandas 1.5.3 has requirement python-dateutil>=2.8.1, 
    # but you'll have python-dateutil 2.7.3 which is incompatible.
    sudo pip install --upgrade python-dateutil
    ```

## Getting Started
This repository are organized in two parts: crowd_sim/ folder contains the simulation environment and
crowd_nav/ folder contains codes for training and testing the policies. Details of the simulation framework can be found
[here](crowd_sim/README.md). Below are the instructions for training and testing policies, and they should be executed
inside the crowd_nav/ folder.

```python
cd crowd_nav/
## 1. Train a policy.
# python3 train.py --policy rgl
python3 train.py --output_dir data/output_debug --gpu True --debug True

## 2. Test policies with 500 test cases.
#python3 test.py --policy rgl --model_dir data/output --phase test
python3 test.py --model_dir data/output_rgl --phase test

## 3. Run policy for one episode and visualize the result.
#python3 test.py --policy rgl --model_dir data/output --phase test --visualize --test_case 0
python3 test.py --model_dir data/output_rgl --phase test --visualize --test_case 0

## 4. Plot training curve
python3 utils/plot.py data/output/output.log
# 第四步不出图，后续再看
```

## Experiments
The experiments data and trained modal has beed place on [google drive](https://drive.google.com/drive/folders/17hXul83oWV7X5t9EvHPoaoAPslTrCGLm?usp=drive_link). For more information about experiment analysis, refer to my [thesis paper](https://jasonz5.github.io/assets/projects/crowd_nav/thesis.pdf) (only Chinese version).