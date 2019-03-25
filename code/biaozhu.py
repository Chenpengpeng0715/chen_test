#-*- coding: UTF-8 -*-
import os,sys
import subprocess
#print sys.path
def main():

	path = r"D:\fanyifu\face_database\rgb1"
	pic_path =r"D:\fanyifu\face_database\fyf\31.jpg"


	
	#os.system(r"D:\fanyifu\face_database\fyf\testHat.exe " + pic_path)
	#os.system(r'cd D:\fanyifu\face_database\fyf')
	#os.system(r"D:\fanyifu\face_database\fyf\testHat.exe " + pic_path)
	cmd_all = r'cd D:\fanyifu\face_database\fyf & D:\fanyifu\face_database\fyf\testHat.exe' + pic_path
	p = subprocess.Popen(cmd_all, shell=True, cwd='D:\fanyifu\face_database\fyf')  
	#同步执行  
	retcode = p.wait()



if __name__ == "__main__":
	main()