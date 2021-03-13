from read_config import *
from image_codes import *

stream0 = 'D:/darknet_fender_protection/ship/test_data/video2.mp4'  # path1
stream1 = 'rtsp://192.168.29.73:8554/vlc'
stream2 = 'rtsp://admin:DS-2CD206@192.168.29.32'
stream3 = 'rtsp://localhost:8554/stream'
stream4 = 'rtsp://192.168.51.37:8554/streams'
stream5 = 'rtsp://192.168.6.62:8554/stream'

# Method 1 ---- using OPENCV
cap = cv2.VideoCapture(stream3, cv2.CAP_FFMPEG)
ctr = 0
print(cap)
while True and ctr < 20 :
    print(cap.isOpened())
    time.sleep(4)
    ret, frame = cap.read()
    print(ret, type(frame))
    ctr = ctr+1


# Method 2  --------> using vlc
vlc_player_object = vlc.MediaPlayer(stream3)
time.sleep(1)
vlc_player_object.play()
ctr = 0
while (True and ctr<10) or (vlc_player_object.is_playing() and ctr<100):
#while True:
    print(vlc_player_object.is_playing())
    print(ctr)
    time.sleep(2)
    vlc_player_object.video_take_snapshot(0, 'D:/darknet_fender_protection/vlc_stream.jpg', 0, 0)
    ctr = ctr +1
vlc_player_object.pause()
#vlc_player_object.release()
del vlc_player_object


# Method 3 ----------> using RTSP
with rtsp.Client(rtsp_server_uri = stream3) as client:
    ctr = 0
    time.sleep(2)
    while True and ctr < 20:
        time.sleep(4)
        _image = client.read(raw=True)
        ctr+=1
        print(type(_image))
    #return _image

import requests
image_path = 'D:/darknet_fender_protection/vlc_stream.jpg'
notification_url='http://localhost:3011/api/v1/notification/create'
headers = {'x-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQyMzA3ZDZhM2IyMjI2YjgyZmE0MmMiLCJyb2xlIjoiQURNSU4iLCJpYXQiOjE2MTUyODMyMTR9.FPv1C_AELB9UStxx-Jwj5Vax7OgRJr6Rr3sFPRxMa4M'}
files = {'imageUrl': open(image_path, 'rb')}
payload = {'title': "Dummy", 'status': 'threat',
           'type': 'known',
           'siteNumber': '4'}
session = requests.Session()
temp_ = session.post(notification_url, headers=headers, data=payload, files=files)
print(temp_.status_code, temp_.json())