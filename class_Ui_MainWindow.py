



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
        self.pushButton_jiance.setStyleSheet("font: 48pt \"黑体\";")
        self.pushButton_jiance.setObjectName("pushButton_jiance")
        self.pushButton_keshihua = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_keshihua.setGeometry(QtCore.QRect(0, 150, 411, 111))
        self.pushButton_keshihua.setStyleSheet("font: 36pt \"黑体\";")
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
        self.label_3.setMouseTracking(True)

        # ui.label00.setStyleSheet("color: white")
        # ui.label11.setStyleSheet("color: white")
        # 设置两个label参数
        self.label00 = QtWidgets.QLabel(self.page_2)
        self.label00.setStyleSheet("background-color:transparent;")  # 设置背景透明
        self.label00.setAttribute(Qt.WA_TranslucentBackground)  # 启用透明度特性
        self.label00.setFixedSize(300, 50)
        self.label00.setStyleSheet("font: 16pt \"黑体\";color:rgb(125,162,220);")
        self.label22 = QtWidgets.QLabel(self.page_2)
        self.label22.setStyleSheet("background-color:transparent;")  # 设置背景透明
        self.label22.setAttribute(Qt.WA_TranslucentBackground)  # 启用透明度特性
        self.label22.setFixedSize(300, 50)
        self.label22.setStyleSheet("font: 16pt \"黑体\";color:rgb(125,162,220);")
        self.label11 = QtWidgets.QLabel(self.page_2)
        self.label11.setStyleSheet("background-color:transparent;")  # 设置背景透明
        self.label11.setAttribute(Qt.WA_TranslucentBackground)  # 启用透明度特性
        self.label11.setFixedSize(300, 50)
        self.label11.setStyleSheet("font: 16pt \"黑体\";color:rgb(125,162,220);")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        

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
        # 原始尺寸图片
        jpg = QtGui.QPixmap(self.imgName)
        # 图片宽度，高度
        self.width = jpg.width()
        self.height = jpg.height()
        self.w_kong = (1900 - 400 - jpg.width()) / 2
        self.h_kong = (1100 - jpg.height()) / 2
        # 控制台输出图片宽度和高度
        print("图片",self.width, self.height)
        # 控制台输出label长度和宽度
        print(self.label_3.width(), self.label_3.height())
        # 将图片放置在label上
        self.label_3.setPixmap(jpg)

    # 结果存放路径
    def msg2(self):
        self.directory2 = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")
        self.pushButton_4.setText(self.directory2)

    # 保存导入图片路径
    def msg3(self):
        self.txtName, imgType = QtWidgets.QFileDialog.getOpenFileName(None, "导入图片", "./", "*.txt;")
        self.pushButton_6.setText(self.txtName)

    # 判断当前检测的器件
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

    # 判断是否设置文件夹、导入图片  和  返回后台检测器件型号
    def Pushbutton4(self):
        if self.imgName == "" or self.directory2 == "" or self.txtName == "":
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '警告',
                                            '请先导入图片和txt文件或设置结果存放的文件夹！')  # Information可替换为Warning、Critical其他提示框类型
            msg_box.exec_()
        else:
            a = self.Comboxreturn()
            print(a)
