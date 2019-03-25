#-*- coding: UTF-8 -*-
import os
import shutil
#检索出重复的ID

def main():
	root = os.getcwd()
	root_path = r"D:\fanyifu\face_database\aboard\white"
	dest_path = r"D:\fanyifu\repeat"
	path = os.path.join(root, "result.txt")
	fin = open(path, 'r')
	line_result = []
	result = []
	count = []
	flag = 0
	for line in fin:
		if line.find("pic") != -1 and line.find("isNoFace") != -1:
			pic = line.split('/')
			pic_1 = pic[3]
			file_path = os.path.join(root_path, pic[3])
			pic_image = pic[4]
			pic_bmp = pic[4].split(',')[0]
			pic_short = os.path.splitext(pic_bmp)[0] + '.short'
			filename_bmp = os.path.join(file_path, pic_bmp)
			filename_short = os.path.splitext(filename_bmp)[0] + '.short'
			file_path = os.path.join(root_path, pic_1)
			file_image_path = os.path.join(file_path, pic_image)
			continue
		if line.find("template") != -1 and line.find("isNoFace") != -1:
			temp_1 = line.split('/')
			temp = temp_1[3]
			temp_image = temp_1[4]
			temp_path = os.path.join(dest_path, temp)
			bmp_newpath = os.path.join(temp_path, temp)
			if not os.path.exists(temp_path):
				os.makedirs(temp_path)
			if not os.path.exists(os.path.join(temp_path, "template")):
				os.makedirs(os.path.join(temp_path, "template"))
			if (os.path.exists(filename_bmp) and os.path.exists(filename_short)) and (not os.path.exists(os.path.join(bmp_newpath, temp_image))):
				shutil.copy(filename_bmp, bmp_newpath)
				shutil.copy(filename_bmp, temp_path)
			continue
		if line.find("result") != -1 and line.find("FAR") != -1:
			flag = 0
	fin.close()

if __name__ == '__main__':
    main()