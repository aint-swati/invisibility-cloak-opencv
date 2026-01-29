"""
Invisibility Cloak using Python and Computer Vision
Creates a Harry Potter-style invisibility effect using a RED colored cloth
"""

import cv2
import numpy as np
import time

def capture_background(cap, num_frames=30):

    #Captures the background by averaging multiple frames
    print("Capturing background! Please move out of the frame")
    print("Background capture will start in 3 seconds")
    time.sleep(3)

    background = None
    for i in range(num_frames):
        ret, frame = cap.read()
        if ret:
            if background is None:
                background = np.float32(frame)
            else:
                cv2.accumulateWeighted(frame, background, 0.5)

        #Shows Progress
        print(f"Capturing frame{i+1}/{num_frames}", end="\r")

    print("\n Background captured succesfully!")
    background = np.uint8(background)
    return background    
        
# Creating a mask for specified color range
def create_colour_mask(frame, lower_range, upper_range):

    # Convert BGR/RGB into HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Creates mask for the color
    mask = cv2.inRange(hsv, lower_range, upper_range)

    # Morphological operations to remove noise and fill gaps
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)

    return mask

def main():

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open WebCam")
        return
    
    # Set camera properties for better performance
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Capture the background
    background = capture_background(cap)

    # Red color has two ranges in HSV (Hue-Saturation-Value)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    print("\n"+"="*50)
    print("INVISIBILITY CLOAK ACTIVATED!")
    print("="*50)
    print("\n Instructions:")
    print(" - Cover yourself with RED cloth to be invisible")
    print(" - Press 'q' to quit")
    print(" - Press 'b' to recapture background")   
    print("="*50+"\n")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame")
            break

        # Flip frame horizontally for mirror effect
        frame=cv2.flip(frame,1)

        # Create masks for red color (two ranges)
        mask1 = create_colour_mask(frame, lower_red1, upper_red1)
        mask2 = create_colour_mask(frame, lower_red2, upper_red2)

        # Combine both masks
        mask = mask1+mask2

        # Invert the mask to get the non-cloak region
        mask_inv = cv2.bitwise_not(mask)

        # Extract the cloak region from background
        cloak_area = cv2.bitwise_and(background, background, mask=mask)
        
        # Extract the non-cloak region from current frame
        non_cloak_area = cv2.bitwise_and   (frame,frame, mask=mask_inv)
        
        # Combine both regions to create the final output
        final_output = cv2.addWeighted(cloak_area,1,non_cloak_area,1,0)

        # Display the results
        cv2.imshow('Invisibility Cloak', final_output)
        cv2.imshow('Original', frame)
        cv2.imshow('Mask',mask)

        # Handle keyboard inputs
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            print("Exiting Application...")
            break
        elif key == ord('b'):
            print("\nRecapturing Background...")
            background = capture_background(cap)

    #Clean up
    cap.release()
    cv2.destroyAllWindows()
    print("Application Closed Successfully")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nApplication Interrupted by User")
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"\nAn Error occurred: {str(e)}")
        cv2.destroyAllWindows()

