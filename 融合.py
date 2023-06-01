import math
import sys
import MouseMinWidth
import cv2
# Form implementation generated from reading ui file 'demo4.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import pyqtSignal, QObject

x1, y1, x2, y2 = 0, 0, 0, 0
piancha = 0
# 微调高度，注意y轴正方向
sut_width = 400
trim_up = -5
trim_upup = -10
weitiaoleft = -8
weitiaomiddle = 8
img = cv2.imread("result_color.png")
xiaoup = cv2.imread("cut2.png")
xiaoleft = cv2.imread("cut1.png")
xiaodown = cv2.imread("cut4.png")
xiaoright = cv2.imread("cut3.png")

algorithm_num=-1
class Ui_MainWindow(object):
    global algorithm_num
    imgName = ""
    directory2 = ""
    pixmap = ""
    txtName = ""



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1900, 1100)
        MainWindow.setMinimumSize(QtCore.QSize(1900, 1100))
        MainWindow.setMaximumSize(QtCore.QSize(1900, 1100))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, 0, 401, 1101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(170, 185, 238);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 401, 261))
        self.label.setStyleSheet("font: 72pt \"Algerian\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 279, 411, 431))
        self.frame_2.setStyleSheet("QPushButton:focus{\n"
                                   "    background-color: rgb(235, 238, 251);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed{\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "    border-style: inset;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "background-color:rgb(235, 238, 251); color: black;\n"
                                   "}\n"
                                   "\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_jiance = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_jiance.setGeometry(QtCore.QRect(0, 0, 411, 101))
        self.pushButton_jiance.setStyleSheet("font: 48pt \"华文行楷\";")
        self.pushButton_jiance.setObjectName("pushButton_jiance")
        self.pushButton_keshihua = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_keshihua.setGeometry(QtCore.QRect(0, 150, 411, 111))
        self.pushButton_keshihua.setStyleSheet("font: 36pt \"华文行楷\";")
        self.pushButton_keshihua.setObjectName("pushButton_keshihua")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(400, 0, 1501, 1101))
        self.stackedWidget.setStyleSheet("background-color: rgb(235, 238, 251);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(110, 90, 971, 111))
        self.label_2.setStyleSheet("font: 48pt \"黑体\";")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(270, 260, 981, 91))
        self.comboBox.setStyleSheet("font: 36pt \"黑体\";\n"
                                    "")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_1 = QtWidgets.QPushButton(self.page)
        self.pushButton_1.setGeometry(QtCore.QRect(80, 490, 251, 71))
        self.pushButton_1.setStyleSheet("font: 28pt \"黑体\";")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 600, 251, 71))
        self.pushButton_2.setStyleSheet("font: 28pt \"黑体\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 710, 251, 71))
        self.pushButton_3.setStyleSheet("font: 28pt \"黑体\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 500, 961, 51))
        self.pushButton_4.setStyleSheet("font: 18pt \"黑体\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 610, 961, 51))
        self.pushButton_5.setStyleSheet("font: 18pt \"黑体\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.page)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 720, 961, 51))
        self.pushButton_6.setStyleSheet("font: 18pt \"黑体\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(1070, 920, 371, 91))
        self.pushButton.setStyleSheet("font: 36pt \"黑体\";")
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1501, 1101))
        self.label_3.setText("")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SUT"))
        self.pushButton_jiance.setText(_translate("MainWindow", "检测"))
        self.pushButton_keshihua.setText(_translate("MainWindow", "检测结果可视化"))
        self.label_2.setText(_translate("MainWindow", "请选择要检测的器件："))
        self.comboBox.setItemText(0, _translate("MainWindow", "LSR16C-1100-上冷板分组件-密封座"))
        self.comboBox.setItemText(1, _translate("MainWindow", "LSR16C-1100-上冷板分组件-外围钎焊"))
        self.comboBox.setItemText(2, _translate("MainWindow", "LSR16C-2000-下冷板分组件-外围钎焊"))
        self.comboBox.setItemText(3, _translate("MainWindow", "IGBT散热器-正方形"))
        self.comboBox.setItemText(4, _translate("MainWindow", "IGBT散热器-八角形"))
        self.pushButton_1.setText(_translate("MainWindow", "结果存放"))
        self.pushButton_2.setText(_translate("MainWindow", "导入图片"))
        self.pushButton_3.setText(_translate("MainWindow", "导入txt文件"))
        self.pushButton_4.setText(_translate("MainWindow", " "))
        self.pushButton_5.setText(_translate("MainWindow", " "))
        self.pushButton_6.setText(_translate("MainWindow", " "))
        self.pushButton.setText(_translate("MainWindow", "一键检测"))

        self.pushButton_jiance.clicked.connect(self.jiance)
        self.pushButton_keshihua.clicked.connect(self.keshihua)

        self.pushButton_2.clicked.connect(self.msg)
        self.pushButton_1.clicked.connect(self.msg2)
        self.pushButton.clicked.connect(self.Pushbutton4)
        self.pushButton_3.clicked.connect(self.msg3)

    def jiance(self):
        self.pushButton_jiance.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        """ 销毁 QLabel """
        self.label_4.deleteLater()  # 使用 deleteLater 方法销毁 QLabel

    def keshihua(self):
        self.pushButton_keshihua.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        # 生成一个透明label--label_4
        self.label_4 = MyLabel(self.centralwidget)
        self.label_4.setStyleSheet("background-color:transparent;")  # 设置背景透明
        self.label_4.setAttribute(Qt.WA_TranslucentBackground)  # 启用透明度特性
        self.label_4.setGeometry(QtCore.QRect(sut_width, 0, 1501, 1101))
        # self.label_4.setText("Label444444444444444444")
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_4.setMouseTracking(True)
        self.label_4.setObjectName("label_4")

        self.label_4.raise_()
        self.label_4.show()
        print("走到这了")
        print("算法num：", self.Comboxreturn())

    def msg(self):
        num = 0
        self.imgName, imgType = QtWidgets.QFileDialog.getOpenFileName(None, "导入图片", "./", "*.png;*.tif;")
        # imgName, imgType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./","All Files (*);;Text Files (*.txt)")
        self.pushButton_5.setText(self.imgName)
        if self.imgName == "":
            return
        file_path = self.imgName
        # img = Image.open(file_path)
        img = cv2.imread(file_path, 1)
        row, col, s = img.shape  # 大小/尺寸
        # w = col  # 图片的宽
        # h = row  # 图片的高
        # print(w,h,f)
        img_rate = float(col / row)  # 图片长宽比
        lable_rate = float(self.label_3.width() / self.label_3.height())  # label长宽比

        """if lable_rate > img_rate:
            jpg = QtGui.QPixmap(self.imgName).scaled(self.label_3.height() / row * col, self.label_3.height())
            print(self.label_3.height() / row * col, self.label_3.height())
        else:
            jpg = QtGui.QPixmap(self.imgName).scaled(self.label_3.width(), self.label_3.width() / col * row)
            print(self.label_3.width(), self.label_3.width() / col * row)"""
        # 原始尺寸输出
        jpg = QtGui.QPixmap(self.imgName)
        print(self.label_3.width(), self.label_3.height())  # 控制台输出label长度和宽度
        print(col, row)  # 控制台输出图片的长度和宽度

        pixmap = QtGui.QPixmap(jpg)
        #
        # painter = QtGui.QPainter(pixmap)
        # # 设置线条颜色和宽度
        # pen = QtGui.QPen(QtGui.QColor(255, 0, 0))
        # pen.setWidth(3)
        # painter.setPen(pen)
        # # self.mouseMoveEvent()
        # # 在 QPixmap 上画线
        # painter.drawLine(0, 0, 100, 100)
        #
        # # 结束绘制
        # painter.end()
        # 将 QPixmap 设置为 self.label_3 的 pixmap
        self.label_3.setPixmap(pixmap)
        # self.label_3.setPixmap(jpg)                                         #在label_3处展示等比例缩放后的图片
        # self.mid(self,imgName)

        # 结果保存路径路径

    def msg2(self):
        self.directory2 = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")
        self.pushButton_4.setText(self.directory2)

        # 根据选择的器件返回不同值函数

    def msg3(self):
        self.txtName, imgType = QtWidgets.QFileDialog.getOpenFileName(None, "导入图片", "./", "*.txt;")
        self.pushButton_6.setText(self.txtName)

    def Comboxreturn(self):

        global algorithm_num
        data = self.comboBox.currentText()
        if data == "LSR16C-1100-上冷板分组件-密封座":
            algorithm_num = 0
        elif data == "LSR16C-1100-上冷板分组件-外围钎焊":
            algorithm_num = 1
        elif data == "LSR16C-2000-下冷板分组件-外围钎焊":
            algorithm_num = 2
        elif data == "IGBT散热器-正方形":
            algorithm_num = 3
        elif data == "IGBT散热器-八角形":
            algorithm_num = 4
        return algorithm_num

        # 判断是否设置文件夹、导入图片    返回后台检测器件型号

    def Pushbutton4(self):
        if self.imgName == "" or self.directory2 == "" or self.txtName == "":
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '警告',
                                            '请先导入图片和txt文件或设置结果存放的文件夹！')  # Information可替换为Warning、Critical其他提示框类型
            msg_box.exec_()
        else:
            # a = self.Comboxreturn()
            # print(a)
            print("算法返回值：",self.Comboxreturn())


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 创建应用程序
    mainwindow = QtWidgets.QMainWindow()  # 创建主窗口
    # ui = demo1.Ui_mainWindow()     # 调用中的主窗口
    # ui = demo1_demo.Ui_mainWindow()  # 调用中的主窗口
    ui = Ui_MainWindow()  # 调用中的主窗口
    ui.setupUi(mainwindow)  # 向主窗口添加控件
    mainwindow.show()  # 显示窗口

    sys.exit(app.exec_())  # 程序执行循环
