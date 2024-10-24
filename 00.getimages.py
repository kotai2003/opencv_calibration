import cv2
import pickle

def main():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the webcam.")
        return

    # Get frame size (width and height)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frameSize = (width, height)

    # Save frame size to a file
    with open('./calib_files/frameSize.pkl', 'wb') as f:
        pickle.dump(frameSize, f)

    print(f"Frame size {frameSize} saved.")

    num = 0

    while cap.isOpened():

        success, img = cap.read()

        k = cv2.waitKey(5)

        if k == 27 or  k == ord('q'):
            break
        elif k == ord('s'): # wait for 's' key to save and exit
            cv2.imwrite('./images/img' + str(num) + '.png', img)
            print("Image saved!")
            num += 1

        cv2.imshow("Press S to Capture images while changing the position of the checkerboard", img)

    # Release and destroy all windows before termination
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
