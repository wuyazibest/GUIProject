#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File   : calculator.py
# @Time   : 2024/5/4 18:57
# @Author : wuyazibest
# @Email  : wuyazibest@163.com
# @Desc   :


import sys

# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget
# 导入我们生成的界面
from ui import Ui_Form


# 继承QWidget类，以获取其属性和方法
class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.setupUi(self)
        
        self.current_val = ''
        self.display = ''
        self.result = 0
        self.bind()
    
    def bind(self):
        """
        将按钮动作和需要触发的事件绑定
        :return:
        """
        self.pushButton_0.clicked.connect(lambda: self.addNumber('0'))
        self.pushButton_1.clicked.connect(lambda: self.addNumber('1'))
        self.pushButton_2.clicked.connect(lambda: self.addNumber('2'))
        self.pushButton_3.clicked.connect(lambda: self.addNumber('3'))
        self.pushButton_4.clicked.connect(lambda: self.addNumber('4'))
        self.pushButton_5.clicked.connect(lambda: self.addNumber('5'))
        self.pushButton_6.clicked.connect(lambda: self.addNumber('6'))
        self.pushButton_7.clicked.connect(lambda: self.addNumber('7'))
        self.pushButton_8.clicked.connect(lambda: self.addNumber('8'))
        self.pushButton_9.clicked.connect(lambda: self.addNumber('9'))
        self.pushButton_10.clicked.connect(lambda: self.operator(' + '))
        self.pushButton_11.clicked.connect(lambda: self.operator(' - '))
        self.pushButton_12.clicked.connect(lambda: self.operator(' * '))
        self.pushButton_13.clicked.connect(lambda: self.operator(' / '))
        self.pushButton_16.clicked.connect(self.dot)
        self.pushButton_14.clicked.connect(self.equal)
    
    def addNumber(self, number):
        self.current_val = self.current_val + number
        self.display = self.display + number
        self.textBrowser.setText(self.display)
    
    def operator(self, insignia):
        """
        只要textBrowser中有数字则进行运算，不管是不是上次的计算结果
        """
        if self.textBrowser.toPlainText() and self.textBrowser.toPlainText()[-1].isdecimal():
            self.current_val = ''
            self.display = self.textBrowser.toPlainText() + insignia
            self.textBrowser.setText(self.display)
    
    def dot(self):
        """
        只有当前输入的是数字切没有小数点的情况下才能输出小数点
        """
        if self.current_val and '.' not in self.current_val:
            self.current_val = self.current_val + '.'
            self.display = self.display + '.'
            self.textBrowser.setText(self.display)
    
    def equal(self):
        """
        必须要textBrowser中最后一位是数字才能进行结果运算，连续两次则清空当次计算
        """
        if self.textBrowser.toPlainText() and self.textBrowser.toPlainText()[-1].isdecimal():
            self.current_val = ''
            if self.display:
                self.textBrowser.setText(str(eval(self.display)))
                self.display = ''
            else:
                self.textBrowser.clear()


# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)
    
    # 初始化并展示我们的界面组件
    window = MyWidget()
    window.show()
    
    # 结束QApplication
    sys.exit(app.exec())
