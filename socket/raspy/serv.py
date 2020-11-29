import socket
import pickle
import cv2

pic = pickle.dumps('taki.png')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IPアドレスとポートを指定
    s.bind(('127.0.0.1', 50007))
    # 接続
    s.listen(1)
    # connection待
    while True:
        # アクセス時コネクションとアドレス交換
        conn, addr = s.accept()
        with conn:
            while True:
                # データを受け取る
                data = conn.recv(1024)
                if not data:
                    break
                print('data : {}, addr: {}'.format(data, addr))
                # conn.sendall(b'Received: ' + data)
                conn.sendall(b'Received:'+pic)
print('end')
