#-*- coding:utf-8 -*-
import os
import xlrd
#对缺失信息的原始数据进行重新标注（性别、年龄）

def main():

	path = r"F:\fanyifu\test"
	data = xlrd.open_workbook(r"D:\fanyifu\code\six.xlsx")
	# sheets = data.sheetnames
	# for i in range(len(sheets)):
	# table = data[sheets[i]]
	table = data.sheets()[4]
	nrows = table.nrows
	# ncols = table.ncols
	count = 0
	for i in range(1, nrows):
		info = table.row_values(i)
		ID = str(info[1])[-5:]
		sexs = info[2].lower()
		age = int(info[3])
		if sexs == 'm':
			sex = 'm'
		if sexs == 'f':
			sex = 'f'
		for file in os.listdir(path):
			file_path = os.path.join(path, file)
			for id_name in os.listdir(file_path):
				id_name_light = id_name.split("-")[-1]
				if ID in id_name:
					#ID_new = ID[-4:]
					count += 1
					#print(ID_new)
					print(count)
					new_name = ID + "-africa-" + str(age) + "-" + sex + "-n-" + id_name_light
					print(new_name)
					#os.rename(os.path.join(path, id_name), os.path.join(path, new_name))
if __name__ == "__main__":
	main()
