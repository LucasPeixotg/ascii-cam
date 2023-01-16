import cv2
import os
import math

# define a video capture object
vid = cv2.VideoCapture(0)

def process_image(raw_image, pixel_size):
    raw_height, raw_width = raw_image.shape[:2]

    resized_image = cv2.blur(cv2.resize(raw_image, (raw_width*3, raw_height)), (5,5))

    resized_height, resized_width = resized_image.shape[:2]
    # Input size
    # Desired "pixelated" size
    pixelated_width, pixelated_height = (resized_width // pixel_size, resized_height // pixel_size)

    img_temp = cv2.resize(resized_image, (pixelated_width, pixelated_height), interpolation=cv2.INTER_LINEAR)
    img_pixelated = cv2.resize(img_temp, (resized_width, resized_height), interpolation=cv2.INTER_NEAREST)
    img_pixelated_grey = cv2.cvtColor(img_pixelated, cv2.COLOR_BGR2GRAY)

    return img_pixelated_grey


def intensity_to_ascii(intensity):
    ordered_ascii = " .:-=+*#%@"

    threshold = math.ceil(255 / len(ordered_ascii))
    index = intensity // threshold

    return ordered_ascii[index]

def print_frame(frame, pixel_size):
    os.system('clear')
    row_index = 0
    for row in frame.tolist():
        if row_index % pixel_size == 0:
            col_index = 0
            for col in row:
                if col_index % pixel_size == 0:
                    print(intensity_to_ascii(col), end='')

                col_index+=1
            print('\n')

        row_index += 1

def main():
    while(True):

        # Capture the video frame
        # by frame
        ret, raw_frame = vid.read()

        pixel_size = 12
        processed_frame = process_image(raw_frame, pixel_size)

        #pixel_size = (processed_frame.shape[0] // width, processed_frame.shape[1] // height)
        print_frame(processed_frame, pixel_size)
        
        cv2.imshow('image', processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()