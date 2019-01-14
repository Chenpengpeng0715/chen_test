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
    语言选择（中英文切换）
    """
    img_path = 'img'
    current_value = ''

    def save_img(self, img_name):
        rtc.CaptureToImage('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    @unittest.SkipTest
    @BeautifulReport.add_test_img('test02')
    def test_app_install_1_default_select_off(self):
        self.save_img('test02')
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        self.current_value = install_lang_window.CheckBoxControl().CurrentValue()
        # 检查是否默认不选中
        self.assertEqual(self.current_value, "ToggleState.Off")

    @unittest.SkipTest
    def test_app_install_2_select_on(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        install_lang_window.ButtonControl(Name='同意').Click()

    @unittest.SkipTest
    def test_app_install_3_select_on_check(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        self.current_value = install_lang_window.CheckBoxControl().CurrentValue()
        # 检查是否选中
        self.assertEqual(self.current_value, "ToggleState.On")

    def test_app_install_2_select_lang_chinese(self):
        """

        :return:
        """
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")

        self.assertTrue(install_lang_window)

        install_lang_window.ComboBoxControl(ClassName='WindowsForms10.COMBOBOX.app.0.2bf8098_r36_ad1').Select(
            name='English')
        self.current_value = install_lang_window.ComboBoxControl(
            ClassName='WindowsForms10.BUTTON.app.0.2bf8098_r36_ad1').CurrentValue()
        self.save_img('Select_Language_English')
        self.assertEqual(self.current_value, 'Update')

        install_lang_window.ComboBoxControl(ClassName='WindowsForms10.COMBOBOX.app.0.2bf8098_r36_ad1').Select(name='中文')
        self.current_value = install_lang_window.ComboBoxControl(
            ClassName='WindowsForms10.BUTTON.app.0.2bf8098_r36_ad1').CurrentValue()
        self.save_img('Select_Language_Chinese')
        self.assertEqual(self.current_value, '一键升级')


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