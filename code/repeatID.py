#-*- coding: UTF-8 -*-
import os
#检索出重复的ID
#keys = ("01", "01", "12", "23")
#dest_path = os.path.join("result.txt")
def main():

    root = os.getcwd()
    path = os.path.join(root, "result.txt")
    fin = open(path, 'r')
    line_result = []
    result = []
    count = []
    flag = 0
    for line in fin:
        if line.find("pic") != -1 and line.find("isNoFace") != -1:
            pic_1 = line.split('/')
            pic = pic_1[3]
            line_result.append(pic)
            flag = 1
            continue
        if line.find("template") != -1 and line.find("isNoFace") != -1:
            temp_1 = line.split('/')
            temp = temp_1[3]
            line_result.append(temp)
            continue
        if line.find("result") != -1 and line.find("FAR") != -1:
            flag = 0
            list1 = line_result[:2]
            list1.sort()
            key = list1[0] + ',' + list1[1]
            flag1 = 0
            for i in range(len(result)):
                if key == result[i]:
                    count[i] += 1
                    flag1 = 1
                    break
            if flag1 == 0:
                result.append(key)
                count.append(1)
            line_result = []
    result1 = []
    final_result = []
    d = {}
	
    for i in range(len(result)):
        result1.append(result[i].split(','))
        str1 = result1[i][0] + 'and' + result1[i][1]
        final_result.append(str1)
        d[final_result[i]] = count[i]
        dit = sorted(d.items(), key=lambda k: k[1], reverse=True)
    print (dit)
    path1 = os.path.join(root, "test.txt")
    f = file(path1, "w")
    fp = open(path1, 'a')
    for i in range(len(dit)):
        # new_line = []
        # new_line = list(dit[i])
        # print(new_line)
        # # print (type(new_line))
        # for j in range(len(new_line)):
        #     s = new_line[j]
        #     print(s)
        #     fp.write(s)
        fp.write(dit[i][0]+':'+str(dit[i][1]))
        fp.writelines('\n')
    fp.close()
    fin.close()

if __name__ == '__main__':
    main()