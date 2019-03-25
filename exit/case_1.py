# -*- coding: utf-8 -*-
# author: cwx520375 
# time: 2019/3/19

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
    Exit
    在未连接头盔情况下，点击关闭来关闭PC VR客户端
    """

    def test_app_close_001(self):
        self.screen.click(image_config.Common.client_path)
        self.screen.wait(image_config.ControlPanel.control_panel_no_connected_path)
        self.screen.click(image_config.ControlPanel.control_close_path)
        time.sleep(2)
        self.screen.wait(image_config.ControlPanel.control_panel_no_connected_path)
        self.assertFalse(self.screen.exist(image_config.ControlPanel.control_panel_no_connected_path))

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
