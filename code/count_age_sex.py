#-*- coding: UTF-8 -*-
#统计三个年龄段的男女数量0-15、15-60、60+
import os
def main():
	path = r"D:\fanyifu\face_database\aboard\tmp"
	
	for country in os.listdir(path):
		count_child_f = 0
		count_child_m = 0
		count_adult_f = 0
		count_adult_m = 0
		count_old_f = 0
		count_old_m = 0
		country_path = os.path.join(path, country)
		for id_name in os.listdir(country_path):
			id_len = len(id_name.split("-"))
			if id_len > 3:
				sex = (id_name.split("-")[-3]).lower()
				age = int(id_name.split("-")[-4])		
				if age <= 15 and sex == "f":
					count_child_f += 1
				if age <= 15 and sex == "m":
					count_child_m += 1
				if 15 < age <60 and sex == "f":
					count_adult_f += 1
				if 15 < age <60 and sex == "m":
					count_adult_m += 1
				if age >= 60 and sex == "f":
					count_old_f += 1
				if age >= 60 and sex == "m":
					count_old_m += 1
		print("country: %s"%country)
		print("<=15f: %d"%count_child_f)
		print("<=15m: %d"%count_child_m)
		print("15-60f: %d"%count_adult_f)
		print("15-60m: %d"%count_adult_m)
		print(">60f: %d"%count_old_f)
		print(">60m: %d"%count_old_m)
	
if __name__ == "__main__":
	main()