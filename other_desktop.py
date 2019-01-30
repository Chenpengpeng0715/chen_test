# -*- coding: utf-8 -*-
# author: cwx520375 
# time: 2019/1/29

import os
import time
import numpy
import cv2
import mss
import mss.tools
import lzma

"""
1. How to get cursor in desktop? get the cursor position then redraw it.
2. Compress the video and audio data after created.

with mss.mss() as sct:
    # 为每个显示器截取一张图片
    # monitor-1.png
    # monitor-2.png
    for filename in sct.save():
        print(filename)

    # 为1号显示器截取一张图片
    filename = sct.shot()
    print(filename)

    # 将所有显示器图像截图并合并到一张图片
    filename = sct.shot(mon=-1, output='fullscreen.png')
    print(filename)

    # 截取2号显示器图像并保存图片
    monitor_number = 2
    mon = sct.monitors[monitor_number]
    sct_img = sct.grab(mon)
    mss.tools.to_png(sct_img.rgb, sct_img.size, output='a.png')

"""


def record_screen():
    with mss.mss() as sct:
        sct.compression_level = 20
        monitor_number = 2
        mon = sct.monitors[monitor_number]
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        timestamp = str(time.strftime("%Y%m%d%H%M", time.localtime()))
        path = r"D:\other_desktop"
        file_path = os.path.join(path, timestamp)
        print(file_path)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        out = cv2.VideoWriter(os.path.join(file_path, 'test.avi'), fourcc, 20.0, (1920, 1080))
        count = 0
        while True:
            count += 1
            last_time = time.time()
            img = numpy.array(sct.grab(mon))
            # numpy.resize(img, (600, 800))
            img = numpy.flip(img[:, :, :3], 2)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            # cv2.imshow("OpenCV/Numpy normal", img)
            cv2.waitKey(1)
            out.write(img)
            # print("fps: {}".format(1 / (time.time() - last_time)))
            #if cv2.waitKey(25) & 0xFF == ord("q"):
            if count > 1000 or cv2.waitKey(25) & 0xFF == ord("q"):
                out.release()
                cv2.destroyAllWindows()
                break
        time.sleep(2)
        record_screen()


if __name__ == '__main__':
    record_screen()
