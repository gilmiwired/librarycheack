#!/usr/bin/env python
import time
import os
import sys
import datetime
import subprocess
from multiprocessing import Process

def run_proc():
    #時間取得
    a=datetime.datetime.now()
    b=a.hour*100+a.minute
    print('現在時刻は',a.hour,'時',a.minute,'分です。')

    #撮影命令
    #subprocess.call(["fswebcam","{}.jpg".format(b),"-q"])

#デーモン化
def daemonize():
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc)
    print('start child process.')
    p.start()
    p.join()
    print('end child process.')

if __name__ == '__main__':
    while True:
        daemonize()
        time.sleep(60)
