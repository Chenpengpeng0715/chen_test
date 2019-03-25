#-*- coding:utf-8 -*-
import subprocess
import os
import time
import threading
import time

def main():
	serial_nos = devices_list()
	path_database = r"D:\fanyifu\face_database\test"
	pull_path = r"/data/faceidUnitTestResult"
	dest_path = r"D:\fanyifu\result\test"
	# data = time.strftime('%Y-%m-%d%H%', time.localtime())
	data = "B122"
	dest_file_path = os.path.join(dest_path, data)
	file_name = os.listdir(path_database)
	for i in range(len(file_name)):
		sn = serial_nos[i]
		result_path = os.path.join(dest_file_path, file_name[i])
		people_path = os.path.join(path_database, file_name[i])
		if not os.path.isdir(result_path):
			os.makedirs(result_path)
		start_pull_server(pull_path, result_path, sn)
				
def devices_list():
	devices = subprocess.Popen('adb devices'.split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]
	serial_nos = []
	for item in devices.split():
		filters = ['list', 'of', 'device', 'devices', 'attached']
		if item.lower() not in filters:
			serial_nos.append(item)
	return serial_nos		

def pull(pull_path, result_path, sn):
	os.system("adb -s " + sn + " pull " + pull_path + " " + result_path)

def start_pull_server(pull_path, result_path, sn):
	server_pull = threading.Thread(target = pull, args = (pull_path, result_path, sn))
	server_pull.start()
	
if __name__ == '__main__':
    main()	

