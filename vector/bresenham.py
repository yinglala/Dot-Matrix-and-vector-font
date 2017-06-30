from PIL import Image
import math
import numpy as np

def Line(img,start,end):
	#print start,end
	delta_x = end[0] - start[0]
	delta_y = end[1] - start[1]
	
	#img = Image.new('P',(300,300))
	'''
	bresenham.Line(img,start,end)
	img = PIL.Image.new('P',(300,300))
	example:
	>>>bresenham.Line(img,(30,30),(200,200))
	it will draw a line in img
	'''
	#vertical line

	inte = -1 if delta_x == 0 else int(math.floor(abs(delta_y*1.0/delta_x)))

	if inte == 0:
		if start[0] > end[0]:
			temp = end
			end = start
			start = temp

		delta_x = end[0] - start[0]
		delta_y = abs(end[1] - start[1])

		x = start[0]
		y = start[1]

		p = 2*delta_y - delta_x

		#print p

		img.putpixel([x,y],255)

		while x!=end[0]:
			if p < 0:
				x = x+1
				y = y
				p = p+2*delta_y
			else:
				x = x+1
				if end[1]-start[1]<0:
					y = y-1
				else:
					y = y+1
				p = p+2*(delta_y-delta_x)
			#print x,y
			img.putpixel([x,y],255)
		#img.show()
	else:
		if start[1] > end[1]:
			temp = end
			end = start
			start = temp

		delta_x = abs(end[0] - start[0])
		delta_y = end[1] - start[1]

		x = start[0]
		y = start[1]
		
		p = 2*delta_x - delta_y

		img.putpixel([x,y],255)

		while y!=end[1]:
			if p < 0:
				y = y+1
				x = x
				p = p+2*delta_x
			else:
				y = y+1
				if end[0] - start[0] < 0:
					x = x-1
				else:
					x = x+1
				p = p+2*(delta_x-delta_y)
			#print x,y
			img.putpixel([x,y],255)
		#img.show()
#Line((28,27),(22,30))