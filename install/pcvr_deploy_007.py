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
        切换语言后，检查上一步语言和用户协议显示
        """
        # 打开安装程序
        self.app.open(5)
        self.screen.wait(image_config.Install.install_home_page_path, 3)
        self.assertTrue(self.screen.exists(image_config.Install.install_home_page_path))
        self.assertTrue(self.screen.exists(image_config.Install.install_button_gray_path))

    def test_app_install_002(self):
        # 点击同意协议
        self.screen.click(image_config.Install.agreement_no_selected_path)
        self.screen.wait(image_config.Install.agreement_selected_path, 2)
        self.assertTrue(self.screen.exists(image_config.Install.agreement_selected_path))
        self.assertTrue(self.screen.exists(image_config.Install.install_button_high_light_path))

    def test_app_install_003(self):
        # 点击开始安装
        self.screen.click(image_config.Install.install_button_high_light_path)
        self.assertTrue(self.screen.exists(image_config.Install.install_home_page_2_path))

    def test_app_install_004(self):
        # 切换语言为英文
        self.screen.click(image_config.Install.language_path)
        self.screen.click(image_config.Install.install_folder_path)
        self.screen.click(image_config.Install.English_language_path)
        self.assertTrue(self.screen.exists(image_config.Install.install_home_page_English_2_path))

    def test_app_install_005(self):
        # 点击【上一步】
        self.screen.click(image_config.get_file_path()['BACK'])
        self.assertTrue(self.screen.exists(image_config.get_file_path()['install_home_page_English']))

    def test_app_install_006(self):
        # 点击【用户协议】
        self.screen.click(image_config.get_file_path()['install_agreement_English'])
        self.screen.wait(image_config.get_file_path()['agreement_page_English'], 1)
        self.assertTrue(self.screen.exists(image_config.get_file_path()['agreement_page_English']))

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
        os.popen("taskkill /im HwPCVRAssistant_9.0.0.105.tmp -f")