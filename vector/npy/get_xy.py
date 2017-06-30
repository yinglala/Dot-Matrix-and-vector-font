import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys

def get_xy(img_name,save_name):
	img = Image.open(img_name)

	shape = img.size

	plt.imshow(img)

	temp = np.array([shape])
	ans = np.array([])

	while len(temp)!=0:
		if len(ans) == 0:
			ans = temp
		else:
			ans = np.vstack((ans,[0,0]))
			ans = np.vstack((ans,temp))
		temp = plt.ginput(0,0)

	np.save(save_name,ans)
get_xy(sys.argv[1],sys.argv[2])