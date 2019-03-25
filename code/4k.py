#-*- coding:utf-8 -*-
import os
#删除文件夹中被隐藏的文件
def main():
	path = r"D:\fanyifu\face_database\aboard\tmp\tmp\Argentina"
	for root, dirs, files in os.walk(path):
		for file in files:
			file_path = os.path.join(root, file)
			size = os.path.getsize(file_path)
			if size == 4096:
				os.remove(file_path)
				print(file_path)

if __name__ == "__main__":
	main()