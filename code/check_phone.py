#-*- coding: UTF-8 -*-
import os
#检查push的文件是否全部push完成，是否不全
def main():
	path = r"D:\fanyifu\face_database\China\jd_zhucheng"
	sn = ""
	for file_name in os.listdir(path):
		file_name_path = os.path.join(path, file_name)
		# template_path = os.path.join(file_name_path, )
		# print(file_name)
		for image_name in os.listdir(file_name_path):
			if image_name == "tempalte":
				for tempalte_image_path in os.listdir(os.path.join(file_name_path, "tempalte")):
					print(tempalte_image_path)
					if "No such file or directory" in os.popen("adb " + " shell ls /data/test/" + file_name + "/template/" + image_name).read():
						temp = "tempalte" + file_name + "-" + image_name
						print("%s is not exists"%temp)
			# print(image_name)
			# print(os.popen("adb " + " shell ls /data/test/" + file_name + "/" + image_name).read())
			if "No such file or directory" in os.popen("adb " + " shell ls /data/test/" + file_name + "/" + image_name).read():
				tmp = file_name + "-" + image_name
				print("%s is not exists"%tmp)
		
if __name__ == '__main__':
    main()	