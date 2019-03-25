#-*- coding: UTF-8 -*-
import os
#统计bmp的数量
def main():
	path = r"D:\fanyifu\face_database_error\B130\mexico"
	count = 0
	for root, dirs, files in os.walk(path):
		for file in files:
			if ".bmp" in file:
				count += 1
	print count
	
if __name__ == '__main__':
        main()