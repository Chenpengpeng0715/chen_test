#-*- coding: UTF-8 -*-
import os
#删除挑完之后不可解的图片
def main():
	path = r"D:\fanyifu\face_database_error\B130\white"
	src_path = r"D:\fanyifu\face_database\aboard\white"
	
	for file_name in os.listdir(path):
		file_path = os.path.join(path, file_name)
		for image_name in os.listdir(file_path):
			if os.path.splitext(image_name)[1] == ".bmp" or os.path.splitext(image_name)[1] == ".short":
				image_id = image_name.split(",")[0]
				image_pic = image_name.split("-")[-1]
				# print(image_pic)
				src_id_path = os.path.join(src_path, image_id)
				src_pic_path = os.path.join(src_id_path, image_pic)
				# print(src_pic_path)
				if os.path.exists(src_pic_path):
					os.remove(src_pic_path)
					print(src_pic_path)
if __name__ == '__main__':
    main()			
	