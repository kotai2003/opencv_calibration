import numpy as np
import cv2 as cv
import pickle

# Load the saved calibration data
with open('./calib_files/calibration.pkl', 'rb') as f:
    cameraMatrix, dist = pickle.load(f)

# Load frame size from file
with open('./calib_files/frameSize.pkl', 'rb') as f:
    frameSize = pickle.load(f)
    print(f"Loaded frame size: {frameSize}")

# Load object points and image points for reprojection error calculation
with open('./calib_files/objpoints.pkl', 'rb') as f:
    objpoints = pickle.load(f)
with open('./calib_files/imgpoints.pkl', 'rb') as f:
    imgpoints = pickle.load(f)

# Load rvecs and tvecs for reprojection error calculation
with open('./calib_files/rvecs.pkl', 'rb') as f:
    rvecs = pickle.load(f)
with open('./calib_files/tvecs.pkl', 'rb') as f:
    tvecs = pickle.load(f)

# Load test image for undistortion
img = cv.imread('./test_images/test-image.png')
h, w = img.shape[:2]

# Get new optimal camera matrix
newCameraMatrix, roi = cv.getOptimalNewCameraMatrix(cameraMatrix, dist, (w, h), 1, (w, h))

# Undistort the image
dst = cv.undistort(img, cameraMatrix, dist, None, newCameraMatrix)

# Crop the image based on the region of interest (roi)
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]

# Alternative method using remapping
mapx, mapy = cv.initUndistortRectifyMap(cameraMatrix, dist, None, newCameraMatrix, (w, h), 5)
dst_remap = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)

# Crop the remapped image
dst_remap = dst_remap[y:y+h, x:x+w]

# Show the original image
cv.imshow('Original Image', img)

# Show the undistorted image
cv.imshow('Undistorted Image', dst)

# Show the remapped image
cv.imshow('Remapped Image', dst_remap)

# Wait indefinitely until a key is pressed
cv.waitKey(0)

# Close all the windows
cv.destroyAllWindows()

# Repro
