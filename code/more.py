import time
#标注多个因素
def main():
	root = os.getcwd()
	print(root)
	out_path = os.path.join(root, "out.txt")
	path = r"D:\fanyifu\face_database\rgb1\chaina"
	file_num  = 0
	# for id in os.listdir(path):
		# id_path = os.path.join(path, id)
		# attribute_path = os.path.join(id_path, "attribute.txt")
		# file_template_path = os.path.join(id_path, "template")
		# template_attribute_path = os.path.join(file_template_path, "attribute.txt")
		# file_template_attribute = open(template_attribute_path, "a+")
		# file_template_attribute.write("1 \n")
		# file_template_attribute.write("image_id hat \n")
		# file_template_attribute.close()
		# for file in os.listdir(id_path):
			# file_path = os.path.join(id_path, file)
			# if os.path.isfile(file_path):
				# file_num += 1
		# bmp_num = (file_num/2)
		# file_attribute = open(attribute_path, "a+")
		# file_attribute.write(str(bmp_num) + " \n")
		# file_attribute.write("image_id emotion bread glass \n")
		# file_attribute.close()
		
	for root, dirs, files in os.walk(path):
		for file in files:
			pic_path = os.path.join(root, file)
			os.system(r"D:\fanyifu\face_database\fyf\testother.exe " + pic_path)
			
	file_out = open(out_path, 'r')
	lines = file_out.readlines()
	file_out.close()
	for i in range(len(lines)-1):
		if i%2 == 0:
			data = os.path.split(lines[i])
			data_path = data[0] + '\\'
			attribute_path = data_path + 'attribute.txt'
			print(attribute_path)
			data_result = lines[i+1]
			result_list = data_result.split(",")[3:]
			result = " ".join(result_list)
			attribute_file = open(attribute_path, "a")
			imformation = data[-1].strip() + ' ' + result
			attribute_file.write(imformation)
			attribute_file.write("\n")
			pass
			# if "hat: no" in data_result:
				# result = "0"
				# imformation = data[-1].strip() + ' ' + result
				# attribute_file.write(imformation)
				# attribute_file.write("\n")
			# if "hat: yes" in data_result:
				# result = "1"
				# imformation = data[-1].strip() + ' ' + result
				# attribute_file.write(imformation)
				# attribute_file.write("\n")
			# if "no face detect" in data_result:
				# result = "s"
				# imformation = data[-1].strip() + ' ' + result
				# attribute_file.write(imformation)
				# attribute_file.write("\n")
	
if __name__ == "__main__":
	main()
