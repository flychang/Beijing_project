from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    imgName = ""
    directory2 = ""
    pixmap = ""
    txtName = ""
    width = 0
    height = 0
    w_kong = (1900 - 400 - width) / 2
    h_kong = (1100 - height) / 2
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1900, 1100)
        MainWindow.setMinimumSize(QtCore.QSize(1900, 1100))
        MainWindow.setMaximumSize(QtCore.QSize(1900, 1100))
       

        # ui.label00.setStyleSheet("color: white")
        # ui.label11.setStyleSheet("color: white")
        #设置两个label参数
        self.label00 = QtWidgets.QLabel(self.page_2)
        self.label00.setStyleSheet("background-color:transparent;")  # 设置背景透明
        self.label00.setAttribute(Qt.WA_TranslucentBackground)  # 启用透明度特性
        self.label00.setFixedSize(190, 50)
        self.label00.setStyleSheet("font: 16pt \"黑体\";color:rgb(125,162,220);")
        self.label11 = QtWidgets.QLabel(self.page_2)
        self.label11.setStyleSheet("background-color:transparent;")  # 设置背景透明
        self.label11.setAttribute(Qt.WA_TranslucentBackground)  # 启用透明度特性
        self.label11.setFixedSize(190,50)
        self.label11.setStyleSheet("font: 16pt \"黑体\";color:rgb(125,162,220);")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

   

        self.pushButton_jiance.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_keshihua.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        self.pushButton_2.clicked.connect(self.msg)
        self.pushButton_1.clicked.connect(self.msg2)
        self.pushButton.clicked.connect(self.Pushbutton4)
        self.pushButton_3.clicked.connect(self.msg3)


    def msg(self):
        num = 0
        self.imgName, imgType = QtWidgets.QFileDialog.getOpenFileName(None, "导入图片", "./", "*.png;*.tif;")
        self.pushButton_5.setText(self.imgName)
        if self.imgName == "":
            return
        #原始尺寸图片
        jpg = QtGui.QPixmap(self.imgName)
        #图片宽度，高度
        self.width = jpg.width()
        self.height = jpg.height()
        self.w_kong = (1900 - 400 - self.width) / 2
        self.h_kong = (1100 - self.height) / 2
        # 控制台输出图片宽度和高度
        print(self.width,self.height)
        #控制台输出label长度和宽度
        print(self.label_3.width(), self.label_3.height())
        # 将图片放置在label上
        self.label_3.setPixmap(jpg)


    #结果存放路径
    def msg2(self):
        self.directory2 = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")
        self.pushButton_4.setText(self.directory2)

    #保存导入图片路径
    def msg3(self):
        self.txtName, imgType = QtWidgets.QFileDialog.getOpenFileName(None, "导入图片", "./", "*.txt;")
        self.pushButton_6.setText(self.txtName)

    #判断当前检测的器件
    def Comboxreturn(self):
        data = self.comboBox.currentText()
        if data == "LSR16C-1100-上冷板分组件-密封座":
            a = 0
        elif data == "LSR16C-1100-上冷板分组件-外围钎焊":
            a = 1
        elif data == "LSR16C-2000-下冷板分组件-外围钎焊":
            a = 2
        elif data == "IGBT散热器-正方形":
            a = 3
        elif data == "IGBT散热器-八角形":
            a = 4
        return a

    #判断是否设置文件夹、导入图片  和  返回后台检测器件型号
    def Pushbutton4(self):
        if self.imgName == "" or self.directory2 == "" or self.txtName == "":
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '警告',
                                            '请先导入图片和txt文件或设置结果存放的文件夹！')  # Information可替换为Warning、Critical其他提示框类型
            msg_box.exec_()
        else:
            a = self.Comboxreturn()
            print(a)
