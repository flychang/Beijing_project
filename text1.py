# import demo1
# import demo1_demo
import demo2_demo


import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore



if __name__=='__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app=QApplication(sys.argv)      #创建应用程序
    mainwindow=QMainWindow()        #创建主窗口
    # ui = demo1.Ui_mainWindow()     # 调用中的主窗口
    # ui = demo1_demo.Ui_mainWindow()  # 调用中的主窗口
    ui = demo2_demo.Ui_mainWindow()  # 调用中的主窗口
    ui.setupUi(mainwindow)          # 向主窗口添加控件
    mainwindow.show()               # 显示窗口
    sys.exit(app.exec_())           # 程序执行循环

