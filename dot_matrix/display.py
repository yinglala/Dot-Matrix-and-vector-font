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
 
from PIL import Image
import numpy as np
import sys

def display(txt,size,save_name):
	"""
	display(txt,large,save_name)
	example:
	>>>python display.py liu 2 5.png
	this will show a double sized 刘
	and will save it in '5.png'
	"""

	large = int(size)

	x = 24
	y = 24

	X = x*large
	Y = y*large

	pixel_24_24 = np.load(txt + '.npy')

	c = Image.new("P",(X,Y))

	if large == 1:
		for i in range (0,X):
			for j in range (0,Y):
				c.putpixel([j,i],pixel_24_24[i][j]*255)
		c.show()
		c.save(save_name)
		return
	pixel = np.array([[0.0]*Y]*X)

	#patial = np.array([[[0.0]*4]*large]*large)

	#long_distance = 2*large*large
	'''
	for k in range (0,large):
		for m in range (0,large):
					distance 			= 1-(k*k+m*m)*1.0/long_distance
					distance_upright 	= 1-(k*k + (large-m)*(large-m))*1.0/long_distance
					distance_downright 	= 1-((large-k)*(large-k) + (large-m)*(large-m))*1.0/long_distance
					distance_downleft 	= 1-((large-k)*(large-k) + m*m)*1.0/long_distance
					all_distance = distance + distance_downleft + distance_downright + distance_upright
					patial[k][m][0] = distance/all_distance
					patial[k][m][1] = distance_upright/all_distance
					patial[k][m][2] = distance_downright/all_distance
					patial[k][m][3] = distance_downleft/all_distance
	for i in range (0,x):
		for j in range (0,y):
			for k in range(0,large):
				for m in range(0,large):
					if j == y-1:
						upright = 0
						downright = 0
					else:
						upright = pixel_24_24[i][j+1]
						if i == x-1:
							downright = 0
							downleft  = 0
						else:
							downleft  = pixel_24_24[i+1][j]
							downright = pixel_24_24[i+1][j+1]
					pixel[i*large + k][j*large + m] = pixel_24_24[i][j]*patial[k][m][0] + upright*patial[k][m][1] + downright*patial[k][m][2] + downleft*patial[k][m][3] 
	print pixel
	'''
	flag = np.array([[0.0]*y]*x)
	for i in range (0,x):
		for j in range (0,y):
			if pixel_24_24[i][j] == 0 and i!=0 and i!=x-1 and j!=0 and j!=y-1:
				temp = 0
				if pixel_24_24[i-1][j] == 1 and pixel_24_24[i][j-1] == 1:
					flag[i][j] = 2
					for k in range(0,large):
						for m in range(0,large):
							pixel[i*large+k][j*large+m] = (k+m<=large-1)
					temp = 1
				if pixel_24_24[i-1][j] == 1 and pixel_24_24[i][j+1] == 1:
					flag[i][j] = 1 if temp else 3
					for k in range(0,large):
						for m in range(0,large):
							pixel[i*large+k][j*large+m] = 1 if temp else (k<=m)
					temp = 1
				if pixel_24_24[i+1][j] == 1 and pixel_24_24[i][j-1] == 1:
					flag[i][j] = 1 if temp else 4
					for k in range(0,large):
						for m in range(0,large):
							pixel[i*large+k][j*large+m] = 1 if temp else (k>=m)
					temp = 1
				if pixel_24_24[i+1][j] == 1 and pixel_24_24[i][j+1] == 1:
					flag[i][j] = 1 if temp else 5
					for k in range(0,large):
						for m in range(0,large):
							pixel[i*large+k][j*large+m] = 1 if temp else (k+m>=large-1)
					temp = 1
			else:
				flag[i][j] = pixel_24_24[i][j]
				for k in range(0,large):
					for m in range(0,large):
						pixel[i*large+k][j*large+m] = pixel_24_24[i][j]
	
	for i in range (1,x-1):
		for j in range (1,y-1):
			if flag[i][j] == 1 and flag[i-1][j-1] == 4:
				for k in range(0,large):
						for m in range(0,large):
							pixel[(i-1)*large+k][(j-1)*large+m] = pixel[(i-1)*large+k][(j-1)*large+m] or (2*k>=m)
							pixel[(i-1)*large+k][j*large+m] = pixel[(i-1)*large+k][j*large+m] or (2*(k-large/2)>=m)
			if flag[i][j] == 1 and flag[i-1][j+1] == 5:
				for k in range(0,large):
						for m in range(0,large):
							pixel[(i-1)*large+k][j*large+m] = pixel[(i-1)*large+k][j*large+m] or ((2*k+m)>=2*large-1)
							pixel[(i-1)*large+k][(j+1)*large+m] = pixel[(i-1)*large+k][(j+1)*large+m] or ((2*k+m)>=large-1)
			if flag[i][j] == 1 and flag[i+1][j-1] == 2:
				for k in range(0,large):
						for m in range(0,large):
							pixel[(i+1)*large+k][j*large+m] = pixel[(i+1)*large+k][j*large+m] or ((2*k+m)<=large-1)
							pixel[(i+1)*large+k][(j-1)*large+m] = pixel[(i+1)*large+k][(j-1)*large+m] or ((2*k+m)<=2*large-1)
			if flag[i][j] == 1 and flag[i+1][j+1] == 3:
				for k in range(0,large):
						for m in range(0,large):
							pixel[(i+1)*large+k][j*large+m] = pixel[(i+1)*large+k][j*large+m] or (2*k<=m)
							pixel[(i+1)*large+k][(j+1)*large+m] = pixel[(i+1)*large+k][(j+1)*large+m] or (2*(k-large/2)<=m)
			if flag[i][j] == 1 and flag[i-1][j-1] == 3:
				for k in range(0,large):
						for m in range(0,large):
							pixel[(i-1)*large+k][(j-1)*large+m] = pixel[(i-1)*large+k][(j-1)*large+m] or (k<=2*m)
							pixel[i*large+k][(j-1)*large+m] = pixel[i*large+k][(j-1)*large+m] or (k<=2*(m-large/2))
			if flag[i][j] == 1 and flag[i-1][j+1] == 2:
				for k in range(0,large):
						for m in range(0,large):
							pixel[i*large+k][(j+1)*large+m] = pixel[i*large+k][(j+1)*large+m] or ((k+2*m)<=large-1)
							pixel[(i-1)*large+k][(j+1)*large+m] = pixel[(i-1)*large+k][(j+1)*large+m] or ((k+2*m)<=2*large-1)
			if flag[i][j] == 1 and flag[i+1][j-1] == 5:
				for k in range(0,large):
						for m in range(0,large):
							pixel[i*large+k][(j-1)*large+m] = pixel[i*large+k][(j-1)*large+m] or ((k+2*m)>=2*large-1)
							pixel[(i+1)*large+k][(j-1)*large+m] = pixel[(i+1)*large+k][(j-1)*large+m] or ((k+2*m)>=large-1)
			if flag[i][j] == 1 and flag[i+1][j+1] == 4:
				for k in range(0,large):
						for m in range(0,large):
							pixel[(i)*large+k][(j+1)*large+m] = pixel[i*large+k][(j+1)*large+m] or (k>=2*m)
							pixel[(i+1)*large+k][(j+1)*large+m] = pixel[(i+1)*large+k][(j+1)*large+m] or (k>=2*(m-large/2))
	#print flag
	
	for i in range (0,X):
		for j in range (0,Y):
			c.putpixel([j,i],pixel[i][j]*255)

	c.show()
	c.save(save_name)
	#np.save('part.npy',patial)
display(sys.argv[1],sys.argv[2],sys.argv[3])