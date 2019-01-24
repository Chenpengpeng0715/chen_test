# -*- coding: utf-8 -*-
import cv2 as cv
import datetime
import time
from multiprocessing import Process, Event, Queue
from queue import Queue
from multiprocessing.managers import BaseManager
import psutil

# 任务发送队列
task_queue = Queue()
# 任务结果接受队列
result_queue = Queue()


# 从BaseManager继承
class QueueManager(BaseManager):
    pass


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


def init_camera(queue):
    start = time.clock()
    capture = cv.VideoCapture(0)
    #capture.set(3, 3264)
    #capture.set(4, 2448)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    value = [1]
    out = None
    while True:
        end = time.clock()
        ret, frame = capture.read()
        if ret is True:
            frame = cv.resize(frame, (3264, 2448))
            #cv.imshow("frame", frame)
            cv.waitKey(1)
            if value[0] == 'video_end':
                out.release()
                value = [1]

            if value[0] == 'video':
                if out is None:
                    out = cv.VideoWriter('{}'.format(value[1]), fourcc, 20.0, (3264, 2448))
                out.write(frame)

            if queue.empty():
                continue
            else:
                value = queue.get(True)
                if value[0] == 'photo':
                    cv.imwrite('{}'.format(value[1]), frame)
                    continue
                elif value[0] == 'video':
                    continue
        else:
            out.release()
            capture.release()
            cv.destroyAllWindows()
            break


def init_sysinfo(queue):
    while True:
        if queue.empty():
            continue
        value = queue.get(True)
        print(value)


def multi_control():
    init_p = Process(target=init_camera, args=(result, ))
    init_p.start()
    init_p.join()


def sysinfo_control():
    init_p = Process(target=init_sysinfo, args=(task,))
    init_p.start()
    init_p.join()


if __name__ == '__main__':
    # 讲Queue注册到网络上，callable参数关联了Queue对象
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    manager = QueueManager(address=('127.0.0.1', 5002), authkey=b'abc')
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    multi_control()
    #sysinfo_control()
    manager.shutdown()
