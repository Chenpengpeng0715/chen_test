#-*- coding: UTF-8 -*-
import os
import shutil
#移出RGB图
def main():
	path = r"F:\fanyifu\argentina"
	dest_path = r"F:\fanyifu_rgb\argentina"
	# for file_country in os.listdir(path):#移动所有国家或者地区的rgb
		# country_path = os.path.join(path, file_country)
		# dest_country_path = os.path.join(dest_path, file_country)
		# if not os.path.isdir(dest_country_path):
			# os.makedirs(dest_country_path)
	move(path, dest_path)
def move(path, dest_path):
	for id in os.listdir(path):#移动一个国家或者地区的rgb，country_path 改为 path（path为id路径的上一层）
		id_path = os.path.join(path, id)
		dest_id_path = os.path.join(dest_path, id)
		if not os.path.isdir(dest_id_path):
			os.makedirs(dest_id_path)
		for file in os.listdir(id_path):
			if file == "template":
				tempate_path = os.path.join(id_path, "template")
				dest_template_path = os.path.join(dest_id_path, "template")
				if not os.path.isdir(dest_template_path):
					os.makedirs(dest_template_path)
				for file_tmp in os.listdir(tempate_path):
					if ".jpg" in file_tmp:
						shutil.move(os.path.join(tempate_path, file_tmp), os.path.join(dest_template_path, file_tmp))
						print(os.path.join(tempate_path, file_tmp))
			if ".jpg" in file:
				shutil.move(os.path.join(id_path, file), os.path.join(dest_id_path, file))	
				print(os.path.join(id_path, file))
				
				
def back(path, dest_path):
	for id in os.listdir(path):#移动一个国家或者地区的rgb，country_path 改为 path（path为id路径的上一层）
		id_path = os.path.join(path, id)
		dest_id_path = os.path.join(dest_path, id)
		for file in os.listdir(id_path):
			if file == "template":
				tempate_path = os.path.join(id_path, "template")
				dest_template_path = os.path.join(dest_id_path, "template")
				for file_tmp in os.listdir(tempate_path):
					if ".jpg" in file_tmp:
						shutil.move(os.path.join(tempate_path, file_tmp), os.path.join(dest_template_path, file_tmp))
						print(os.path.join(tempate_path, file_tmp))
			if ".jpg" in file:
				shutil.move(os.path.join(id_path, file), os.path.join(dest_id_path, file))	
				print(os.path.join(id_path, file))

if __name__ == "__main__":
	main()