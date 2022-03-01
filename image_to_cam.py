import pyvirtualcam
import cv2
import sys
import numpy as np


def main(path, mirror):
    frame = cv2.imread(path)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if mirror:
        frame = np.fliplr(frame)
    width = frame.shape[1]
    height = frame.shape[0]
    cam = pyvirtualcam.Camera(width=width, height=height, fps=20)
    while True:
        cam.send(frame)
        cam.sleep_until_next_frame()
    
if __name__ == "__main__":
    path = "media/images/1.jpeg"
    mirror = True
    if len(sys.argv) == 2 :
        path = sys.argv[1]
    print(path)
    main(path, mirror)