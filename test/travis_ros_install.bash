#!/bin/bash -xve

#pip upgrade
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
python3 get-pip.py

#required packages
pip install --upgrade pip
pip install catkin_pkg
pip install empy
pip install pyyaml
pip install rospkg
