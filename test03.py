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
    不勾选使用协议
    """
    img_path = 'img'
    current_value = ''

    def save_img(self, img_name):
        rtc.CaptureToImage('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    @BeautifulReport.add_test_img('test02')

    def test_app_install_1_default_select_off(self):
        time.sleep(0.5)
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        self.current_value = install_lang_window.CheckBoxControl().CurrentToggleState()
        install_lang_window.CheckBoxControl().CurrentToggleState()
        # 检查是否默认不选中
        self.assertEqual(self.current_value, 0)

    @unittest.SkipTest
    def test_app_install_21_select_on_test(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        install_lang_window.CheckBoxControl(Name='同意').Click()

    @unittest.SkipTest
    def test_app_install_22_select_on_check(self):
        time.sleep(0.5)
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        self.current_value = install_lang_window.CheckBoxControl().CurrentToggleState()
        # 检查是否选中
        self.assertEqual(self.current_value, 1)

    def test_app_install_2_select_update(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        install_lang_window.ButtonControl(Name='一键升级').Click()

    def test_app_install_3_select_update_check(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        self.current_value = install_lang_window.TextControl().AccessibleCurrentName()
        print(self.current_value)
        self.assertEqual(self.current_value, "请勾选同意华为VR2升级工具使用协议")

    def test_app_install_4_select_update_argee(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        install_lang_window.ButtonControl(Name='确定').Click()#Name='关闭'

    def test_app_install_5_select_update_argee_check(self):
        self.assertTrue(automation.WindowControl(searchDepth=1, ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1"))

    def setUp(self):
        """

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
            subprocess.Popen(app_path)
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