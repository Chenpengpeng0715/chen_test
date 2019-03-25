#-*- coding: UTF-8 -*-
import os
import shutil
#将FAR每一个模板照片以及和这个模板比对的照片都移动到指定文件目录，检查互解照片
def main():

	root = os.getcwd()
	src_path = r"D:\fanyifu\face_database\aboard\black"
	dest_path = r"D:\result\black"
	path = os.path.join(root, "result.txt")
	fin = open(path, 'r')
	
	for line in fin:
		if line.find("pic") != -1 and line.find("isNoFace") != -1:
			id = line.split("/")[3]
			tmp = line.split("/")[4]
			pid = tmp.split(",")[0]
			src_id_path = os.path.join(src_path, id)
			dest_id_path = os.path.join(dest_path, id)
			src_pid_path = os.path.join(src_id_path, pid)
			pid_newname = id + "," + pid
			
			if not os.path.exists(dest_id_path):
				# print(dest_id_path)
				os.makedirs(dest_id_path)
			if (os.path.exists(src_pid_path)) and (not os.path.exists(os.path.join(dest_id_path, pid_newname))):
				shutil.copy(os.path.join(src_id_path, pid), os.path.join(dest_id_path, pid_newname))
				print("copy %s completed"%pid)
			continue
			
		if line.find("template") != -1 and line.find("isNoFace") != -1:
			template_id = line.split("/")[3]
			print(template_id)
			template_tmp = line.split("/")[5]
			file_template = line.split("/")[4]
			template_pid = template_tmp.split(",")[0]
			src_template_id = os.path.join(src_path, template_id)
			template_path = os.path.join(dest_id_path, file_template)
			template_pid_newname = template_id + "," + template_pid
			src_template_id_path = os.path.join(src_template_id, "template")
			if not os.path.exists(template_path):
				os.makedirs(template_path)
			if (os.path.exists(os.path.join(src_template_id_path, template_pid))) and (not os.path.exists(os.path.join(template_path, template_pid_newname))):
				shutil.copy(os.path.join(src_template_id_path, template_pid), os.path.join(template_path, template_pid_newname))
				print("copy completed")
			continue
			
if __name__ == '__main__':
        main()