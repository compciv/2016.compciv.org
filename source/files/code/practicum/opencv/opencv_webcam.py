from os.path import exists, join
from os import makedirs
import cv2
import requests
DATA_DIR = 'tempdata'
makedirs(DATA_DIR, exist_ok=True)
CASCADE_FILENAME = join(DATA_DIR, "altfacecascade.xml")
SOURCE_CASCADE_URL = 'http://stash.compciv.org.s3.amazonaws.com/opencv/haarcascades/haarcascade_frontalface_alt.xml'
if not exists(CASCADE_FILENAME):
# download the cascade file
    print("Downloading", SOURCE_CASCADE_URL)
    resp = requests.get(SOURCE_CASCADE_URL)
    with open(CASCADE_FILENAME, 'w') as f:
        f.write(resp.text)
        print("Downloaded to", CASCADE_FILENAME)

the_cascade = cv2.CascadeClassifier(CASCADE_FILENAME)
# start the camera
video_capture = cv2.VideoCapture(0)
# infinite loop
while True:
    # Capture frame-by-frame
    ret, videoframe = video_capture.read()

    gray_frame = cv2.cvtColor(videoframe, cv2.COLOR_BGR2GRAY)
    detected_objs = the_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,
        minNeighbors=2,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in detected_objs:
        cv2.rectangle(videoframe, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', videoframe)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
