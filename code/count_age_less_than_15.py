import os

def main():
	path = r"D:\fanyifu\face_database\aboard\tmp\tmp\indore"
	cnt = 0
	for folder in os.listdir(path):
		words = folder.split('-')
		age = int(words[2])
		if age <= 15:
			cnt += 1
	print cnt

if __name__ == "__main__":
	main()