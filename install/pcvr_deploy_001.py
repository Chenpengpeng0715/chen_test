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
        检测PC VR助手安装主页面与用户协议的正常显示
        """
        self.app.open(5)
        self.screen.wait(image_config.Install.install_home_page_path, 3)
        self.assertTrue(self.screen.exists(image_config.Install.install_home_page_path))
        self.assertTrue(self.screen.exists(image_config.Install.install_button_gray_path))

        self.screen.click(image_config.Install.install_agreement_path)
        self.screen.wait(image_config.Install.agreement_page_path, 3)
        self.assertTrue(self.screen.exists(image_config.Install.agreement_page_path))

        self.screen.click(image_config.Install.agreement_confirm_button_path)
        # self.screen.wait(image_config.Install.install_home_page_path, 5)
        time.sleep(1)
        self.assertTrue(self.screen.exists(image_config.Install.install_home_page_path))

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