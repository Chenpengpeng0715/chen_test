# -*- coding: utf-8 -*-
# author: cwx520375 
# time: 2019/3/21

 
import os
import time
import unittest
from pcvr_conf import config
from jpype import *
from setup import setup
from pcvr_conf import image_config

app_path = config.client_path


class PCVRAssistantTestCase(unittest.TestCase):
    """
    class doc:  PCVRAssistantTestCase
    重复安装
    """

    def test_app_install_001(self):
        # 打开安装程序
        self.app.open(5)
        self.screen.click(image_config.Install.agreement_no_selected_path)
        self.screen.wait(image_config.Install.agreement_selected_path, 2)
        self.screen.click(image_config.Install.install_button_high_light_path)
        self.screen.wait(image_config.get_file_path()['install_home_page_2'], 2)
        self.screen.click(image_config.get_file_path()['next_step'])
        time.sleep(5)
        self.screen.wait(image_config.get_file_path()['install_complete'], 2)
        self.screen.click(image_config.get_file_path()['experience'])
        self.screen.wait(image_config.get_file_path()['control_panel_no_connected'], 5)
        self.assertTrue(self.screen.exists(image_config.get_file_path()['control_panel_no_connected']))

    def test_app_install_002(self):
        # 再次安装
        self.app.open(5)
        self.screen.wait(image_config.get_file_path()['repeat_install'], 3)
        self.assertTrue(self.screen.exists(image_config.get_file_path()['repeat_install']))
        # 点击【重试】
        self.screen.click(image_config.get_file_path()['repetition_install'])
        self.assertTrue(self.screen.exists(image_config.get_file_path()['repeat_install']))
        # 点击【取消】
        self.screen.click(image_config.get_file_path()['repetition_install_cancel'])
        time.sleep(0.5)
        self.assertFalse(self.screen.exists(image_config.get_file_path()['repeat_install']))

    def setUp(self):
        """
        卸载驱动
        不连接头盔
        :return:
        """
    def tearDown(self):
        """
        :return:
        """

    @classmethod
    def setUpClass(cls):
        """
        set up method
        :return:
        """
        # setup.setup(cls)
        startJVM(getDefaultJVMPath(), '-ea', r'-Djava.class.path=F:\PCVR\sikulix\new\sikulixapi.jar')
        Screen = JClass("org.sikuli.script.Screen")
        Key = JClass("org.sikuli.script.Key")
        APP = JClass("org.sikuli.script.App")
        cls.screen = Screen()
        cls.key = Key()
        cls.app = APP(app_path)

    @classmethod
    def tearDownClass(cls):
        """
        :param cls:
        :return:
        """
        # Screen = JClass("org.sikuli.script.Screen")
        # screen = Screen()
        # screen.click('img/close_install.PNG')
        # screen.click('img/close_install_make_sure_chinese.PNG')
        shutdownJVM()
        os.popen("taskkill /im HwPCVRAssistant.exe -f")