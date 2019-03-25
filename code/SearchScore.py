#-*- coding: UTF-8 -*-
import shutil
import os

def main():
    root = os.getcwd()
    root_path = r"D:\fanyifu\face_database\aboard\tmp\Egypt"
    dest_path = r"D:\fanyifu\face_database_error\B130\aiji"
    path = os.path.join(root, "FRR.txt")
    #score = raw_input("plase input score :")
    SearchScore(path, root_path, dest_path)
#copy不合格的图片，并按不同ID计算各自不合格的张数，再排序
def SearchScore(path, root_path, dest_path):
    flag = 0
    dict = {}
    fin = open(path, 'r')
    # for i in range(10):
    #     if not os.path.exists(os.path.join(dest_path, str(i))):
    #         os.mkdirs(os.path.join(dest_path, str(i)))
    for line in fin:
        if line.find("pic") != -1 and line.find("isNoFace") != -1:
            pic = line.split('/')
            file_path = os.path.join(root_path, pic[3])
            pic_bmp = pic[4].split(',')[0]
            pic_short = os.path.splitext(pic_bmp)[0] + '.short'
            filename_bmp = os.path.join(file_path, pic_bmp)
            filename_short = os.path.splitext(filename_bmp)[0] + '.short'
        if line.find("template") != -1 and line.find("isNoFace") != -1:
            templata = line.split('/')[5]
            templata_result = templata.split(',')[2]
            result = float(templata_result.split(':')[1])
            if result == "fail":
                score_num_int = int(score_num)/10
                if not os.path.exists(os.path.join(dest_path, str(score_num_int))):
                    os.makedirs(os.path.join(dest_path, str(score_num_int)))
                newpath = os.path.join(dest_path, str(score_num_int))
                bmp_newpath = os.path.join(newpath, pic[3] + "," + str(score_num) + '-' + pic_bmp)
                short_newpath = os.path.join(newpath, pic[3] + "," + str(score_num) + '-' + pic_short)
                if os.path.exists(filename_bmp) and os.path.exists(filename_short):
                    shutil.copy(filename_bmp, bmp_newpath)
                    print("%s copy completed"%pic_bmp)
                    shutil.copy(filename_short, short_newpath)
                    print("%s copy completed"%pic_short)
                if score_num_int in dict.keys():
                    dict[score_num_int] += 1
                else:
                    dict[score_num_int] = 1
            else:
                continue
    print(dict)

    # if not os.path.exists(os.path.join(dest_path, "ScoreResult.txt")):
    #     path1 = os.path.join(dest_path, "ScoreResult.txt")
    #     f = file(path1, "w")
    #     fp = open(path1, 'a')
    #     for i in range(len(dict)):
    #         # new_line = []
    #         # new_line = list(dit[i])
    #         # print(new_line)
    #         # # print (type(new_line))
    #         # for j in range(len(new_line)):
    #         #     s = new_line[j]
    #         #     print(s)
    #         #     fp.write(s)
    #         fp.write(str(dict[i]) + ':' + str(dict[i]))
    #         fp.writelines('\n')
        # fp.close()
	fin.close()
if __name__ == '__main__':
        main()