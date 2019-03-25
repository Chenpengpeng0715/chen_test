import shutil
import os

def main():
	path = r""
	dest_path = r""
	for city in os.listdir(path):
		city_path = os.path.join(path, city)
		for id in os.listdir(city_path):
			id_path = os.path.join(city_path, id)
			a = id.split("-")[1]
			age = id.split("-")[2]
			sex = id.split("-")[3].lower()
			if 15 < age < 60 and a = "xushui":
				if sex = "f":
					count_f += 1
					shutil.copy(id_path, dest_path)
				if 