# -*- coding: utf-8 -*-
# author: cwx520375 
# time: 2019/3/11

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
    uninstall
    """

    def test_app_uninstall_001(self):
        """
        打开文件位置,运行PC VR情况下卸载
        """
        if self.screen.exists(image_config.Common.client_path):
            self.screen.click(image_config.Common.client_path)
            self.screen.rightClick(image_config.Common.client_path)
            self.screen.click(image_config.Uninstall.file_folder_path)
            self.screen.click(image_config.Uninstall.max_size_path)
            self.screen.doubleClick(image_config.Uninstall.uninstall_path)
            self.screen.wait(image_config.Uninstall.prompt_path, 3)
            self.assertTrue(self.screen.exists(image_config.Uninstall.prompt_path))
            self.screen.click(image_config.Uninstall.repetition_path)  # 点击重试
            self.assertTrue(self.screen.exists(image_config.Uninstall.prompt_path))
            self.screen.click(image_config.Uninstall.cancel_path)  # 点击取消
            self.assertFalse(self.screen.exists(image_config.Uninstall.prompt_path))

    def test_app_uninstall_002(self):
        """
        PCVR 不运行的情况下卸载
        :return:
        """
        if self.screen.exists(image_config.Common.client_path):
            self.screen.click(image_config.Common.client_path)
            self.screen.rightClick(image_config.Common.client_path)
            self.screen.click(image_config.Uninstall.file_folder_path)
            if not self.screen.exists(image_config.Uninstall.recover_size_path):
                self.screen.click(image_config.Uninstall.max_size_path)
            time.sleep(2)
            self.screen.doubleClick(image_config.Uninstall.uninstall_path)
            self.screen.wait(image_config.Uninstall.uninstall_guide_path, 3)
            self.assertTrue(self.screen.exists(image_config.Uninstall.uninstall_guide_path))
            # self.screen.click(image_config.Uninstall.no_path)  # 点击否
            # time.sleep(2)
            # self.assertFalse(self.screen.exists(image_config.Uninstall.uninstall_guide_path))
            self.screen.click(image_config.Uninstall.yes_path)  # 点击是
            self.screen.wait(image_config.Uninstall.uninstall_completed_path)
            self.assertTrue(self.screen.exists(image_config.Uninstall.uninstall_completed_path))
            self.screen.click(image_config.Uninstall.confirm_path)  # 点击确定
            time.sleep(1)
            self.assertFalse(self.screen.exists(image_config.Uninstall.uninstall_completed_path))
            self.assertFalse(self.screen.exists(image_config.Common.client_path))

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

