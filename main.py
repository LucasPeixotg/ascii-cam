import cv2

# define a video capture object
vid = cv2.VideoCapture(0)

def process_image(raw_image):
    # Input size
    height, width = raw_image.shape[:2]
    # Desired "pixelated" size
    w, h = (90, 60)

    temp = cv2.resize(raw_image, (w, h), interpolation=cv2.INTER_LINEAR)

    pixelated_image = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    processed_image = cv2.cvtColor(pixelated_image, cv2.COLOR_BGR2GRAY)

    return processed_image

while(True):

    # Capture the video frame
    # by frame
    ret, raw_frame = vid.read()

    processed_frame = process_image(raw_frame)

    # Display the resulting frame
    cv2.imshow('frame', processed_frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()