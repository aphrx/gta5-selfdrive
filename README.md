# GTA V Automous Driving

Wouldn't it be cool if we could use GTA V as a simulator to test self-driving technology. Well that is what this project is all about!

## Pre-requisites
* Python 2.7
* Python Libraries (`pip install ...`):
	* Numpy
	* Pillow (PIL)
	* Time
	* Math
	* CV2
	* CTypes

## To Run

In order to run the service, simply open a command window and run:
```
python gta5_auto.py
```

## How it works

### Obtaining the image:
We are simply using the ImageGrab() functionality from PIL to grab a screenshot within an infinite while loop in order to grab the image.

### Image Processing:
Once we get the image, we then 'process' it by doing the following OpenCV functionalities:
 * Grayscaling
 * Edge Detection
 * Gaussian Blur (Blurs the details of the image)
 * Region of Interest crop (Cuts out unnecessary parts of the image
 
 ### Detecting Lanes:
Once the image is processed, we feed it into a command which will try to find the lines. We use Hough Lines within OpenCV to detect lines within the image that meet a certain requirement.

Those lines are then sent to a method which detects which lines are most likely to be the lane lines and displays them on the screen.


## Screenshots
![Screenshot of python attempting to detect lines](https://scontent-yyz1-1.xx.fbcdn.net/v/t1.15752-0/p480x480/69982064_2138067863160521_8629945394933006336_n.png?_nc_cat=103&_nc_oc=AQkFxsZRQntK3HmTMobb5Jo6abTlbJ9baPHSOzQjDH9xkEXkjifw4YPoPg-ZFp5zmDY&_nc_ht=scontent-yyz1-1.xx&oh=754b2523838e28c52110fb27ac7c0937&oe=5E08D004)
The image on the left is the GTA V game running while the left is the live feed of the lines drawn over the image. 
 
## Credits
* Sentdex
