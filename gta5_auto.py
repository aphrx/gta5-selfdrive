import numpy as np
from PIL import ImageGrab
import cv2
import time

def process_img(img):
	processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	## processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)
	processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
	return processed_img

def main():
	while(True):
		printscreen_pil = ImageGrab.grab(bbox=(0, 30, 1024, 768))
		img = cv2.cvtColor(np.array(printscreen_pil), cv2.COLOR_BGR2RGB)
		cv2.imshow('window', process_img(img))
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break