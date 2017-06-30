import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys

def point_in(image,point):
	print point
	if image[point[1]][point[0]] == 255:
		return False
	temp = [0]*4
	for i in range(0,point[0]):
		if image[point[1]][i] == 255:
			temp[0] = temp[0] + 1
	for i in range(0,point[1]):
		if image[i][point[0]] == 255:
			temp[1] = temp[1] + 1
	for i in range(point[1],image.shape[0]):
		if image[i][point[0]] == 255:
			temp[2] = temp[2] + 1
	for i in range(point[0],image.shape[1]):
		if image[point[1]][i] == 255:
			temp[3] = temp[3] + 1
	if temp[0]%2==1 or temp[1]%2==1 or temp[2]%2==1 or temp[3]%2==1:
		return True
	return False

def fill(txt):
	img = Image.open(txt)

	image = np.array(img)

	flag = np.array([[0]*img.size[1]]*img.size[0])

	plt.imshow(img)
	while True:
		point_float = plt.ginput(1,0)

		point = (int(point_float[0][0]),int(point_float[0][1]))

		wait = [point]
		flag[point[0]][point[1]] = 1
		while len(wait)!=0:
			if image[wait[0][1]][wait[0][0]]!=255:
				img.putpixel(wait[0],255)
				if wait[0][0] > 0 and flag[wait[0][0]-1][wait[0][1]]!=1:
					wait.append((wait[0][0]-1,wait[0][1]))
					flag[wait[0][0]-1][wait[0][1]]=1
				if wait[0][1] > 0 and flag[wait[0][0]][wait[0][1]-1]!=1:
					wait.append((wait[0][0],wait[0][1]-1))
					flag[wait[0][0]][wait[0][1]-1]=1
				if wait[0][0] < img.size[0]-1 and flag[wait[0][0]+1][wait[0][1]]!=1:
					wait.append((wait[0][0]+1,wait[0][1]))
					flag[wait[0][0]+1][wait[0][1]]=1
				if wait[0][1] < img.size[1]-1 and flag[wait[0][0]][wait[0][1]+1]!=1:
					wait.append((wait[0][0],wait[0][1]+1))
					flag[wait[0][0]][wait[0][1]+1]=1
			wait.pop(0)
		img.show()
fill(sys.argv[1])