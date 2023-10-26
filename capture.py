import time
import picamera

# Set the interval (in seconds) for capturing images
interval = 144  # Change this to your desired interval

# Set the path where you want to save the captured images
output_directory = "./cam-out"

def capture_image(camera):
    # You can configure camera settings here, e.g., camera.resolution, camera.annotate_text, etc.
    
    # Capture an image and save it with a timestamp
    image_name = f"{output_directory}/image_{time.strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
    camera.capture(image_name, quality=50)
    print(f"Captured {image_name}")

if __name__ == "__main__":
    camera = picamera.PiCamera()
    camera.resolution = (3280, 2464)
    camera.exposure_mode = "auto"
    time.sleep(2)  # Wait for 2 seconds to stabilize exposure

    try:
        while True:
            start_time = time.time()
            capture_image(camera)
            end_time = time.time()
            execution_time = end_time - start_time

            # Calculate the remaining time for the interval
            remaining_time = max(0, interval - execution_time)
            time.sleep(remaining_time)
    except KeyboardInterrupt:
        print("Image capture stopped.")
