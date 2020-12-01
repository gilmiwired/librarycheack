import socket
import cv2
import io
from PIL import Image


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IPアドレスとポートを指定
    s.bind(('127.0.0.1', 50007))
    # 接続
    s.listen(1)
    # connection待
    while True:
        # アクセス時コネクションとアドレス交換
        conn, addr = s.accept()

        pic = Image.open("taki.png")
        with io.BytesIO() as output:
            pic.save(output,format="PNG")
            picb = output.getvalue()#バイナリ取得

        with conn:
            while True:
                # データを受け取る
                data = conn.recv(1024)
                if not data:
                    break
                print('data : {}, addr: {}'.format(data, addr))
                # conn.sendall(b'Received: ' + data)
                conn.sendall(b'Received:'+picb)
print('end')
