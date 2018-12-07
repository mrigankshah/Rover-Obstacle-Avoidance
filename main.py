import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 

cap = cv.VideoCapture(0)

while True:
	_,frame1 = cap.read()
	#imCopy = im.copy()
	#color_frame = frame[400:, :]
	#cv.imshow("frame", frame)
	#cv.imshow("View", frame)
	frame = cv.blur(frame1,(20,20))

	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)	

	#filter for values below 50
	#gaussian blur that shit
	lower_black = np.array([0,0,0])
	upper_black = np.array([180,255,40])

	mask = cv.inRange(hsv, lower_black, upper_black)
	res = cv.bitwise_not(mask)

	#cv.imshow('frame',frame)
	cv.imshow('mask',mask)
	#cv.imshow('res',res)

	image,contours,_ = cv.findContours(res,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
	cv.drawContours(frame, contours, 0, (0,255,0), 3)
	#print "Number of contours detected %d" %len(contours)
	cv.imshow('res',res)
	cv.imshow('frame',frame)
	
	try:
		cnt = contours[0]

		M = cv.moments(cnt)
		#print( M )
		try:
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			#print cx
			#print cy

		except ZeroDivisionError:
			continue

		if cx<320:
			print "turn left"
		else:
			print "turn right"
	
	except IndexError:
		continue
			
	k = cv.waitKey(5) & 0xFF
 	if k == 27:
 		break
    

cv.destroyAllWindows()
cap.release()
