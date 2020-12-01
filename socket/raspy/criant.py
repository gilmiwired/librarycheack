import socket
import cv2
import io
from PIL import Image

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
    s.connect(('127.0.0.1', 50007))
    # サーバにメッセージを送る
    s.sendall(b'hello mother fuckin beach')
    # ネットワークのバッファサイズは1024。
    data = s.recv(1024)
#im = Image.open(io.BytesIO(data))
#im.save("logo_py.png", colors=255)
#cv2.imshow('test', im)
#cv2.waitKey()
#cv2.destroyAllWindows()
#print(im.shape)
