import cv2
import numpy as np

image1 = cv2.imread('image1.jpg', 0)  # Image without an open edge, read as grayscale
image2 = cv2.imread('image2.jpg', 0)  # Image with an open edge, read as grayscale

edge_diff = np.abs(image1 - image2)

threshold = 50  # Threshold to identify open edge positions

binary_edge = np.zeros_like(edge_diff)
binary_edge[edge_diff >= threshold] = 255


cv2.imshow('Open Edge', binary_edge)
cv2.waitKey(0)
cv2.destroyAllWindows()


#cv2.imwrite('open_edge.jpg', binary_edge)