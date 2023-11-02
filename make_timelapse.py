import math
import cv2
import os
import time
from colorama import init
init(autoreset=True)
from colorama import Cursor
from termcolor import colored

# Input folder containing the images
input_folder = "./downloaded-images-outside/cam-out/"

# Output video file name and properties
output_video = "timelapse-outside.mp4"
frame_rate = 60  # Adjust as needed
frame_size = (3280, 2464)  # Adjust as needed
use_every_nth_frame = 50

# List all image files in the input folder
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
image_files = image_files[::use_every_nth_frame]


print(f"Found {len(image_files)} files")
# Sort the image files by their names (assuming the names represent the order)
image_files.sort()

# Initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use the appropriate codec
out = cv2.VideoWriter(output_video, fourcc, frame_rate, frame_size)

# Loop through the image files and add them to the video
time_start = time.time()
display_width = 83
print_every_nth_frame = math.ceil(min(50, len(image_files)/(display_width-4)))
for index, image_file in enumerate(image_files):
    if ((index % print_every_nth_frame == 0 or index == 1) or index == (len(image_files)-1)):
        print("="*int((display_width)//2 -11), end="")
        print(f" {index+1:^10d}/{len(image_files):^10d} ", end="")
        print("="*int((display_width)//2 -11))
        current_time = time.time()
        time_passed = current_time - time_start # Seconds passed
        fraction_complete = (index+1)/len(image_files) # 0-1
        time_left = time_passed/fraction_complete - time_passed
        print(f"  Process has taken ", 
              colored(f"{time_passed/60:8.1f}m", 'cyan'),
              f". Estimated {time_left:8.1f}s (",
              colored(f"{time_left/60:8.1f}min", 'green'),
              f") ({time_left/3600:8.1f}h) left", sep="")
        
        # Prog-bar
        print(" [", end="")
        bar_width = display_width-4
        print(colored("#", "yellow")*math.ceil(bar_width*fraction_complete), end="")
        print(colored(" ", "white")*math.floor(bar_width*(1-fraction_complete)), end="")
        print("] ")
        print("="*display_width)
        print(Cursor.UP(5))

    image_path = os.path.join(input_folder, image_file)
    frame = cv2.imread(image_path)
    out.write(frame)


print()
print()
print()
print()
print()

print(f"Process took ", colored(f"{time_passed/60:8.1f}m", 'cyan'),)
# Release the video writer
out.release()

# Clean up
cv2.destroyAllWindows()

print(f"Timelapse video '{output_video}' has been created.")
