# -*- coding: utf-8 -*-
# author: cwx520375 
# time: 2019/3/21

import time
import unittest
from jpype import *
from pcvr_conf import image_config


class PCVRAssistantTestCase(unittest.TestCase):
    """
    class doc:  PCVRAssistantTestCase
    Exit
    在连接头盔情况下，点击最小化PC VR客户端
    """

    def test_app_close_001(self):
        # 将此处检查的图片改成已连接即可（control_panel_no_connected）
        self.screen.doubleClick(image_config.Common.client_path)
        self.screen.wait(image_config.ControlPanel.control_panel_no_connected_path, 5)
        self.screen.click(image_config.get_file_path()['control_minimize'])
        time.sleep(0.5)
        self.assertFalse(self.screen.exists(image_config.get_file_path()['control_panel_no_connected']))

    def setUp(self):
        """
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
        # cls.app = APP(app_path)

    @classmethod
    def tearDownClass(cls):
        """
        :param cls:
        :return:
        """
        shutdownJVM()