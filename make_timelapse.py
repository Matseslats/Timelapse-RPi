import cv2
import os
import time

# Input folder containing the images
input_folder = "./downloaded-images-outside/cam-out/"

# Output video file name and properties
output_video = "timelapse-outside.mp4"
frame_rate = 60  # Adjust as needed
frame_size = (3280, 2464)  # Adjust as needed

# List all image files in the input folder
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

print(f"Found {len(image_files)} files")
# Sort the image files by their names (assuming the names represent the order)
image_files.sort()

# Initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use the appropriate codec
out = cv2.VideoWriter(output_video, fourcc, frame_rate, frame_size)

# Loop through the image files and add them to the video
time_start = time.time()
for index, image_file in enumerate(image_files):
    if ((index % 50 == 0 or index == 10) and index >= 1):
        print("="*33, end="")
        print(f" {index:7d}/{len(image_files):7d} ", end="")
        print("="*33)
        current_time = time.time()
        time_passed = current_time - time_start # Seconds passed
        fraction_complete = index/len(image_files) # 0-1
        time_left = time_passed/fraction_complete
        print(f"  Process has taken {time_passed&60:8.1f}m. Estimated {time_left:8.1f}s ({time_left/60:8.1f}min) ({time_left/3600:8.1f}h) left")
        print("="*83)
        print()
        

    image_path = os.path.join(input_folder, image_file)
    frame = cv2.imread(image_path)
    out.write(frame)

# Release the video writer
out.release()

# Clean up
cv2.destroyAllWindows()

print(f"Timelapse video '{output_video}' has been created.")
