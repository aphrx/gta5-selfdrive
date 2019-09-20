import numpy as np
from PIL import ImageGrab
import cv2
import time
import math
from keyboard_mapper import W, A, S, D, Forward, Left, Right, Back, PressKey, ReleaseKey

def process_img(img):
	processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
	processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)
	return processed_img

def region_of_interest(img):
	height = img.shape[0]
	width = img.shape[1]
	interest = np.array([[(0, 600),(0,400), (200, 300), (600, 300), (800, 400), (800, 600)]])
	mask = np.zeros_like(img)
	cv2.fillPoly(mask, interest, 255)
	masked_img = cv2.bitwise_and(img, mask)
	return masked_img

def display_lines(img, lines):
	line_image = np.zeros_like(img)
	m1 = 0; ## Right
	m2 = 0; ## Left
	length1 = 0
	length2 = 0
	m1coords = [[0, 0], [0,0]]
	m2coords = [[0, 0], [0,0]]

	if lines is not None:
		for line in lines:
			x1, y1, x2, y2 = line.reshape(4)
			
			#x = ((x2.item()-x1.item())(x2.item()-x1.item()) + (y2.item()-y1.item())(y2.item()-y1.item()))
			x = (float)(x2.item() - x1.item())
			y = (float)(y2.item() - y1.item())
			if (x != 0 and y != 0):
				m = y/x
				z = (x*x)+(y*y)
				length = math.sqrt(z)
				#if(length > 0):
				print(length)
				if(math.fabs(m) > 0.2 and math.fabs(m) < 0.8):
					#length = math.sqrt((x*x)+(y*y))

					if(m > m1):# and length1 < length):
						m = m1
						m1coords[0] = [x1, y1]
						m1coords[1] = [x2, y2]

						
					elif(m < m2):# and length2 < length):
						m = m2
						m2coords[0] = [x1, y1]
						m2coords[1] = [x2, y2]
			cv2.line(line_image, (m1coords[0][0], m1coords[0][1]), (m1coords[1][0], m1coords[1][1]), (255, 255, 255), 1)
			cv2.line(line_image, (m2coords[0][0], m2coords[0][1]), (m2coords[1][0], m2coords[1][1]), (255, 255, 255), 1)

	return line_image, m1, m2

def display_lines2(img, lines):
	line_image = np.zeros_like(img)
	m1 = 0; ## Right
	m2 = 0; ## Left
	length1 = 0
	length2 = 0
	m1coords = [[0, 0], [0,0]]
	m2coords = [[0, 0], [0,0]]

	if lines is not None:
		for line in lines:
			x1, y1, x2, y2 = line.reshape(4)
			
			#x = ((x2.item()-x1.item())(x2.item()-x1.item()) + (y2.item()-y1.item())(y2.item()-y1.item()))
			x = (float)(x2.item() - x1.item())
			y = (float)(y2.item() - y1.item())
			if (x != 0 and y != 0):
				m = y/x
				z = (x*x)+(y*y)
				length = math.sqrt(z)
				#if(length > 0):
				print(length)
				if(math.fabs(m) > 0.2 and math.fabs(m) < 0.8):
					#length = math.sqrt((x*x)+(y*y))

					if(m > m1 and length1 < length):
						m = m1
						m1coords[0] = [x1, y1]
						m1coords[1] = [x2, y2]

						
					elif(m < m2 and length2 < length):
						m = m2
						m2coords[0] = [x1, y1]
						m2coords[1] = [x2, y2]
			cv2.line(line_image, (m1coords[0][0], m1coords[0][1]), (m1coords[1][0], m1coords[1][1]), (255, 255, 255), 10)
			cv2.line(line_image, (m2coords[0][0], m2coords[0][1]), (m2coords[1][0], m2coords[1][1]), (255, 255, 255), 10)


	
	## cv2.line(line_image, (0, 400), (800, 400), (255, 255, 255), 5)		
	return line_image, m1, m2

def main():
	while(True):
		printscreen_pil = ImageGrab.grab(bbox=(0, 30, 800, 600))
		img = cv2.cvtColor(np.array(printscreen_pil), cv2.COLOR_BGR2RGB)
		processed_img = region_of_interest(process_img(img))
		
		lines = cv2.HoughLinesP(processed_img, 2, np.pi/180, 100, np.array([]), minLineLength=300, maxLineGap=5)

		lined_img, m1, m2 = display_lines(processed_img, lines)
		lined_img, m1, m2 = display_lines2(processed_img, lines)

		overlayed_img = cv2.addWeighted(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 0.8, lined_img, 1, 1)

		cv2.imshow('window', overlayed_img)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break
		
		start = 0
		durTurn = 0

		if(m1 == 0):
			if(durTurn == 0):
				start = time.time()
				durTurn = 1
				#PressKey(D)
		elif(m2 == 0):
			if(durTurn == 0):
				start = time.time()
				durTurn = 1
				#PressKey(A)
		if((time.time()-start==1) and durTurn == 1):
			print("Releasing key D")
			#ReleaseKey(D)
			durTurn = 0
		if((time.time()-start==1) and durTurn == 1):
			print("Releasing key A")
			#ReleaseKey(A)
			durTurn = 0
main()
