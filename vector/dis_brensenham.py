# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        display
# Purpose:
#
# Author:     liuchanglu
#
# Created:    03-06-2017
# Copyright:   (c) liuchanglu 2017
# Licence:    
#-------------------------------------------------------------------------------
 
import numpy as np
from bresenham import *
from PIL import Image
import sys

def display(txt,size,save_name):
	"""
	display(txt,large,save_name)
	example:
	>>>python display.py ./npy/liu 2 5.png
	this will show a double sized 刘
	and will save it in '5.png'
	"""

	points_float = np.load(txt+'.npy')
	points = []

	large = int(size)

	for i in range(0,len(points_float)):
		points.append((large*int(round(points_float[i][0])),large*int(round(points_float[i][1]))))

	points = np.array(points)

	#print points

	X = points[0][0]
	Y = points[0][1]

	img = Image.new("P",(X,Y))
	start_point = points[2]
	i = 2
	while i != len(points)-1:
		if points[i+1][0]==0 and points[i+1][1]==0:
			Line(img,points[i],start_point)
			start_point = points[i+2]
			i = i + 2
		else:
			Line(img,points[i],points[i+1])
			i = i + 1

	Line(img,points[len(points)-1],start_point)

	img.show()
	img.save(save_name)
	
display(sys.argv[1],sys.argv[2],sys.argv[3])