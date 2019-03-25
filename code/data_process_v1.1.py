#-*- coding:utf-8 -*-
import os
import shutil
import cv2
from natsort import natsorted

def main():
	path = r"D:\fanyifu\face_database\aboard\zicai\feilvbing"
	#dest_path = r"D:\fanyifu\face_database_template\aboard\tmp\Africa"
	path = unicode(path, encoding='utf-8')
	template_path = r"D:\fanyifu\face_database_error\B112_1\test\philipines"
	
	# image_shape_path = r"D:\fanyifu\check-image"
	#1、移动文件到path并删除源文件夹
	#2、删除除bmp和short以外格式的图片
	#3、重命名（文件名改成只有时间，保持bmp与short一一对应）
	#4、添加文件编号
	#5、生成模板文件夹
	#6、移动模板文件到模板文件夹
	#7、检查文件是否只有bmp和short和是否没有被重命名（修改完记得再执行检查一遍）
	delete_file(path)
	# move_dir(path)
	# delete_two_image(path)
	# bmp_jpg(path)
	# check_image(path)
	# check_file_ram(path)
	# rename_file(path)
	# delete_file_all(path)
	# add_number(path)
	# generate_template(path)
	# move_to_template(path)
	# search(path)

	#8、检查图片尺寸
	#9、查找空文件夹
	# check_file(path)
	# move_template(path,template_path)
	# add_number_rgb(path)
	# check_file_name(path)
	# move_error_image(path, dest_path)
	# delete_template_image(path)
	# check_template_file(path)
	# add_template_number(path)
	# rename_file(path)
	# check_number(path)
	# generate_mask(path)
	# generate_scarf(path)
	# move_file_to_mask_outdoor(path)
	# move_file_to_scarf_outdoor(path)
	# move_file_to_mask(path)
	# move_file_to_scarf(path)
	# add_indoor(path)
	# add_outdoor(path)
	# generate_folder(path, path1)
	# move_mask_and_scarf_to_folder(path, path1)
	# remove_template_file(path)
	# copy_template_file(path1, path)
	# count_age_is_less_than_number(path, path2, 16)
	# check_the_number_of_files(path, path3, path4)
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
def move_to_template(path):
	for file in os.listdir(path):
		file_path = os.path.join(path, file)
		for name in os.listdir(file_path):
			template_path = os.path.join(file_path, "template")
			if "_0.bmp" in name or "_0.short" in name or "_0.jpg" in name:
				shutil.move(os.path.join(file_path, name), os.path.join(template_path, name))
				print(os.path.join(file_path, name))
				
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
		
		
# def move_dir(path):
	# dirs = os.listdir(path)
	# print dirs
	# for folder in dirs:
		# light = folder.split('-')
		# folder_path = os.path.join(path, folder)
		# folder_list = os.listdir(folder_path)
        # for folder2 in folder_list:
			# shutil.move(os.path.join(folder_path, folder2), path)
			# if light[2] == 'sn':
				# folder2_new = folder2 + '-indoor'				
				# os.rename(os.path.join(folder_path, folder2), os.path.join(folder_path, folder2_new))
			# elif light[2] == 'sw':
				# folder2_new = folder2 + '-outdoor'
				# os.rename(os.path.join(folder_path, folder2), os.path.join(folder_path, folder2_new))
			
        # # os.rmdir(os.path.join(path, folder))
        # # print("%s move file is completed"%folder_path)
	
def delete_image(path):
	for root, dirs, files in os.walk(path):    
		for file in files:                             
			if os.path.splitext(file)[1] != ".short" and file.find("IR2D") == -1:   
				os.remove(os.path.join(root, file))
				print("%s delete is completed"%os.path.join(root, file))

def delete_two_image(path):
	for root, dirs, files in os.walk(path):
		for file in files:
			if not (os.path.splitext(file)[1] == ".short" or file.find("IR2D") != -1 or file.find("RGB") != -1):
				os.remove(os.path.join(root, file))
				print("%s delete is completed"%os.path.join(root, file))
# def check_file(path):
	# for root, dirs, files in os.walk(path):
		# filelist = natsorted(files)
		# ir_name = ""
		# depth_name = ""
		# for file in filelist:
			# if os.path.splitext(file)[1] == ".short":
				# ir_name = os.path.splitext(file)[0]
			# if os.path.splitext(file)[1] == ".bmp":
				# depth_name = os.path.splitext(file)[0]
			# if len(ir_name) != 0 and len(depth_name) != 0:
				# if ir_name[0:23] != depth_name[0:23]:
					# print(os.path.join(root, file))
					# break
				# ir_name = ""
				# depth_name = ""

def check_file(path):
	for root, dirs, files in os.walk(path):
		filelist = natsorted(files)
		ir_name = ""
		depth_name = ""
		for file in filelist:
			if os.path.splitext(file)[1] == ".short":
				ir_name = os.path.splitext(file)[0]
				bmp_name = os.path.splitext(file)[0] + '.bmp'
				if not os.path.exists(os.path.join(root, bmp_name)):
					print(os.path.join(root, file))
			if os.path.splitext(file)[1] == ".bmp":
				depth_name = os.path.splitext(file)[0]
				short_name = os.path.splitext(file)[0] + '.short'
				if not os.path.exists(os.path.join(root,short_name)):
					print(os.path.join(root, file))
			# if len(ir_name) != 0 and len(depth_name) != 0:
				# if ir_name[0:23] != depth_name[0:23]:
					# #print(os.path.join(root, file))
					# break
				# ir_name = ""
				# depth_name = ""	
				
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
					print(os.path.join(root, file))
					#os.remove(os.path.join(root, file))
			if os.path.splitext(file)[1] == ".bmp":
				depth_name = os.path.splitext(file)[0]
				short_name = os.path.splitext(file)[0] + '.short'
				if not os.path.exists(os.path.join(root,short_name)):
					print(os.path.join(root, file))
					#os.remove(os.path.join(root, file))	

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
					os.remove(os.path.join(root, file))
			if os.path.splitext(file)[1] == ".bmp":
				depth_name = os.path.splitext(file)[0]
				short_name = os.path.splitext(file)[0] + '.short'
				rgb_name = os.path.splitext(file)[0] + '.jpg'
				if not os.path.exists(os.path.join(root,short_name)) or not os.path.exists(os.path.join(root, rgb_name)):
					os.remove(os.path.join(root, file))	
			if os.path.splitext(file)[1] == ".jpg":
				color_name = os.path.splitext(file)[0]
				Short_name = os.path.splitext(file)[0] + '.short'
				Bmp_name = os.path.splitext(file)[0] + '.bmp'
				if not os.path.exists(os.path.join(root,Short_name)) or not os.path.exists(os.path.join(root, Bmp_name)):
					os.remove(os.path.join(root, file)) 
def check_file_name(path):
	for root, dirs, files in os.walk(path):
		filelist = natsorted(files)
		for file in filelist:
			if len(os.path.splitext(file)[0]) != 23:
				print(os.path.join(root, file))
				
def check_number(path):
	for root, dirs, files in os.walk(path):
		for folder in dirs:
			folder_path = os.path.join(root, folder)
			file_list = os.listdir(folder_path)
			cnt = 0
			for file in file_list:
				if os.path.splitext(file)[1] == ".bmp":
					cnt += 1
			if cnt != 101 and cnt != 107:
				print folder
				print cnt
				
def rename_file(path):
	for root, dirs, files in os.walk(path):
		natsort_file_list = natsorted(files)
		for file in natsort_file_list:
			image_name = os.path.splitext(file)[0]
			file_name = image_name[0:23] + os.path.splitext(file)[1]
			if os.path.exists(os.path.join(root, file_name)) == 0:
				os.rename(os.path.join(root, file), os.path.join(root, file_name))
				print("%s rename completed"%os.path.join(root, file))
			
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

def add_number_rgb(path):
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
				os.rename(os.path.join(folder_path, file), os.path.join(folder_path, ir_new))
				print("%s add number completed"%os.path.join(folder_path, file))
				cnt += 1




				
def add_template_number(path):
	dirs = os.listdir(path)
	for folder in dirs:
		tmp = os.path.join(path, folder)
		folder_path = os.path.join(tmp, "template")
		tmp1 = os.listdir(folder_path)
		files = natsorted(tmp1)
		cnt = 1
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
				
def remove_template_file(path):
	dirs = os.listdir(path)
	for folder in dirs:
		tmp = os.path.join(path, folder)
		folder_path = os.path.join(tmp, "template")
		files = os.listdir(folder_path)
		for file in files:
			if os.path.splitext(file)[1] == ".bmp":
				words = os.path.splitext(file)[0].split('_')
				cnt = int(words[len(words) - 1])
			if os.path.splitext(file)[1] == ".bmp" and cnt != 1:
				depth_image = os.path.splitext(file)[0] + ".short"
				os.remove(os.path.join(folder_path, file))
				os.remove(os.path.join(folder_path, depth_image))				
		print("%s remove template file completed"%folder_path)
		
				
def generate_template(path):
	dirs = os.listdir(path)
	for folder in dirs:
		dir_path = os.path.join(path, folder)
		template_dir_path = os.path.join(dir_path, "template")
		print(template_dir_path)
		cmd = "md %s"%template_dir_path
		#cmd = unicode(cmd, encoding='utf-8')
		os.system(cmd)
					
# def move_file_to_template(path, path_result):
	# for root, dirs, files in os.walk(path):
		# natsort_file_list = natsorted(files)
		# cnt = 0
		# for file in natsort_file_list:
			# if os.path.splitext(file)[1] == ".bmp" and cnt < 1:
				# template_dir_path = os.path.join(root, "template")
				# depth_image = os.path.splitext(file)[0] + ".short"
				# if root.find("template") == -1:
					# path_template = os.path.join(path_result, "template")
					# if not os.path.exists(path_template):
						# os.makedirs(path_template)
					# shutil.copy(os.path.join(root, file), os.path.join(path_template, file))
					
					# shutil.move(os.path.join(root, file), os.path.join(template_dir_path, file))
					# shutil.move(os.path.join(root, depth_image), os.path.join(template_dir_path, depth_image))
					# cnt += 1
			# if cnt >= 1:
				# print("%s move file is completed"%root)
				# break
				
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
				
def generate_mask(path):
	dirs = os.listdir(path)
	for folder in dirs:
		dir_path = os.path.join(path, folder)
		mask_dir_path = os.path.join(dir_path, "mask")
		os.system("md %s"%mask_dir_path)
		
def generate_scarf(path):
	dirs = os.listdir(path)
	for folder in dirs:
		dir_path = os.path.join(path, folder)
		mask_dir_path = os.path.join(dir_path, "scarf")
		os.system("md %s"%mask_dir_path)
		
def move_file_to_mask(path):
	for folder in os.listdir(path):
		dir_path = os.path.join(path, folder)
		for file in os.listdir(dir_path):
			if os.path.splitext(file)[1] == ".bmp":
				words = os.path.splitext(file)[0].split('_')
				cnt = int(words[len(words) - 1])
			if os.path.splitext(file)[1] == ".bmp" and (cnt == 27 or cnt == 28 or cnt == 29 or cnt == 57 or cnt == 58 or cnt == 59 or cnt == 86 or cnt == 87 or cnt == 88):
				mask_dir_path = os.path.join(dir_path, "mask")
				depth_image = os.path.splitext(file)[0] + ".short"
				shutil.move(os.path.join(dir_path, file), os.path.join(mask_dir_path, file))
				shutil.move(os.path.join(dir_path, depth_image), os.path.join(mask_dir_path, depth_image))
		print("%s move file is completed"%dir_path)
			
def move_file_to_scarf(path):
	for folder in os.listdir(path):
		dir_path = os.path.join(path, folder)
		for file in os.listdir(dir_path):
			if os.path.splitext(file)[1] == ".bmp":
				words = os.path.splitext(file)[0].split('_')
				cnt = int(words[len(words) - 1])
			if os.path.splitext(file)[1] == ".bmp" and (cnt == 22 or cnt == 23 or cnt == 24 or cnt == 25 or cnt == 26 or cnt == 52 or cnt == 53 or cnt == 54 or cnt == 55 or cnt == 56 or cnt == 81 or cnt == 82 or cnt == 83 or cnt == 84 or cnt == 85):
				scarf_dir_path = os.path.join(dir_path, "scarf")
				depth_image = os.path.splitext(file)[0] + ".short"
				shutil.move(os.path.join(dir_path, file), os.path.join(scarf_dir_path, file))
				shutil.move(os.path.join(dir_path, depth_image), os.path.join(scarf_dir_path, depth_image))
		print("%s move file is completed"%dir_path)
		
def move_file_to_mask_outdoor(path):
	for folder in os.listdir(path):
		dir_path = os.path.join(path, folder)
		for file in os.listdir(dir_path):
			if os.path.splitext(file)[1] == ".bmp":
				words = os.path.splitext(file)[0].split('_')
				cnt = int(words[len(words) - 1])
			if os.path.splitext(file)[1] == ".bmp" and (cnt == 29 or cnt == 30 or cnt == 31 or cnt == 63 or cnt == 64 or cnt == 65 or cnt == 92 or cnt == 93 or cnt == 94):
				mask_dir_path = os.path.join(dir_path, "mask")
				depth_image = os.path.splitext(file)[0] + ".short"
				shutil.move(os.path.join(dir_path, file), os.path.join(mask_dir_path, file))
				shutil.move(os.path.join(dir_path, depth_image), os.path.join(mask_dir_path, depth_image))
		print("%s move file is completed"%dir_path)
			
def move_file_to_scarf_outdoor(path):
	for folder in os.listdir(path):
		dir_path = os.path.join(path, folder)
		for file in os.listdir(dir_path):
			if os.path.splitext(file)[1] == ".bmp":
				words = os.path.splitext(file)[0].split('_')
				cnt = int(words[len(words) - 1])
			if os.path.splitext(file)[1] == ".bmp" and (cnt == 24 or cnt == 25 or cnt == 26 or cnt == 27 or cnt == 28 or cnt == 58 or cnt == 59 or cnt == 60 or cnt == 61 or cnt == 62 or cnt == 87 or cnt == 88 or cnt == 89 or cnt == 90 or cnt == 91):
				scarf_dir_path = os.path.join(dir_path, "scarf")
				depth_image = os.path.splitext(file)[0] + ".short"
				shutil.move(os.path.join(dir_path, file), os.path.join(scarf_dir_path, file))
				shutil.move(os.path.join(dir_path, depth_image), os.path.join(scarf_dir_path, depth_image))
		print("%s move file is completed"%dir_path)
		
def move_file_to_looking_up(path):
	for folder in os.listdir(path):
		dir_path = os.path.join(path, folder)
		for file in os.listdir(dir_path):
			if os.path.splitext(file)[1] == ".bmp":
				words = os.path.splitext(file)[0].split('_')
				cnt = int(words[len(words) - 1])
			if os.path.splitext(file)[1] == ".bmp" and (cnt == 3 or cnt == 4 or cnt == 9 or cnt == 14 or cnt == 19 or cnt == 24 or cnt == 33 or cnt == 38 or cnt == 44 or cnt == 49 or cnt == 54 or cnt == 62 or cnt == 83 or cnt == 84 or cnt == 85):
				scarf_dir_path = os.path.join(dir_path, "scarf")
				depth_image = os.path.splitext(file)[0] + ".short"
				shutil.move(os.path.join(dir_path, file), os.path.join(scarf_dir_path, file))
				shutil.move(os.path.join(dir_path, depth_image), os.path.join(scarf_dir_path, depth_image))
		print("%s move file is completed"%dir_path)
			
def delete_template_image(path):
	dirs = os.listdir(path)
	for folder in dirs:
		dir_path = os.path.join(path, folder)
		template_dir_path = os.path.join(dir_path, "template")
		for root, dirs, files in os.walk(template_dir_path):
			natsort_file_list = natsorted(files)
			cnt = 0
			for file in natsort_file_list:
				if os.path.splitext(file)[1] == ".bmp":
					cnt += 1
			if cnt != 13:
				continue
			cnt = 0
			for file in natsort_file_list:
				if os.path.splitext(file)[1] == ".bmp":
					cnt += 1
					if cnt == 7 or cnt == 9 or cnt == 11 or cnt == 13:
						ir_name = os.path.splitext(file)[0]
						depth_image = ir_name + ".short"
						os.remove(os.path.join(root, file))
						os.remove(os.path.join(root, depth_image))
						print("%s is removed"%os.path.join(root, file))
						print("%s is removed"%os.path.join(root, depth_image))
						
def check_template_file(path):
	dirs = os.listdir(path)
	for folder in dirs:
		dir_path = os.path.join(path, folder)
		template_dir_path = os.path.join(dir_path, "template")
		for root, dirs, files in os.walk(template_dir_path):
			natsort_file_list = natsorted(files)
			cnt = 0
			for file in natsort_file_list:
				if os.path.splitext(file)[1] == ".bmp":
					cnt += 1
			if cnt != 9:
				print(template_dir_path)
				
def check_the_number_of_files(path, path3, path4):
	for folder in os.listdir(path):
		cnt = 0
		for file in os.listdir(os.path.join(path, folder)):
			if os.path.splitext(file)[1] == ".bmp":
				cnt += 1
		if (folder.find("indoor") != -1 and cnt == 101) or (folder.find("outdoor") != -1 and cnt == 107):
			if folder.find("indoor") != -1:
				shutil.move(os.path.join(path, folder), path3)
				print("%s is completed"%os.path.join(path, folder))
			if folder.find("outdoor") != -1:
				shutil.move(os.path.join(path, folder), path4)
				print("%s is completed"%os.path.join(path, folder))
			# print(os.path.join(path, folder))
				
def add_indoor(path):
	dirs = os.listdir(path)
	for folder in dirs:
		new_name = folder + "-indoor"
		os.rename(os.path.join(path, folder), os.path.join(path, new_name))
		print("%s add is completed"%os.path.join(path, folder))
		
def add_outdoor(path):
	dirs = os.listdir(path)
	for folder in dirs:
		new_name = folder + "-outdoor"
		os.rename(os.path.join(path, folder), os.path.join(path, new_name))
		print("%s add is completed"%os.path.join(path, folder))
				
def generate_folder(path, path1):
	dirs = os.listdir(path)
	for folder in dirs:
		folder_path = os.path.join(path1, folder)
		os.system("md %s"%folder_path)
		
def move_mask_and_scarf_to_folder(path, path1):
	dirs = os.listdir(path)
	for folder in dirs:
		old_folder = os.path.join(path, folder)
		old_mask_folder = os.path.join(old_folder, "mask")
		old_scarf_folder = os.path.join(old_folder, "scarf")
		old_template_folder = os.path.join(old_folder, "template")
		new_folder = os.path.join(path1, folder)
		new_mask_folder = os.path.join(new_folder, "mask")
		new_scarf_folder = os.path.join(new_folder, "scarf")
		new_template_folder = os.path.join(new_folder, "template")
		shutil.move(old_mask_folder, new_mask_folder)
		shutil.move(old_scarf_folder, new_scarf_folder)
		shutil.copytree(old_template_folder, new_template_folder)
		print("%s add is completed"%os.path.join(path, folder))
				
def count_age_is_less_than_number(path, path2, number):
	cnt = 0
	for folder in os.listdir(path):
		words = folder.split('-')
		if len(words[2]) != 2:
			print(os.path.join(path, folder))
		if len(words[2]) == 2:
			age = int(words[2])
		if age < number:
			shutil.move(os.path.join(path, folder), os.path.join(path2, folder))
			print("%s is completed"%os.path.join(path, folder))
			cnt += 1
	print("count is %d"%cnt)
	
def copy_template_file(path1, path):
	for folder in os.listdir(path1):
		old_folder = os.path.join(path1, folder)
		old_template_folder = os.path.join(old_folder, "template")
		new_folder = os.path.join(path, folder)
		new_template_folder = os.path.join(new_folder, "template")
		shutil.rmtree(new_template_folder)
		shutil.copytree(old_template_folder, new_template_folder)
		print("%s add is completed"%os.path.join(path, folder))
		
def search(path):
	for files in os.listdir(path):
		file_path = os.path.join(path, files)
		for file_name in files:
			if os.path.isdir(file_path):
				if not os.listdir(file_path):
					print(file_path)
		
def check_image(path):
	for root, dirs, files in os.walk(path):
		for file in files:
			if os.path.splitext(file)[1] == ".bmp": 
				try:
					img = cv2.imread(os.path.join(root, file))
					size = img.shape
					if size[0] != 480L and size[1] != 640L:
						print(os.path.join(root, file))
				except:
					print("opencv error:%s"%os.path.join(root, file))
				
def check_file_ram(path):
	for root, dirs, files in os.walk(path):
		for file in files:
			file_path = os.path.join(root, file)
			size = os.path.getsize(file_path)
			if size == 4096:
				os.remove(file_path)
				print(file_path)
	
def move_error_image(path, dest_path):
	for country_name in os.listdir(path):
		country_name_path = os.path.join(path, country_name)
		for file_name in os.listdir(country_name_path):
			file_name_path = os.path.join(country_name_path, file_name)
			template_path = os.path.join(file_name_path, "template")
			if os.path.isdir(template_path):
				dest_country_path = os.path.join(dest_path, country_name)
				if not os.path.isdir(dest_country_path):
					os.makedirs(dest_country_path)
				shutil.move(file_name_path, dest_country_path)
				print("%s move is completed"%file_name_path)
				
if __name__ == "__main__":
	main()