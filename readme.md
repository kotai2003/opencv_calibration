# Camera Calibration with OpenCV

This repository contains scripts for performing **camera calibration** using OpenCV. Camera calibration is an essential process in computer vision to correct the distortion introduced by camera lenses and to extract accurate information from images captured by the camera. The scripts in this repository will help you to:
1. Capture images from a camera for calibration.
2. Perform camera calibration using a chessboard pattern.
3. Apply distortion correction to images or real-time webcam feed using the calibration results.

## Table of Contents
- [Overview](#overview)
- [Camera Calibration Process](#camera-calibration-process)
- [Included Scripts](#included-scripts)
  - [00.getimages.py](#00getimagespy)
  - [01.calibration.py](#01calibrationpy)
  - [02.undistort_image.py](#02undistort_imagepy)
  - [03.undistort_webcam.py](#03undistort_webcampy)
- [Requirements](#requirements)
- [How to Use](#how-to-use)
- [License](#license)

## Overview

### Camera Calibration Purpose
Camera calibration is used to estimate the **camera parameters** such as focal length, principal point, and distortion coefficients. These parameters allow us to correct image distortion caused by the lens and accurately map 3D points to 2D points in the image.

### Why is Camera Calibration Important?
- **Correcting lens distortion**: Lenses, especially wide-angle lenses, introduce distortion that can bend straight lines in images. Calibration helps to correct this distortion.
- **Accurate 3D reconstruction**: In applications like 3D scanning or stereo vision, accurate camera parameters are crucial for reliable 3D data.
- **AR Applications**: Augmented reality applications require precise camera calibration to accurately project virtual objects into the real world.

### Applications that Require Camera Calibration
- Robotics and autonomous vehicles
- Augmented reality (AR)
- 3D reconstruction and modeling
- Medical imaging systems (e.g., endoscopy)
- Industrial vision systems

## Camera Calibration Process

1. **Image Capture**: Capture multiple images of a known pattern (such as a chessboard) from different angles.
2. **Corner Detection**: Detect the corners of the chessboard in the images.
3. **Calibration**: Use the detected corners and the known physical dimensions of the chessboard to calculate the camera's intrinsic and extrinsic parameters.
4. **Undistortion**: Apply the calibration parameters to correct the distortion in captured images or video feeds.

## Included Scripts

### 00.getimages.py
This script captures images from a webcam and saves them for camera calibration. It also retrieves and saves the camera's resolution (`frameSize`) for use in calibration and undistortion processes.

- Press `s` to capture and save images.
- Press `q` or `ESC` to quit.

### 01.calibration.py
This script performs camera calibration using the captured chessboard images. It calculates the intrinsic parameters (camera matrix), distortion coefficients, and extrinsic parameters (rotation and translation vectors).

- It uses the images saved by `00.getimages.py`.
- The calculated calibration data is saved to files for later use.

### 02.undistort_image.py
This script applies the camera calibration results to an image to correct distortion. The undistorted image is displayed along with the original image for comparison.

- The calibration data saved by `01.calibration.py` is used for distortion correction.
- You can provide any image to apply distortion correction.

### 03.undistort_webcam.py
This script applies the camera calibration results in real-time to a webcam feed. It shows both the original and undistorted video frames side by side.

- Useful for applications like AR or real-time video processing with calibrated camera settings.

## Requirements

To use the scripts in this repository, you'll need to have the following installed:

- Python 3.x
- OpenCV (`opencv-python`, `opencv-contrib-python`)
- Numpy
- Pickle (standard Python library)

You can install OpenCV and Numpy using pip:

```bash
pip install opencv-python opencv-contrib-python numpy
```

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/camera-calibration-opencv.git
   cd camera-calibration-opencv
   ```

2. **Capture Images**:
   Run the `00.getimages.py` script to capture images for calibration:

   ```bash
   python 00.getimages.py
   ```

   Press `s` to capture images of a chessboard at different angles. These images will be used for calibration.

3. **Perform Camera Calibration**:
   Run the `01.calibration.py` script to calculate the camera parameters based on the captured images:

   ```bash
   python 01.calibration.py
   ```

   The calibration data will be saved for later use.

4. **Undistort an Image**:
   Run the `02.undistort_image.py` script to undistort an image using the saved calibration data:

   ```bash
   python 02.undistort_image.py
   ```

   This will display the original and undistorted images side by side.

5. **Undistort Webcam Feed in Real-time**:
   Run the `03.undistort_webcam.py` script to correct the distortion in the live webcam feed:

   ```bash
   python 03.undistort_webcam.py
   ```

   This will show both the original and corrected video feed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



