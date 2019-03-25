# -*- coding: utf-8 -*-
import os
import csv
import json

import time
from conf import config
import xlrd


class Timer(object):
    def __init__(self, start=None):
        self.start = start if start is not None else time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_val is None

    def cost(self):
        print(time.time() - self.start)


def exl_json(exl_path):
    sceneList = "sceneList"
    test_case_list = "test_case_list"
    with open(config.csv_json_path, "w", encoding='utf-8') as jf:

        data = xlrd.open_workbook(os.path.join(exl_path, "test.xlsx"))
        table = data.sheets()[1]
        nrows = table.nrows
        dic_1 = {}
        value_list_1 = []
        value_list_2 = []
        value_list_3 = []
        rst_2 = []
        rst_3 = []
        key_1 = []
        key_2 = []
        key_3 = []
        for i in range(nrows):
            info = table.row_values(i)
            if i == 0:
                key_1 = info[:3]
                key_2 = info[3:7]
                key_3 = info[7:]
            else:
                value_1 = info[:3]
                value_2 = info[3:7]
                value_3 = info[7:]
                value_list_1.append(value_1)
                value_list_2.append(value_2)
                value_list_3.append(value_3)

        for v_1 in value_list_1:
            if v_1 != [""]*len(key_1):
                for i in range(len(key_1)):
                    dic_1[key_1[i]] = v_1[i]
        for v_2 in value_list_2:
            dic_2 = {}
            if v_2 != [""]*len(key_2):
                for i in range(len(key_2)):
                    dic_2[key_2[i]] = v_2[i]
                rst_2.append(dic_2)
        item_list = []
        #分割最后一组的分属
        for item in enumerate(value_list_3):
            if item[1] == [""]*len(key_3):
                item_list.append(item[0])
        item_list.append(len(value_list_3))
        num_list = []
        for i in range(1, len(item_list)):
            num = int(item_list[i]) - int(item_list[i-1]) -1
            if num >= 1:
                num_list.append(num)
        for v_3 in value_list_3:
            dic_3 = {}
            if v_3 != [""]*len(key_3):
                for i in range(len(key_3)):
                    dic_3[key_3[i]] = v_3[i]
                rst_3.append(dic_3)
        s = 0
        for i in range(len(rst_2)):
                s = s + num_list[i]
                rst_2[i][test_case_list] = rst_3[:s][-num_list[i]:]
        print(rst_2)
        dic_1[sceneList] = rst_2

        json.dump(dic_1, jf, indent=4)


if __name__ == "__main__":
    with Timer() as timer:
        exl_path = r"F:\pc"
        exl_json(exl_path)
    timer.cost()