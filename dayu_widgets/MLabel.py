#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from qt import *
from MTheme import global_theme

qss = '''
QLabel
QLabel[type=main_head]{{
    {main_head_font}
    {font_family}
}}
QLabel[type=sub_head]{{
    {sub_head_font}
    {font_family}
}}
QLabel[type=small_head]{{
    {small_head_font}
    {font_family}
}}
QLabel[type=text]{{
    {text_font}
    {font_family}
}}
QLabel[type=help]{{
    {help_font}
    {font_family}
}}
QLabel[type=link]{{
    {link_font}
    {font_family}
}}
QLabel:disabled{{
    {disabled_font}
    {font_family}
}}
'''.format(**global_theme)


class MLabel(QLabel):
    MainHeadType = 'main_head'
    SubHeadType = 'sub_head'
    SmallHeadType = 'small_head'
    TextType = 'text'
    HelpType = 'help'
    LinkType = 'like'

    def __init__(self, text='', type=None, parent=None):
        super(MLabel, self).__init__(parent=parent)
        self.setProperty('text', text)
        self.setProperty('type', type or MLabel.TextType)
        self.setStyleSheet(qss)