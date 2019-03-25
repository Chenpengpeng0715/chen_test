#-*- coding:utf-8 -*-
import os
import shutil
#copy出template照片
def main():
	path = r"F:\fanyifu\xushui\test1"
	path = unicode(path, encoding='utf-8')
	path_template = r"F:\fanyifu\xushui\test1_tmp"
	f_t_p = open(os.path.join(path_template, "error.txt"), "w")
	count = 0
	for folder in os.listdir(path):
		template_dir_path = os.path.join(os.path.join(path, folder), "template")
		for template in os.listdir(template_dir_path):
			if os.path.splitext(template)[1] == ".jpg":#在这修改文件格式选择要移出的图片类型
				count += 1
				bmp_newname = folder + ',' + template
				shutil.copy(os.path.join(template_dir_path, template), os.path.join(path_template, bmp_newname))
				print(os.path.join(template_dir_path, template))
				f_t_p.write(bmp_newname)
				f_t_p.write("\n")
	f_t_p.write(str(count))
	f_t_p.close()
if __name__ == '__main__':
    main()