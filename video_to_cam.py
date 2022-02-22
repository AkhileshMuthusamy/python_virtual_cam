import av
import pyvirtualcam
import sys

supported_heights = [360, 720, 1080]

def main(path):
    container = av.open(path)
    height = container.streams[0].codec_context.coded_height 
    width = container.streams[0].codec_context.coded_width
    print(f'Height: {height}')
    
    if height not in supported_heights:
        trimmed_height = 0
        for i in range(len(supported_heights)):
            if height > supported_heights[i]:
                trimmed_height = supported_heights[i]
        
        height = trimmed_height

    cam = pyvirtualcam.Camera(width=width, height=height, fps=20)

    while True:
        container = av.open(path) # reopened the file to loop the video
        stream = container.streams.video[0]
        for frame in container.decode(stream):
            '''
            format: bgr24, rgb24
            '''
            frame = frame.to_ndarray(format='rgb24')
            cam.send(frame)
            cam.sleep_until_next_frame()
        
if __name__ == "__main__":
    path = "media/1.mp4"
    if len(sys.argv) == 2 :
        path = sys.argv[1]
    print(path)
    main(path)