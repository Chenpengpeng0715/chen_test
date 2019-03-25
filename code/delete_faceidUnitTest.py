import os

def main(sn):
	sn = raw_input("input sn: ")
	serial_nos = devices_list()
	for i in range(len(serial_nos)):
		sn = serial_nos[i]
		os.system("start cmd /k adb -s " + sn + " shell rm -rf /data/test")
		os.system("adb -s " + sn + " shell rm -rf /data/faidUnitTest/*")
		os.system("abd -s " + sn + " shell rm -rf /data/faidUnitTestResult")

def devices_list():
	devices = subprocess.Popen('adb devices'.split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]
	serial_nos = []
	for item in devices.split():
		filters = ['list', 'of', 'device', 'devices', 'attached']
		if item.lower() not in filters:
			serial_nos.append(item)
	return serial_nos
	
if __name__ == '__main__':
	main()	
	