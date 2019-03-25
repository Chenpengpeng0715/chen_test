#-*- coding: UTF-8 -*-
import os
#单因子分析
def main():
	root = os.getcwd()
	path = r"D:\fanyifu\face_database\test\black"
	template_dic = {}
	id_dic = {}
	for id in os.listdir(path):
		id_path = os.path.join(path, id)
		template_path = os.path.join(id_path, "template")
		file_template = open(os.path.join(template_path, "attribute.txt"), "r")
		template_list = file_template.readlines()
		attributes = template_list[1].split(" ")[1:]
		for j in range(len(template_list)):
			if j >= 2:
				template_info = template_list[j].split(" ")
				template_name = id + template_info[0]
				template = template_info[1:len(template_info)]
				template_dic[template_name] = template	
		file_id = open(os.path.join(id_path, "attribute.txt"), "r")
		id_list = file_id.readlines()
		for i in range(len(id_list)):
			if i >= 2:
				id_info = id_list[i].split(" ")
				id_name = id + id_info[0]
				match = id_info[1:len(id_info)]
				id_dic[id_name] = match		
	success_dic = dict()
	total_dic = dict()
	score_dic = dict()
	success_score_dic = dict()
	attribute_list = []
	for attribute in attributes:
		success_dic.update([(attribute, [[0, 0], [0, 0]])])
		total_dic.update([(attribute, [[0, 0], [0, 0]])])
		score_dic.update([(attribute, [[0, 0], [0, 0]])])
		success_score_dic.update([(attribute, [[0, 0], [0, 0]])])
		attribute_list.append(attribute)
	file_frr = open(os.path.join(root, "FRR.txt"), "r")
	flag = 0
	for line in file_frr:
		if line.find("pic") != -1 and line.find("isNoFace") != -1:
			id_name = line.split("/")[3]
			pic_name = line.split("/")[4].split(",")[0]
			id_pic = id_name + pic_name
			match_1 = id_dic[id_pic]
			flag = 0
			continue
		if line.find("template") != -1 and line.find("isNoFace") != -1:
			result = line.split(",")[2]
			template_id = line.split("/")[3]
			template_pic = line.split("/")[5].split(",")[0]
			score = float(line.split(",")[3].split(":")[1])
			id_template = template_id + template_pic		
			template_1 = template_dic[id_template]
			for i in range(len(total_dic)):
				total_dic.get(attribute_list[i])[int(template_1[i])][int(match_1[i])] += 1
				score_dic.get(attribute_list[i])[int(template_1[i])][int(match_1[i])] += score
				if result == " result:sucess":
					success_dic.get(attribute_list[i])[int(template_1[i])][int(match_1[i])] += 1
					success_score_dic.get(attribute_list[i])[int(template_1[i])][int(match_1[i])] += score
			flag = 0
			continue
		if line.find("result") != -1 and line.find("FAR") != -1:
			flag = 1	
			break	
	for key in total_dic.keys():
		for i in range(2):
			for j in range(2):
				total_value = int(total_dic[key][i][j])
				success_value = int(success_dic[key][i][j])
				score_value = int(score_dic[key][i][j])
				success_score_value = int(success_score_dic[key][i][j])
				if total_value != 0:
					success_result = success_value/total_value
					score_result = score_value/total_value
					success_score_result = success_score_value/total_value
					success_ij = float("%.2f"% success_result)
					print("%s: %d%d: %d"%(key,i,j,success_ij))#单因子结果
					print("+++++++++++++++++++++++++++++++++++++++++")
					print("%s: %d%d: %d"%(key,i,j,score_result))
					print("=======================================")
					print("%s: %d%d: %d"%(key,i,j,success_score_result))
			
	print(total_dic)	
	print(success_dic)
	print(score_dic)
	print(success_score_dic)
if __name__ == "__main__":
	main()