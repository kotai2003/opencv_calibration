import cv2

def main():

    cap = cv2.VideoCapture(0)

    num = 0

    while cap.isOpened():

        succes, img = cap.read()

        k = cv2.waitKey(5)

        if k == 27 or  k == ord('q'):
            break
        elif k == ord('s'): # wait for 's' key to save and exit
            cv2.imwrite('./images/img' + str(num) + '.png', img)
            print("image saved!")
            num += 1

        cv2.imshow("Press S to Capture images while changing the position of the checkerboard",img)

    # Release and destroy all windows before termination
    cap.release()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()