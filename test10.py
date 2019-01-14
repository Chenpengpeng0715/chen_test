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
    点击“华为VR2升级工具使用协议”
    """
    img_path = 'img'
    current_value = ''

    def save_img(self, img_name):
        rtc.CaptureToImage('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    @BeautifulReport.add_test_img('test02')
    def test_app_install_1_default_language_Chinese(self):
        # self.save_img('test10')
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        self.current_value = install_lang_window.ComboBoxControl().CurrentValue()
        # 检查是否默认中文
        self.assertEqual(self.current_value, "中文")

    def test_app_install_2_click_Agreement(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                     ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        install_lang_window.TextControl(Name='华为VR2升级工具使用协议').Click()

    @unittest.SkipTest
    def test_app_install_3_check_agreement(self):
        self.assertTrue(automation.EditControl(searchDepth=1,
                                               ClassName="WindowsForms10.EDIT.app.0.2bf8098_r36_ad1"))
        install_lang_window = automation.EditControl(searchDepth=1,
                                                     ClassName="WindowsForms10.EDIT.app.0.2bf8098_r36_ad1")
        self.current_value = install_lang_window.EditControl().CurrentValue()
        if "华为VR2升级工具使用协议" in self.current_value:
            return True
        else:
            print("language error")

    def test_app_install_4_click_close(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.EDIT.app.0.2bf8098_r36_ad1")
        install_lang_window.ButtonControl(Name='关闭').Click()

    def test_app_install_5_check_close(self):
        self.assertFalse(automation.EditControl(searchDepth=1, ClassName="WindowsForms10.EDIT.app.0.2bf8098_r36_ad1"))

    def setUp(self):
        """
        默认中文情况下
        :return:
        """

    @classmethod
    def setUpClass(cls):
        """
        set up method
        :return:
        """
        if 1:
            # automation.ShowDesktop()
            app_p = subprocess.Popen(app_path)
            time.sleep(0.5)
            # type(automation.WindowControl(ClassName="TSelectLanguageForm").Exists(maxSearchSeconds=1))
            # print(automation.WindowControl(ClassName="TSelectLanguageForm").Exists())

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