#-*- coding: UTF-8 -*-
import os
#统计每个小组在对应城市采集数据的数量
def main():
	path = r"D:\fanyifu\face_database\China"
	dict_group_city = {}
	dirs = os.listdir(path)
	for file_name in dirs:
		new_file_name = file_name.split("-")
		group_city_name = new_file_name[0][0:2].lower() + "_" + new_file_name[1]
		if group_city_name in dict_group_city.keys():
			dict_group_city[group_city_name] += 1
		else:
			dict_group_city[group_city_name] = 1
	print(dict_group_city)	
	
	# path1 = os.path.join(path, "test.txt")
	# f = file(path1, "w")
    # fp = open(path1, 'a')
	# for (key, value) in dict_group_city:
		# fp.write(key)

if __name__ == '__main__':
    main()	
	