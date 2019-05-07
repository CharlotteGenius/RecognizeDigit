#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:35:09 2019

@author: xiangyinyu
"""

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

app = QApplication([])
app.setStyle('Macintosh')
# styles: 'Fusion', 'Windows', 'WindowsVista' (Windows only) and 'Macintosh' (Mac only


window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Hello'))
layout.addWidget(QPushButton('World'))
layout.addWidget(QPushButton('!'))
window.setLayout(layout)
window.show()
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setPalette(palette)
button = QPushButton('Hello World')
button.show()
app.exec_()
