# -*- coding: utf-8 -*-
import time
from multiprocessing.managers import BaseManager
import datetime


class QueueManager(BaseManager):
    pass


def connect_camera():
    QueueManager.register("get_result_queue")
    manager = QueueManager(address=("127.0.0.1", 5002), authkey=b"abc")
    manager.connect()
    # task = manager.get_task_queue()
    result = manager.get_result_queue()
    return result


def camera_screenshot(img_path='test.jpeg'):
    result = connect_camera()
    result.put(('photo', img_path))


def camera_video(video_path='E:\\captureScreen\\camera_%s.avi' % datetime.datetime.now().strftime('%Y%m%d%H%M%S')):
    result = connect_camera()
    result.put(('video', video_path))
    time.sleep(300)
    result.put(('video_end',))


def connect_sysinfocontrol():
    QueueManager.register("get_task_queue")
    manager = QueueManager(address=("127.0.0.1", 5002), authkey=b"abc")
    manager.connect()
    task = manager.get_task_queue()
    return task


def send_sysinfo():
    task = connect_sysinfocontrol()
    task.put('message!')


if __name__ == '__main__':

    print('1 screenshot')
    camera_screenshot('1.jpeg')
    print('test video')
    camera_video()
    print('2 screenshot')
    camera_screenshot('2.jpeg')


    #send_sysinfo()
