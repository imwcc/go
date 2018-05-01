#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

dirname, filename = os.path.split(os.path.abspath(__file__))

install_content=[]

with open(os.path.join(dirname, '.install_file'), 'r') as f:
    install_content = f.readlines()

print(install_content)
with open(os.path.join(os.environ['HOME'], '.bashrc'), 'a') as f:
    for line in install_content:
        print(line)
        f.writelines(line)

print("install successfuly")
