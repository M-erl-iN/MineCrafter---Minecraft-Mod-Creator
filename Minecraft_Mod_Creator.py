# -*- coding: utf-8 -*-
#
# Created by: Muracaev Erlan Ruslanovich
#
# The first global project of this author
#
# The latest versions of Minecraft BE are supported.
#
# WARNING: It is supported only on computers with files
# of the * format.jpegs can be opened as a notepad.
import time
import uuid
from os import mkdir
from PyQt5 import QtCore, QtWidgets, QtGui
from PIL import Image
import sys, traceback


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(1056, 30, 860, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('images_for_creator/ore_icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(775, 10, 30, 30))
        self.pushButton_17.setStyleSheet(StyleSheet(15))
        self.pushButton_17.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_for_creator/end_no_sp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon)
        self.pushButton_17.setObjectName("pushButton_17")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(560, 270, 191, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(5, 5, 805, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(StyleLabel13)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 180, 91, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(550, 130, 301, 179))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(StyleLabel13)
        self.label_9.setTextFormat(QtCore.Qt.PlainText)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(156, 180, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(StyleSheet(8))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(635, 10, 30, 30))
        self.pushButton_15.setStyleSheet(StyleSheet(8))
        self.pushButton_15.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images_for_creator/world_no_sp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_15.setIcon(icon1)
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 10, 175, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(StyleLabel13)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 90, 240, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(5, 45, 791, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(StyleLabel13)
        self.label_7.setTextFormat(QtCore.Qt.PlainText)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(456, 180, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(StyleSheet(8))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(690, 10, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(StyleLabel13)
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 180, 47, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(StyleLabel13)
        self.label_11.setTextFormat(QtCore.Qt.PlainText)
        self.label_11.setObjectName("label_11")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(360, 180, 91, 30))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(455, 10, 175, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(StyleLabel13)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 90, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(StyleSheet(8))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(325, 90, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(StyleSheet(8))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(400, 10, 30, 30))
        self.pushButton_16.setStyleSheet(StyleSheet(15))
        self.pushButton_16.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images_for_creator/nether_no_sp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_16.setIcon(icon2)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(760, 270, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(StyleSheet(8))
        self.pushButton.setObjectName("pushButton")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(5, 135, 537, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(StyleLabel13)
        self.label_10.setTextFormat(QtCore.Qt.PlainText)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(310, 180, 47, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(StyleLabel13)
        self.label_12.setTextFormat(QtCore.Qt.PlainText)
        self.label_12.setObjectName("label_12")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 90, 240, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(330, 310, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setText("")
        self.label_16.setTextFormat(QtCore.Qt.PlainText)
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 265, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(StyleSheet(8))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(364, 265, 91, 30))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(64, 265, 91, 30))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(5, 220, 537, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(StyleLabel13)
        self.label_13.setTextFormat(QtCore.Qt.PlainText)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 265, 45, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(StyleLabel13)
        self.label_14.setTextFormat(QtCore.Qt.PlainText)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(314, 265, 47, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(StyleLabel13)
        self.label_15.setTextFormat(QtCore.Qt.PlainText)
        self.label_15.setObjectName("label_15")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(160, 265, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(StyleSheet(8))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(410, 317, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet(*GlobalStyleSheetButton)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 320, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(StyleSheet(15))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 860, 400))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images_for_creator/bg_4.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.label_13.raise_()
        self.label_10.raise_()
        self.label_7.raise_()
        self.label_2.raise_()
        self.label_9.raise_()
        self.pushButton_17.raise_()
        self.lineEdit.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_3.raise_()
        self.pushButton_15.raise_()
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_5.raise_()
        self.label_5.raise_()
        self.label_11.raise_()
        self.lineEdit_5.raise_()
        self.label_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        self.pushButton_16.raise_()
        self.pushButton.raise_()
        self.label_12.raise_()
        self.lineEdit_4.raise_()
        self.label_16.raise_()
        self.pushButton_6.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_7.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.pushButton_7.raise_()
        self.pushButton_10.raise_()
        self.pushButton_8.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Руда"))
        self.label_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Генерация:"))
        self.label_9.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "дроп(привязанный\n"
"к дополнению\n"
"(minecraft:name;\n"
" project:name)):"))
        self.pushButton_3.setText(_translate("MainWindow", "Задать"))
        self.label_4.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Нижний Мир"))
        self.label_7.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Название руды в игре(US):       в системе:"))
        self.pushButton_5.setText(_translate("MainWindow", "Задать"))
        self.label_5.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Край"))
        self.label_11.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "от"))
        self.label_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Верхний Мир"))
        self.pushButton_2.setText(_translate("MainWindow", "Задать"))
        self.pushButton_4.setText(_translate("MainWindow", "Задать"))
        self.pushButton.setText(_translate("MainWindow", "Задать"))
        self.label_10.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "количество дропа(целое число):"))
        self.label_12.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "до"))
        self.label_16.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "Задать"))
        self.label_13.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Высота спавна:"))
        self.label_14.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "от"))
        self.label_15.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "до"))
        self.pushButton_7.setText(_translate("MainWindow", "Задать"))
        self.pushButton_10.setText(_translate("MainWindow", "[Создать]"))
        self.pushButton_8.setText(_translate("MainWindow", "Выбрать текстуру"))


class Ore(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self, project):
        super().__init__()
        self.setupUi(self)
        self.project = project
        self.name = None
        self.RUname = None
        self.drop = None
        self.sound = None
        self.corr_im = True
        self.spawn_in_world = [None, None]
        self.count = [None, None]
        self.biomes = []
        self.pushButton_15.clicked.connect(self.overworld)
        self.pushButton_16.clicked.connect(self.nether)
        self.pushButton_17.clicked.connect(self.the_end)
        self.pushButton_2.clicked.connect(self.setName)
        self.pushButton_4.clicked.connect(self.setRUname)
        self.pushButton_7.clicked.connect(self.setMinHeight)
        self.pushButton_6.clicked.connect(self.setMaxHeight)
        self.pushButton_3.clicked.connect(self.setMinDrop)
        self.pushButton_5.clicked.connect(self.setMaxDrop)
        self.pushButton.clicked.connect(self.setDrop)
        self.pushButton_8.clicked.connect(self.setImage)
        self.pushButton_10.clicked.connect(self.Func)


    def setName(self):
        self.name = self.lineEdit_2.text()
        self.lineEdit_2.setText('')

    def setRUname(self):
        self.RUname = self.lineEdit_4.text()
        self.lineEdit_4.setText('')

    def setMinHeight(self):
        try:
            self.spawn_in_world[0] = str(int(self.lineEdit_7.text()))
            self.lineEdit_7.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                   "images_for_creator/error_icon.png"))

    def setMaxHeight(self):
        try:
            self.spawn_in_world[1] = str(int(self.lineEdit_6.text()))
            self.lineEdit_6.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                    "images_for_creator/error_icon.png"))

    def setMinDrop(self):
        try:
            self.count[0] = str(int(self.lineEdit_3.text()))
            self.lineEdit_3.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                   "images_for_creator/error_icon.png"))

    def setMaxDrop(self):
        try:
            self.count[1] = str(int(self.lineEdit_5.text()))
            self.lineEdit_5.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                    "images_for_creator/error_icon.png"))

    def setDrop(self):
        drop = self.lineEdit.text()
        if ':' in drop:
            self.drop = drop
            self.lineEdit.setText('')
        else:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def Biomes(self, biome, button, images):
        if biome not in self.biomes:
            self.biomes.append(biome)
            self.button_image(button, images[0])
        else:
            del(self.biomes[self.biomes.index(biome)])
            self.button_image(button, images[1])

    def button_image(self, button, image):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            button.setIcon(icon)

    def nether(self):
        self.Biomes('nether', self.pushButton_16, ['images_for_creator/neth_sp', 'images_for_creator/nether_no_sp'])
        self.sound = 'netherrack'

    def overworld(self):
        self.Biomes('overworld', self.pushButton_15, ['images_for_creator/world_sp', 'images_for_creator/world_no_sp'])
        self.sound = 'stone'

    def the_end(self):
        self.Biomes('the_end', self.pushButton_17, ['images_for_creator/end_sp', 'images_for_creator/end_no_sp'])
        self.sound = 'stone'

    def setCount(self):
        try:
            self.count = [str(int(self.lineEdit_3.text())), str(int(self.lineEdit_5.text()))]
            self.lineEdit_3.setText('')
            self.lineEdit_5.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setImage(self):
        if self.name != None:
            try:
                self.adress = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать картинку(в последнюю очередь)', '', 'Image (*.jpg);;Image (*.png)')[0]
                self.texture = Image.open(self.adress)
                self.texture.save(self.project + '\\' + self.project + '(r)\\textures\\blocks\\' + self.name + '.png')
                self.corr_im = False
            except AttributeError:
                pass

    def Func(self):
        variables = [self.name, self.RUname, self.project, self.drop, self.spawn_in_world, self.biomes, self.count, self.sound]
        if None in variables or self.corr_im:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))
        else:
            ore_register(*variables)
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/complete_icon.png"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, title, image):
        MainWindow.setObjectName("MainWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setGeometry(1015, 30, 905, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(5, 160, 881, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(StyleLabel13)
        self.label_10.setTextFormat(QtCore.Qt.PlainText)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(5, 245, 701, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(StyleLabel13)
        self.label_9.setTextFormat(QtCore.Qt.PlainText)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(405, 200, 261, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setTextFormat(QtCore.Qt.PlainText)
        self.label_12.setObjectName("label_12")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(650, 86, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(StyleSheet(20))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(617, 290, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(StyleSheet(8))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 205, 240, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(464, 93, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(StyleSheet(8))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(15, 200, 131, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setTextFormat(QtCore.Qt.PlainText)
        self.label_11.setObjectName("label_11")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(12, 290, 240, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 95, 211, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 50, 211, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(745, 180, 122, 42))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(StyleSheet(12))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(720, 250, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setText("")
        self.label_16.setTextFormat(QtCore.Qt.PlainText)
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(371, 290, 240, 30))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(256, 290, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(StyleSheet(8))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(357, 332, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(*GlobalStyleSheetButton)
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(670, 205, 61, 32))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(5, 5, 641, 151))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(StyleLabel13)
        self.label_7.setTextFormat(QtCore.Qt.PlainText)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(650, 14, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(StyleSheet(20))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 90, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1021, 581))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images_for_creator/bg_3.jpg"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label_7.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.label_12.raise_()
        self.pushButton_7.raise_()
        self.pushButton_4.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_2.raise_()
        self.label_11.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit.raise_()
        self.pushButton_5.raise_()
        self.label_16.raise_()
        self.lineEdit_6.raise_()
        self.pushButton_3.raise_()
        self.pushButton_8.raise_()
        self.lineEdit_5.raise_()
        self.pushButton_9.raise_()
        self.label.raise_()
        self.Arm_label = QtWidgets.QLabel(self.centralwidget)
        self.Arm_label.setGeometry(QtCore.QRect(9, 325, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Arm_label.setFont(font)
        self.Arm_label.setStyleSheet(StyleLabel13)
        self.Arm_label.setTextFormat(QtCore.Qt.PlainText)
        self.Arm_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.Arm_label.setObjectName("Arm_label")
        self.ArmModel_but = QtWidgets.QPushButton(self.centralwidget)
        self.ArmModel_but.setGeometry(QtCore.QRect(260, 370, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ArmModel_but.setFont(font)
        self.ArmModel_but.setStyleSheet(StyleSheet(8))
        self.ArmModel_but.setObjectName("ArmModel_but")
        self.Arm_line = QtWidgets.QLineEdit(self.centralwidget)
        self.Arm_line.setGeometry(QtCore.QRect(16, 370, 240, 30))
        self.Arm_line.setObjectName("Arm_line")
        self.retranslateUi(MainWindow, title)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, title):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", title))
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Броня"))
        self.Arm_label.setWhatsThis(_translate("MainWindow",
                                               "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.Arm_label.setText(_translate("MainWindow", "Модель(название):"))
        self.ArmModel_but.setText(_translate("MainWindow", "Задать"))
        self.label_10.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "Починка на наковальне:"))
        self.label_9.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Защита:                              Прочность:"))
        self.label_12.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "Процент починки:"))
        self.pushButton_7.setText(_translate("MainWindow", "Выбрать текстуру"))
        self.pushButton_4.setText(_translate("MainWindow", "Задать"))
        self.pushButton_2.setText(_translate("MainWindow", "Задать"))
        self.label_11.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Предмет:"))
        self.pushButton_5.setText(_translate("MainWindow", "Задать"))
        self.label_16.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Задать"))
        self.pushButton_8.setText(_translate("MainWindow", "[Создать]"))
        self.label_7.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Название элемента брони в игре(US):"))
        self.pushButton_9.setText(_translate("MainWindow", "Выбрать модель"))
        self.label.setText(_translate("MainWindow", "В системе:"))


class Armor(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self, project, windowTitle, func, image):
        super().__init__()
        self.setupUi(self, windowTitle, image)
        self.func = func
        self.project = project
        self.damage = None
        self.ArmorSetName = None
        self.protection = None
        self.name = None
        self.RUname = None
        self.materials = []
        self.max_durability = None
        self.modelname = None
        self.ArmModel_but.clicked.connect(self.setArmModelName)
        self.pushButton_3.clicked.connect(self.setProtection)
        self.pushButton_4.clicked.connect(self.setMaxDurability)
        self.pushButton_2.clicked.connect(self.setNames)
        self.pushButton_5.clicked.connect(self.setMaterials)
        self.pushButton_7.clicked.connect(self.setImage)
        self.pushButton_9.clicked.connect(self.setModel)
        self.pushButton_8.clicked.connect(self.Func)

    def setProtection(self):
        try:
            self.protection = str(int(self.lineEdit_4.text()))
            self.lineEdit_4.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setNames(self):
        RUname = self.lineEdit.text()
        name = self.lineEdit_2.text()
        if US_text(name) and RUname != '':
            self.name = name
            self.lineEdit.setText('')
            self.RUname = RUname
            self.lineEdit_2.setText('')
        else:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setArmModelName(self):
        model = self.Arm_line.text()
        if US_text(model) and model != '':
            self.modelname = model
            self.Arm_line.setText('')
        else:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setMaterials(self):
        try:
            self.materials.append(self.lineEdit_3.text())
            self.materials.append(str(int(self.lineEdit_5.text()) / 100))
            self.lineEdit_3.setText('')
            self.lineEdit_5.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setMaxDurability(self):
        try:
            self.max_durability = str(int(self.lineEdit_6.text()))
            self.lineEdit_6.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setImage(self):
        if self.name != None:
            try:
                self.adress = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать картинку(в последнюю очередь)', '',
                                                          'Image (*.jpg, *.png)')[0]
                texture = Image.open(self.adress)
                texture.save(self.project + '\\' + self.project + '(r)\\' + 'textures\\items\\' + self.name + '.png')
            except AttributeError:
                pass

    def setModel(self):
        if self.modelname != None:
            try:
                self.adress = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать картинку(в последнюю очередь)', '',
                                                              'Image (*.jpg, *.png)')[0]
                model = Image.open(self.adress)
                model.save(self.project + '\\' + self.project + '(r)\\textures\\models\\armor\\' + self.modelname + '.png')
            except AttributeError:
                pass

    def Func(self):
        variables = [self.modelname, self.name, self.RUname, self.project,
                     self.materials, self.protection, self.max_durability]
        if None in variables or '' in variables:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))
        else:
            self.func(*variables)
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/complete_icon.png"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(1400, 30, 525, 395)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 261, 271))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(StyleLabel13)
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 125, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(55, 200, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(StyleSheet(16))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 300, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(*GlobalStyleSheetButton)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(430, 300, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setText("")
        self.label_16.setTextFormat(QtCore.Qt.PlainText)
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")

        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(320, 350, 36, 36))
        self.pushButton_16.setStyleSheet(StyleSheet(15))
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(320, 290, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet(StyleLabel13)
        self.label_11.setTextFormat(QtCore.Qt.PlainText)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(286, 12, 221, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(StyleLabel13)
        self.label_9.setTextFormat(QtCore.Qt.PlainText)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(310, 130, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet(StyleSheet(16))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 525, 395))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images_for_creator/bg_3.jpg"))
        self.label.setObjectName("label")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(286, 220, 220, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(StyleSheet(15))
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(25, 90, 211, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(25, 160, 211, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(297, 90, 199, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label.raise_()
        self.label_8.raise_()
        self.label_2.raise_()
        self.pushButton_9.raise_()
        self.pushButton_8.raise_()
        self.label_16.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.pushButton_16.raise_()
        self.pushButton_10.raise_()
        self.pushButton_7.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Предмет"))
        self.label_8.setWhatsThis(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Название пред     \n"
                                                      "мета в игре(US):"))
        self.label_2.setText(_translate("MainWindow", "в системе:"))
        self.pushButton_9.setText(_translate("MainWindow", "Задать"))
        self.pushButton_8.setText(_translate("MainWindow", "[Создать]"))
        self.label_16.setWhatsThis(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_9.setWhatsThis(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_11.setWhatsThis(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "кол-во пред     \n"
                                                      "метов в стаке:"))
        self.label_11.setText(_translate("MainWindow", "топливо"))
        self.pushButton_10.setText(_translate("MainWindow", "Задать"))
        self.pushButton_7.setText(_translate("MainWindow", "Выбрать текстуру"))


class Item(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self, project):
        super().__init__()
        self.setupUi(self)
        self.name = None
        self.RUname = None
        self.count = None
        self.corr_im = True
        self.is_foil = True
        self.project = project
        self.pushButton_9.clicked.connect(self.names)
        self.pushButton_10.clicked.connect(self.setCount)
        self.pushButton_7.clicked.connect(self.setImage)
        self.pushButton_8.clicked.connect(self.Func)
        self.pushButton_16.clicked.connect(self.setFoil)

    def names(self):
        name = self.lineEdit_2.text()
        RUname = self.lineEdit.text()
        if US_text(name) and name != '' and RUname != '':
            self.name = name
            self.RUname = RUname
            self.lineEdit_2.setText('')
            self.lineEdit.setText('')
        else:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setCount(self):
        try:
            self.count = str(int(self.lineEdit_3.text()))
            self.lineEdit_3.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setFoil(self):
        if self.is_foil:
            self.is_foil = False
            self.button_image(self.pushButton_16, 'images_for_creator/error_icon.png')
        else:
            self.is_foil = True
            self.button_image(self.pushButton_16, 'images_for_creator/complete_icon.png')

    def button_image(self, button, image):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)

    def setImage(self):
        if self.name != None and self.name != '':
            try:
                self.adress = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать картинку(в последнюю очередь)', '', 'Image (*.jpg, *.png)')[0]
                self.texture = Image.open(self.adress)
                self.texture.save(self.project + '\\' + self.project + '(r)\\textures\\items\\' + self.name + '.png')
                self.corr_im = False
            except AttributeError:
                pass

    def Func(self):
        variables = [self.name, self.RUname, self.project, self.count, str(self.is_foil).lower()]
        if None in variables or self.corr_im:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))
        else:
            item_register(*variables)
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/complete_icon.png"))

class Ui_furnase(object):
    def setupUi(self, furnase):
        furnase.setObjectName("furnase")
        furnase.setGeometry(1360, 30, 558, 367)
        furnase.setWindowTitle("Печь")
        furnase.setInputMethodHints(QtCore.Qt.ImhNone)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('images_for_creator/furnace_front_on.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        furnase.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(furnase)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(179, 50, 240, 30))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(464, 135, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet(StyleSheet(8))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(424, 50, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(StyleSheet(8))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(15, 5, 495, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(StyleLabel13)
        self.label_17.setTextFormat(QtCore.Qt.PlainText)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_17.setObjectName("label_17")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(30, 260, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet(*GlobalStyleSheetButton)
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(360, 90, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(StyleLabel13)
        self.label_21.setTextFormat(QtCore.Qt.PlainText)
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_21.setObjectName("label_21")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(364, 180, 180, 180))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("")
        self.label_28.setText("")
        self.label_28.setTextFormat(QtCore.Qt.PlainText)
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(364, 135, 91, 30))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(269, 220, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet(StyleSheet(8))
        self.pushButton_12.setObjectName("pushButton_12")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(24, 220, 240, 30))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(13, 175, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(StyleLabel13)
        self.label_18.setTextFormat(QtCore.Qt.PlainText)
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_18.setObjectName("label_18")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(270, 135, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet(StyleSheet(8))
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(14, 90, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(StyleLabel13)
        self.label_19.setTextFormat(QtCore.Qt.PlainText)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_19.setObjectName("label_19")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(25, 135, 240, 30))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -100, 558, 558))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images_for_creator/furnace_front_on.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.label_19.raise_()
        self.label_21.raise_()
        self.label_18.raise_()
        self.label_17.raise_()
        self.lineEdit_11.raise_()
        self.pushButton_14.raise_()
        self.pushButton_11.raise_()
        self.pushButton_13.raise_()
        self.label_28.raise_()
        self.lineEdit_14.raise_()
        self.pushButton_12.raise_()
        self.lineEdit_12.raise_()
        self.pushButton_15.raise_()
        self.lineEdit_13.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(furnase)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_14.setText(_translate("furnase", "Задать"))
        self.pushButton_11.setText(_translate("furnase", "Задать"))
        self.label_17.setWhatsThis(_translate("furnase", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_17.setText(_translate("furnase", "Название крафта в системе:"))
        self.pushButton_13.setText(_translate("furnase", "[Создать]"))
        self.label_21.setWhatsThis(_translate("furnase", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_21.setText(_translate("furnase", "количество:"))
        self.label_28.setWhatsThis(_translate("furnase", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.pushButton_12.setText(_translate("furnase", "Задать"))
        self.label_18.setWhatsThis(_translate("furnase", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_18.setText(_translate("furnase", "Получаемый предмет:"))
        self.pushButton_15.setText(_translate("furnase", "Задать"))
        self.label_19.setWhatsThis(_translate("furnase", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_19.setText(_translate("furnase", "Материал:"))


class Furnace(QtWidgets.QWidget, Ui_furnase):
    def __init__(self, project, func):
        super().__init__()
        self.setupUi(self)
        self.project = project
        self.func = func
        self.fileadress = None
        self.input_item = None
        self.output_item = None
        self.count = None
        self.pushButton_15.clicked.connect(self.setInputItem)
        self.pushButton_12.clicked.connect(self.setOutputItem)
        self.pushButton_14.clicked.connect(self.setCount)
        self.pushButton_11.clicked.connect(self.setCraftName)
        self.pushButton_13.clicked.connect(self.Func)

    def setCraftName(self):
        adress = self.lineEdit_11.text()
        if US_text(adress):
            self.fileadress = self.project + '\\' + self.project + '\\recipes\\furnace\\' + adress
            self.lineEdit_11.setText('')
        else:
            self.label_28.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setInputItem(self):
        input_ = self.lineEdit_13.text()
        if US_text(input_) and ':' in input_:
            self.input_item = input_
            self.lineEdit_13.setText('')
        else:
            self.label_28.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setOutputItem(self):
        output_ = self.lineEdit_12.text()
        if US_text(output_) and ':' in output_:
            self.output_item = output_
            self.lineEdit_12.setText('')
        else:
            self.label_28.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setCount(self):
        try:
            self.count = str(int(self.lineEdit_14.text()))
            self.lineEdit_14.setText('')
        except ValueError:
            self.label_28.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def Func(self):
        variables = [self.fileadress, self.input_item, self.output_item,
                     self.count]
        if None in variables:
            self.label_28.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))
        else:
            self.func(*variables)
            self.label_28.setPixmap(QtGui.QPixmap(
                "images_for_creator/complete_icon.png"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(1080, 30, 837, 475)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('images_for_creator/beef_cooked.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(491, 107, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(StyleSheet(15))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 7, 641, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(StyleLabel13)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 52, 223, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 390, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(*GlobalStyleSheetButton)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 60, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(StyleSheet(8))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(400, 20, 235, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(251, 55, 235, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 180, 199, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(9, 102, 221, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(StyleLabel13)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setTextFormat(QtCore.Qt.PlainText)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(33, 220, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet(StyleSheet(16))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(239, 102, 242, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(StyleLabel13)
        self.label_10.setTextFormat(QtCore.Qt.PlainText)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(263, 220, 192, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(StyleSheet(16))
        self.pushButton_11.setObjectName("pushButton_11")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 180, 220, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(660, 10, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet(StyleLabel13)
        self.label_11.setTextFormat(QtCore.Qt.PlainText)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_11.setObjectName("label_11")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(784, 52, 36, 36))
        self.pushButton_16.setStyleSheet(StyleSheet(15))
        self.pushButton_16.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\1\\PycharmProjects\\pythonProject1\\buttons/nether_no_sp.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_16.setIcon(icon)
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(491, 167, 145, 108))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(StyleLabel13)
        self.label_12.setTextFormat(QtCore.Qt.PlainText)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_12.setObjectName("label_12")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(502, 207, 125, 30))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 240, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(StyleSheet(8))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(641, 167, 191, 108))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(StyleLabel13)
        self.label_13.setTextFormat(QtCore.Qt.PlainText)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_13.setObjectName("label_13")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(652, 207, 171, 30))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(646, 240, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(StyleSheet(8))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(730, 240, 95, 26))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 288, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_14.setFont(font)
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setStyleSheet(StyleLabel13)
        self.label_14.setTextFormat(QtCore.Qt.PlainText)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_14.setObjectName("label_14")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(134, 330, 36, 36))
        self.pushButton_17.setStyleSheet(StyleSheet(15))
        self.pushButton_17.setText("")
        self.pushButton_17.setIcon(icon)
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(191, 287, 641, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(StyleLabel13)
        self.label_15.setTextFormat(QtCore.Qt.PlainText)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_15.setObjectName("label_15")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(202, 327, 501, 30))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(715, 325, 100, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(StyleSheet(8))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, -66, 837, 609))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images_for_creator/eat_bg.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(320, 387, 80, 80))
        self.label_16.setText("")
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_4.raise_()
        self.label_16.raise_()
        self.label_13.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.label.raise_()
        self.pushButton_7.raise_()
        self.label_2.raise_()
        self.pushButton_8.raise_()
        self.pushButton_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.lineEdit_4.raise_()
        self.label_11.raise_()
        self.pushButton_16.raise_()
        self.label_12.raise_()
        self.lineEdit_5.raise_()
        self.pushButton_4.raise_()
        self.lineEdit_6.raise_()
        self.pushButton_5.raise_()
        self.label_3.raise_()
        self.label_14.raise_()
        self.pushButton_17.raise_()
        self.label_15.raise_()
        self.lineEdit_7.raise_()
        self.pushButton_6.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Панель Создания Пользовательской Еды"))
        self.pushButton_7.setText(_translate("MainWindow", "Выбрать текстуру"))
        self.label.setWhatsThis(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Название еды в игре(US):"))
        self.label_2.setText(_translate("MainWindow", "в системе:"))
        self.pushButton_8.setText(_translate("MainWindow", "[Создать]"))
        self.pushButton_3.setText(_translate("MainWindow", "Задать"))
        self.label_9.setWhatsThis(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "кол-во пред     \\\n"
                                                      "метов в стаке:"))
        self.pushButton_10.setText(_translate("MainWindow", "Задать"))
        self.label_10.setWhatsThis(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "длительность    \\\n"
                                                       "использования:"))
        self.pushButton_11.setText(_translate("MainWindow", "Задать"))
        self.label_11.setWhatsThis(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "топливо"))
        self.label_12.setWhatsThis(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "Сытость:"))
        self.pushButton_4.setText(_translate("MainWindow", "Задать"))
        self.label_13.setWhatsThis(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Насыщение:"))
        self.pushButton_5.setText(_translate("MainWindow", "Задать"))
        self.label_3.setText(_translate("MainWindow", "poor, low, normal, \\\n"
                                                      "good, supernatural"))
        self.label_14.setWhatsThis(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "Можно есть \\\n"
                                                       "всегда"))
        self.label_15.setWhatsThis(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "Эффект(name duration amplifier):"))
        self.pushButton_6.setText(_translate("MainWindow", "Задать"))


class Eat(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self, project):
        super().__init__()
        self.setupUi(self)
        self.project = project
        self.corr_im = True
        self.is_foil = False
        self.name = None
        self.RUname = None
        self.use_duration = None
        self.stack_size = None
        self.nutrition = None
        self.saturation = None
        self.can_alvays_eat = False
        self.effects = []
        self.pushButton_3.clicked.connect(self.setNames)
        self.pushButton_10.clicked.connect(self.setStackSize)
        self.pushButton_11.clicked.connect(self.setUseDuration)
        self.pushButton_16.clicked.connect(self.setFoil)
        self.pushButton_17.clicked.connect(self.setAlvaysEat)
        self.pushButton_4.clicked.connect(self.setNutrition)
        self.pushButton_5.clicked.connect(self.setSaturation)
        self.pushButton_6.clicked.connect(self.setEffects)
        self.pushButton_7.clicked.connect(self.setImage)
        self.pushButton_8.clicked.connect(self.Func)

    def setNames(self):
        name = self.lineEdit_2.text()
        RUname = self.lineEdit.text()
        if US_text(name) and RUname != '':
            self.name = name
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.RUname = RUname
        else:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setStackSize(self):
        try:
            self.stack_size = str(int(self.lineEdit_3.text()))
            self.lineEdit_3.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setImage(self):
        if self.name != None and self.name != '':
            self.adress = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать картинку(в последнюю очередь)', '',
                                                      'Image (*.jpg, *.png)')[0]
            self.texture = Image.open(self.adress)
            self.texture.save(self.project + '\\' + self.project + '(r)\\textures\\items\\' + self.name + '.png')
            self.corr_im = False

    def setFoil(self):
        if self.is_foil:
            self.is_foil = False
            self.button_image(self.pushButton_16, 'images_for_creator/error_icon.png')
        else:
            self.is_foil = True
            self.button_image(self.pushButton_16, 'images_for_creator/complete_icon.png')

    def button_image(self, button, image):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)

    def setUseDuration(self):
        try:
            self.use_duration = str(int(self.lineEdit_4.text()))
            self.lineEdit_4.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setNutrition(self):
        try:
            self.nutrition = str(int(self.lineEdit_5.text()))
            self.lineEdit_5.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setSaturation(self):
        saturation = self.lineEdit_6.text()
        if saturation in ['poor', 'low', 'normal', 'good', 'supernatural']:
            self.saturation = saturation
            self.lineEdit_6.setText('')
        else:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setAlvaysEat(self):
        if self.can_alvays_eat:
            self.can_alvays_eat = False
            self.button_image(self.pushButton_17, 'images_for_creator/error_icon.png')
        else:
            self.can_alvays_eat = True
            self.button_image(self.pushButton_17, 'images_for_creator/complete_icon.png')

    def setEffects(self):
        effect = self.lineEdit_7.text().split()
        try:
            effect_test = [effect[0], str(int(effect[1])), str(int(effect[2]))]
            self.effects.append(effect_test)
            self.lineEdit_7.setText('')
        except IndexError or ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def Func(self):
        variables = [self.name, self.RUname, self.stack_size, self.use_duration, str(self.is_foil).lower(), self.nutrition,
                     self.saturation, str(self.can_alvays_eat).lower(), self.effects, self.project]
        if None in variables:  # or self.corr_im
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))
        else:
            eat_register(*variables)
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/complete_icon.png"))


class Ui_Verctak(object):
    def setupUi(self, Verctak):
        Verctak.setObjectName("Verctak")
        Verctak.setEnabled(True)
        Verctak.setGeometry(1280, 30, 640, 581)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Verctak.sizePolicy().hasHeightForWidth())
        Verctak.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_for_creator/crafting_table_top.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Verctak.setWindowIcon(icon)
        Verctak.setAccessibleName("")
        Verctak.setAutoFillBackground(False)
        Verctak.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(Verctak)
        self.centralwidget.setObjectName("centralwidget")
        self.setCountButton = QtWidgets.QPushButton(self.centralwidget)
        self.setCountButton.setGeometry(QtCore.QRect(191, 432, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.setCountButton.setFont(font)
        self.setCountButton.setStyleSheet(StyleSheet(8))
        self.setCountButton.setObjectName("setCountButton")
        self.CraftNameButton = QtWidgets.QPushButton(self.centralwidget)
        self.CraftNameButton.setGeometry(QtCore.QRect(480, 50, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CraftNameButton.setFont(font)
        self.CraftNameButton.setStyleSheet(StyleSheet(8))
        self.CraftNameButton.setObjectName("CraftNameButton")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(80, 5, 491, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(StyleLabel13)
        self.label_17.setTextFormat(QtCore.Qt.PlainText)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_17.setObjectName("label_17")
        self.Func_button = QtWidgets.QPushButton(self.centralwidget)
        self.Func_button.setGeometry(QtCore.QRect(170, 480, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.Func_button.setFont(font)
        self.Func_button.setStyleSheet(*GlobalStyleSheetButton)
        self.Func_button.setObjectName("Func_button")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(460, 340, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("")
        self.label_28.setText("")
        self.label_28.setTextFormat(QtCore.Qt.PlainText)
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.NameButton = QtWidgets.QPushButton(self.centralwidget)
        self.NameButton.setGeometry(QtCore.QRect(340, 370, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NameButton.setFont(font)
        self.NameButton.setStyleSheet(StyleSheet(8))
        self.NameButton.setObjectName("NameButton")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(80, 326, 351, 145))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(StyleLabel13)
        self.label_18.setTextFormat(QtCore.Qt.PlainText)
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(80, 93, 355, 87))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(StyleLabel13)
        self.label_19.setTextFormat(QtCore.Qt.PlainText)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_19.setObjectName("label_19")
        self.transcription = QtWidgets.QTextEdit(self.centralwidget)
        self.transcription.setGeometry(QtCore.QRect(302, 195, 258, 40))
        self.transcription.setObjectName("transcription")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(444, 93, 51, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(StyleLabel13)
        self.label_24.setTextFormat(QtCore.Qt.PlainText)
        self.label_24.setObjectName("label_24")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(320, 240, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(StyleLabel13)
        self.label_27.setTextFormat(QtCore.Qt.PlainText)
        self.label_27.setObjectName("label_27")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(320, 100, 107, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.CraftingTableGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.CraftingTableGrid.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.CraftingTableGrid.setContentsMargins(0, 0, 0, 0)
        self.CraftingTableGrid.setSpacing(0)
        self.CraftingTableGrid.setObjectName("CraftingTableGrid")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(35, 35))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.CraftingTableGrid.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(35, 35))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.CraftingTableGrid.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(35, 35))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.CraftingTableGrid.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(35, 35))
        self.lineEdit.setObjectName("lineEdit")
        self.CraftingTableGrid.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(35, 35))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.CraftingTableGrid.addWidget(self.lineEdit_5, 1, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(35, 35))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.CraftingTableGrid.addWidget(self.lineEdit_6, 0, 2, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setMaximumSize(QtCore.QSize(35, 35))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.CraftingTableGrid.addWidget(self.lineEdit_7, 2, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setMaximumSize(QtCore.QSize(35, 35))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.CraftingTableGrid.addWidget(self.lineEdit_8, 2, 2, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setMaximumSize(QtCore.QSize(35, 35))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.CraftingTableGrid.addWidget(self.lineEdit_9, 1, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(78, 187, 491, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(StyleLabel13)
        self.label_20.setTextFormat(QtCore.Qt.PlainText)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_20.setObjectName("label_20")
        self.BgLabel = QtWidgets.QLabel(self.centralwidget)
        self.BgLabel.setGeometry(QtCore.QRect(0, 0, 640, 610))
        self.BgLabel.setText("")
        self.BgLabel.setPixmap(QtGui.QPixmap("images_for_creator/crafting_table_top.png"))
        self.BgLabel.setScaledContents(True)
        self.BgLabel.setObjectName("BgLabel")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(235, 50, 240, 30))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(91, 370, 240, 30))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(91, 432, 91, 30))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(91, 402, 173, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.SetCraftingTableGridButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetCraftingTableGridButton.setGeometry(QtCore.QRect(180, 140, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SetCraftingTableGridButton.setFont(font)
        self.SetCraftingTableGridButton.setStyleSheet(StyleSheet(6))
        self.SetCraftingTableGridButton.setObjectName("SetCraftingTableGridButton")
        self.TransctiptionButton = QtWidgets.QPushButton(self.centralwidget)
        self.TransctiptionButton.setGeometry(QtCore.QRect(100, 260, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TransctiptionButton.setFont(font)
        self.TransctiptionButton.setStyleSheet(StyleSheet(6))
        self.TransctiptionButton.setObjectName("TransctiptionButton")
        self.BgLabel.raise_()
        self.label_18.raise_()
        self.label_20.raise_()
        self.label_19.raise_()
        self.label_17.raise_()
        self.CraftNameButton.raise_()
        self.Func_button.raise_()
        self.label_28.raise_()
        self.NameButton.raise_()
        self.transcription.raise_()
        self.label_24.raise_()
        self.label_27.raise_()
        self.gridLayoutWidget.raise_()
        self.setCountButton.raise_()
        self.lineEdit_10.raise_()
        self.lineEdit_11.raise_()
        self.lineEdit_12.raise_()
        self.label_2.raise_()
        self.SetCraftingTableGridButton.raise_()
        self.TransctiptionButton.raise_()

        self.retranslateUi(Verctak)
        QtCore.QMetaObject.connectSlotsByName(Verctak)

    def retranslateUi(self, Verctak):
        _translate = QtCore.QCoreApplication.translate
        Verctak.setWindowTitle(_translate("Verctak", "Верстак"))
        self.setCountButton.setText(_translate("Verctak", "Задать"))
        self.CraftNameButton.setText(_translate("Verctak", "Задать"))
        self.label_17.setWhatsThis(_translate("Verctak", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_17.setText(_translate("Verctak", "Название крафта в системе:"))
        self.Func_button.setText(_translate("Verctak", "[Создать]"))
        self.label_28.setWhatsThis(_translate("Verctak", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.NameButton.setText(_translate("Verctak", "Задать"))
        self.label_18.setWhatsThis(_translate("Verctak", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_18.setText(_translate("Verctak", "Получаемый предмет:"))
        self.label_19.setWhatsThis(_translate("Verctak", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_19.setText(_translate("Verctak", "Сетка крафта:"))
        self.label_24.setWhatsThis(_translate("Verctak", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_24.setText(_translate("Verctak", "D D D\\\n"
"F D F \\\n"
"X F X"))
        self.label_27.setWhatsThis(_translate("Verctak", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_27.setText(_translate("Verctak", "D - minecraft:iron_ingot     \\\n"
"F - project:itemname           \\\n"
"X - minecraft:diamond"))
        self.label_20.setWhatsThis(_translate("Verctak", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_20.setText(_translate("Verctak", "Расшифковка:"))
        self.label_2.setText(_translate("Verctak", "Количество:"))
        self.SetCraftingTableGridButton.setText(_translate("Verctak", "Задать"))
        self.TransctiptionButton.setText(_translate("Verctak", "Задать"))


class CraftingTableCraft(QtWidgets.QWidget, Ui_Verctak):
    def __init__(self, project):
        super().__init__()
        self.setupUi(self)
        self.project = project
        self.output_item = None
        self.filename = None
        self.count = None
        self.strings_of_craft = ['""', '""', '""']
        self.keys = {}
        self.TransctiptionButton.clicked.connect(self.setTranckription)
        self.CraftNameButton.clicked.connect(self.setName)
        self.SetCraftingTableGridButton.clicked.connect(self.SetCraftGridFunc)
        self.NameButton.clicked.connect(self.setOutputItem)
        self.setCountButton.clicked.connect(self.setCount)
        self.Func_button.clicked.connect(self.Func)

    def setOutputItem(self):
        output_item = self.lineEdit_11.text()
        if ':' in output_item:
            self.output_item = output_item
            self.lineEdit_11.setText('')
        else:
            self.label_28.setPixmap(QtGui.QPixmap(
                "C:\\Users\\1\\PycharmProjects\\pythonProject1\\Project_yandeXXX\\images_for_creator/error_icon.png"))

    def setTranckription(self):
        transkription = self.transcription.toPlainText().split('\n')
        rule = False
        for i in transkription:
            if ' - ' not in i and ':' not in i and not US_text(i):
                rule = True
        if rule:
            self.label_28.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))
        else:
            for i in transkription:
                key = i.split(' - ')
                self.keys[key[0]] = key[1]
            self.transcription.setText('')

    def setName(self):
        name = self.lineEdit_10.text()
        if US_text(name):
            self.filename = name
            self.lineEdit_10.setText('')
        else:
            self.label_28.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setCount(self):
        try:
            self.count = str(int(self.lineEdit_12.text()))
            self.lineEdit_12.setText('')
        except ValueError:
            self.label_28.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def SetCraftGridFunc(self):
        grid = [self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_6.text(),
                self.lineEdit_9.text(), self.lineEdit_4.text(), self.lineEdit_5.text(),
                self.lineEdit.text(), self.lineEdit_7.text(), self.lineEdit_8.text()]
        for i in range(9):
            if grid[i] == '':
                grid[i] = ' '
        rule = (len(list(filter(lambda x: len(x) < 2, grid))) == len(grid))
        if rule:
            self.strings_of_craft[0] = '"' + ''.join(grid[:3]) + '"'
            self.strings_of_craft[1] = '"' + ''.join(grid[3:6]) + '"'
            self.strings_of_craft[2] = '"' + ''.join(grid[6:]) + '"'
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.lineEdit_3.setText('')
            self.lineEdit_4.setText('')
            self.lineEdit_5.setText('')
            self.lineEdit_6.setText('')
            self.lineEdit_7.setText('')
            self.lineEdit_8.setText('')
            self.lineEdit_9.setText('')
        else:
            self.label_28.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def Func(self):
        variables = [self.filename, self.project, self.output_item, self.strings_of_craft, self.keys, self.count]
        try:
            test = US_text(self.filename)
        except AttributeError:
            test = False
        if None in variables or not test:
            self.label_28.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))
        else:
            crafting_table_recipe_register(*variables)
            self.label_28.setPixmap(QtGui.QPixmap(
                "images_for_creator/complete_icon.png"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(1500, 30, 419, 292)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_for_creator/block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(5, 5, 408, 151))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(StyleLabel13)
        self.label_7.setTextFormat(QtCore.Qt.PlainText)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(325, 118, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(StyleSheet(8))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 118, 240, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 50, 240, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(325, 50, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(StyleSheet(8))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(5, 216, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet(*GlobalStyleSheetButton)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(5, 160, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(StyleSheet(15))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(17, 90, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -77, 419, 500))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images_for_creator/block.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label_7.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_4.raise_()
        self.pushButton_4.raise_()
        self.pushButton_10.raise_()
        self.pushButton_8.raise_()
        self.label.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Блок"))
        self.label_7.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Название блока в игре(US):"))
        self.pushButton_2.setText(_translate("MainWindow", "Задать"))
        self.pushButton_4.setText(_translate("MainWindow", "Задать"))
        self.pushButton_10.setText(_translate("MainWindow", "[Создать]"))
        self.pushButton_8.setText(_translate("MainWindow", "Выбрать текстуру"))
        self.label.setText(_translate("MainWindow", "в системе:"))


class Block(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self, project):
        super().__init__()
        self.setupUi(self)
        self.project = project
        self.name = None
        self.RUname = None
        self.corr_im = True
        self.pushButton_2.clicked.connect(self.setName)
        self.pushButton_4.clicked.connect(self.setRUname)
        self.pushButton_8.clicked.connect(self.setImage)
        self.pushButton_10.clicked.connect(self.Func)

    def setName(self):
        name = self.lineEdit_2.text()
        if US_text(name):
            self.name = name
            self.lineEdit_2.setText('')

    def setRUname(self):
        self.RUname = self.lineEdit_4.text()
        self.lineEdit_4.setText('')

    def setImage(self):
        if self.name != None:
            try:
                self.adress = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать картинку(в последнюю очередь)', '', 'Image (*.jpg);;Image (*.png)')[0]
                self.texture = Image.open(self.adress)
                self.texture.save(self.project + '\\' + self.project + '(r)\\textures\\blocks\\' + self.name + '.png')
                self.corr_im = False
            except AttributeError:
                pass

    def Func(self):
        variables = [self.name, self.RUname, self.project]
        try:
            test = US_text(self.name)
        except AttributeError:
            test = False
        if None not in variables and test:
            block_register(*variables)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, title, image):
        MainWindow.setObjectName("MainWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.setGeometry(1250, 30, 666, 604)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(180, 520, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(*GlobalStyleSheetButton)
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(280, 460, 61, 32))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(5, 365, 561, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(StyleLabel13)
        self.label_10.setTextFormat(QtCore.Qt.PlainText)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 460, 261, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setTextFormat(QtCore.Qt.PlainText)
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(15, 410, 131, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setTextFormat(QtCore.Qt.PlainText)
        self.label_11.setObjectName("label_11")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(100, 520, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setText("")
        self.label_16.setTextFormat(QtCore.Qt.PlainText)
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(8, 5, 631, 191))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(StyleLabel13)
        self.label_9.setTextFormat(QtCore.Qt.PlainText)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(15, 50, 240, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 14, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(StyleSheet(8))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(375, 50, 240, 30))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 14, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(StyleSheet(8))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(15, 150, 240, 30))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(260, 150, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(StyleSheet(8))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 410, 240, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(370, 100, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(StyleSheet(15))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 116, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 290, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(5, 205, 641, 151))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(StyleLabel13)
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(240, 295, 211, 30))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(464, 293, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(StyleSheet(16))
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(340, 250, 211, 30))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(385, 445, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet(StyleSheet(16))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 671, 611))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images_for_creator/bg_2.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.pushButton_8.raise_()
        self.lineEdit_5.raise_()
        self.label_12.raise_()
        self.label_11.raise_()
        self.label_16.raise_()
        self.label_9.raise_()
        self.lineEdit_4.raise_()
        self.pushButton_3.raise_()
        self.lineEdit_6.raise_()
        self.pushButton_4.raise_()
        self.lineEdit_7.raise_()
        self.pushButton_6.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit_8.raise_()
        self.pushButton_9.raise_()
        self.lineEdit_9.raise_()
        self.pushButton_10.raise_()

        self.retranslateUi(MainWindow, title)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, title):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", title))
        self.pushButton_8.setText(_translate("MainWindow", "[Создать]"))
        self.label_10.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "Починка на наковальне:"))
        self.label_12.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "Процент починки:"))
        self.label_11.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Предмет:"))
        self.label_16.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_9.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Урон:                                  Прочность:"))
        self.pushButton_3.setText(_translate("MainWindow", "Задать"))
        self.pushButton_4.setText(_translate("MainWindow", "Задать"))
        self.pushButton_6.setText(_translate("MainWindow", "Задать"))
        self.pushButton_7.setText(_translate("MainWindow", "Выбрать текстуру"))
        self.label.setText(_translate("MainWindow", "Скорость копания:"))
        self.label_2.setText(_translate("MainWindow", "в системе:"))
        self.label_8.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Генерация</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Название инструмента в игре(US):"))
        self.pushButton_9.setText(_translate("MainWindow", "Задать"))
        self.pushButton_10.setText(_translate("MainWindow", "Задать"))


class Tools(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self, project, windowTitle, func, image):
        super().__init__()
        self.setupUi(self, windowTitle, image)
        self.func = func
        self.project = project
        self.corr_im = True
        self.damage = None
        self.destroy_speed = None
        self.name = None
        self.RUname = None
        self.materials = []
        self.max_durability = None
        self.texture = None
        self.pushButton_3.clicked.connect(self.setDamage)
        self.pushButton_4.clicked.connect(self.setMaxDurability)
        self.pushButton_6.clicked.connect(self.setDestroySpeed)
        self.pushButton_9.clicked.connect(self.setNames)
        self.pushButton_10.clicked.connect(self.setMaterials)
        self.pushButton_7.clicked.connect(self.setImage)
        self.pushButton_8.clicked.connect(self.Func)

    def setDamage(self):
        try:
            self.damage = str(int(self.lineEdit_4.text()))
            self.lineEdit_4.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setDestroySpeed(self):
        try:
            self.destroy_speed = str(int(self.lineEdit_7.text()))
            self.lineEdit_7.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setNames(self):
        self.name = self.lineEdit_8.text()
        self.RUname = self.lineEdit_9.text()
        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')

    def setMaterials(self):
        try:
            self.materials.append(self.lineEdit_3.text())
            self.materials.append(str(int(self.lineEdit_5.text()) / 100))
            self.lineEdit_3.setText('')
            self.lineEdit_5.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setMaxDurability(self):
        try:
            self.max_durability = str(int(self.lineEdit_6.text()))
            self.lineEdit_6.setText('')
        except ValueError:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))

    def setImage(self):
        if self.name != None:
            try:
                self.adress = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать картинку(в последнюю очередь)', '', 'Image (*.jpg, *.png)')[0]
                texture = Image.open(self.adress)
                texture.save(self.project + '\\' + self.project + '(r)\\' + 'textures\\items\\' + self.name + '.png')
                self.corr_im = False
            except AttributeError:
                pass

    def Func(self):
        variables = [self.name, self.RUname, self.project, self.materials, self.damage,
                     self.max_durability, self.destroy_speed]
        if None in variables or self.corr_im:
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/error_icon.png"))
        else:
            self.func(*variables)
            self.label_16.setPixmap(QtGui.QPixmap(
                "images_for_creator/complete_icon.png"))


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('images_for_creator/title.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1903, 971)
        MainWindow.setWindowTitle("")
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("MainWindow::MainWindow(QWidget *parent) :\n"
"QMainWindow(parent),\n"
"ui(new Ui::MainWindow)\n"
"{\n"
"ui->setupUi(this);\n"
"QPixmap bkgnd(\"images_for_creator/fone_for_project.jpg\");\n"
"bkgnd = bkgnd.scaled(this->size(), Qt::IgnoreAspectRatio);\n"
"QPalette palette;\n"
"palette.setBrush(QPalette::Background, bkgnd);\n"
"this->setPalette(palette);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(55, 20, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(StyleSheet(10))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_for_creator/iron_sword_gamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("images_for_creator/iron_sword_gamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("images_for_creator/iron_sword_gamed.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(128, 128))
        self.pushButton.setShortcut("")
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(55, 215, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(StyleSheet(10))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images_for_creator/iron_pickaxe_gamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("images_for_creator/iron_pickaxe_gamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("images_for_creator/iron_pickaxe_gamed.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(55, 410, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(StyleSheet(10))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images_for_creator/iron_axe_gamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(55, 605, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(StyleSheet(10))
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images_for_creator/iron_showel_gamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(55, 800, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(StyleSheet(10))
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images_for_creator/iron_hoe_gamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1941, 1131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images_for_creator/fone_for_project.jpg"))
        self.label.setObjectName("label")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 410, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(StyleSheet(10))
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images_for_creator/leggimgs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(250, 215, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(StyleSheet(10))
        self.pushButton_7.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images_for_creator/chestplate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(250, 20, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(StyleSheet(10))
        self.pushButton_8.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images_for_creator/helmet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_8.setShortcut("")
        self.pushButton_8.setAutoRepeat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(250, 605, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(StyleSheet(10))
        self.pushButton_9.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images_for_creator/boots.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(640, 30, 190, 120))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(StyleSheet(10))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images_for_creator/item_gamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon9)
        self.pushButton_11.setIconSize(QtCore.QSize(104, 104))
        self.pushButton_11.setShortcut("")
        self.pushButton_11.setAutoRepeat(False)
        self.pushButton_11.setAutoRepeatDelay(100)
        self.pushButton_11.setAutoRepeatInterval(300)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(445, 20, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet(StyleSheet(10))
        self.pushButton_12.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images_for_creator/block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon10)
        self.pushButton_12.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_12.setShortcut("")
        self.pushButton_12.setAutoRepeat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(640, 215, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet(StyleSheet(10))
        self.pushButton_13.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("images_for_creator/beef_gamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon11)
        self.pushButton_13.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_13.setShortcut("")
        self.pushButton_13.setAutoRepeat(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(445, 215, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet(StyleSheet(10))
        self.pushButton_14.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("images_for_creator/ore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon12)
        self.pushButton_14.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_14.setShortcut("")
        self.pushButton_14.setAutoRepeat(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(885, 20, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet(StyleSheet(10))
        self.pushButton_15.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("images_for_creator/crafting_table_top2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_15.setIcon(icon13)
        self.pushButton_15.setIconSize(QtCore.QSize(110, 110))
        self.pushButton_15.setShortcut("")
        self.pushButton_15.setAutoRepeat(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(830, 200, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet(StyleSheet(10))
        self.pushButton_16.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("images_for_creator/furnace2"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_16.setIcon(icon14)
        self.pushButton_16.setIconSize(QtCore.QSize(110, 110))
        self.pushButton_16.setShortcut("")
        self.pushButton_16.setAutoRepeat(False)
        self.pushButton_16.setObjectName("pushButton_16")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.pushButton_15.raise_()
        self.pushButton_16.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_11.setText(_translate("MainWindow", "item"))
        MainWindow.setWindowTitle(_translate("MainWindow", '!Minecraft Mod Creator!'))


class Minecraft_Mod_Creator(QtWidgets.QWidget, Ui_MainWindow1):
    def __init__(self, project):
        super().__init__()
        self.setupUi(self)
        self.project = project
        self.showMaximized()
        #  start_project(project)
        self.pushButton.clicked.connect(self.setSword)
        self.pushButton_2.clicked.connect(self.setPickaxe)
        self.pushButton_3.clicked.connect(self.setAxe)
        self.pushButton_4.clicked.connect(self.setShowel)
        self.pushButton_5.clicked.connect(self.setHoe)
        self.pushButton_8.clicked.connect(self.setHelmet)
        self.pushButton_7.clicked.connect(self.setChestplate)
        self.pushButton_6.clicked.connect(self.setLeggings)
        self.pushButton_9.clicked.connect(self.setBoots)
        self.pushButton_11.clicked.connect(self.setItem)
        self.pushButton_16.clicked.connect(self.setFurnaceRecipe)
        self.pushButton_14.clicked.connect(self.setOre)
        self.pushButton_15.clicked.connect(self.setCraft)
        self.pushButton_12.clicked.connect(self.setBlock)
        self.pushButton_13.clicked.connect(self.setEat)

    def setSword(self):
        self.exSword = Tools(self.project, 'Панель Создания Пользовательского Меча', sword_register, 'images_for_creator/iron_sword.png')
        self.exSword.show()

    def setPickaxe(self):
        self.exPickaxe = Tools(self.project, 'Панель Создания Пользовательской Кирки', pickaxe_register, 'images_for_creator/iron_pickaxe.png')
        self.exPickaxe.show()

    def setAxe(self):
        self.exAxe = Tools(self.project, 'Панель Создания Пользовательского Топора', axe_register, 'images_for_creator/iron_axe.png')
        self.exAxe.show()

    def setShowel(self):
        self.exShowel = Tools(self.project, 'Панель Создания Пользовательской Лопаты', shovel_register, 'images_for_creator/iron_shovel.png')
        self.exShowel.show()

    def setHoe(self):
        self.exHoe = Tools(self.project, 'Панель Создания Пользовательской Мотыги', hoe_register, 'images_for_creator/iron_hoe.png')
        self.exHoe.show()

    def setHelmet(self):
        self.ex = Armor(self.project, 'Панель Создания Пользовательского Шлема', helmet_register, 'images_for_creator/iron_helmet.png')
        self.ex.show()

    def setChestplate(self):
        self.exChestplate = Armor(self.project, 'Панель Создания Пользовательского Нагрудника', chestplate_register, 'images_for_creator/iron_chestplate.png')
        self.exChestplate.show()

    def setLeggings(self):
        self.exLeggings = Armor(self.project, 'Панель Создания Пользовательских Штанов', leggings_register, 'images_for_creator/iron_leggings.png')
        self.exLeggings.show()

    def setBoots(self):
        self.exBoots = Armor(self.project, 'Панель Создания Пользовательских Ботинок', boots_register, 'images_for_creator/iron_boots.png')
        self.exBoots.show()

    def setFurnaceRecipe(self):
        self.exFurnace = Furnace(self.project, furnace_recipe_register)
        self.exFurnace.show()

    def setItem(self):
        self.exItem = Item(self.project)
        self.exItem.show()

    def setOre(self):
        self.exOre = Ore(self.project)
        self.exOre.show()

    def setCraft(self):
        self.exCraft = CraftingTableCraft(self.project)
        self.exCraft.show()

    def setBlock(self):
        self.exBlock = Block(self.project)
        self.exBlock.show()

    def setEat(self):
        self.exEat = Eat(self.project)
        self.exEat.show()


def US_text(text):
    text = text.lower()
    us = 'qwertyuiopasdfghjklzxcvbnm_:1234567890'
    for i in range(len(text)):
        if text[i] not in us:
            return False
    return True


def uuid_generate():
    return str(uuid.uuid4())


def start_project(project):
    test_project = open('projects.txt', 'r')
    test_lines = list(map(lambda x: x[:-1], test_project.readlines()))
    test_project.close()
    if project not in test_lines:
        mkdir(project)
        project_for_projects = project
        project += '\\' + project
        mkdir(project)
        mkdir(project + '(r)')
        mkdir(project + '\\recipes')
        mkdir(project + '\\recipes\\furnace')
        mkdir(project + '(r)' + '\\textures')
        mkdir(project + '\\loot_tables')
        mkdir(project + '\\loot_tables\\blocks')
        mkdir(project + '(r)\\texts')
        mkdir(project + '\\items')
        mkdir(project + '(r)\\textures\\models')
        mkdir(project + '(r)\\textures\\models\\armor')
        mkdir(project + '\\functions')
        mkdir(project + '(r)\\items')
        mkdir(project + '\\features')
        mkdir(project + '(r)\\attachables')
        mkdir(project + '\\feature_rules')
        mkdir(project + '\\blocks')
        manifest = open(project + '\\manifest.json', 'x')
        uuid_beh = uuid_generate()
        uuid_res = uuid_generate()
        uuid_beh_2 = uuid_generate()
        uuid_res_2 = uuid_generate()
        text_manifest = ['{\n',
                         '    "format_version": 2,\n',
                         '    "header": {\n',
                         '        "description": "Was created by Minecraft Mod Creator'
                         '(From Murakaev Erlan Ruslanovich)",\n',
                         '        "name": "' + project_for_projects + '",\n',
                         '        "uuid": "' + uuid_beh + '",\n',
                         '        "version": [0, 0, 1],\n',
                         '        "min_engine_version": [1, 14, 0]\n'
                         '    },\n',
                         '    "modules": [\n',
                         '        {\n',
                         '            "description": "v.2.God_Mod_Creator",\n',
                         '            "type": "data",\n',
                         '            "uuid": "' + uuid_beh_2 + '",\n',
                         '            "version": [0, 0, 1]\n',
                         '        }\n',
                         '    ]\n',
                         '}']
        manifest.writelines(text_manifest)
        manifest.close()
        biome_client = open(project + '\\biome_client.json', 'x')
        biome_client.write('{\n  "biomes": {}\n}')
        biome_client.close()
        blocks = open(project + '(r)\\blocks.json', 'x')
        blocks.write('{\n  "format_version": [1, 1, 0]\n}')
        blocks.close()
        manifest = open(project + '(r)\\manifest.json', 'x')
        lines_of_manifest2 = ['{\n',
                              '  "format_version": 2,\n',
                              '  "header": {\n',
                              '    "name": "' + project_for_projects + '",\n',
                              '    "description": "Was created by Minecraft Mod Creator(From Murakaev'
                              ' Erlan Ruslanovich)",\n',
                              '    "uuid": "' + uuid_res + '",\n',
                              '    "version": [1, 0, 0],\n',
                              '    "min_engine_version": [1, 14, 0]\n',
                              '  },\n',
                              '  "modules": [\n',
                              '    {\n',
                              '      "description": "v.2.God_Mod_Creator",\n',
                              '      "type": "resources",\n',
                              '      "uuid": "' + uuid_res_2 + '",\n',
                              '      "version": [1, 0, 0]\n',
                              '    }\n',
                              '  ]\n',
                              '}']
        manifest.writelines(lines_of_manifest2)
        manifest.close()

        lines = ['{\n',
                 '  "resource_pack_name": "' + project_for_projects + '",\n',
                 '  "texture_name": "atlas.items",\n',
                 '  "texture_data": {\n',
                 '  }\n',
                 '}']
        opened_file = open(project + '(r)\\textures\\item_texture.json', 'x')
        opened_file.writelines(lines)
        opened_file.close()

        lines = ['{\n',
                 '  "resource_pack_name": "' + project_for_projects + '",\n',
                 '  "texture_name": "atlas.terrain",\n',
                 '  "padding": 8,\n',
                 '  "num_mip_levels": 4,\n',
                 '  "texture_data": {\n',
                 '  }\n',
                 '}']
        opened_file = open(project + '(r)\\textures\\terrain_texture.json', 'x')
        mkdir(project + '(r)\\textures\\items')
        mkdir(project + '(r)\\textures\\blocks')
        opened_file.writelines(lines)
        opened_file.close()
        pack_icon = Image.open('images_for_creator\\icon.png')
        pack_icon.save(project + '\\pack_icon.png')
        pack_icon.save(project + '(r)\\pack_icon.png')
        projects_txt = open('projects.txt', 'r')
        projects = projects_txt.readlines()
        projects.append(project_for_projects + '\n')
        projects_txt.close()
        projects_lines = open('projects.txt', 'w')
        projects_lines.writelines(projects)


def register_in_functions(name, project):
    adress = project + '/' + project
    lines_of_file = 'give @p ' + project + ':' + name
    try:
        opened_file = open(adress + '/functions/' + name + '.mcfunction', 'x')
    except FileExistsError:
        opened_file = open(adress + '/functions/' + name + '.mcfunction', 'w')
    opened_file.write(lines_of_file)
    opened_file.close()


def crafting_table_recipe_register(filename, project, output_item, strings_of_craft, keys, count):
    adress = project + '/' + project
    strings_of_craft = ['      ' + a for a in strings_of_craft]
    craft = ['{\n',
             '  "format_version": "1.12",\n',
             '  "minecraft:recipe_shaped": {\n',
             '    "description": {\n',
             '    "identifier": "' + output_item + '"\n',
             '    },\n',
             '    "tags": [ "crafting_table" ],\n',
             '    "pattern": [\n',
             '    ],\n',
             '    "key": {\n',
             '    },\n',
             '    "result": {\n',
             '      "item": "' + output_item + '",\n',
             '        "count": ' + count + '\n',
             '    }\n',
             '  }\n',
             '}']
    for i in range(len(strings_of_craft) - 1):
        craft = craft[:-9] + [strings_of_craft[i] + ',\n'] + craft[-9:]
    craft = craft[:-9] + [strings_of_craft[-1] + '\n'] + craft[-9:]
    list_of_keys = []
    keys_of_keys = list(keys.keys())
    for i in range(len(keys_of_keys) - 1):
        list_of_keys.extend(
            ['      "' + keys_of_keys[i] + '": {\n', '        "item": "' + keys[keys_of_keys[i]] + '"\n',
             '      },\n'])
    list_of_keys.extend(
        ['      "' + keys_of_keys[-1] + '": {\n', '        "item": "' + keys[keys_of_keys[-1]] + '"\n', '      }\n'])
    craft = craft[:-7] + list_of_keys + craft[-7:]
    try:
        opened_file = open(adress + '/recipes/' + filename + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/recipes/' + filename + '.json', 'w')
    opened_file.writelines(craft)
    opened_file.close()


def furnace_recipe_register(filename, input_item, output_item, count):
    craft = ['{\n',
             '  "format_version": "1.12",\n',
             '  "minecraft:recipe_furnace": {\n',
             '    "description": {\n',
             '    "identifier": "' + output_item + '"\n',
             '    },  \n',
             '    "tags": ["furnace", "blast_furnace", "smoking"],\n',
             '    "input": "' + input_item + '",\n',
             '    "output": "' + output_item + '",\n',
             '    "count": ' + count + '\n',
             '  } \n',
             '}']
    try:
        furnace_file_craft = open(filename + '.json', 'x')
    except FileExistsError:
        furnace_file_craft = open(filename + '.json', 'w')
    furnace_file_craft.writelines(craft)
    furnace_file_craft.close()


def biome_register(biome, spawn_in_world, name, project):
    adress = project + '/' + project
    lines_of_file = '{\n  "format_version": "1.13.0",\n  "minecraft:feature_rules": ' \
                    '{\n    "description": {\n      "identifier": "overworld_underground_' + \
                    name + '_feature",\n      "places_feature": "' + name + '_feature"\n  ' \
                    '  },\n    "conditions": {\n      "placement_pass": "underground_pass",' \
                    '\n      "minecraft:biome_filter": [\n        {\n          "any_of": [\n' \
                    '            {\n              "test": "has_biome_tag",\n' \
                    '              "operator": "==",\n              "value": "' + \
                    biome + '"\n            }\n          ]\n        }\n      ]\n    },\n' \
                    '    "distribution": {\n      "iterations": 16,\n      "coordinate_eval_order":' \
                    ' "zyx",\n      "x": {\n        "distribution": "uniform",\n        "extent": [\n' \
                    '          0,\n          16\n        ]\n      },\n      "y": {\n' \
                    '        "distribution": "uniform",\n        "extent": [\n' \
                    '          ' + spawn_in_world[0] + ',\n          ' + \
                    spawn_in_world[1] + '\n        ]\n      },\n      "z": {\n' \
                    '        "distribution": "uniform",\n        "extent": [\n' \
                    '          0,\n          16\n        ]\n      }\n    }\n  }\n}'
    try:
        opened_file = open(adress + '/feature_rules/overworld_underground_' + name + '_feature.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/feature_rules/overworld_underground_' + name + '_feature.json', 'w')
    opened_file.write(lines_of_file)
    opened_file.close()


def ore_register(name, runame, project, drop, spawn_in_world, biomes, count, sound, destroy='0.5'):
    adress = project + '/' + project
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.0",\n',
                     '  "minecraft:block": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "register_to_creative_menu": true\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:loot": "loot_tables/blocks/' + name +'.json",\n',
                     '      "minecraft:destroy_time": ' + destroy + ',\n',
                     '      "minecraft:friction": 0.7,\n',
                     '      "minecraft:map_color": "#3C3C3C",\n',
                     '      "minecraft:type": "metal",\n',
                     '      "minecraft:block_light_absorption": 15.0,\n',
                     '      "minecraft:block_light_emission": 0.0,\n',
                     '      "minecraft:explosion_resistance": 1.0\n',
                     '    }\n',
                     '  }\n',
                     '}']
    try:
        opened_file = open(adress + '/blocks/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/blocks/' + name + '.json', 'w')
    opened_file.writelines(lines_of_file)
    opened_file.close()
    register_in_functions(name, project)
    lines_of_file = ['{\n',
                     '  "pools": [\n',
                     '    {\n',
                     '      "rolls": 1,\n',
                     '      "entries": [\n',
                     '        {\n',
                     '          "type": "item",\n',
                     '          "weight": 1,\n',
                     '          "name": "' + drop + '",\n',
                     '          "functions": [\n',
                     '            {\n',
                     '              "function": "set_count",\n',
                     '              "count": {\n',
                     '                "min": ' + count[0] + ',\n',
                     '                "max": ' + count[1] + '\n',
                     '              }\n',
                     '            }\n',
                     '          ]\n',
                     '        }\n',
                     '      ]\n',
                     '    }\n',
                     '  ]\n',
                     '}']
    translate_in_game(name, runame, project)
    try:
        opened_file = open(adress + '/loot_tables/blocks/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/loot_tables/blocks/' + name + '.json', 'w')
    opened_file.writelines(lines_of_file)
    opened_file.close()
    for i in biomes:
        biome_register(i, spawn_in_world, name, project)
    lines_of_file = ['{\n',
                     '  "format_version": "1.13.0",\n',
                     '  "minecraft:ore_feature": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + name + '_feature"\n',
                     '    },\n',
                     '    "count": 12,\n',
                     '    "places_block": "' + project + ':' + name + '",\n',
                     '    "may_replace": [\n',
                     '      {\n',
                     '        "name": "minecraft:stone",\n',
                     '        "states": {\n',
                     '          "stone_type": "andesite"\n',
                     '        }\n',
                     '      },\n',
                     '      {\n',
                     '        "name": "minecraft:stone",\n',
                     '        "states": {\n',
                     '          "stone_type": "andesite_smooth"\n',
                     '        }\n',
                     '      },\n',
                     '      {\n',
                     '        "name": "minecraft:stone",\n',
                     '        "states": {\n',
                     '          "stone_type": "diorite"\n',
                     '        }\n',
                     '      },\n',
                     '      {\n',
                     '        "name": "minecraft:stone",\n',
                     '        "states": {\n',
                     '          "stone_type": "diorite_smooth"\n',
                     '        }\n',
                     '      },\n',
                     '      {\n',
                     '        "name": "minecraft:stone",\n',
                     '        "states": {\n',
                     '          "stone_type": "granite"\n',
                     '        }\n',
                     '      },\n',
                     '      {\n',
                     '        "name": "minecraft:stone",\n',
                     '        "states": {\n',
                     '          "stone_type": "granite_smooth"\n',
                     '        }\n',
                     '      },\n',
                     '      {\n',
                     '        "name": "minecraft:stone",\n',
                     '        "states": {\n',
                     '          "stone_type": "stone"\n',
                     '        }\n',
                     '      },\n',
                     '      {\n',
                     '        "name": "minecraft:netherrack",\n',
                     '        "states": {}\n',
                     '      },\n',
                     '      {\n',
                     '        "name": "minecraft:netherrack",\n',
                     '        "states": {}\n',
                     '      },\n',
                     '      {\n',
                     '        "name": "minecraft:netherrack",\n',
                     '        "states": {}\n',
                     '      },\n',
                     '      {\n',
                     '        "name": "minecraft:netherrack",\n',
                     '        "states": {}\n',
                     '      },\n',
                     '      {\n',
                     '        "name": "minecraft:netherrack",\n',
                     '        "states": {}\n',
                     '      },\n',
                     '      {\n',
                     '        "name": "minecraft:netherrack",\n',
                     '        "states": {}\n',
                     '      },\n',
                     '      {\n',
                     '        "name": "minecraft:netherrack",\n',
                     '        "states": {}\n',
                     '      }\n',
                     '    ]\n',
                     '  }\n',
                     '}']
    try:
        opened_file = open(adress + '/features/' + name + '_feature.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/features/' + name + '_feature.json', 'w')
    opened_file.writelines(lines_of_file)
    opened_file.close()
    reg_in_items(adress, name)
    reg_in_terrains(adress, name, project, sound)


def block_register(name, runame, project, destroy='0.5'):
    adress = project + '/' + project
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.0",\n',
                     '  "minecraft:block": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "register_to_creative_menu": true\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:loot": "loot_tables/blocks/' + name +'.json",\n',
                     '      "minecraft:destroy_time": ' + destroy + ',\n',
                     '      "minecraft:friction": 0.7,\n',
                     '      "minecraft:map_color": "#3C3C3C",\n',
                     '      "minecraft:type": "metal",\n',
                     '      "minecraft:block_light_absorption": 15.0,\n',
                     '      "minecraft:block_light_emission": 0.0,\n',
                     '      "minecraft:explosion_resistance": 1.0\n',
                     '    }\n',
                     '  }\n',
                     '}']
    try:
        opened_file = open(adress + '/blocks/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/blocks/' + name + '.json', 'w')
    opened_file.writelines(lines_of_file)
    opened_file.close()
    register_in_functions(name, project)
    lines_of_file = ['{\n',
                     '  "pools": [\n',
                     '    {\n',
                     '      "rolls": 1,\n',
                     '      "entries": [\n',
                     '        {\n',
                     '          "type": "item",\n',
                     '          "weight": 1,\n',
                     '          "name": "' + project + ':' + name + '",\n',
                     '          "functions": [\n',
                     '            {\n',
                     '              "function": "set_count",\n',
                     '              "count": {\n',
                     '                "min": 1,\n',
                     '                "max": 1\n',
                     '              }\n',
                     '            }\n',
                     '          ]\n',
                     '        }\n',
                     '      ]\n',
                     '    }\n',
                     '  ]\n',
                     '}']
    try:
        opened_file = open(adress + '/loot_tables/blocks/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/loot_tables/blocks/' + name + '.json', 'w')
    opened_file.writelines(lines_of_file)
    opened_file.close()
    reg_in_items(adress, name)
    reg_in_terrains(adress, name, project, 'stone')
    translate_in_game(name, runame, project)


def item_register(name, runame, project, max_stack_size, foil):
    adress = project + '/' + project
    register_in_functions(name, project)
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.100",\n',
                     '  "minecraft:item": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "category": "Items"\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:creative_category": {\n',
                     '        "parent": "itemGroup.name.diamond"\n',
                     '      },\n',
                     '      "minecraft:stacked_by_data": true,\n',
                     '      "minecraft:foil": ' + foil + ',\n',
                     '      "minecraft:max_stack_size": ' + max_stack_size + ',\n',
                     '      "minecraft:icon": {\n',
                     '      "texture": "' + name + '"\n',
                     '      },\n',
                     '      "minecraft:render_offsets": "apple",\n',
                     '      "minecraft:display_name": {}\n',
                     '    }\n',
                     '  }\n',
                     '}']
    try:
        opened_file = open(adress + '/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/items/' + name + '.json', 'w')
    opened_file.writelines(lines_of_file)
    opened_file.close()
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.100",\n',
                     '  "minecraft:item": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "category": "Items"\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:creative_category": {\n',
                     '        "parent": "itemGroup.name.diamond"\n',
                     '      },\n',
                     '      "minecraft:stacked_by_data": true,\n',
                     '      "minecraft:foil": ' + foil + ',\n',
                     '      "minecraft:max_stack_size": ' + max_stack_size + ',\n',
                     '      "minecraft:icon": {\n',
                     '      "texture": "' + name + '"\n',
                     '      },\n',
                     '      "minecraft:render_offsets": "apple",\n',
                     '      "minecraft:display_name": {}\n',
                     '    }\n',
                     '  }\n',
                     '}']
    try:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'w')
    opened_file.writelines(lines_of_file)
    opened_file.close()
    translate_in_game(name, runame, project)
    reg_in_items(adress, name)


def eat_register(name, runame, max_stack_size, use_duration, foil,
                 nutrition, saturation, can_always_eat, effects, project):
    adress = project + '\\' + project
    register_in_functions(name, project)
    translate_in_game(name, runame, project)
    lines = ['{\n',
             '  "format_version": "1.10",\n',
             '  "minecraft:item": {\n',
             '    "description": {\n',
             '      "identifier": "' + project + ':' + name + '",\n',
             '      "category": "Nature"\n',
             '    },\n',
             '\n',
             '    "components": {\n',
             '      "minecraft:icon": "' + name + '",\n',
             '      "minecraft:use_animation": "eat",\n',
             '      "minecraft:render_offsets": "apple"\n',
             '    }\n',
             '  }\n',
             '}']
    try:
        opened_file = open(adress + '(r)\\items\\' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)\\items\\' + name + '.json', 'w')
    opened_file.writelines(lines)
    opened_file.close()
    eff = ['        "effects": [\n',
           (''.join(['          {\n            "name": "' + effects[i][0] +
                     '",\n            "chance": 1.0,\n            "duration": ' +
                      effects[i][1] + ',\n            "amplifier": ' + effects[i][2] +
                      '\n          },\n' for i in range(0, len(effects))]))[:-2], '\n        ]'] if len(effects) != 0 else []
    lines = ['{\n',
             '  "format_version": "1.10",\n',
             '  "minecraft:item": {\n',
             '    "description": {\n',
             '      "identifier": "' + project + ':' + name + '"\n',
             '    },\n',
             '\n',
             '    "components": {\n',
             '      "minecraft:hand_equipped": false,\n',
             '      "minecraft:stacked_by_data": true,\n',
             '      "minecraft:max_stack_size": ' + max_stack_size + ',\n',
             '      "minecraft:use_duration": ' + use_duration + ',\n',
             '      "minecraft:foil": ' + foil + ',\n',
             '      "minecraft:food": {\n',
             '        "nutrition": ' + nutrition + ',\n',
             '        "saturation_modifier": "' + saturation + '",\n',
             '        "can_always_eat": ' + can_always_eat + ',\n',
             *eff,
             '\n      }\n',
             '    }\n',
             '  }\n',
             '}']
    try:
        opened_file = open(adress + '\\items\\' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '\\items\\' + name + '.json', 'w')
    opened_file.writelines(lines)
    opened_file.close()
    reg_in_items(adress, name)


def translate_in_game(name, gamename, project):
    adress = project + '/' + project
    opened_file = open(adress + '(r)/texts/en_US.lang', 'a')
    lines_of_file = [('\nitem.' + project + ':' + name + '.name=' + gamename)]
    opened_file.writelines(lines_of_file)
    opened_file.close()


def sword_register(name, runame, project, materials, damage, max_durability, destroy_speed):
    adress = project + '/' + project
    register_in_functions(name, project)
    try:
        opened_file = open(adress + '/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/items/' + name + '.json', 'w')
    lines_of_file = ['{\n',
                     '   "format_version": "1.16.100",\n',
                     '   "minecraft:item": {\n',
                     '     "description": {\n',
                     '       "identifier": "' + project + ':' + name + '",\n',
                     '       "category": "Equipment"\n',
                     '     },\n',
                     '     "components": {\n',
                     '       "tag:is_sword": {},\n',
                     '       "minecraft:icon": {\n',
                     '       "texture": "' + name + '"\n',
                     '       },\n',
                     '       "minecraft:display_name": {},\n',
                     '       "minecraft:max_stack_size": 1,\n',
                     '       "minecraft:hand_equipped": true,\n',
                     '       "minecraft:can_destroy_in_creative": false,\n',
                     '       "minecraft:creative_category": {\n',
                     '         "parent": "itemGroup.name.sword"\n',
                     '       },\n',
                     '       "minecraft:repairable": {\n',
                     '        "repair_items": [\n',
                     *['          {\n             "items":[\n               "' + materials[i] +
                          '"\n             ],\n             "repair_amount": "query.max_durability * ' +
                          materials[i + 1] + '"\n           },\n' for i in range(0, len(materials), 2)],
                     '{\n            "items":[\n',
                     '              "' + project + ':' + name + '"\n',
                     '            ],\n',
                     '            "repair_amount": "context.other->query.remaining_durability + '
                     '0.4 * context.other->query.max_durability"\n',
                     '          }\n',
                     '        ]\n',
                     '      },\n',
                     '      "minecraft:weapon": {\n',
                     '        "on_hurt_entity": {\n',
                     '            "event": "' + project + ':durability",\n',
                     '            "target": "self"\n',
                     '        }\n',
                     '      },\n',
                     '      "minecraft:damage": ' + damage + ',\n',
                     '      "minecraft:durability": {\n',
                     '        "max_durability": ' + max_durability + ',\n',
                     '        "damage_chance": {\n',
                     '          "min": 60,\n',
                     '          "max": 100\n',
                     '        }\n',
                     '      },\n',
                     '      "minecraft:digger": {\n',
                     '        "use_efficiency": false,\n',
                     '        "destroy_speeds": [\n',
                     '          {\n',
                     '            "block": "minecraft:web",\n',
                     '            "speed": ' + destroy_speed + '\n',
                     '          },\n',
                     '          {\n',
                     '            "block": "minecraft:bamboo",\n',
                     '            "speed": ' + destroy_speed + '\n',
                     '          }\n',
                     '        ],'
                     '          "on_dig": {\n',
                     '            "event": "' + project + ':durability"\n',
                     '            }\n',
                     '           },\n',
                     '       "minecraft:mining_speed": 4\n',
                     '     },\n',
                     '     "events":{\n',
                     '       "' + project + ':durability":{\n',
                     '         "damage": {\n',
                     '           "type": "durability",\n',
                     '           "amount": 1\n',
                     '         }\n',
                     '       }\n',
                     '     }\n',
                     '   }\n',
                     ' }']
    opened_file.writelines(lines_of_file)
    opened_file.close()
    try:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.100",\n',
                     '  "minecraft:item": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "category": "Equipment"\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:creative_category": {\n',
                     '        "parent": "itemGroup.name.sword"\n',
                     '      },\n',
                     '      "minecraft:icon": {\n',
                     '        "texture": "' + name + '"\n',
                     '      },\n',
                     '      "minecraft:render_offsets": "Tools",\n',
                     '      "minecraft:display_name": {}\n',
                     '    }\n',
                     '  }\n',
                     '}']
    opened_file.writelines(lines_of_file)
    opened_file.close()
    translate_in_game(name, runame, project)
    reg_in_items(adress, name)


def reg_in_items(adress, name):
    test_item = open('items.txt', 'r')
    list_ = list(map(lambda x: x[:-1], test_item.readlines()))
    if name not in list_:
        opened_file = open(adress + '(r)/textures/item_texture.json', 'r')
        test = ''
        lines_of_file = opened_file.read()
        if lines_of_file[-7] == '}':
            test = ','
        lines_of_file = lines_of_file[
                        :-6] + test + '\n    "' + name + '":{"textures":"textures/items/' + name + '"\n    }\n  }\n}'
        opened_file.close()
        opened_file = open(adress + '(r)/textures/item_texture.json', 'w')
        opened_file.write(lines_of_file)
        opened_file.close()
        list_.append(name)
        test_item.close()
        test_item = open('items.txt', 'w')
        test_item.writelines(list(map(lambda x: x + '\n', list_)))



def reg_in_terrains(adress, name, project, sound):
    test_item = open('terrains.txt', 'r')
    list_ = list(map(lambda x: x[:-1], test_item.readlines()))
    if name not in list_:
        opened_file = open(adress + '(r)/textures/terrain_texture.json', 'r')
        test = ''
        lines_of_file = opened_file.read()
        if lines_of_file[-7] == '}':
            test = ','
        lines_of_file = lines_of_file[:-6] + test + '\n    "' + name + '":{\n      "textures": [\n' \
                                                                       '        "textures/blocks/' + name + '"\n      ]\n    }\n  }\n}'
        opened_file.close()
        opened_file = open(adress + '(r)/textures/terrain_texture.json', 'w')
        opened_file.write(lines_of_file)
        opened_file.close()
        opened_file = open(adress + '(r)/blocks.json', 'r')
        lines_of_file = opened_file.read()
        lines_of_file = lines_of_file[:-2] + ',\n    "' + project + ':' + name + \
                        '": {\n    "textures": "' + name + '",\n    "sound": "' + sound + '"\n    }\n}'
        opened_file.close()
        opened_file = open(adress + '(r)/blocks.json', 'w')
        opened_file.write(lines_of_file)
        opened_file.close()
        list_.append(name)
        test_item.close()
        test_item = open('terrains.txt', 'w')
        test_item.writelines(list(map(lambda x: x + '\n', list_)))


def pickaxe_register(name, runame, project, materials, damage, max_durability, destroy_speed):
    adress = project + '/' + project
    register_in_functions(name, project)
    try:
        opened_file = open(adress + '/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/items/' + name + '.json', 'w')
    s = ['{\n',
         '  "format_version": "1.16.100",\n',
         '  "minecraft:item": {\n',
         '    "description": {\n',
         '      "identifier": "' + project + ':' + name + '",\n',
         '      "category": "Equipment"\n',
         '    },\n',
         '    "components": {\n',
         '      "tag:is_multitool": {},\n',
         '      "minecraft:icon": {\n',
         '      "texture": "' + name + '"\n',
         '      },\n',
         '      "minecraft:display_name": {},\n',
         '      "minecraft:max_stack_size": 1,\n',
         '      "minecraft:hand_equipped": true,\n',
         '      "minecraft:can_destroy_in_creative": false,\n',
         '      "minecraft:creative_category": {\n',
         '        "parent": "itemGroup.name.pickaxe"\n',
         '      },\n',
         '      "minecraft:repairable": {\n',
         '        "repair_items": [\n',
         *['          {\n             "items":[\n               "' + materials[i] +
                          '"\n             ],\n             "repair_amount": "query.max_durability * ' +
                          materials[i + 1] + '"\n           },\n' for i in range(0, len(materials), 2)],
         '          {\n            "items":[\n',
         '              "' + project + ':' + name + '"\n',
         '            ],\n',
         '            "repair_amount": "context.other->query.remaining_durability + '
         '0.4 * context.other->query.max_durability"\n',
         '          }\n',
         '        ]\n',
         '      },\n',
         '      "minecraft:weapon": {\n',
         '        "on_hurt_entity": {\n',
         '            "event": "' + project + ':durability",\n',
         '            "target": "self"\n',
         '        }\n',
         '      },\n',
         '\n',
         '      "minecraft:damage": ' + damage + ',\n',
         '\n',
         '      "minecraft:durability": {\n',
         '        "max_durability": ' + max_durability + ',\n',
         '        "damage_chance": {\n',
         '          "min": 60,\n',
         '          "max": 100\n',
         '        }\n',
         '      },\n',
         '      "minecraft:digger": {\n',
         '        "use_efficiency": true,\n',
         '        "destroy_speeds": [\n',
         '          {\n',
         '            "block": {\n',
         '              "tags": "q.any_tag(\'stone\', \'metal\', \'diamond_pick_diggable\')"\n',
         '            },\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:ice",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:nether_gold_ore",\n',
         '            "speed": 30\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:netherite_block",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:nether_quartz_ore",\n',
         '            "speed": 30\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:nether_bricks",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:netherrack",\n',
         '            "speed": 40\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:lapis_block",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:gold_block",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:iron_block",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:diamond_block",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:emerald_block",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:redstone_block",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:quartz_block",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:coal_block",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:bone_block",\n',
         '            "speed": 8\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:red_nether_bricks",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:obsidian",\n',
         '            "speed": 2\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:furnace",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:basalt",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_basalt",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:enchanting_table",\n',
         '            "speed": 8\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:end_stone",\n',
         '            "speed": 7\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:redstone_lamp",\n',
         '            "speed": 20\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:ender_chest",\n',
         '            "speed": 4\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:beacon",\n',
         '            "speed": 6\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:magma_block",\n',
         '            "speed": 15\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:iron_door",\n',
         '            "speed": 12\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:brewing_stand",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:cauldron",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:sandstone",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:warped_nylium",\n',
         '            "speed": 20\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:dispenser",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:chiseled_sandstone",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:cut_sandstone",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:crimson_nylium",\n',
         '            "speed": 20\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:nether_brick_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:brick_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stone_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:cut_sandstone_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:prismarine_brick_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:prismarine_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:purpur_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:cut_red_sandstone_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:red_sandstone_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:dark_prismarine_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:purpur_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:purpur_pillar",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:smooth_stone",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:purpur_block",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:smooth_red_sandstone",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_basalt",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:soul_soil",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_blackstone_pressure_plate",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stone_pressure_plate",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:spawner",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:infested_cracked_stonebricks",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:infested_mossy_stonebricks",\n',
         '            "speed": 5\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:infested_stonebricks",\n',
         '            "speed": 5\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:infested_cobblestone",\n',
         '            "speed": 5\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:infested_stone",\n',
         '            "speed": 5\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stonebrick",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:infested_chiseled_stonebricks",\n',
         '            "speed": 5\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:infested_cracked_stonebricks",\n',
         '            "speed": 5\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:infested_mossy_stonebricks",\n',
         '            "speed": 5\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:infested_stonebricks",\n',
         '            "speed": 5\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stone_brick_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:brick_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:cracked_stonebricks",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:chiseled_stonebricks",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:mossy_stonebricks",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:nether_brick_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:nether_brick_fence",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:chiseled_nether_bricks",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:cracked_nether_bricks",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:nether_bricks",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:beacon",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:ender_chest",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:sandstone_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:end_stone_bricks",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:end_stone",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:chipped_anvil",\n',
         '            "speed": 8\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:anvil",\n',
         '            "speed": 8\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_blackstone_wall",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_blackstone_brick_wall",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:blackstone_wall",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:hopper",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:nether_quartz_ore",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:heavy_weighted_pressure_plate",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:light_weighted_pressure_plate",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:damaged_anvil",\n',
         '            "speed": 8\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:dropper",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:quartz_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:quartz_bricks",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:hardened_clay",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 0,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 3,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 4,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 5,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 6,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 7,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 8,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 9,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 10,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 11,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 0,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 12,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 13,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 14,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 15,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 1,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stained_hardened_clay",\n',
         '            "data": 2,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:prismarine_brick_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:prismarine_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:dark_prismarine",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:prismarine_bricks",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:prismarine",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:red_sandstone_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:cut_red_sandstone",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:chiseled_red_sandstone",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:red_sandstone",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:dark_prismarine_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:white_shulker_box",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:red_nether_bricks",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:observer",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:magma_block",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:undyed_shulker_box",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 0,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 0,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 1,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 2,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 3,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 4,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 5,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 6,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 7,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 8,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 9,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 10,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 11,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 12,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 13,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 14,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shulker_box",\n',
         '            "data": 15,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:yellow_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:light_blue_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:magenta_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:orange_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:white_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:cyan_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:light_gray_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:gray_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:pink_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:lime_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:red_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:green_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:brown_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:blue_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:purple_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:black_glazed_terracotta",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 0,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 1,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 2,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 3,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 4,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 5,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 6,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 7,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 8,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 9,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 10,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 11,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 12,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 13,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 14,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:concrete",\n',
         '            "data": 15,\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:smooth_red_sandstone_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_granite_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:stone_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:end_stone_brick_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:mossy_cobblestone_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_diorite_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:mossy_stone_brick_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:red_nether_brick_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:andesite_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:granite_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:smooth_quartz_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:smooth_sandstone_stairs",\n',
         '            "speed": 10\n',
         '         },\n',
         '          {\n',
         '            "block": "minecraft:mossy_stone_brick_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:smooth_red_sandstone_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_granite_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:diorite_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_andesite_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:smooth_quartz_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:smooth_sandstone_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:end_stone_brick_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:mossy_cobblestone_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_diorite_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:diorite_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_andesite_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:red_nether_brick_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:andesite_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:granite_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:blackstone",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:crying_obsidian",\n',
         '            "speed": 2\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:ancient_debris",\n',
         '            "speed": 3\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:netherite_block",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:lodestone",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_blackstone_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_blackstone",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:gilded_blackstone",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:iron_trapdoor",\n',
         '            "speed": 16\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:blackstone_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:blackstone_slab",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_blackstone_brick_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:chiseled_polished_blackstone",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_blackstone_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_blackstone_bricks",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:polished_blackstone_brick_stairs",\n',
         '            "speed": 10\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:respawn_anchor",\n',
         '            "speed": 5,\n',
         '          }\n',
         '        ],\n',
         '            "on_dig": {\n',
         '              "event": "' + project + ':durability"\n',
         '            }\n',
         '          },\n',
         '      "minecraft:mining_speed": 24\n',
         '    },\n',
         '    "events":{\n',
         '      "' + project + ':durability":{\n',
         '        "damage": {\n',
         '          "type": "durability",\n',
         '          "amount": 1\n',
         '        }\n',
         '      }\n',
         '    }\n',
         '  }\n',
         '}']
    a = '0987654321'
    for i in range(0, len(s)):
        if '"speed": ' in s[i]:
            t = s[i].find('"speed": ') + 9
            if s[i][t + 1:t + 2] in a:
                s[i] = s[i][:t] + str(int(destroy_speed) * int(s[i][t:t + 2]) / 10)[:-2] + '\n'
            else:
                s[i] = s[i][:t] + str(int(destroy_speed) * int(s[i][t]) / 10)[:-2] + '\n'
    opened_file.writelines(s)
    opened_file.close()
    try:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.100",\n',
                     '  "minecraft:item": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "category": "Equipment"\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:creative_category": {\n',
                     '        "parent": "itemGroup.name.pickaxe"\n',
                     '      },\n',
                     '      "minecraft:icon": {\n',
                     '        "texture": "' + name + '"\n',
                     '      },\n',
                     '      "minecraft:render_offsets": "Tools",\n',
                     '      "minecraft:display_name": {}\n',
                     '    }\n',
                     '  }\n',
                     '}']
    opened_file.writelines(lines_of_file)
    opened_file.close()
    translate_in_game(name, runame, project)
    reg_in_items(adress, name)


def shovel_register(name, runame, project, materials, damage, max_durability, destroy_speed):
    adress = project + '/' + project
    register_in_functions(name, project)
    try:
        opened_file = open(adress + '/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/items/' + name + '.json', 'w')
    s = ['{\n',
         '  "format_version": "1.16.100",\n',
         '  "minecraft:item": {\n',
         '    "description": {\n',
         '      "identifier": "' + project + ':' + name + '",\n',
         '      "category": "Equipment"\n',
         '    },\n',
         '    "components": {\n',
         '      "tag:is_shovel": {},\n',
         '      "minecraft:icon": {\n',
         '      "texture": "' + name + '"\n',
         '      },\n',
         '      "minecraft:display_name": {},\n',
         '      "minecraft:use_on": {\n',
         '        "blocks": [\n',
         '          "minecraft:grass",\n',
         '          "minecraft:snow",\n',
         '          "minecraft:snow_layer"\n',
         '        ]\n',
         '      },\n',
         '      "minecraft:max_stack_size": 1,\n',
         '      "minecraft:hand_equipped": true,\n',
         '      "minecraft:can_destroy_in_creative": false,\n',
         '      "minecraft:creative_category": {\n',
         '        "parent": "itemGroup.name.shovel"\n',
         '      },\n',
         '      "minecraft:repairable": {\n',
         '        "repair_items": [\n',
         *['          {\n             "items":[\n               "' + materials[i] +
                          '"\n             ],\n             "repair_amount": "query.max_durability * ' +
                          materials[i + 1] + '"\n           },\n' for i in range(0, len(materials), 2)],
         '          {\n            "items":[\n',
         '              "' + project + ':' + name + '"\n',
         '            ],\n',
         '            "repair_amount": "context.other->query.remaining_durability + '
         '0.4 * context.other->query.max_durability"\n',
         '          }\n',
         '        ]\n',
         '      },\n',
         '      "minecraft:weapon": {\n',
         '        "on_hurt_entity": {\n',
         '            "event": "' + project + ':durability",\n',
         '            "target": "self"\n',
         '        }\n',
         '      },\n',
         '\n',
         '      "minecraft:damage": ' + damage + ',\n',
         '\n',
         '      "minecraft:durability": {\n',
         '        "max_durability": ' + max_durability + ',\n',
         '        "damage_chance": {\n',
         '          "min": 60,\n',
         '          "max": 100\n',
         '        }\n',
         '      },\n',
         '      "minecraft:digger": {\n',
         '        "use_efficiency": true,\n',
         '        "destroy_speeds": [\n',
         '          {\n',
         '            "block": {\n',
         '              "tags": "q.any_tag(\'dirt\', \'sand\', \'gravel\', \'grass\', \'snow\')"\n',
         '            },\n',
         '            "speed": 10\n',
         '          }\n',
         '        ],\n',
         '        "on_dig": {\n',
         '          "event": "' + project + ':durability"\n',
         '        }\n',
         '      },\n',
         '      "minecraft:mining_speed": 4\n',
         '    },\n',
         '    "events":{\n',
         '      "' + project + ':durability":{\n',
         '        "damage": {\n',
         '          "type": "durability",\n',
         '          "amount": 1\n',
         '        }\n',
         '      }\n',
         '    }\n',
         '  }\n',
         '}']
    a = '0987654321'
    for i in range(0, len(s)):
        if '"speed": ' in s[i]:
            t = s[i].find('"speed": ') + 9
            if s[i][t + 1:t + 2] in a:
                s[i] = s[i][:t] + str(int(destroy_speed) * int(s[i][t:t + 2]) / 10)[:-2] + '\n'
            else:
                s[i] = s[i][:t] + str(int(destroy_speed) * int(s[i][t]) / 10)[:-2] + '\n'
    opened_file.writelines(s)
    opened_file.close()
    try:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.100",\n',
                     '  "minecraft:item": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "category": "Equipment"\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:creative_category": {\n',
                     '        "parent": "itemGroup.name.shovel"\n',
                     '      },\n',
                     '      "minecraft:icon": {\n',
                     '        "texture": "' + name + '"\n',
                     '      },\n',
                     '      "minecraft:render_offsets": "Tools",\n',
                     '      "minecraft:display_name": {}\n',
                     '    }\n',
                     '  }\n',
                     '}']
    opened_file.writelines(lines_of_file)
    opened_file.close()
    translate_in_game(name, runame, project)
    reg_in_items(adress, name)


def axe_register(name, runame, project, materials, damage, max_durability, destroy_speed):
    adress = project + '/' + project
    register_in_functions(name, project)
    try:
        opened_file = open(adress + '/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/items/' + name + '.json', 'w')
    lines_axe = ['{\n',
                 '  "format_version": "1.16.100",\n',
                 '  "minecraft:item": {\n',
                 '    "description": {\n',
                 '      "identifier": "' + project + ':' + name + '",\n',
                 '      "category": "Equipment"\n',
                 '    },\n',
                 '    "components": {\n',
                 '      "tag:is_axe": {},\n',
                 '      "minecraft:icon": {\n',
                 '      "texture": "' + name + '"\n',
                 '      },\n',
                 '      "minecraft:display_name": {},\n',
                 '      "minecraft:use_on": {\n',
                 '        "blocks": [\n',
                 '          "log",\n',
                 '          "log2",\n',
                 '          "wood"\n',
                 '        ]\n',
                 '      },\n',
                 '      "minecraft:max_stack_size": 1,\n',
                 '      "minecraft:hand_equipped": true,\n',
                 '      "minecraft:can_destroy_in_creative": false,\n',
                 '      "minecraft:creative_category": {\n',
                 '        "parent": "itemGroup.name.axe"\n',
                 '      },\n',
                 '      "minecraft:repairable": {\n',
                 '        "repair_items": [\n',
                 *['          {\n             "items":[\n               "' + materials[i] +
                          '"\n             ],\n             "repair_amount": "query.max_durability * ' +
                          materials[i + 1] + '"\n           },\n' for i in range(0, len(materials), 2)],
                 '          {\n            "items":[\n',
                 '              "' + project + ':' + name + '"\n',
                 '            ],\n',
                 '            "repair_amount": "context.other->query.remaining_durability + '
                 '0.4 * context.other->query.max_durability"\n',
                 '          }\n',
                 '        ]\n',
                 '      },\n',
                 '      "minecraft:weapon": {\n',
                 '        "on_hurt_entity": {\n',
                 '            "event": "' + project + ':durability",\n',
                 '            "target": "self"\n',
                 '        }\n',
                 '      },\n',
                 '\n',
                 '      "minecraft:damage": ' + damage + ',\n',
                 '\n',
                 '      "minecraft:durability": {\n',
                 '        "max_durability": ' + max_durability + ',\n',
                 '        "damage_chance": {\n',
                 '          "min": 60,\n',
                 '          "max": 100\n',
                 '        }\n',
                 '      },\n',
                 '      "minecraft:digger": {\n',
                 '        "use_efficiency": true,\n',
                 '        "destroy_speeds": [\n',
                 '            {\n',
                 '                "block": {\n',
                 '                    "tags": "q.any_tag(\'wood\', \'pumpkin\', \'plant\')"\n',
                 '                },\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:chest",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:melon_block",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:crafting_table",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:crimson_planks",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:crimson_stem",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:stripped_crimson_stem",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:stripped_crimson_hyphae",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:crimson_hyphae",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:crimson_slab",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:crimson_pressure_plate",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:crimson_fence",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:crimson_trapdoor",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:crimson_fence_gate",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:crimson_stairs",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:crimson_button",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:crimson_wall_sign",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:warped_planks",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:warped_stem",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:stripped_warped_stem",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:stripped_warped_hyphae",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:warped_hyphae",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:warped_slab",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:warped_pressure_plate",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:warped_fence",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:warped_trapdoor",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:warped_fence_gate",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:warped_button",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:warped_door",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:warped_wall_sign",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:crimson_door",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:loom",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:trapped_chest",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:lectern",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:bookshelf",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:composter",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:jukebox",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:soul_campfire",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:campfire",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:bee_nest",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:beehive",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:cartography_table",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:scaffolding",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:warped_stairs",\n',
                 '                "speed": 16,\n',
                 '            },\n',
                 '            {\n',
                 '                "block": "minecraft:noteblock",\n',
                 '                "speed": 16,\n',
                 '            }        ],\n',
                 '        "on_dig": {\n',
                 '          "event": "' + project + ':durability"\n',
                 '        }\n',
                 '      },\n',
                 '      "minecraft:mining_speed": 4\n',
                 '    },\n',
                 '    "events":{\n',
                 '      "' + project + ':durability":{\n',
                 '        "damage": {\n',
                 '          "type": "durability",\n',
                 '          "amount": 1\n',
                 '        }\n',
                 '      }\n',
                 '    }\n',
                 '  }\n',
                 '}']
    a = '0987654321'
    for i in range(0, len(lines_axe)):
        if '"speed": ' in lines_axe[i]:
            t = lines_axe[i].find('"speed": ') + 9
            if lines_axe[i][t + 1] in a:
                lines_axe[i] = lines_axe[i][:t] + str(int(destroy_speed) * int(lines_axe[i][t:t + 2]) / 16)[:-2] + '\n'
            else:
                lines_axe[i] = lines_axe[i][:t] + str(int(destroy_speed) * int(lines_axe[i][t]) / 16)[:-2] + '\n'
    opened_file.writelines(lines_axe)
    opened_file.close()
    try:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.100",\n',
                     '  "minecraft:item": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "category": "Equipment"\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:creative_category": {\n',
                     '        "parent": "itemGroup.name.axe"\n',
                     '      },\n',
                     '      "minecraft:icon": {\n',
                     '        "texture": "' + name + '"\n',
                     '      },\n',
                     '      "minecraft:render_offsets": "Tools",\n',
                     '      "minecraft:display_name": {}\n',
                     '    }\n',
                     '  }\n',
                     '}']
    opened_file.writelines(lines_of_file)
    opened_file.close()
    translate_in_game(name, runame, project)
    reg_in_items(adress, name)


def hoe_register(name, runame, project, materials, damage, max_durability, destroy_speed):
    adress = project + '/' + project
    register_in_functions(name, project)
    try:
        opened_file = open(adress + '/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/items/' + name + '.json', 'w')
    s = ['{\n',
         '  "format_version": "1.16.100",\n',
         '  "minecraft:item": {\n',
         '    "description": {\n',
         '      "identifier": "' + project + ':' + name + '",\n',
         '      "category": "Equipment"\n',
         '    },\n',
         '    "components": {\n',
         '      "tag:is_hoe": {},\n',
         '      "minecraft:icon": {\n',
         '      "texture": "' + name + '"\n',
         '      },\n',
         '      "minecraft:display_name": {},\n',
         '      "minecraft:use_on": {\n',
         '        "blocks": [\n',
         '          "grass",\n',
         '          "dirt",\n',
         '          "grass_path"\n',
         '        ]\n',
         '      },\n'
         '      "minecraft:max_stack_size": 1,\n',
         '      "minecraft:hand_equipped": true,\n',
         '      "minecraft:can_destroy_in_creative": false,\n',
         '      "minecraft:creative_category": {\n',
         '        "parent": "itemGroup.name.hoe"\n',
         '      },\n',
         '      "minecraft:repairable": {\n',
         '        "repair_items": [\n',
         *['          {\n             "items":[\n               "' + materials[i] +
                          '"\n             ],\n             "repair_amount": "query.max_durability * ' +
                          materials[i + 1] + '"\n           },\n' for i in range(0, len(materials), 2)],
         '          {\n            "items":[\n',
         '              "' + project + ':' + name + '"\n',
         '            ],\n',
         '            "repair_amount": "context.other->query.remaining_durability + '
         '0.4 * context.other->query.max_durability"\n',
         '          }\n',
         '        ]\n',
         '      },\n',
         '      "minecraft:weapon": {\n',
         '        "on_hurt_entity": {\n',
         '            "event": "' + project + ':durability",\n',
         '            "target": "self"\n',
         '        }\n',
         '      },\n',
         '\n',
         '      "minecraft:damage": ' + damage + ',\n',
         '\n',
         '      "minecraft:durability": {\n',
         '        "max_durability": ' + max_durability + ',\n',
         '        "damage_chance": {\n',
         '          "min": 60,\n',
         '          "max": 100\n',
         '        }\n',
         '      },\n',
         '      "minecraft:digger": {\n',
         '        "use_efficiency": true,\n',
         '        "destroy_speeds": [\n',
         '          {\n',
         '            "block": "minecraft:leaves",\n',
         '            "speed": 16,\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:leaves2",\n',
         '            "speed": 16,\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:warped_wart_block",\n',
         '            "speed": 16,\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:nether_wart_block",\n',
         '            "speed": 16,\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:shroomlight",\n',
         '            "speed": 16,\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:sponge",\n',
         '            "speed": 16,\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:target",\n',
         '            "speed": 16,\n',
         '          },\n',
         '          {\n',
         '            "block": "minecraft:hay_block",\n',
         '            "speed": 16,\n',
         '          }\n'
         '        ],\n',
         '        "on_dig": {\n',
         '          "event": "' + project + ':durability"\n',
         '        }\n',
         '      },\n',
         '      "minecraft:mining_speed": 4\n',
         '    },\n',
         '    "events":{\n',
         '      "' + project + ':durability":{\n',
         '        "damage": {\n',
         '          "type": "durability",\n',
         '          "amount": 1\n',
         '        }\n',
         '      }\n',
         '    }\n',
         '  }\n',
         '}']
    a = '0987654321'
    for i in range(0, len(s)):
        if '"speed": ' in s[i]:
            t = s[i].find('"speed": ') + 9
            if s[i][t + 1:t + 2] in a:
                s[i] = s[i][:t] + str(int(destroy_speed) * int(s[i][t:t + 2]) / 16)[:-2] + '\n'
            else:
                s[i] = s[i][:t] + str(int(destroy_speed) * int(s[i][t]) / 16)[:-2] + '\n'
    opened_file.writelines(s)
    opened_file.close()
    try:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.100",\n',
                     '  "minecraft:item": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "category": "Equipment"\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:creative_category": {\n',
                     '        "parent": "itemGroup.name.hoe"\n',
                     '      },\n',
                     '      "minecraft:icon": {\n',
                     '        "texture": "' + name + '"\n',
                     '      },\n',
                     '      "minecraft:render_offsets": "Tools",\n',
                     '      "minecraft:display_name": {}\n',
                     '    }\n',
                     '  }\n',
                     '}']
    opened_file.writelines(lines_of_file)
    opened_file.close()
    translate_in_game(name, runame, project)
    reg_in_items(adress, name)


def boots_register(model_name, name, runame, project, materials, protection, max_durability):
    adress = project + '/' + project
    register_in_functions(name, project)
    translate_in_game(name, runame, project)
    try:
        opened_file = open(adress + '/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/items/' + name + '.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.100",\n',
                     '  "minecraft:item": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "category": "Equipment"\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:creative_category": {\n',
                     '        "parent": "itemGroup.name.boots"\n',
                     '      },\n',
                     '      "minecraft:repairable": {\n',
                     '        "repair_items": [\n',
                     *['          {\n            "items":[\n              "' + materials[i] +
                       '"\n            ],\n            "repair_amount": "query.max_durability * ' +
                       materials[i + 1] + '"\n          },\n' for i in range(0, len(materials), 2)],
                     '          {\n',
                     '            "items":[\n',
                     '              "' + project + ':' + name + '"\n',
                     '            ],\n',
                     '            "repair_amount": "context.other->query.remaining_durability + '
                     '0.4 * context.other->query.max_durability"\n',
                     '          }\n',
                     '        ]\n',
                     '      },\n',
                     '      "minecraft:max_stack_size": 1,\n',
                     '      "minecraft:enchantable": {\n',
                     '        "value": 10,\n',
                     '        "slot": "armor_feet"\n',
                     '      },\n',
                     '      "minecraft:durability": {\n',
                     '        "max_durability": ' + max_durability + ',\n',
                     '        "damage_chance": {\n',
                     '          "min": 60,\n',
                     '          "max": 100\n',
                     '        }\n',
                     '      },\n',
                     '      "minecraft:mining_speed": 8,\n',
                     '      "minecraft:damage": 3,\n',
                     '      "minecraft:armor": {\n',
                     '        "protection": ' + protection + '\n',
                     '      },\n',
                     '      "minecraft:wearable": {\n',
                     '        "slot": "slot.armor.feet"\n',
                     '      },\n',
                     '      "minecraft:icon": {\n',
                     '        "texture": "' + name + '"\n',
                     '      },\n',
                     '      "minecraft:render_offsets": "boots",\n',
                     '      "minecraft:display_name": {}\n',
                     '    }\n',
                     '  }\n',
                     '}']
    opened_file.writelines(lines_of_file)
    opened_file.close()
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.100",\n',
                     '  "minecraft:item": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "category": "Equipment"\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:creative_category": {\n',
                     '        "parent": "itemGroup.name.boots"\n',
                     '      },\n',
                     '      "minecraft:icon": {\n',
                     '        "texture": "' + name + '"\n',
                     '      },\n',
                     '      "minecraft:render_offsets": "boots",\n',
                     '      "minecraft:display_name": {}\n',
                     '    }\n',
                     '  }\n',
                     '}']
    try:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'w')
    opened_file.writelines(lines_of_file)
    opened_file.close()
    reg_in_items(adress, name)
    try:
        opened_file = open(adress + '(r)/attachables/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/attachables/' + name + '.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.8.0",\n',
                     '  "minecraft:attachable": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "materials": {\n',
                     '        "default": "armor",\n',
                     '        "enchanted": "armor_enchanted"\n',
                     '      },\n',
                     '      "textures": {\n',
                     '        "default": "textures/models/armor/' + model_name + '",\n',
                     '        "enchanted": "textures/misc/enchanted_item_glint"\n',
                     '      },\n',
                     '      "geometry": {\n',
                     '        "default": "geometry.humanoid.armor.boots"\n',
                     '      },\n',
                     '      "scripts": {\n',
                     '        "parent_setup": "variable.boot_layer_visible = 0.0;"\n',
                     '      },\n',
                     '      "render_controllers": [ "controller.render.armor" ]\n',
                     '    }\n',
                     '  }\n',
                     '}\n']
    opened_file.writelines(lines_of_file)
    opened_file.close()
    try:
        opened_file = open(adress + '(r)/attachables/' + name + '.player.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/attachables/' + name + '.player.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.10.0",\n',
                     '  "minecraft:attachable": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '.player",\n',
                     '      "item": { "' + project + ':' + name +
                     '": "query.owner_identifier == \'minecraft:player\'" },\n',
                     '      "materials": {\n',
                     '        "default": "armor",\n',
                     '        "enchanted": "armor_enchanted"\n',
                     '      },\n',
                     '      "textures": {\n',
                     '        "default": "textures/models/armor/' + model_name + '",\n',
                     '        "enchanted": "textures/misc/enchanted_item_glint"\n',
                     '      },\n',
                     '      "geometry": {\n',
                     '        "default": "geometry.player.armor.boots"\n',
                     '      },\n',
                     '      "scripts": {\n',
                     '        "parent_setup": "variable.boot_layer_visible = 0.0;",\n',
                     '        "animate": [\n',
                     '          "offset"\n',
                     '        ]\n',
                     '      },\n',
                     '      "animations": {\n',
                     '        "offset": "animation.armor.boots.offset"\n',
                     '      },\n',
                     '      "render_controllers": [ "controller.render.armor" ]\n',
                     '    }\n',
                     '  }\n',
                     '}\n']
    opened_file.writelines(lines_of_file)
    opened_file.close()


def chestplate_register(model_name, name, runame, project, materials, protection, max_durability):
    adress = project + '/' + project
    register_in_functions(name, project)
    translate_in_game(name, runame, project)
    try:
        opened_file = open(adress + '/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/items/' + name + '.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.100",\n',
                     '  "minecraft:item": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "category": "Equipment"\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:creative_category": {\n',
                     '        "parent": "itemGroup.name.chestplate"\n',
                     '      },\n',
                     '      "minecraft:repairable": {\n',
                     '        "repair_items": [\n',
                     *['          {\n            "items":[\n              "' + materials[i] +
                       '"\n            ],\n            "repair_amount": "query.max_durability * ' +
                       materials[i + 1] + '"\n          },\n' for i in range(0, len(materials), 2)],
                     '          {\n',
                     '            "items":[\n',
                     '              "' + project + ':' + name + '"\n',
                     '            ],\n',
                     '            "repair_amount": "context.other->query.remaining_durability + '
                     '0.4 * context.other->query.max_durability"\n',
                     '          }\n',
                     '        ]\n',
                     '      },\n',
                     '      "minecraft:max_stack_size": 1,\n',
                     '      "minecraft:enchantable": {\n',
                     '        "value": 10,\n',
                     '        "slot": "armor_torso"\n',
                     '      },\n',
                     '      "minecraft:durability": {\n',
                     '        "max_durability": ' + max_durability + ',\n',
                     '        "damage_chance": {\n',
                     '          "min": 60,\n',
                     '          "max": 100\n',
                     '        }\n',
                     '      },\n',
                     '      "minecraft:mining_speed": 8,\n',
                     '      "minecraft:damage": 3,\n',
                     '      "minecraft:armor": {\n',
                     '        "protection": ' + protection + '\n',
                     '      },\n',
                     '      "minecraft:wearable": {\n',
                     '        "slot": "slot.armor.chest"\n',
                     '      },\n',
                     '      "minecraft:icon": {\n',
                     '        "texture": "' + name + '"\n',
                     '      },\n',
                     '      "minecraft:render_offsets": "chestplates",\n',
                     '      "minecraft:display_name": {}\n',
                     '    }\n',
                     '  }\n',
                     '}']
    opened_file.writelines(lines_of_file)
    opened_file.close()
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.100",\n',
                     '  "minecraft:item": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "category": "Equipment"\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:creative_category": {\n',
                     '        "parent": "itemGroup.name.chestplate"\n',
                     '      },\n',
                     '      "minecraft:icon": {\n',
                     '        "texture": "' + name + '"\n',
                     '      },\n',
                     '      "minecraft:render_offsets": "chestplate",\n',
                     '      "minecraft:display_name": {}\n',
                     '    }\n',
                     '  }\n',
                     '}']
    try:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'w')
    opened_file.writelines(lines_of_file)
    opened_file.close()
    reg_in_items(adress, name)
    try:
        opened_file = open(adress + '(r)/attachables/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/attachables/' + name + '.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.8.0",\n',
                     '  "minecraft:attachable": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "materials": {\n',
                     '        "default": "armor",\n',
                     '        "enchanted": "armor_enchanted"\n',
                     '      },\n',
                     '      "textures": {\n',
                     '        "default": "textures/models/armor/' + model_name + '",\n',
                     '        "enchanted": "textures/misc/enchanted_item_glint"\n',
                     '      },\n',
                     '      "geometry": {\n',
                     '        "default": "geometry.humanoid.armor.chestplate"\n',
                     '      },\n',
                     '      "scripts": {\n',
                     '        "parent_setup": "variable.chest_layer_visible = 0.0;"\n',
                     '      },\n',
                     '      "render_controllers": [ "controller.render.armor" ]\n',
                     '    }\n',
                     '  }\n',
                     '}\n']
    opened_file.writelines(lines_of_file)
    opened_file.close()
    try:
        opened_file = open(adress + '(r)/attachables/' + name + '.player.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/attachables/' + name + '.player.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.10.0",\n',
                     '  "minecraft:attachable": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '.player",\n',
                     '      "item": { "' + project + ':' + name +
                     '": "query.owner_identifier == \'minecraft:player\'" },\n',
                     '      "materials": {\n',
                     '        "default": "armor",\n',
                     '        "enchanted": "armor_enchanted"\n',
                     '      },\n',
                     '      "textures": {\n',
                     '        "default": "textures/models/armor/' + model_name + '",\n',
                     '        "enchanted": "textures/misc/enchanted_item_glint"\n',
                     '      },\n',
                     '      "geometry": {\n',
                     '        "default": "geometry.player.armor.chestplate"\n',
                     '      },\n',
                     '      "scripts": {\n',
                     '        "parent_setup": "variable.chest_layer_visible = 0.0;"\n',
                     '      },\n',
                     '      "render_controllers": [ "controller.render.armor" ]\n',
                     '    }\n',
                     '  }\n',
                     '}\n']
    opened_file.writelines(lines_of_file)
    opened_file.close()


def helmet_register(model_name, name, runame, project, materials, protection, max_durability):
    adress = project + '/' + project
    register_in_functions(name, project)
    translate_in_game(name, runame, project)
    try:
        opened_file = open(adress + '/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/items/' + name + '.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.100",\n',
                     '  "minecraft:item": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "category": "Equipment"\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:creative_category": {\n',
                     '        "parent": "itemGroup.name.helmet"\n',
                     '      },\n',
                     '      "minecraft:repairable": {\n',
                     '        "repair_items": [\n',
                     *['          {\n            "items":[\n              "' + materials[i] +
                       '"\n            ],\n            "repair_amount": "query.max_durability * ' +
                       materials[i + 1] + '"\n          },\n' for i in range(0, len(materials), 2)],
                     '          {\n            "items":[\n',
                     '              "' + project + ':' + name + '"\n',
                     '            ],\n',
                     '            "repair_amount": "context.other->query.remaining_durability + '
                     '0.4 * context.other->query.max_durability"\n',
                     '          }\n',
                     '        ]\n',
                     '      },\n',
                     '      "minecraft:max_stack_size": 1,\n',
                     '      "minecraft:enchantable": {\n',
                     '        "value": 10,\n',
                     '        "slot": "armor_head"\n',
                     '      },\n',
                     '      "minecraft:durability": {\n',
                     '        "max_durability": ' + max_durability + ',\n',
                     '        "damage_chance": {\n',
                     '          "min": 60,\n',
                     '          "max": 100\n',
                     '        }\n',
                     '      },\n',
                     '      "minecraft:mining_speed": 8,\n',
                     '      "minecraft:damage": 3,\n',
                     '      "minecraft:armor": {\n',
                     '        "protection": ' + protection + '\n',
                     '      },\n',
                     '      "minecraft:wearable": {\n',
                     '        "slot": "slot.armor.head"\n',
                     '      },\n',
                     '      "minecraft:icon": {\n',
                     '        "texture": "' + name + '"\n',
                     '      },\n',
                     '      "minecraft:render_offsets": "helmets",\n',
                     '      "minecraft:display_name": {}\n',
                     '    }\n',
                     '  }\n',
                     '}']
    opened_file.writelines(lines_of_file)
    opened_file.close()
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.100",\n',
                     '  "minecraft:item": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "category": "Equipment"\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:creative_category": {\n',
                     '        "parent": "itemGroup.name.helmet"\n',
                     '      },\n',
                     '      "minecraft:icon": {\n',
                     '        "texture": "' + name + '"\n',
                     '      },\n',
                     '      "minecraft:render_offsets": "helmet",\n',
                     '      "minecraft:display_name": {}\n',
                     '    }\n',
                     '  }\n',
                     '}']
    try:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'w')
    opened_file.writelines(lines_of_file)
    opened_file.close()
    reg_in_items(adress, name)

    try:
        opened_file = open(adress + '(r)/attachables/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/attachables/' + name + '.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.8.0",\n',
                     '  "minecraft:attachable": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "materials": {\n',
                     '        "default": "armor",\n',
                     '        "enchanted": "armor_enchanted"\n',
                     '      },\n',
                     '      "textures": {\n',
                     '        "default": "textures/models/armor/' + model_name + '",\n',
                     '        "enchanted": "textures/misc/enchanted_item_glint"\n',
                     '      },\n',
                     '      "geometry": {\n',
                     '        "default": "geometry.humanoid.armor.helmet"\n',
                     '      },\n',
                     '      "scripts": {\n',
                     '        "parent_setup": "variable.helmet_layer_visible = 0.0;"\n',
                     '      },\n',
                     '      "render_controllers": [ "controller.render.armor" ]\n',
                     '    }\n',
                     '  }\n',
                     '}\n']
    opened_file.writelines(lines_of_file)
    opened_file.close()
    try:
        opened_file = open(adress + '(r)/attachables/' + name + '.player.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/attachables/' + name + '.player.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.10.0",\n',
                     '  "minecraft:attachable": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '.player",\n',
                     '      "item": { "' + project + ':' + name + '": "query.owner_identifier == \'minecraft:player\'" },\n',
                     '      "materials": {\n',
                     '        "default": "armor",\n',
                     '        "enchanted": "armor_enchanted"\n',
                     '      },\n',
                     '      "textures": {\n',
                     '        "default": "textures/models/armor/' + model_name + '",\n',
                     '        "enchanted": "textures/misc/enchanted_item_glint"\n',
                     '      },\n',
                     '      "geometry": {\n',
                     '        "default": "geometry.player.armor.helmet"\n',
                     '      },\n',
                     '      "scripts": {\n',
                     '        "parent_setup": "variable.helmet_layer_visible = 0.0;"\n',
                     '      },\n',
                     '      "render_controllers": [ "controller.render.armor" ]\n',
                     '    }\n',
                     '  }\n',
                     '}']
    opened_file.writelines(lines_of_file)
    opened_file.close()


def leggings_register(model_name, name, runame, project, materials, protection, max_durability):
    adress = project + '/' + project
    register_in_functions(name, project)
    translate_in_game(name, runame, project)
    try:
        opened_file = open(adress + '/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '/items/' + name + '.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.100",\n',
                     '  "minecraft:item": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "category": "Equipment"\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:creative_category": {\n',
                     '        "parent": "itemGroup.name.leggings"\n',
                     '      },\n',
                     '      "minecraft:repairable": {\n',
                     '        "repair_items": [\n',
                     *['          {\n            "items":[\n              "' + materials[i] +
                     '"\n            ],\n            "repair_amount": "query.max_durability * ' +
                       materials[i + 1] + '"\n          },\n' for i in range(0, len(materials), 2)],
                     '          {\n',
                     '            "items":[\n',
                     '              "' + project + ':' + name + '"\n',
                     '            ],\n',
                     '            "repair_amount": "context.other->query.remaining_durability + '
                     '0.4 * context.other->query.max_durability"\n',
                     '          }\n',
                     '        ]\n',
                     '      },\n',
                     '      "minecraft:max_stack_size": 1,\n',
                     '      "minecraft:enchantable" : {\n',
                     '        "value": 10,\n',
                     '        "slot": "armor_legs"\n',
                     '      },\n',
                     '      "minecraft:durability": {\n',
                     '        "max_durability": ' + max_durability + ',\n',
                     '        "damage_chance": {\n',
                     '          "min": 60,\n',
                     '          "max": 100\n',
                     '        }\n',
                     '      },\n',
                     '      "minecraft:mining_speed": 8,\n',
                     '      "minecraft:damage": 3,\n',
                     '      "minecraft:armor": {\n',
                     '        "protection": ' + protection + '\n',
                     '      },\n',
                     '      "minecraft:wearable": {\n',
                     '        "slot": "slot.armor.legs"\n',
                     '      },\n',
                     '      "minecraft:icon": {\n',
                     '        "texture": "' + name + '"\n',
                     '      },\n',
                     '      "minecraft:render_offsets": "leggings",\n',
                     '      "minecraft:display_name": {}\n',
                     '    }\n',
                     '  }\n',
                     '}']
    opened_file.writelines(lines_of_file)
    opened_file.close()
    lines_of_file = ['{\n',
                     '  "format_version": "1.16.100",\n',
                     '  "minecraft:item": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "category": "Equipment"\n',
                     '    },\n',
                     '    "components": {\n',
                     '      "minecraft:creative_category": {\n',
                     '        "parent": "itemGroup.name.leggings"\n',
                     '      },\n',
                     '      "minecraft:icon": {\n',
                     '        "texture": "' + name + '"\n',
                     '      },\n',
                     '      "minecraft:render_offsets": "leggings",\n',
                     '      "minecraft:display_name": {}\n',
                     '    }\n',
                     '  }\n',
                     '}']
    try:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/items/' + name + '.json', 'w')
    opened_file.writelines(lines_of_file)
    opened_file.close()
    reg_in_items(adress, name)

    try:
        opened_file = open(adress + '(r)/attachables/' + name + '.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/attachables/' + name + '.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.8.0",\n',
                     '  "minecraft:attachable": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '",\n',
                     '      "materials": {\n',
                     '        "default": "armor",\n',
                     '        "enchanted": "armor_enchanted"\n',
                     '      },\n',
                     '      "textures": {\n',
                     '        "default": "textures/models/armor/' + model_name + '",\n',
                     '        "enchanted": "textures/misc/enchanted_item_glint"\n',
                     '      },\n',
                     '      "geometry": {\n',
                     '        "default": "geometry.humanoid.armor.leggings"\n',
                     '      },\n',
                     '      "scripts": {\n',
                     '        "parent_setup": "variable.leg_layer_visible = 0.0;"\n',
                     '      },\n',
                     '      "render_controllers": [ "controller.render.armor" ]\n',
                     '    }\n',
                     '  }\n',
                     '}\n']
    opened_file.writelines(lines_of_file)
    opened_file.close()
    try:
        opened_file = open(adress + '(r)/attachables/' + name + '.player.json', 'x')
    except FileExistsError:
        opened_file = open(adress + '(r)/attachables/' + name + '.player.json', 'w')
    lines_of_file = ['{\n',
                     '  "format_version": "1.10.0",\n',
                     '  "minecraft:attachable": {\n',
                     '    "description": {\n',
                     '      "identifier": "' + project + ':' + name + '.player",\n',
                     '      "item": { "' + project + ':' + name +
                     '": "query.owner_identifier == \'minecraft:player\'" },\n',
                     '      "materials": {\n',
                     '        "default": "armor",\n',
                     '        "enchanted": "armor_enchanted"\n',
                     '      },\n',
                     '      "textures": {\n',
                     '        "default": "textures/models/armor/' + model_name + '",\n',
                     '        "enchanted": "textures/misc/enchanted_item_glint"\n',
                     '      },\n',
                     '      "geometry": {\n',
                     '        "default": "geometry.player.armor.leggings"\n',
                     '      },\n',
                     '      "scripts": {\n',
                     '        "parent_setup": "variable.leg_layer_visible = 0.0;"\n',
                     '      },\n',
                     '      "render_controllers": [ "controller.render.armor" ]\n',
                     '    }\n',
                     '  }\n',
                     '}\n']
    opened_file.writelines(lines_of_file)
    opened_file.close()


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)

    text += ''.join(traceback.format_tb(tb))

    print(text)
    QtWidgets.QMessageBox.critical(None, 'Error', text)

    sys.exit()


sys.excepthook = log_uncaught_exceptions


def StyleSheet(br):
    styleSheet = GlobalStyleSheetButton
    styleSheet.insert(1, f"    border-radius: {br}px;\n")
    return styleSheet


GlobalStyleSheetButton = ["QPushButton{\n",
"    border: 2px solid rgba(255, 255, 255, 255);\n",
"    background-color: rgba(231, 231, 231, 80);\n",
"}\n",
"\n",
"QPushButton:hover{\n",
"    border: 2px solid rgba(110, 160, 255, 255);\n",
"    background-color: rgba(168, 200, 255, 100);\n",
"}\n",
"\n",
"QPushButton:pressed {\n",
"    border: 2px solid rgba(90, 140, 255, 255);\n",
"    background-color: rgba(140, 170, 255, 120);\n"
"}"]
StyleLabel13 = ["QLabel{\n"
"    border-radius: 13px;\n"
"    border: 2px solid rgba(255, 255, 255, 255);\n"
"    background-color: rgba(231, 231, 231, 80);\n"
"}"]
