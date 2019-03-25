# -*- coding: utf-8 -*-
# author: cwx520375 
# time: 2019/3/5
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
        time.sleep(3)
        self.assertTrue(self.screen.exists(image_config.Install.install_home_page_path))

    def test_app_install_002(self):
        """
        勾选用户同意,检测PC VR助手安装主页面正常显示
        """
        self.screen.click(image_config.Install.agreement_no_selected_path)
        self.screen.wait(image_config.Install.agreement_selected_path, 2)
        self.assertTrue(self.screen.exists(image_config.Install.agreement_selected_path))
        self.assertTrue(self.screen.exists(image_config.Install.install_button_highlight_path))

    def test_app_install_003(self):
        """
        关闭安装页面
        """
        self.screen.click(image_config.Install.install_close_path)
        self.screen.wait(image_config.Install.cancel_install_path, 2)
        self.assertTrue(self.screen.exists(image_config.Install.cancel_install_path))

    def test_app_install_004(self):
        """
        点击关闭,不终止安装
        """
        self.screen.click(image_config.Install.terminate_install_close_path)
        self.screen.wait(image_config.Install.agree_home_page_path, 3)
        self.assertTrue(self.screen.exists(image_config.Install.agree_home_page_path))

    @unittest.SkipTest
    def test_app_install_00(self):
        """
        点击取消,不终止安装
        """
        self.screen.click(image_config.Install.terminate_install_cancel_path)
        self.screen.wait(image_config.Install.agreen_home_page_path)
        self.assertTrue(self.screen.exists(image_config.Install.agreen_home_page_path))

    @unittest.SkipTest
    def test_app_install_00(self):
        """
        点击确定终止安装
        """
        self.screen.click(image_config.Install.terminate_install_confirm_path)
        self.screen.wait(image_config.Install.agreen_home_page_path)
        self.assertFalse(self.screen.exists(image_config.Install.agreen_home_page_path))

    def test_app_install_005(self):
        """
        点击安装，进入下一页
        :return:
        """
        self.screen.click(image_config.Install.install_button_highlight_path)
        self.screen.wait(image_config.Install.install_home_page_2_path, 3)
        self.assertTrue(self.screen.exists(image_config.Install.install_home_page_2_path))

    def test_app_install_006(self):
        """
        点击上一步，点击安装，点击下一步
        :return:
        """
        self.screen.click(image_config.Install.last_step_path)
        self.screen.wait(image_config.Install.agree_home_page_path)
        self.assertTrue(self.screen.exists(image_config.Install.agree_home_page_path))

        self.screen.click(image_config.Install.next_step_path)
        self.screen.wait(image_config.Install.install_complete_path, 10)
        self.assertTrue(self.screen.exists(image_config.Install.install_complete_path))

    def test_app_install_007(self):
        """
        未连接头盔，点击立即体验
        :return:
        """
        self.screen.click(image_config.Install.experience_path)
        self.screen.wait(image_config.ControlPanel.control_panel_no_conneted_path)
        self.assertTrue(self.screen.exists(image_config.ControlPanel.control_panel_no_conneted_path))

    def test_app_install_008(self):
        """
        已连接头盔，点击立即体验
        :return:
        """
        pass

    def test_app_install_009(self):
        """
        重复安装
        :return:
        """
        self.app.open(5)
        self.screen.wait(image_config.Install.repeat_install_path)
        self.assertTrue(self.screen.exists(image_config.Install.repeat_install_path))
        "点击重试"
        self.screen.click(image_config.Install.repetition_install_path)
        self.assertTrue(self.screen.exists(image_config.Install.repeat_install_path))
        "点击取消或者直接关闭"
        self.screen.click(image_config.Install.repetition_install_cancel_path)
        # self.screen.click(image_config.Install.repetition_install_close_path)
        self.assertFalse(self.screen.exists(image_config.Install.repeat_install_path))

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
        # os.popen("taskkill /im HwPCVRAssistant_9.0.0.105.tmp -f")
        # os.popen("taskkill /im HwPCVRAssistant.exe -f")