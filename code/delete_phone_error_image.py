#-*- coding: UTF-8 -*-
import os 
#删除手机中规格中制定不可解的图片
def main():
	path = r""
	delete_q(path)
	#delete_a(path)

def delete_a(path):
	for id_name in os.listdir(path):
		id_path = os.path.join(path, id_name)
		for file_name in os.listdir(id_path):
			file_name_path = os.path,join(id_path, file_name)
			if file_name = "template":
				for tempalte_image_path in os.listdir(os.path.join(id_path, "tempalte")):
					print(tempalte_image_path)
					phone_template = os.popen("adb " + " shell ls /data/test/" + id_name + "/template/" + file_name).read()
					if not phone_template in tempalte_image_path:
						os.popen("adb shell rm -rf /data/faceidUnitTest/" + phone_template)
						print("deleted tempalte completed")
			if not os.popen("adb shell ls /data/faceidUnitTest/" + id_name + file_name).read() in file_name_path:
				os.popen("adb rm -rf /data/faceidUnitTest/" + id_name + file_name)
				print("deleted completed")

def delete():
	os.popen("adb rm -rf /data/faceidUnitTest/*/.*")

def delete_q():
	for id_name in os.listdir(path):
		id_path = os.path.join(path, id_name)
			if os.popen("adb shell ls /data/faceidUnitTest/" + id_name).read() in id_path:
				os.popen("adb rm -rf /data/faceidUnitTest/" + id_name + file_name)
				print("deleted completed")
if __name__ == '__main__':
	main()