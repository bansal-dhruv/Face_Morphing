import numpy as np
import imutils
import dlib
import cv2
from collections import OrderedDict
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import matplotlib.pyplot as plt

def rect_to_bb(rect):	
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y

	return (x, y, w, h)


def shape_to_np(shape, dtype="int"):
	coords = np.zeros((68, 2), dtype=dtype)

	for i in range(0, 68):
		coords[i] = (shape.part(i).x, shape.part(i).y)
	return coords

def mainFunction(filename):
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
	# filename="4.jpeg"
	image = cv2.imread(filename)
	# image = imutils.resize(image, width=500)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# detect faces 
	rects = detector(gray, 1)


	for (i, rect) in enumerate(rects):
		shape = predictor(gray, rect)
		shape = shape_to_np(shape)
		(x, y, w, h) = rect_to_bb(rect)
		
		# for i in range(len(shape)):
		# 	cv2.circle(image, (convexpointsx[i],convexpointsy[i] ), 3, (0, 0, 255), -1)
		for i in range(len(filename)):
			print(i)
			print(filename[i])
			if(filename[i]=='/'):
				filename=filename[i:]
				break


		file1 = open('text'+filename+".txt","w") 
		for i in range(len(shape)):
			data=str(shape[i][0])+" "+str(shape[i][1])+"\n"
			file1.write(data)
		file1.close()  

	# cv2.imshow("Output", image)
	# cv2.waitKey(0) 

