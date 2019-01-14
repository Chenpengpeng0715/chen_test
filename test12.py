# -*- coding: utf-8 -*-
import time

__author__ = 'l00346311'

from BeautifulReport import BeautifulReport
import uiautomation as automation
import subprocess
import unittest
import os

rtc = automation.GetRootControl()

app_path = r"C:\Program Files (x86)\Huawei VR2 Updater\WalleXPCUpgrader.exe"


class UIVR2UpgradeToolTestCase(unittest.TestCase):
    """
    class doc:  UIVR2UpgradeToolTestCase
    升级检测环节点击关闭和检测环节点击关闭
    """
    img_path = 'img'
    current_value = ''

    def save_img(self, img_name):
        rtc.CaptureToImage('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    @BeautifulReport.add_test_img('test02')
    def test_app_install_1_agree(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        install_lang_window.ButtonControl(Name='同意').Click()

    def test_app_install_2_click_update(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        install_lang_window.ButtonControl(Name='一键升级').Click()
    #   time.sleep(5)
    def test_app_install_3_click_close(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                     ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        install_lang_window.ButtonControl(Name='关闭').Click()

        self.assertTrue(automation.TextControl(searchDepth=1, ClassName="Static"))

    def test_app_install_4_click_YES(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.8.app.app.0.2bf8098_r36_ad1")
        install_lang_window.ButtonControl(Name='是(Y)').Click()
        self.assertFalse(automation.TextControl(searchDepth=1, ClassName="WindowsForms10.STATIC.app.0.2bf8098_r36_ad1"))

    def test_app_install_5_click_NO(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.8.app.app.0.2bf8098_r36_ad1")
        install_lang_window.ButtonControl(Name='否(N)').Click()
        self.assertTrue(automation.EditControl(searchDepth=1, ClassName="WindowsForms10.STATIC.app.0.2bf8098_r36_ad1"))

    def setUp(self):
        """
        头盔连接下
        :return:
        """

    @classmethod
    def setUpClass(cls):
        """
        set up method
        :return:
        """
        if 1:
            app_p = subprocess.Popen(app_path)
            time.sleep(0.5)

    def tearDown(self):
        """

        :return:
        """

    @classmethod
    def tearDownClass(cls):
        """

        :param cls:
        :return:
        """