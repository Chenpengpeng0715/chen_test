# -*- coding: utf-8 -*-
# author: cwx520375 
# time: 2019/3/11

import os

curr_path = r"C:\Users\cwx520375\AppData\Local\conda\conda\envs\conda35" \
            r"\Lib\site-packages\BeautifulReport\PCVR_Image"
Common_path = os.path.join(curr_path, "Common")
Install_path = os.path.join(curr_path, "Install")
ControlPanel_path = os.path.join(curr_path, "ControlPanel")
Uninstall_path = os.path.join(curr_path, "Uninstall")
file_path_dic = {}


def get_file_path():
    curr_path = r"C:\Users\cwx520375\AppData\Local\conda\conda\envs\conda35" \
                r"\Lib\site-packages\BeautifulReport\PCVR_Image"
    for roots, dirs, files in os.walk(curr_path):
        for file in files:
            if ".PNG" in file:
                file_name = file.split(".")[0]
                file_path_dic[file_name] = os.path.join(roots, file)
    return file_path_dic


class Common(object):
    client_path = os.path.join(Common_path, "client.PNG")


class Install(object):
    agree_home_page_path = os.path.join(Install_path, "agree_home_page.PNG")
    agreement_close_path = os.path.join(Install_path, "agreement_close.PNG")
    agreement_confirm_button_path = os.path.join(Install_path, "agreement_confirm_button.PNG")
    agreement_no_selected_path = os.path.join(Install_path, "agreement_no_selected.PNG")
    agreement_page_path = os.path.join(Install_path, "agreement_page.PNG")
    agreement_selected_path = os.path.join(Install_path, "agreement_selected.PNG")
    cancel_install_path = os.path.join(Install_path, "cancel_install.PNG")
    default_language_path = os.path.join(Install_path, "default_language.PNG")
    experience_path = os.path.join(Install_path, "experience.PNG")
    install_agreement_path = os.path.join(Install_path, "install_agreement.PNG")
    install_button_gray_path = os.path.join(Install_path, "install_button_gray.PNG")
    install_button_high_light_path = os.path.join(Install_path, "install_button_high_light.PNG")
    install_cancel_path = os.path.join(Install_path, "install_cancel.PNG")
    install_close_path = os.path.join(Install_path, "install_close.PNG")
    install_complete_path = os.path.join(Install_path, "install_complete.PNG")
    install_folder_path = os.path.join(Install_path, "install_folder.PNG")
    install_home_page_path = os.path.join(Install_path, "install_home_page.PNG")
    install_home_page_2_path = os.path.join(Install_path, "install_home_page_2.PNG")
    install_minimize_path = os.path.join(Install_path, "install_minimize.PNG")
    language_path = os.path.join(Install_path, "language.PNG")
    last_step_path = os.path.join(Install_path, "last_step.PNG")
    next_step_path = os.path.join(Install_path, "next_step.PNG")
    repeat_install_path = os.path.join(Install_path, "repeat_install.PNG")
    repetition_install_path = os.path.join(Install_path, "repetition_install.PNG")
    repetition_install_cancel_path = os.path.join(Install_path, "repetition_install_cancel.PNG")
    repetition_install_close_path = os.path.join(Install_path, "repetition_install_close.PNG")
    terminate_install_cancel_path = os.path.join(Install_path, "terminate_install_cancel.PNG")
    terminate_install_confirm_path = os.path.join(Install_path, "terminate_install_confirm.PNG")
    terminate_install_close_path = os.path.join(Install_path, "terminate_install_close.PNG")
    English_language_path = os.path.join(Install_path, "English_language.PNG")
    install_home_page_English_path = os.path.join(Install_path, "install_home_page_English.PNG")
    install_home_page_English_2_path = os.path.join(Install_path, "install_home_page_2_English.PNG")
    agreement_confirm_button_English_path = os.path.join(Install_path, "agreement_confirm_button_English.PNG")
    install_agreement_English_path = os.path.join(Install_path, "install_agreement_English.PNG")
    install_button_gray_English_path = os.path.join(Install_path, "install_button_gray_English.PNG")
    install_button_highlight_English_path = os.path.join(Install_path, "install_button_highlight_English.PNG")
    BACK_path = os.path.join(Install_path, "BACK.PNG")
    file_close_path = os.path.join(Install_path, "file_close.PNG")
    Change_path = os.path.join(Install_path, "Change.PNG")
    NEXT_path = os.path.join(Install_path, "NEXT.PNG")
    install_complete_English = os.path.join(Install_path, "install_complete_English.PNG")
    experience_English = os.path.join(Install_path, "experience_English.PNG")
    change_folder_file_path = os.path.join(Install_path, "change_folder_file.PNG")
    QUIT_path = os.path.join(Install_path, "QUIT.PNG")
    DONT_QUIT_path = os.path.join(Install_path, "DONT_QUIT.PNG")


class ControlPanel(object):
    control_panel_no_connected_path = os.path.join(ControlPanel_path, "control_panel_no_connected.PNG")
    control_close_path = os.path.join(ControlPanel_path, "control_close.PNG")
    control_minimize_path = os.path.join(ControlPanel_path, "control_minimize.PNG")
    control_panel_no_connected_English = os.path.join(ControlPanel_path, "control_panel_no_connected_English.PNG")


class Uninstall(object):
    cancel_path = os.path.join(Uninstall_path, "cancel.PNG")
    close_path = os.path.join(Uninstall_path, "close.PNG")
    confirm_path = os.path.join(Uninstall_path, "confirm.PNG")
    file_folder_path = os.path.join(Uninstall_path, "file_folder.PNG")
    max_size_path = os.path.join(Uninstall_path, "max_size.PNG")
    min_size_path = os.path.join(Uninstall_path, "min_size.PNG")
    no_path = os.path.join(Uninstall_path, "no.PNG")
    prompt_path = os.path.join(Uninstall_path, "prompt.PNG")
    recover_size_path = os.path.join(Uninstall_path, "recover_size.PNG")
    repetition_path = os.path.join(Uninstall_path, "repetition.PNG")
    uninstall_path = os.path.join(Uninstall_path, "uninstall.PNG")
    uninstall_completed_path = os.path.join(Uninstall_path, "uninstall_completed.PNG")
    uninstall_guide_path = os.path.join(Uninstall_path, "uninstall_guide.PNG")
    yes_path = os.path.join(Uninstall_path, "yes.PNG")


# get_file_path(curr_path)
