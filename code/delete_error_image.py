import os
#删除手机中规格中制定不可解的图片
def main():
    root_path = r"D:\fanyifu\face_database_error\B113\aboard\mexico"
    delete_error_image(root_path)

def delete_error_image(root_path):
    dirs = os.listdir(root_path)
    # print(dirs)
    for files in dirs:
        if os.path.isdir(os.path.join(root_path, files)):
        #print (files)
            for file_name in os.listdir(os.path.join(root_path, files)):
                if os.path.splitext(file_name)[1] == ".bmp" or os.path.splitext(file_name)[1] == ".short":
                    ID = file_name.split(",")[0]
                    image_name = file_name.split("-")[1]
                    # print(image_name)
                    os.popen("adb shell rm /data/faceidUnitTest/" + ID + "/" + image_name)
                    print("delete %s completed" % image_name)
if __name__ == '__main__':
    main()