# -*- coding: utf-8 -*-
from PIL import ImageGrab
import numpy as np
import cv2
import datetime

p = ImageGrab.grab()
k = np.zeros((200, 200), np.uint8)

width, height = p.size
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('E:\\captureScreen\\test_%s.avi' % datetime.datetime.now().strftime('%Y%m%d%H%M%S'), fourcc, 20.0, (width, height))

while True:
    im = ImageGrab.grab()
    imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
    video.write(imm)
    cv2.imshow('imm', k)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
