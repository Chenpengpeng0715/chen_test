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
    首次使用（未安装驱动）
    """
    img_path = 'img'
    current_value = ''

    def save_img(self, img_name):
        rtc.CaptureToImage('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    @BeautifulReport.add_test_img('test02')
    def test_app_install_1_default_select_off(self):
        self.save_img('test02')
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        self.current_value = install_lang_window.CheckBoxControl().CurrentToggleState()
        # 检查是否默认不选中
        self.assertEqual(self.current_value, 0)

    @unittest.SkipTest
    def test_app_install_2_select_on(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        install_lang_window.ButtonControl(Name='同意').Click()

    @unittest.SkipTest
    def test_app_install_3_select_on_check(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        self.current_value = install_lang_window.CheckBoxControl().CurrentToggleState()
        # 检查是否选中
        self.assertEqual(self.current_value, 1)

    def test_app_install_4_select_update(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        install_lang_window.ButtonControl(Name='一键升级').Click()

    def test_app_install_5_install_driver(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="#32770")
        self.current_value = install_lang_window.TextControl().AccessibleCurrentName()
        self.assertEqual(self.current_value, "欢迎使用设备驱动程序安装向导!")
        install_lang_window.ButtonControl(Name='下一步(N) >').Click()

    def test_app_install_6_install_driver_check(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="#32770")
        self.current_value = install_lang_window.TextControl().AccessibleCurrentName()
        self.assertEqual(self.current_value, "设备已更新")

    def test_app_install_7_install_driver_end(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        install_lang_window.ButtonControl(Name='完成').Click()
    #不接头盔
    @unittest.SkipTest
    def test_app_install_8_driver_over_NOHMD(self):
        install_lang_window = automation.WindowControl(searchDepth=1,
                                                       ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        self.current_value = install_lang_window.TextControl().AccessibleCurrentName()
        self.assertEqual(self.current_value, "未识别到头盔设备，请确认头盔连接电脑")
        install_lang_window.ButtonControl(Name='确定').Click()

    def test_app_install_9_driver_over_NOHMD_check(self):
        self.assertTrue(automation.WindowControl(searchDepth=1, ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1"))

    def setUp(self):
        """
        卸载驱动
        不连接头盔
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