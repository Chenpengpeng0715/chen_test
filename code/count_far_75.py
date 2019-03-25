import os

def main():
	root_path = os.getcwd()
	far_file = os.path.join(root_path, "FAR.txt")
	fin = open(far_file, 'r')
	threshold = 77.0
	cnt = 0

	for line in fin:
		if line.find("template") != -1 and line.find("result") != -1:
			words = line.split(',')
			score_word = words[3].split(':')

			score = float(score_word[1])
			if score >= threshold:
				cnt += 1
	print(cnt)
				
	
if __name__ == '__main__':
	main()