from PIL import Image
import math
import numpy as np

def Bezier(img,start,mid,end):
	#print start,mid,end
	delta = abs(mid[0]-start[0])+abs(mid[1]-start[1])+abs(end[0]-mid[0])+abs(end[0]-mid[0])
	temp = 0
	delta = 1.0/(5*delta)
	t_list = []
	while temp < 1:
		t_list.append(temp)
		temp = temp + delta
	t_list.append(1)

	#img = Image.new('P',(300,300))

	point = [0,0]

	for t in t_list:
		point[0] = int(round((end[0]+start[0]-2*mid[0])*t*t + (mid[0]-start[0])*2*t + start[0]))
		point[1] = int(round((end[1]+start[1]-2*mid[1])*t*t + (mid[1]-start[1])*2*t + start[1]))
		img.putpixel(point,255)
	#img.show()
	'''
	Bezier.Bezier(img,start,mid,end)
	img = PIL.Image.new('P',(300,300))
	example:
	>>>Bezier.Bezier(img,(30,30),(70,70),(200,200))
	it will draw a Bezier curve in img
	'''
	#img.save('Bezier_example.png')
#Bezier((30,30),(230,180),(40,270))
#Bezier((240,100),(240,180),(240,200))