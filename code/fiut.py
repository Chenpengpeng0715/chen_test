#-*- coding:utf-8 -*-
import os
import shutil
import cv2
from natsort import natsorted
import subprocess
import threading
import time
def main():
	#总的原始数据路径
	path_database = r"D:\fanyifu\face_database\aboard\zicai\tmp"
	#测试结果保存父路径
	dest_path = r"D:\fanyifu\result\11.14"
	#获取devices列表
	serial_nos = devices_list()
	#手机端测试路径
	push_path = r"/data/faceidUnitTest"
	#手机端测试结果路径
	pull_path = r"/data/faceidUnitTestResult"
	#获取当前时间
	#data = time.strftime('%Y-%m-%d %H%:%M:%S', time.localtime(c["time"]))
	data = "five"
	#结果父路径：以时间命名的版本结果路径
	dest_file_path = os.path.join(dest_path, data)
	#获取所有人种列表
	file_list = os.listdir(path_database)
	for i in range(len(file_list)):
		sn = serial_nos[i]
		file_name =file_list[i]
		result_path = os.path.join(dest_file_path, file_name)
		if not os.path.isdir(result_path):
			os.makedirs(result_path)
		#每个人种的原始文件路径
		#people_path = os.path.join(path_database, file_name)
		start_server(pull_path, result_path, sn)
						
def devices_list():
	devices = subprocess.Popen('adb devices'.split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]
	serial_nos = []
	for item in devices.split():
		filters = ['list', 'of', 'device', 'devices', 'attached']
		if item.lower() not in filters:
			serial_nos.append(item)
	return serial_nos	
	
def FIUT(pull_path, result_path, sn):
	#ret = os.system("adb -s " + sn + " push " + people_path + " " + push_path)
	#if ret == 0:
	os.system("adb -s " + sn + " wait-for-device")
	os.system("adb -s " + sn + " remount")
	os.system("adb -s " + sn + " shell setprop vendor.faceid.ut.testType FRR_FAR")
	os.system("adb -s " + sn + " shell setprop vendor.faceid.ut.enable 1")
	os.system("adb -s " + sn + " shell setprop vendor.faceid.ut.algoType hw")
	os.system("adb -s " + sn + " shell setprop vendor.faceid.ut.irType bmp")
	os.system("adb -s " + sn + " shell setprop vendor.faceid.ut.irW 640")
	os.system("adb -s " + sn + " shell setprop vendor.faceid.ut.irH 480")
	os.system("adb -s " + sn + " shell setprop vendor.faceid.ut.depthType short")
	os.system("adb -s " + sn + " shell setprop vendor.faceid.ut.depthW 480")
	os.system("adb -s " + sn + " shell setprop vendor.faceid.ut.depthH 640")
	os.system("adb -s " + sn + " shell rm -rf /sdcard/DCIM/Camera/*")
	os.system("adb -s " + sn + " shell rm -rf /storage/emulated/0/Pictures/Screenshots/*")
	os.system("adb -s " + sn + " shell rm -rf /storage/emulated/0/DCIM/Camera/*")
	os.system("adb -s " + sn + " shell rm -rf /data/vendor/camera/img/*")
	os.system("adb -s " + sn + " shell rm -rf /data/log/android_logs/*")
	os.system("adb -s " + sn + " shell rm -rf /data/system/dropbox/*")
	os.system("adb -s " + sn + " shell rm -rf /data/vendor/log/isp-log/*")
	os.system("adb -s " + sn + " shell rm -rf /data/vendor/log/hisi_logs/tee/*")
	os.system("adb -s " + sn + " shell rm -rf /data/data/face/*")
	os.system("adb -s " + sn + " shell setenforce 0")
	os.popen("adb -s " + sn + " shell input keyevent 26")
	logcmd = "adb -s " + sn + " logcat -s FIUTCA_faceid_ree"		
	#logcmd = "adb -s " + sn + " logcat -v threadtime | findstr FIUTCA"FIUTCA_UnitTest: testFAR(), end
	#logcmd = "adb -s " + sn + " logcat -v threadtime | findstr FIUTCA_UnitTest: testFAR(), end"
	pipe = subprocess.Popen(logcmd, shell=True, stdout=subprocess.PIPE)
	for i in iter(pipe.stdout.readline, "b"):
		if "testFAR(), end" in i:
			os.popen("start cmd /c adb -s " + sn + " pull " + pull_path + " " + result_path)

def start_server(pull_path, result_path, sn):
	server_sn = threading.Thread(target = FIUT, args = (pull_path, result_path, sn))
	server_sn.start()
	
if __name__ == '__main__':
	main()