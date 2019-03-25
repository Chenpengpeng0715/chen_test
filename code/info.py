#-*- coding:utf-8 -*-
import os
import shutil
import cv2
from natsort import natsorted

def main():
	path = r"F:\fanyifu\china"
	# move_dir(path)#修改目录结构
	# delete_two_image(path)#删除不需要的图片
	# bmp_jpg(path)#修改RGB→JPG
	# check_image(path)#检查文件尺寸
	check_file_ram(path)#检查文件大小
	# rename_file(path)#重命名图片名
	# delete_file_all(path)#检查IR、depth、RGB是否一一对应
	# add_number(path)#添加图片文件编号
	# generate_template(path)#创建template文件夹，用来放置模板文件
	# move_to_template(path)#移动指定编号的图片到template
	# search(path)#检查template是否为空
def move_dir(path):
	dirs = os.listdir(path)
	for folder in dirs:
		folder_path = os.path.join(path, folder)
		folder_list = os.listdir(folder_path)
		# print(folder_list)
		for folder2 in folder_list:
			words = folder.split('-')
			if words[2].lower() == 'sn' or words[3].lower() == 'sn':
				folder2_new = folder2 + '-indoor'
				shutil.move(os.path.join(folder_path, folder2), os.path.join(path, folder2_new))
			if words[2].lower() == 'sw' or words[3].lower() == 'sw':
				folder2_new = folder2 + '-outdoor'
				shutil.move(os.path.join(folder_path, folder2), os.path.join(path, folder2_new))
				
		os.rmdir(os.path.join(path, folder))
		print("%s move file is completed"%folder_path)
		

def delete_two_image(path):
	for root, dirs, files in os.walk(path):
		for file in files:
			if not (os.path.splitext(file)[1] == ".short" or file.find("IR2D") != -1 or file.find("RGB") != -1):
				os.remove(os.path.join(root, file))
				print("%s delete is completed"%os.path.join(root, file))
		
def bmp_jpg(path):
	for root, dirs, files in os.walk(path):
		filelist = natsorted(files)
		for file in files:
			if "RGB" in file:
				try:
					img = cv2.imread(os.path.join(root, file))
					new_name = file.replace(".bmp", ".jpg")
					cv2.imwrite(os.path.join(root, new_name), img)
					os.remove(os.path.join(root, file))
					print(os.path.join(root, file))
				except:
					print("error:%s"%os.path.join(root, file))
		
def check_image(path):
	for root, dirs, files in os.walk(path):
		for file in files:
			if os.path.splitext(file)[1] == ".bmp": 
				try:
					img = cv2.imread(os.path.join(root, file))
					size = img.shape
					# print("OK")
					if size[0] != "480L" or size[1] != "640L":
						print(os.path.join(root, file))
				except:
					print("opencv error:%s"%os.path.join(root, file))
		print("end")
def check_file_ram(path):
	for root, dirs, files in os.walk(path):
		for file in files:
			file_path = os.path.join(root, file)
			size = os.path.getsize(file_path)
			if size <= 4096:
				os.remove(file_path)
				print(file_path)
			print(file)	
def rename_file(path):
	for root, dirs, files in os.walk(path):
		natsort_file_list = natsorted(files)
		for file in natsort_file_list:
			image_name = os.path.splitext(file)[0]
			file_name = image_name[0:23] + os.path.splitext(file)[1]
			if os.path.exists(os.path.join(root, file_name)) == 0:
				os.rename(os.path.join(root, file), os.path.join(root, file_name))
				print("%s rename completed"%os.path.join(root, file))

def delete_file_all(path):
	for root, dirs, files in os.walk(path):
		filelist = natsorted(files)
		# ir_name = ""
		# depth_name = ""
		for file in filelist:
			if os.path.splitext(file)[1] == ".short":
				ir_name = os.path.splitext(file)[0]
				bmp_name = os.path.splitext(file)[0] + '.bmp'
				jpg_name = os.path.splitext(file)[0] + '.jpg'
				if not os.path.exists(os.path.join(root, bmp_name)) or not os.path.exists(os.path.join(root, jpg_name)):
					print(os.path.join(root, file))
					os.remove(os.path.join(root, file))
			if os.path.splitext(file)[1] == ".bmp":
				depth_name = os.path.splitext(file)[0]
				short_name = os.path.splitext(file)[0] + '.short'
				rgb_name = os.path.splitext(file)[0] + '.jpg'
				if not os.path.exists(os.path.join(root,short_name)) or not os.path.exists(os.path.join(root, rgb_name)):
					print(os.path.join(root, file))
					os.remove(os.path.join(root, file))	
			if os.path.splitext(file)[1] == ".jpg":
				color_name = os.path.splitext(file)[0]
				Short_name = os.path.splitext(file)[0] + '.short'
				Bmp_name = os.path.splitext(file)[0] + '.bmp'
				if not os.path.exists(os.path.join(root,Short_name)) or not os.path.exists(os.path.join(root, Bmp_name)):
					os.remove(os.path.join(root, file))
					print(os.path.join(root, file))
					
					
def add_number(path):
	dirs = os.listdir(path)
	for folder in dirs:
		folder_path = os.path.join(path, folder)
		tmp = os.listdir(folder_path)
		files = natsorted(tmp)
		cnt = 0
		for file in files:
			if os.path.splitext(file)[1] == ".bmp":
				file_name = os.path.splitext(file)[0] + "_" + str(cnt)
				ir_new = file_name + ".bmp"
				depth_old = os.path.splitext(file)[0] + ".short"
				depth_new = file_name + ".short"
				rgb_old = os.path.splitext(file)[0] + ".jpg"
				rgb_new = file_name + ".jpg"
				os.rename(os.path.join(folder_path, file), os.path.join(folder_path, ir_new))
				os.rename(os.path.join(folder_path, depth_old), os.path.join(folder_path, depth_new))
				os.rename(os.path.join(folder_path, rgb_old), os.path.join(folder_path, rgb_new))
				print("%s add number completed"%os.path.join(folder_path, file))
				cnt += 1
				
def generate_template(path):
	dirs = os.listdir(path)
	for folder in dirs:
		dir_path = os.path.join(path, folder)
		template_dir_path = os.path.join(dir_path, "template")
		print(template_dir_path)
		cmd = "md %s"%template_dir_path
		#cmd = unicode(cmd, encoding='utf-8')
		os.system(cmd)
				
def move_to_template(path):
	for file in os.listdir(path):
		file_path = os.path.join(path, file)
		for name in os.listdir(file_path):
			template_path = os.path.join(file_path, "template")
			if "_0.bmp" in name or "_0.short" in name or "_0.jpg" in name:
				shutil.move(os.path.join(file_path, name), os.path.join(template_path, name))
				print(os.path.join(file_path, name))
				
def search(path):
	for files in os.listdir(path):
		file_path = os.path.join(path, files)
		for file_name in files:
			if os.path.isdir(file_path):
				if not os.listdir(file_path):
					print(file_path)
				

if __name__ == "__main__":
	main()