import cv2
import vlc
import time
import rtsp

stream1 = 'rtsp://admin:DS-2CD206@192.168.29.32'
stream2 ='rtsp://192.168.29.73:8554/vlcc'
#with rtsp.Client(stream) as client:
#    time.sleep(1)
#    client.preview()


def read_frames_using_vlc(player, delay_time, cam_id, base_path):
    player.play()  # --> play
    if player.is_playing():
        time.sleep(delay_time)
        player.video_take_snapshot(0, base_path + str(cam_id) + '.jpg', 0, 0)
        return True
    else:
        return False

def fender_coordi(path_):
    print('Fender_Reference_image ',path_)
    fender_ref = cv2.imread(path_)  # ---> H=400, W=500
    lst_x = []
    lst_y = []
    for i in range(fender_ref.shape[0]):  # ----> Height
        for j in range(fender_ref.shape[1]):  # ----> Width
            if fender_ref[i, j, 0] > 20:
                lst_x.append(j)
                lst_y.append(i)
    min_x = min(lst_x)
    max_x = max(lst_x)
    min_y = min(lst_y)
    max_y = max(lst_y)

    # fender_ref = cv2.circle(fender_ref, (min_x,min_y), radius=5, color=(255, 0, 255), thickness=3)
    # fender_ref = cv2.circle(fender_ref, (max_x,max_y), radius=5, color=(156, 0, 167), thickness=3)
    return fender_ref, min_x,min_y, max_x, max_y


def check_for_overlap(rec1_x1, rec1_y1, rec1_x2, rec1_y2, rec2_x1, rec2_y1, rec2_x2, rec2_y2):
    rectangle_a = {"x1":rec1_x1, "y1":rec1_y1, "x2":rec1_x2,"y2":rec1_y2}   # ----> det
    rectangle_b = {"x1": rec2_x1, "y1":rec2_y1, "x2":rec2_x2,"y2":rec2_y2}  # ----> fender

    # from Left
    if rectangle_a["y1"] < rectangle_b["y2"] and rectangle_a["x2"] > rectangle_b["x1"]:
        print("OVERLAP from LEFT ! ")
        return True
    else:
        print("there is no overlap")
        return False

def read_frames_rtsp_lib(url, obj_client):
    #with rtsp.Client(rtsp_server_uri = url) as client:
    time.sleep(2)
    #while True:
    _image = obj_client.read(raw=True)
    return _image

#while True:
#    client = rtsp.Client(rtsp_server_uri=stream2)
#    img = read_frames_rtsp_lib(stream1, client)
#    print(type(img))



#a,b,c = read_frames_using_vlc()

