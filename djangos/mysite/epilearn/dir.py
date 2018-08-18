#!/usr/bin/python
import os 

dir_path = os.path.dirname(os.path.realpath(__file__)) 

filename = os.path.join(dir_path, 'static/epilearn/img/SImodel.png')
print(filename)
