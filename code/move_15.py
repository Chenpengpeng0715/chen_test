#-*- coding: UTF-8 -*-
import os
import shutil

#移出0-13岁的文件
def main():
	count = 0
	path = r"D:\fanyifu\face_database\China\zhongguo"
	new_path = r"D:\fanyifu\face_database\China\15\new"
	fp = open(os.path.join(new_path, "15new.txt"), "w")
	for id_name in os.listdir(path):
		age = int(id_name.split("-")[2])
		if age <= 15:
			count += 1
			print(id_name)
			shutil.move(os.path.join(path, id_name), new_path)
			fp.write(id_name)
			fp.write("\n")
	fp.write(str(count))
	fp.close()
if __name__ == "__main__":
	main()
