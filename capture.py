import time
import picamera

# Set the interval (in seconds) for capturing images
interval = 5  # Change this to your desired interval

# Set the path where you want to save the captured images
output_directory = "./cam-out"

def capture_image():
    with picamera.PiCamera() as camera:
        # You can configure camera settings here, e.g., camera.resolution, camera.annotate_text, etc.
        camera.resolution = (640, 480)
        camera.annotate_text = "Captured at %s" % time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Capture an image and save it with a timestamp
        image_name = f"{output_directory}/image_{int(time.time())}.jpg"
        camera.capture(image_name, quality=50)
        print(f"Captured {image_name}")

if __name__ == "__main__":
    try:
        while True:
            capture_image()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Image capture stopped.")
