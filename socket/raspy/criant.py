import socket
import pickle
import cv2

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
    s.connect(('127.0.0.1', 50007))
    # サーバにメッセージを送る
    s.sendall(b'hello mother fuckin')
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
    data = s.recv(1024)
    #
    #print(repr(data))
	im = cv2.imread(pickle.loads(data))
	cv2.imshow('test', im)
	cv2.waitKey()
	cv2.destroyAllWindows()

	print(im.shape)
