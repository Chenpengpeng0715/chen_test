#-*- coding:utf-8 -*-
import os
import shutil
#检查新版本不可解老版本可解的照片，复制到对应fail文件夹
#检查新版本可解老版本不可解的照片，复制到对应success文件夹
def main():
	path_new = r"D:\fanyifu\result\B130\africa"
	path_old = r"D:\fanyifu\result\B122_1\africa"
	src_path = r"D:\fanyifu\face_database\aboard\zicai\tmp\egypt"
	dest_path = r"D:\fanyifu\face_database_tar_decrease\B130\africa"
	dest_path_new = os.path.join(path_new, "FRR.txt")
	dest_path_old = os.path.join(path_old, "FRR.txt")
	fp_new = open(dest_path_new, "r")
	fp_old = open(dest_path_old, "r")
	success_path = os.path.join(dest_path, "success")
	fail_path = os.path.join(dest_path, "fail")
	if not os.path.isdir(success_path):
		os.makedirs(success_path)
	if not os.path.isdir(fail_path):
		os.makedirs(fail_path)
	result_lines_new = fp_new.readlines()
	result_lines_old = fp_old.readlines()
	start_fail = 0
	count_fail = 0
	start_success = 0
	count_success = 0
	for i in range(len(result_lines_new)):
		if result_lines_new[i].find("pic") != -1 and result_lines_new[i].find("isNoFace") != -1 and result_lines_new[i+1].find("result:fail") != -1:
			ID = result_lines_new[i].split("/")[3]
			bmp = result_lines_new[i].split("/")[4].split(",")[0]
			for j in range(start_fail, len(result_lines_old)):
				if result_lines_old[j].find(ID) != -1 and result_lines_old[j].find(bmp) != -1 and result_lines_old[j+1].find("result:sucess") != -1:
					ID_path = os.path.join(src_path, ID)
					bmp_newname = ID + "," + bmp
					if os.path.exists(os.path.join(os.path.join(src_path, ID), bmp)):
						shutil.copy(os.path.join(ID_path, bmp), os.path.join(fail_path, bmp_newname))
						count_fail += 1
						print("%s copy is completed"%os.path.join(ID_path, bmp))
						start_fail = j
						break
		if result_lines_new[i].find("pic") != -1 and result_lines_new[i].find("isNoFace") != -1 and result_lines_new[i+1].find("result:sucess") != -1:
			ID = result_lines_new[i].split("/")[3]
			bmp = result_lines_new[i].split("/")[4].split(",")[0]
			for j in range(start_success, len(result_lines_old)):
				if result_lines_old[j].find(ID) != -1 and result_lines_old[j].find(bmp) != -1 and result_lines_old[j+1].find("result:fail") != -1:
					ID_path = os.path.join(src_path, ID)
					bmp_newname = ID + "," + bmp
					if os.path.exists(os.path.join(os.path.join(src_path, ID), bmp)):
						shutil.copy(os.path.join(ID_path, bmp), os.path.join(success_path, bmp_newname))
						count_success += 1
						print("%s copy is completed"%os.path.join(ID_path, bmp))
						start_success = j
						break			
	print("fail: %d"%count_fail)
	print("success: %d"%count_success)
	# for i in range(len(result_lines_new)):
		# if result_lines_new[i].find("pic") != -1 and result_lines_new[i].find("isNoFace") != -1 and result_lines_new[i+1].find("result:sucess") != -1:
			# ID = result_lines_new[i].split("/")[3]
			# bmp = result_lines_new[i].split("/")[4].split(",")[0]
			# for j in range(start_success, len(result_lines_old)):
				# if result_lines_old[j].find(ID) != -1 and result_lines_old[j].find(bmp) != -1 and result_lines_old[j+1].find("result:fail") != -1:
					# ID_path = os.path.join(src_path, ID)
					# bmp_newname = ID + "," + bmp
					# if os.path.exists(os.path.join(os.path.join(src_path, ID), bmp)):
						# shutil.copy(os.path.join(ID_path, bmp), os.path.join(success_path, bmp_newname))
						# count_success += 1
						# print("%s copy is completed"%os.path.join(ID_path, bmp))
						# start_success = j
						# break
	# print("success: %d"%count_success)
if __name__ == '__main__':
    main()