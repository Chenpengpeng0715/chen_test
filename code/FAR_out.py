#-*- coding: UTF-8 -*-
#向下取整
import os
from fractions import Fraction
def main():
	path = r"D:\fanyifu\result\B130\russia"
	file_path = os.path.join(path, "result.txt")
	with open(file_path, "r") as f:
		off = -100
		while True:
			f.seek(off, 2)
			lines = f.readlines()
			if len(lines) >= 3:
				last_line = lines[-1]
				fail = int(last_line.split(")")[1].split("(")[1])
				total = int(last_line.split(")")[2].split("(")[1])
				if fail == 0:
					result = 0
				else:
					c = int(total/fail)
					num = len(str(c))
					if c <= 100000:
						if c >= 10000:
							result1 = str(c)[0]
							result = result1 + ("0"*(num-1))
						else:
							result = c
					else:
						result2 = str(c)[:-5]
						result3 = str(c)[-5]
						if int(result3) < 5:
							result = result2 + "0"*5
						else:
							result = result2 + "5" + "0"*4
				FAR_result = Fraction(1, int(result))
				print(result)
				print(FAR_result)
				break
if __name__ == "__main__":
	main()