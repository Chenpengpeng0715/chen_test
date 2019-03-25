#-*- coding:utf-8 -*-
import os
import shutil
import cv2
from natsort import natsorted

def main():
	path_list = []
	template_path_list = []
	for i in range(len(path_list))
		# path = r"D:\fanyifu\face_database\aboard\tmp\tmp\white"
		# template_path = r"D:\fanyifu\face_database_template\aboard\tmp" 
		path = unicode(path, encoding='utf-8')
		path = path_list[i]
		template_path = template_path_list[i]
		# image_shape_path = r"D:\fanyifu\check-image"
		#1、移动文件到path并删除源文件夹
		#2、删除除bmp和short以外格式的图片
		#3、重命名（文件名改成只有时间，保持bmp与short一一对应）
		#4、添加文件编号
		#5、生成模板文件夹
		#6、移动模板文件到模板文件夹
		#7、检查文件是否只有bmp和short和是否没有被重命名（修改完记得再执行检查一遍）
		# move_dir(path)
		# delete_image(path)
		# rename_file(path)
		# delete_file(path)
		# add_number(path)
		# generate_template(path)
		# move_template(path,template_path)
		# 8、检查图片尺寸
		# 9、查找空文件夹
		# check_file(path)
		# check_image(path)
		# search(path)
					
def move_dir(path):
	print(path)
	dirs = os.listdir(path)
	for folder in dirs:
		folder_path = os.path.join(path, folder)
		folder_list = os.listdir(folder_path)
		# print(folder_list)
		for folder2 in folder_list:
			words = folder.split('-')
			if words[2].lower() == 'sn' or words[3].lower() == 'sn':
				folder2_new = folder2 + '-indoor'
			if words[2].lower() == 'sw' or words[3].lower() == 'sw':
				folder2_new = folder2 + '-outdoor'
			shutil.move(os.path.join(folder_path, folder2), os.path.join(path, folder2_new))
		os.rmdir(os.path.join(path, folder))	
		print("%s move file is completed"%folder_path)
		
def delete_image(path):
	for root, dirs, files in os.walk(path):    
		for file in files:                             
			if os.path.splitext(file)[1] != ".short" and file.find("IR2D") == -1:   
				os.remove(os.path.join(root, file))
				print("%s delete is completed"%os.path.join(root, file))
				
def rename_file(path):
	for root, dirs, files in os.walk(path):
		natsort_file_list = natsorted(files)
		for file in natsort_file_list:
			image_name = os.path.splitext(file)[0]
			file_name = image_name[0:23] + os.path.splitext(file)[1]
			if os.path.exists(os.path.join(root, file_name)) == 0:
				os.rename(os.path.join(root, file), os.path.join(root, file_name))
				print("%s rename completed"%os.path.join(root, file))
				
def delete_file(path):
	for root, dirs, files in os.walk(path):
		filelist = natsorted(files)
		ir_name = ""
		depth_name = ""
		for file in filelist:
			if os.path.splitext(file)[1] == ".short":
				ir_name = os.path.splitext(file)[0]
				bmp_name = os.path.splitext(file)[0] + '.bmp'
				if not os.path.exists(os.path.join(root, bmp_name)):
					os.remove(os.path.join(root, file))
			if os.path.splitext(file)[1] == ".bmp":
				depth_name = os.path.splitext(file)[0]
				short_name = os.path.splitext(file)[0] + '.short'
				if not os.path.exists(os.path.join(root,short_name)):
					os.remove(os.path.join(root, file))	
					
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
				os.rename(os.path.join(folder_path, file), os.path.join(folder_path, ir_new))
				os.rename(os.path.join(folder_path, depth_old), os.path.join(folder_path, depth_new))
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

def move_template(path,path_result):
	for folder in os.listdir(path):
		for file in os.listdir(os.path.join(path, folder)):
			template_dir_path = os.path.join(os.path.join(path, folder), "template")
			if os.path.splitext(file)[1] == ".bmp":
				words = os.path.splitext(file)[0].split('_')
				id = int(words[len(words)-1])
				depth_image = os.path.splitext(file)[0] + ".short"
				if id == 0:
					path_template = os.path.join(path_result, "template")
					if not os.path.exists(path_template):
						os.makedirs(path_template)
					bmp_newname = folder + ',' + file 
					depth_newname = folder + ',' + depth_image 
					if not os.path.exists(path_template):
						os.makedirs(path_template)
					folder_path = os.path.join(path, folder)
					shutil.copy(os.path.join(folder_path, file), os.path.join(path_template, bmp_newname))
					shutil.copy(os.path.join(folder_path, depth_image), os.path.join(path_template, depth_newname))
					shutil.move(os.path.join(folder_path, file), os.path.join(template_dir_path, file))
					shutil.move(os.path.join(folder_path, depth_image), os.path.join(template_dir_path, depth_image))
					print("%s is completed"%folder_path)
	
def delete_file(path):
	for root, dirs, files in os.walk(path):
		filelist = natsorted(files)
		ir_name = ""
		depth_name = ""
		for file in filelist:
			if os.path.splitext(file)[1] == ".short":
				ir_name = os.path.splitext(file)[0]
				bmp_name = os.path.splitext(file)[0] + '.bmp'
				if not os.path.exists(os.path.join(root, bmp_name)):
					os.remove(os.path.join(root, file))
			if os.path.splitext(file)[1] == ".bmp":
				depth_name = os.path.splitext(file)[0]
				short_name = os.path.splitext(file)[0] + '.short'
				if not os.path.exists(os.path.join(root,short_name)):
					os.remove(os.path.join(root, file))	
					
def check_image(path):
	# fp = os.path.join(image_shape_path, "result_image_shape.txt")
	# f = open(fp, "a")
	for root, dirs, files in os.walk(path):
		for file in files:
			if os.path.splitext(file)[1] == ".bmp": 
				img = cv2.imread(os.path.join(root, file))
				size = img.shape
				if size[0] != 480L and size[1] != 640L:
					print(os.path.join(root, file))
					# f.write(os.path.join(root, file))
					# f.write('\n')
	# f.close()	
	

	
if __name__ == '__main__':
    main()