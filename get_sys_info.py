# -*- coding: utf-8 -*-
# author: cwx520375 
# time: 2019/1/2


import os
import cv2
import csv
import sys
import time
import psutil
import logging
import threading
import subprocess
import numpy as np
from PIL import ImageGrab


class Timer(object):
    def __init__(self, start=None):
        self.start = start if start is not None else time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_val is None

    def cost(self):
        print(time.time() - self.start)


def get_sys_memory():
    v_mem = psutil.virtual_memory()
    # s_men = psutil.swap_memory()
    men_percent = v_mem.percent
    # print(s_men)
    print("内存使用率: %s %%" % men_percent)


def get_sys_cpu():
    # cpu = psutil.cpu_percent(0.5, percpu=True)
    cpu_percent = psutil.cpu_percent(interval=2)
    #print(cpu)
    print("CPU使用率: %s %%" % cpu_percent)


def save_desktop(video_path):
    """
    python + opencv 实现屏幕录制_by-_Zjh_
    """
    p = ImageGrab.grab()  # 获得当前屏幕
    k = np.zeros((200,200), np.uint8)
    a, b = p.size  # 获得当前屏幕的大小
    fc = cv2.VideoWriter_fourcc(*'XVID')  # 编码格式
    video = cv2.VideoWriter(video_path, fc, 16, (a, b))  # 输出文件命名为test.mp4,帧率为16，可以自己设置
    while True:
        im = ImageGrab.grab()
        imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)  # 转为opencv的BGR格式
        video.write(imm)

        cv2.imshow('imm', k)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()


def main():
    path = r"D:"
    time_file = str(time.strftime("%Y%m%d%H%M", time.localtime()))
    file_name = time_file + "pc助手"
    file_path = os.path.join(path, file_name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    csv_path = os.path.join(file_path, "sys_info.csv")  # r"C:\sys_info.csv"
    video_path = os.path.join(file_path, "desktop.avi")
    event_log_path = os.path.join(file_path, "event.log")
    # timeout = input("系统资源监控截止时间（格式：hh:mm）: ")
    start_save_server(video_path)
    start_server(csv_path, event_log_path, "notepad++.exe")
    # if time.strftime('%H:%M', time.localtime()) == timeout:
    #     sys.exit()


def get_sys_info(csv_path):
    print(csv_path)
    csv_file = open(csv_path, "w")
    writer = csv.writer(csv_file)
    writer.writerow(["Date", "Used_memory", "Total_memory", "memory_percent", "cpu_count", "cpu_percent"])
    csv_file.close()
    while True:
        #  获取系统资源
        sys_info_list = []
        timestamp = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
        sys_info_list.append(timestamp)
        info = psutil.virtual_memory()
        used_memory = psutil.Process(os.getpid()).memory_info().rss
        sys_info_list.append(used_memory)
        total_memory = info.total
        sys_info_list.append(total_memory)
        memory_percent = info.percent
        sys_info_list.append(memory_percent)
        cpu_count = psutil.cpu_count()
        sys_info_list.append(cpu_count)
        cpu_percent = psutil.cpu_percent(interval=2)
        sys_info_list.append(cpu_percent)
        #  每3s读取一次
        time.sleep(3)
        #  写入csv文件
        csv_file = open(csv_path, "at+", newline='')
        writer = csv.writer(csv_file)
        writer.writerow(sys_info_list)
        csv_file.close()
        time.sleep(2)
        print("get_sys_info is running")
        # print(time.strftime('%H:%M', time.localtime()))
        # print(timeout1)
        # if time.strftime('%H:%M', time.localtime()) == timeout1:
        #     break


def get_event(event_log_path, process_name):
    print("get_event is running")
    try:
        time.sleep(0.5)
        log_format = "%(asctime)s - %(levelname)s - %(message)s"
        date_format = "%m/%d/%Y %H:%M:%S"
        logging.basicConfig(filename=event_log_path, level=logging.DEBUG, format=log_format, datefmt=date_format)
        name_list = []
        pl = psutil.pids()
        pid_list = list(pl)
        for pid in pl:
            name_list.append(psutil.Process(pid).name())
        if process_name in name_list:
            num_index = name_list.index(process_name)
            pid = pid_list[num_index]
            p = psutil.Process(pid)
            #  获取进程状态
            pid_status = p.status()
            #  获取进程使用的内存
            pid_memory = p.memory_info().rss
            #  获取进程使用内存占比
            pid_memory_percent = p.memory_percent(memtype="rss")
            logging.info("%s is exist" % process_name)
            logging.info("pid_status：%s " % pid_status)
            logging.info("pid_used_memory：{}".format(pid_memory))
            logging.info("pid_memory_percent: %d" % pid_memory_percent)
        else:
            logging.info("%s is not exist" % process_name)
    except EOFError:
        logging.ERROR("error")
    finally:
        get_event(process_name, event_log_path)


def start_server(csv_path, event_log_path, process_name):
    server_get_sys_info = threading.Thread(target=get_sys_info, args=(csv_path,))  # , daemon=True
    server_get_sys_info.start()
    server_get_event = threading.Thread(target=get_event, args=(event_log_path, process_name,))  # , daemon=True
    server_get_event.start()
    # server_save_desktop = threading.Thread(target=save_desktop, args=(video_path,))  # , daemon=True
    # server_save_desktop.start()


def start_save_server(video_path):
    server_save_desktop = threading.Thread(target=save_desktop, args=(video_path,))
    server_save_desktop.start()


if __name__ == "__main__":
    main()
    #  with Timer() as timer:
    #     main()
    #  timer.cost()qq
