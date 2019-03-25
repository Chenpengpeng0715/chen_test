# # -*- coding: utf-8 -*-
# import tkinter
# from BeautifulReport import BeautifulReport
# import uiautomation as automation
# import subprocess
# import unittest
# import os
# import time
# from uiautomation import *
# from tkinter import messagebox
# # box = tkinter.Tk()
# # box.title("button_info")
# # theLabel = tkinter.Label(box, text="控件属性")
# # list_info = ['1', '2', '2', '3']
# #
# # list_gui = tkinter.Listbox(box)
# #
# # for i in list_info:
# #     list_gui.insert(0, i)
# #
# #
# # theLabel.pack()
# # list_gui.pack()
# # box.mainloop()
# """
# path = r"F:\pc_update\HuaweiVR2Updater-installer8.0.0.303_dfu266.exe"
#
# def test_1():
#
#     subprocess.Popen(path)
#     time.sleep(0.5)
#
#     install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TSelectLanguageForm")
#     install_lang_window.ButtonControl(Name='确定').Click()
#     time.sleep(0.5)
#     # 点击下一步
#     install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
#     install_lang_window.ButtonControl(Name='下一步(N) >').Click()
#     time.sleep(0.5)
#     # install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
#     # install_lang_window.ButtonControl(Name='关闭').Click()
#
#     install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
#     install_lang_window.CheckBoxControl(Name='创建桌面快捷方式(&D)').Click()
#
#     install_lang_window.Close()
# if __name__ == '__main__':
#     test_1()
# """
#
# def test():
#     control = ControlFromCursor()
#     if control:
#         a = EnumAndLogControlAncestors(control, showAllName=True, showMore=True)
#         messagebox.showinfo(a)
#     else:
#         print("++")
#
# def tker():
#     root = tkinter.Tk()
#     root.geometry("100x100")
#     theLabel = tkinter.Label(root, text="控件属性")
#     button = tkinter.Button(root, text="Click", command=test())
#     button.pack()
#     root.mainloop()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# if __name__ == "__main__":
#     tker()
# -*- coding: utf-8 -*-
import os
import time

__author__ = 'l00346311'

import uiautomation as automation
from tkinter import *
import sys

class WindowList(object):
    def __init__(self):
        self.top = Tk()  # 初始化主窗口的顶层容器
        self.top.title('Windows CheckList')
        self.label = Label(self.top, text='Windows CheckList v1.0')  # 标签控件；可以显示文本和位图
        self.label.pack(anchor=E)  # 包装
        # 显示当前窗体的名称
        self._string_var = StringVar(master=self.top)  # 跟踪变量的值的变化，以保证值的变更随时可以显示在界面上
        # self._string_var.set('Detect will execute after 3 second ...')
        # 设置一个标签，用于显示当前检测到窗体的名称
        self.window_name = Label(self.top, fg='blue', font=('Helvetica', 11, 'bold'))
        self.window_name.pack()
        # 定义显示结果信息窗口
        # 一个容器窗口部件。帧可以有边框和背景，当创建一个应用程序或dialog(对话）版面时，帧被用来组织其它的窗口部件。
        self.window_fm = Frame(self.top)
        self.window_sb = Scrollbar(self.window_fm)  # 滚动滚动条
        self.window_sb.pack(side=RIGHT, fill=Y)
        self.window = Listbox(self.window_fm, height=25, width=100, setgrid=True,
                              selectmode=EXTENDED, yscrollcommand=self.window_sb.set,
                              borderwidth=5, font=('Helvetica', 12,))
        self.window_sb.config(command=self.window.yview)
        self.window.pack(side=LEFT, fill=BOTH, ipadx=10, expand=True)
        self.window_fm.pack(fill=BOTH, expand=True)
        # self.dirn = Entry(self.top, width=50, textvariable=self._string_var)
        # self.dirn.pack()
        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text='Clear', command=self.clrmothod,
                          activeforeground='white', activebackground='blue')
        self.check = Button(self.bfm, text='Detect', command=self.checkmothod,
                            activeforeground='white', activebackground='green')
        self.checkall = Button(self.bfm, text='Detect Total', command=lambda: self.checkmothod(total=True),
                               activeforeground='white', activebackground='green')
        self.quit = Button(self.bfm, text='Quit', command=self.top.quit,
                           activeforeground='white', activebackground='red')

        self.clr.pack(side=LEFT, padx=5)
        self.check.pack(side=LEFT, padx=5)
        self.checkall.pack(side=LEFT, padx=5)
        self.quit.pack(side=LEFT, padx=5)
        self.bfm.pack()
        self.window_name.config(text='Please Click Detect Button or Detect Total Button to detect windows.')

    def checkmothod(self, total=None):
        self.detect_one(total)
        self.window.config(
            selectbackground='LightSkyBlue')

    def clrmothod(self):
        self.window_name.config(text='Please Click Detect Button or Detect Total Button to detect windows.')
        self.window.delete(0, END)

    def detect_one(self, total=None):
        self.window_name.config(text='Detect will execute after 3 second ...')
        self.top.update()
        time.sleep(3)
        depth = 0xFFFFFFFF
        showAllName = True
        showMore = True
        if total:
            control = automation.GetFocusedControl()
            controlList = []
            while control:
                controlList.insert(0, control)
                control = control.GetParentControl()
            if len(controlList) == 1:
                control = controlList[0]
            else:
                control = controlList[1]
            savedStdout = sys.stdout
            with open('out.txt', 'w+') as file:
                sys.stdout = file
                automation.EnumAndLogControl(control, depth, showAllName, showMore)
            sys.stdout = savedStdout
        else:
            control = automation.ControlFromCursor()
            savedStdout = sys.stdout
            with open('out.txt', 'w+') as file:
                sys.stdout = file
                automation.EnumAndLogControlAncestors(control, showAllName=True, showMore=True)
            sys.stdout = savedStdout

        with open('out.txt', 'r') as file:
            for line in file.readlines():
                if line != "":
                    self.window.insert(END, line)
        self.window_name.config(text='Detect Result:')


if __name__ == '__main__':
    d = WindowList()
    mainloop()

