import os

def main():
	log_path = os.getcwd()
	find_fa(log_path)
	# calculate_frr(log_path)
	
def find_fa(log_path):
	src_path = os.path.join(log_path, "FAR.txt")
	dest_path = os.path.join(log_path, "result.txt")
	fsrc = open(src_path, 'r')
	fdest = open(dest_path, 'w')
	lines = []
	flag = 0
	end_flag = 0
	for line in fsrc:
		if line.find("pic") != -1 and line.find("isNoFace") != -1:
			lines.append(line)
			flag = 1
			continue
		if line.find("result") != -1 and line.find("FAR") != -1:
			lines.append(line)
			if line.find("result:sucess") != -1:
				for line1 in lines:
					if line1.find("result:fail") == -1:
						fdest.write(line1)
			lines = []
			flag = 0
		if flag == 1:
			lines.append(line)
			continue
		if line.find("Test_FAR End") != -1:
			end_flag = 1
		if end_flag == 1 and line.find("FAR") != -1:
			fdest.write(line)
	
def calculate_frr(log_path):
	frr_path = os.path.join(log_path, "FRR.txt")
	fin = open(frr_path, 'r')
	lines = []
	flag = 0
	check_flag = 0
	cnt = 0
	point = 83
	for line in fin:
		if line.find("pic") != -1 and line.find("isNoFace") != -1:
			flag = 1
			continue
		if line.find("result") != -1 and line.find("FRR") != -1:
			for line1 in lines:
				words = line1.split(',')
				tmp = words[3].split(':')
				score = float(tmp[1])
				if score >= 73 and score < 80:
					check_flag = 1
			if check_flag == 0:
				cnt += 1
			lines = []
			check_flag = 0
			flag = 0
		if flag == 1:
			lines.append(line)
			continue
	print("number is %d"%cnt)
			
if __name__ == '__main__':
    main()