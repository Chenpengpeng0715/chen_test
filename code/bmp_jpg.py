#-*- coding:utf-8 -*-
import os
import cv2
from natsort import natsorted
from PIL import Image
#将RGB图的bmp格式改成jpg的格式
def main():
	path = r"C:\Users\c00442413\Desktop\4"
	for root, dirs, files in os.walk(path):
		filelist = natsorted(files)
		for file in files:
			if "RGB" in file:
				name = file.split(".")[-2]
				print(name)
				img = cv2.imread(os.path.join(root, file))
				print(file.replace(".bmp", ".jpg"))
				new_name = file.replace(".bmp", ".jpg")
				print("1")
				cv2.imwrite(os.path.join(root, new_name), img)
				print("3")
				os.remove(os.path.join(root, file))
	
if __name__ == "__main__":
	main()