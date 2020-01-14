import cv2
import numpy as np
import math
from enum import Enum

class GripPipeline:
    """
    An OpenCV pipeline generated by GRIP.
    """
    
    def __init__(self):
        """initializes all values to presets or None if need to be set
        """

        self.__blur_type = BlurType.Box_Blur
        self.__blur_radius = 14.414414414414415

        self.blur_output = None

        self.__hsv_threshold_input = self.blur_output
        self.__hsv_threshold_hue = [12.949640287769784, 36.06060606060607]
        self.__hsv_threshold_saturation = [61.915467625899275, 207.77777777777777]
        self.__hsv_threshold_value = [82.55395683453237, 255.0]

        self.hsv_threshold_output = None

        self.__find_blobs_input = self.hsv_threshold_output
        self.__find_blobs_min_area = 0.0
        self.__find_blobs_circularity = [0.31654675658658255, 1.0]
        self.__find_blobs_dark_blobs = False

        self.find_blobs_output = None


    def process(self, source0):
        """
        Runs the pipeline and sets all outputs to new values.
        """
        # Step Blur0:
        self.__blur_input = source0
        print(self.__blur_input)
        (self.blur_output) = self.__blur(self.__blur_input, self.__blur_type, self.__blur_radius)

        # Step HSV_Threshold0:
        self.__hsv_threshold_input = self.blur_output
        (self.hsv_threshold_output) = self.__hsv_threshold(self.__hsv_threshold_input, self.__hsv_threshold_hue, self.__hsv_threshold_saturation, self.__hsv_threshold_value)

        # Step Find_Blobs0:
        self.__find_blobs_input = self.hsv_threshold_output
        (self.find_blobs_output) = self.__find_blobs(self.__find_blobs_input, self.__find_blobs_min_area, self.__find_blobs_circularity, self.__find_blobs_dark_blobs)


    @staticmethod
    def __blur(src, type, radius):
        """Softens an image using one of several filters.
        Args:
            src: The source mat (numpy.ndarray).
            type: The blurType to perform represented as an int.
            radius: The radius for the blur as a float.
        Returns:
            A numpy.ndarray that has been blurred.
        """
        if(type is BlurType.Box_Blur):
            ksize = int(2 * round(radius) + 1)
            return cv2.blur(src, (ksize, ksize))
        elif(type is BlurType.Gaussian_Blur):
            ksize = int(6 * round(radius) + 1)
            return cv2.GaussianBlur(src, (ksize, ksize), round(radius))
        elif(type is BlurType.Median_Filter):
            ksize = int(2 * round(radius) + 1)
            return cv2.medianBlur(src, ksize)
        else:
            return cv2.bilateralFilter(src, -1, round(radius), round(radius))

    @staticmethod
    def __hsv_threshold(input, hue, sat, val):
        """Segment an image based on hue, saturation, and value ranges.
        Args:
            input: A BGR numpy.ndarray.
            hue: A list of two numbers the are the min and max hue.
            sat: A list of two numbers the are the min and max saturation.
            lum: A list of two numbers the are the min and max value.
        Returns:
            A black and white numpy.ndarray.
        """
        out = cv2.cvtColor(input, cv2.COLOR_BGR2HSV)
        return cv2.inRange(out, (hue[0], sat[0], val[0]),  (hue[1], sat[1], val[1]))

    @staticmethod
    def __find_blobs(input, min_area, circularity, dark_blobs):
        """Detects groups of pixels in an image.
        Args:
            input: A numpy.ndarray.
            min_area: The minimum blob size to be found.
            circularity: The min and max circularity as a list of two numbers.
            dark_blobs: A boolean. If true looks for black. Otherwise it looks for white.
        Returns:
            A list of KeyPoint.
        """
        params = cv2.SimpleBlobDetector_Params()
        params.filterByColor = 1
        params.blobColor = (0 if dark_blobs else 255)
        params.minThreshold = 10
        params.maxThreshold = 220
        params.filterByArea = True
        params.minArea = min_area
        params.filterByCircularity = True
        params.minCircularity = circularity[0]
        params.maxCircularity = circularity[1]
        params.filterByConvexity = False
        params.filterByInertia = False
        detector = cv2.SimpleBlobDetector_create(params)
        return detector.detect(input)


BlurType = Enum('BlurType', 'Box_Blur Gaussian_Blur Median_Filter Bilateral_Filter')


pipeline = GripPipeline()

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)
#cap.set(15, -11)
exposure_low = True

font= cv2.FONT_HERSHEY_SIMPLEX

# Distances in inches
ballDiameter = 7

imageWidth = 640.0
imageCenter = imageWidth/2
# FIXME recalculate minArea = 200

def __blur(src, type, radius):
        """Softens an image using one of several filters.
        Args:
            src: The source mat (numpy.ndarray).
            type: The blurType to perform represented as an int.
            radius: The radius for the blur as a float.
        Returns:
            A numpy.ndarray that has been blurred.
        """
        if(type is BlurType.Box_Blur):
            ksize = int(2 * round(radius) + 1)
            return cv2.blur(src, (ksize, ksize))
        elif(type is BlurType.Gaussian_Blur):
            ksize = int(6 * round(radius) + 1)
            return cv2.GaussianBlur(src, (ksize, ksize), round(radius))
        elif(type is BlurType.Median_Filter):
            ksize = int(2 * round(radius) + 1)
            return cv2.medianBlur(src, ksize)
        else:
            return cv2.bilateralFilter(src, -1, round(radius), round(radius))

def __hsv_threshold(input, hue, sat, val):
        """Segment an image based on hue, saturation, and value ranges.
        Args:
            input: A BGR numpy.ndarray.
            hue: A list of two numbers the are the min and max hue.
            sat: A list of two numbers the are the min and max saturation.
            lum: A list of two numbers the are the min and max value.
        Returns:
            A black and white numpy.ndarray.
        """
        out = cv2.cvtColor(input, cv2.COLOR_BGR2HSV)
        return cv2.inRange(out, (hue[0], sat[0], val[0]),  (hue[1], sat[1], val[1]))

def __find_blobs(input, min_area, circularity, dark_blobs):
        """Detects groups of pixels in an image.
        Args:
            input: A numpy.ndarray.
            min_area: The minimum blob size to be found.
            circularity: The min and max circularity as a list of two numbers.
            dark_blobs: A boolean. If true looks for black. Otherwise it looks for white.
        Returns:
            A list of KeyPoint.
        """
        params = cv2.SimpleBlobDetector_Params()
        params.filterByColor = 1
        params.blobColor = (0 if dark_blobs else 255)
        params.minThreshold = 10
        params.maxThreshold = 220
        params.filterByArea = True
        params.minArea = min_area
        params.filterByCircularity = True
        params.minCircularity = circularity[0]
        params.maxCircularity = circularity[1]
        params.filterByConvexity = False
        params.filterByInertia = False
        detector = cv2.SimpleBlobDetector_create(params)
        return detector.detect(input)

def findClosestBall(keypoints):
    # keypoints is a list of the raw keypoints, not keypoints.pt
    # Returns index of the closest ball
    indexCounter = 0
    closestBall = 0
    if len(keypoints) > 1:
        for i in keypoints:
            if i.size > closestBall:
                closestBall = indexCounter 
                indexCounter += 1
            else:
                indexCounter += 1
        return closestBall
    else:
        return 
        
def turnToBall(ballCoords):
    # FIXME DOESTN WORK
    # Returns whether the robot has to turn right or left to get to the ball
    for i in ballCoords:
        if i[0] < imageCenter-5:
            # Turn left
            return 0
        elif i[0] > imageCenter+5:
            # Turn right
            return 2
        else:
            # Drive forward
            return 1

print('Hi')
while True:
    ret, frame = cap.read()
    
    frame2 = __blur(frame, BlurType.Box_Blur, 14.414414414414415)
    #frame2 = cv2.GaussianBlur(frame1,(14,14),cv2.BORDER_DEFAULT)

    hsv_threshold_hue = [12.949640287769784, 36.06060606060607]
    hsv_threshold_saturation = [100.915467625899275, 207.77777777777777]
    hsv_threshold_value = [150.55395683453237, 255.0]
    frame3 = __hsv_threshold(frame2, hsv_threshold_hue, hsv_threshold_saturation, hsv_threshold_value)
    #frame3 = cv2.inRange(frame2, (hsv_threshold_hue[0], hsv_threshold_saturation[0], hsv_threshold_value[0]),  (hsv_threshold_hue[1], hsv_threshold_saturation[1], hsv_threshold_value[1]))

    find_blobs_min_area = 0.0
    find_blobs_circularity = [0.0, 1.0]
    find_blobs_dark_blobs = False

    keypoints = __find_blobs(frame3, find_blobs_min_area, find_blobs_circularity, find_blobs_dark_blobs)
    
    for i in keypoints:
        print("Keypoints = ", i.pt)
        

    im_with_keypoints = cv2.drawKeypoints(frame3, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    print("Keypoints = ", keypoints)

    frame4 = im_with_keypoints

    cv2.imshow("Filtering", frame4)

    k = cv2.waitKey(1)
    if  k == 27:
        break  # esc to quit
    elif k == 13:
        if exposure_low:
            cap.set(cv2.CAP_PROP_EXPOSURE, -6)
        else:
            cap.set(cv2.CAP_PROP_EXPOSURE, -11)
        exposure_low = not exposure_low