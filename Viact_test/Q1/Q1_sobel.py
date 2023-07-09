import cv2 
import numpy as np

def OpeningRectangle(region,Width,Height):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ksize = (Width, Height))
    regionErosion = cv2.erode(region, kernel,iterations = 1, borderType = cv2.BORDER_DEFAULT, borderValue = 0)
    RegionOpening = cv2.dilate(regionErosion, kernel,  borderType = cv2.BORDER_DEFAULT, borderValue = 0)
    return RegionOpening

def SelectShapeAreaAndUnion(Region, minArea, maxArea):
    numLabels, labels, stats, centroids = cv2.connectedComponentsWithStats(Region, 8, cv2.CV_32S)
    h, w = Region.shape

    SelectedRegion = np.zeros((h, w), np.uint8)
    if numLabels <= 1:
        return SelectedRegion, 0

    areas = list(stats[:,4])

    # top,left,width,heigth, area
    numObj = 0
    for i in range(1, numLabels):
        if areas[i] <= maxArea and areas[i] >= minArea:
            ObjectSelected = np.array(labels, dtype=np.uint8)

            ObjectSelected[i == labels] = 255
            ObjectSelected[i != labels] = 0
            SelectedRegion = cv2.bitwise_or(ObjectSelected, SelectedRegion)
            numObj += 1
    return SelectedRegion, numObj

def FillUp(Region):
    im_floodfill = cv2.copyMakeBorder(Region, 1, 1, 1, 1, cv2.BORDER_CONSTANT, 0)

    h, w = im_floodfill.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)

    cv2.floodFill(im_floodfill, mask, (0,0), 255, flags = 4)
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    im_floodfill_inv = im_floodfill_inv[1:(1 + Region.shape[0]), 1:(1 + Region.shape[1])]

    RegionFillUp = Region | im_floodfill_inv
    return RegionFillUp

def sobel(img):
    scale = 1 ;delta = 0 ;ddepth =  cv2.CV_32F
    
    gray_clone = img.copy()
    
    grad_x = cv2.Sobel(gray_clone, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    grad_y = cv2.Sobel(gray_clone, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)

    sobelx2 = cv2.multiply(grad_x, grad_x)
    sobely2 = cv2.multiply(grad_y, grad_y)
    sobel2 = cv2.addWeighted(sobelx2, 1, sobely2, 1, 0)
    
    sobel = np.floor(cv2.sqrt(sobel2)*1)
    sobel = sobel.astype(np.uint8)
    return sobel

def threshold_range(img,t1, t2):
    _,threshold1 =cv2.threshold(img,t1,255,cv2.THRESH_BINARY_INV)
    _,threshold2 =cv2.threshold(img,t2,255,cv2.THRESH_BINARY_INV)

    return cv2.bitwise_xor(threshold2,threshold1)

