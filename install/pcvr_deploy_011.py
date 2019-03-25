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
    install
    """

    def test_app_install_001(self):
        """
        安装完成，点击立即体验（不插头盔 英文）
        """
        # 打开安装程序
        self.app.open(5)
        self.screen.click(image_config.Install.agreement_no_selected_path)
        self.screen.wait(image_config.Install.agreement_selected_path, 2)
        self.screen.click(image_config.Install.install_button_high_light_path)
        self.screen.wait(image_config.get_file_path()['install_home_page_2'], 2)

    def test_app_install_002(self):
        # 选择【English】
        self.screen.click(image_config.get_file_path()['language'])
        time.sleep(0.5)
        self.screen.click(image_config.get_file_path()['English_language'])
        time.sleep(1)
        self.assertTrue(self.screen.exists(image_config.get_file_path()['install_home_page_English_2']))

    def test_app_install_003(self):
        # 点击【NEXT】
        self.screen.click(image_config.get_file_path()['NEXT'])
        time.sleep(5)
        self.screen.wait(image_config.get_file_path()['install_complete_English'], 2)

    def test_app_install_004(self):
        # 点击【立即体验】
        self.screen.click(image_config.get_file_path()['experience_English'])
        self.screen.wait(image_config.get_file_path()['control_panel_no_connected_English'], 5)
        self.assertTrue(self.screen.exists(image_config.get_file_path()['control_panel_no_connected_English']))

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