# -*- coding: utf-8 -*-
import os
import csv
import json
from collections import OrderedDict


def trans_file():
	with open(json_path, 'r') as f:
		json_data = json.load(f, object_hook=OrderedDict)
	print(json_data)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
if __name__ == "__main__":
	json_path = r"C:\Users\cwx520375\AppData\Local\conda\conda\envs\conda35\Lib\site-packages\BeautifulReport\conf\test_scene.json"
	csv_path = r""
	trans_file()