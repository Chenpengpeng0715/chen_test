# -*- coding: utf-8 -*-
import time

__author__ = 'l00346311'

from BeautifulReport import BeautifulReport
import uiautomation as automation
import subprocess
import unittest
import os

rtc = automation.GetRootControl()

app_path = r"F:\pc_update\HuaweiVR2Updater-installer8.0.0.303_dfu266.exe"


class UIVR2UpgradeToolTestCase(unittest.TestCase):
    """
    class doc:  UIVR2UpgradeToolTestCase
    安装
    """
    img_path = 'img'
    current_value = ''
    has_lang_page = False

    def save_img(self, img_name):
        rtc.CaptureToImage('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    @BeautifulReport.add_test_img('Install_Home_Page')
    def test_app_install_01_home_is_ok(self):
        """
        popen exe application to Install home page
        :return:
        """
        time.sleep(0.5)
        self.has_lang_page = True
        self.save_img('Install_Home_Page')
        self.assertTrue(automation.WindowControl(searchDepth=1, ClassName="TSelectLanguageForm"))

    @BeautifulReport.add_test_img('Default_Language_check')
    def test_app_install_02_default_lang_check(self):
        """
        check the install lang page, The default language is chinese or not
        :return:
        """
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TSelectLanguageForm")
        self.current_value = install_lang_window.ComboBoxControl().CurrentValue()
        self.save_img('Default_Language_check')
        self.assertEqual(self.current_value, '中文（简体）')

    @BeautifulReport.add_test_img('Select_Language_Chinese', 'Select_Language_English')
    def test_app_install_03_select_lang_chinese(self):
        """

        :return:
        """
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TSelectLanguageForm")
        self.assertTrue(install_lang_window)

        install_lang_window.ComboBoxControl(ClassName='TNewComboBox').Select(name='English')
        self.current_value = install_lang_window.ComboBoxControl(ClassName='TNewComboBox').CurrentValue()
        self.save_img('Select_Language_English')
        self.assertEqual(self.current_value, 'English')

        install_lang_window.ComboBoxControl(ClassName='TNewComboBox').Select(name='中文（简体）')
        self.current_value = install_lang_window.ComboBoxControl(ClassName='TNewComboBox').CurrentValue()
        self.save_img('Select_Language_Chinese')
        self.assertEqual(self.current_value, '中文（简体）')

    @unittest.SkipTest
    def test_app_install_04_cancel_install_chinese(self):
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TSelectLanguageForm")
        install_lang_window.ButtonControl(Name='取消').Click()
        self.assertIsNone(automation.WindowControl(searchDepth=1, ClassName="TSelectLanguageForm"))

    @BeautifulReport.add_test_img('Before_Guide_Page', 'Install_Guide_Page')
    def test_app_install_05_confirm_lang(self):
        """
        Select Language and Confirm it
        :return:
        """
        self.save_img('Before_Guide_Page')
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TSelectLanguageForm")
        install_lang_window.ButtonControl(Name='确定').Click()
        time.sleep(0.5)
        self.save_img('Install_Guide_Page')

    @unittest.SkipTest
    def test_app_install_06_guide_homepage(self):
        """

        :return:
        """
        self.assertTrue(automation.WindowControl(searchDepth=1, ClassName='TWizardForm',
                                                 RegexName='.*HUAWEI VR2 Updater'))

    @unittest.SkipTest
    def test_app_install_07_guide_installpath(self):
        # guide_window = automation.WindowControl(searchDepth=1, ClassName='TWizardForm', RegexName='.*HUAWEI VR2 Updater')
        guide_window = automation.WindowControl(searchDepth=3, ClassName='TWizardForm',
                                                RegexName='.*HUAWEI VR2 Updater')
        guide_window.Exists()
        # automation.EditControl(ClassName='TEdit', subName='点击').SetValue('aaa')
        # self.assertTrue(os.path.exists(guide_window.EditControl(ClassName='TEdit').CurrentValue()))
        # guide_window.ButtonControl(ClassName='TNewButton', RegexName='.*下一步.*').Click()


    @BeautifulReport.add_test_img('Before_select_path_Page', 'after_select_path_Page')
    def test_app_install_08_select_path(self):
        #点击“下一步”
        self.save_img('Before_select_path_Page')
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
        install_lang_window.ButtonControl(Name='下一步(N) >').Click()
        time.sleep(0.5)
        self.save_img('after_select_path_Page')

    @unittest.SkipTest
    def test_app_install_09_select_path_check(self):
        #检查是否进入下一级页面
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
        self.current_value = install_lang_window.WindowControl().CurrentValue()
        self.assertEqual(self.current_value, "选择附加任务")

    def test_app_install_10_select_shortcut(self):
        #检查默认是否为不选择状态
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
        self.current_value = install_lang_window.CheckBoxControl().CurrentToggleState()
        #检查是否默认不选中
        self.assertEqual(self.current_value, 0)
        '''
        #手动选择创建桌面快捷方式
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
        self.current_value = install_lang_window.ComboBoxControl().CurrentToggleState()
        install_lang_window.CheckBoxControl(Name='创建桌面快捷方式(&D)').Click()
        #检查是否已选中
        self.assertEqual(self.current_value, 1)
        '''

    @unittest.SkipTest
    def test_app_install_11_back_step(self):
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
        install_lang_window.ButtonControl(Name='< 上一步(B)').Click()

    @unittest.SkipTest
    def test_app_install_12_back_step_check(self):
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
        self.current_value = install_lang_window.ComboBoxControl().CurrentValue()
        self.assertEqual(self.current_value, "选择安装位置")

    def test_app_install_13_next_step(self):
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
        install_lang_window.ButtonControl(Name='下一步(N) >').Click()

    def test_app_install_14_next_step_check(self):
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
        self.current_value = install_lang_window.TextControl().AccessibleCurrentName()
        self.assertEqual(self.current_value, "安装准备完毕")

    def test_app_install_15_select_install(self):
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
        install_lang_window.ButtonControl(Name='安装').Click()

    @unittest.SkipTest
    def test_app_install_16_close_window(self):
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
        install_lang_window.ButtonControl(Name='关闭').Click()

    @unittest.SkipTest
    def test_app_install_17_close_window_check(self):
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
        self.current_value = install_lang_window.TextControl().CurrentValue()
        self.assertEqual(self.current_value, "退出安装向导")

    def test_app_install_18_select_install_check(self):
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
        self.current_value = install_lang_window.TextControl().AccessibleCurrentName()
        self.assertEqual(self.current_value, "Huawei VR2 Updater安装完成")

    def test_app_install_19_select_complete(self):
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="TWizardForm")
        install_lang_window.ButtonControl(Name='结束(F)').Click()
        time.sleep(3)

    def test_app_install_20_select_complete_check(self):
        time.sleep(1)
        install_lang_window = automation.WindowControl(searchDepth=1, ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1")
        self.current_value = install_lang_window.WindowControl().CurrentValue()
        self.assertEqual(self.current_value, "一键升级")
        #self.assertTrue(automation.WindowControl(searchDepth=1, ClassName="WindowsForms10.Window.8.app.0.2bf8098_r36_ad1"))

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