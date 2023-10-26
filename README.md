# Raspberry Pi Timelapse Capturer
Code to turn your raspberry pi and camera module into a timelapse recorder.

## Files
### uploat.bat:
Upload the code to your raspberry pi. Replace the IP address with your Pi's IP.

### download.bat
Download the captured images into a folder of your choice. Replace the IP address with your Pi's IP.

### capture.py
Code to capture the timelaspe. Change this to change how the pictures are taken, the interval, resolution, exposure etc.

### make_timelapse.py
Code to turn the captured images into a timelapse. Cange this to change the output resolution and framerate.


## Commands
Start capturing images:
```bash
nohup python3 capture.py &
```

Stop capturing images:
```bash
ps aux | grep nohup
kill <PID>
```

Count the images captured:
```bash
find ./cam-out/ -type f | wc -l
```

Remove images older than x:
```bash
touch -t 202310251500 /tmp/timestamp
find ./cam-out/ -type f ! -newer /tmp/timestamp -delete
```

Find out how much space the images are taking up:
```bash
du -hs ./cam-out/
```