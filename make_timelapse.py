import cv2
import os

# Input folder containing the images
input_folder = "./downloaded-images/cam-out/"

# Output video file name and properties
output_video = "timelapse.mp4"
frame_rate = 60  # Adjust as needed
frame_size = (1360, 768)  # Adjust as needed

# List all image files in the input folder
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

print(f"Found {len(image_files)} files")
# Sort the image files by their names (assuming the names represent the order)
image_files.sort()

# Initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use the appropriate codec
out = cv2.VideoWriter(output_video, fourcc, frame_rate, frame_size)

# Loop through the image files and add them to the video
for image_file in image_files:
    image_path = os.path.join(input_folder, image_file)
    frame = cv2.imread(image_path)
    out.write(frame)

# Release the video writer
out.release()

# Clean up
cv2.destroyAllWindows()

print(f"Timelapse video '{output_video}' has been created.")
