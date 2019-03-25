# coding: UTF-8
import os
import subprocess
import time
subprocess.Popen("adb devices")
cmds = [
	"cd data",
	"ls",
	"exit"  # 这是是非常关键的，退出
]
obj = subprocess.Popen("adb shell", shell= True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
info = obj.communicate(("\n".join(cmds) + "\n").encode('utf-8'));
for item in info:
	if item:
		print(item.decode('gbk'))