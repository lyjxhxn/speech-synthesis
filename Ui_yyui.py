# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\py\语音合成\yyui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(821, 489)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/yylogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setToolTip("")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 70, 481, 171))
        self.plainTextEdit.setPlaceholderText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 20, 191, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.AuditionBut = QtWidgets.QPushButton(Form)
        self.AuditionBut.setGeometry(QtCore.QRect(570, 210, 92, 28))
        self.AuditionBut.setObjectName("AuditionBut")
        self.SubmitBut = QtWidgets.QPushButton(Form)
        self.SubmitBut.setGeometry(QtCore.QRect(660, 420, 101, 41))
        self.SubmitBut.setObjectName("SubmitBut")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 390, 72, 20))
        self.label_2.setObjectName("label_2")
        self.lineEditPath = QtWidgets.QLineEdit(Form)
        self.lineEditPath.setGeometry(QtCore.QRect(150, 390, 511, 21))
        self.lineEditPath.setFrame(True)
        self.lineEditPath.setObjectName("lineEditPath")
        self.browseBut = QtWidgets.QPushButton(Form)
        self.browseBut.setGeometry(QtCore.QRect(680, 390, 81, 21))
        self.browseBut.setObjectName("browseBut")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(50, 250, 721, 131))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_ty = QtWidgets.QWidget()
        self.tab_ty.setObjectName("tab_ty")
        self.radioButton_Xiaoyun = QtWidgets.QRadioButton(self.tab_ty)
        self.radioButton_Xiaoyun.setGeometry(QtCore.QRect(20, 10, 121, 19))
        self.radioButton_Xiaoyun.setChecked(True)
        self.radioButton_Xiaoyun.setObjectName("radioButton_Xiaoyun")
        self.radioButton_Xiaogang = QtWidgets.QRadioButton(self.tab_ty)
        self.radioButton_Xiaogang.setEnabled(True)
        self.radioButton_Xiaogang.setGeometry(QtCore.QRect(150, 10, 131, 19))
        self.radioButton_Xiaogang.setCheckable(True)
        self.radioButton_Xiaogang.setChecked(False)
        self.radioButton_Xiaogang.setObjectName("radioButton_Xiaogang")
        self.radioButton_Ruoxi = QtWidgets.QRadioButton(self.tab_ty)
        self.radioButton_Ruoxi.setEnabled(True)
        self.radioButton_Ruoxi.setGeometry(QtCore.QRect(290, 10, 131, 19))
        self.radioButton_Ruoxi.setCheckable(True)
        self.radioButton_Ruoxi.setChecked(False)
        self.radioButton_Ruoxi.setObjectName("radioButton_Ruoxi")
        self.radioButton_Siqi = QtWidgets.QRadioButton(self.tab_ty)
        self.radioButton_Siqi.setEnabled(True)
        self.radioButton_Siqi.setGeometry(QtCore.QRect(430, 10, 121, 19))
        self.radioButton_Siqi.setCheckable(True)
        self.radioButton_Siqi.setChecked(False)
        self.radioButton_Siqi.setObjectName("radioButton_Siqi")
        self.radioButton_Sijia = QtWidgets.QRadioButton(self.tab_ty)
        self.radioButton_Sijia.setEnabled(True)
        self.radioButton_Sijia.setGeometry(QtCore.QRect(570, 10, 121, 19))
        self.radioButton_Sijia.setCheckable(True)
        self.radioButton_Sijia.setChecked(False)
        self.radioButton_Sijia.setObjectName("radioButton_Sijia")
        self.radioButton_Aida = QtWidgets.QRadioButton(self.tab_ty)
        self.radioButton_Aida.setEnabled(True)
        self.radioButton_Aida.setGeometry(QtCore.QRect(570, 40, 121, 19))
        self.radioButton_Aida.setCheckable(True)
        self.radioButton_Aida.setChecked(False)
        self.radioButton_Aida.setObjectName("radioButton_Aida")
        self.radioButton_Aijia = QtWidgets.QRadioButton(self.tab_ty)
        self.radioButton_Aijia.setEnabled(True)
        self.radioButton_Aijia.setGeometry(QtCore.QRect(290, 40, 131, 19))
        self.radioButton_Aijia.setCheckable(True)
        self.radioButton_Aijia.setChecked(False)
        self.radioButton_Aijia.setObjectName("radioButton_Aijia")
        self.radioButton_Aicheng = QtWidgets.QRadioButton(self.tab_ty)
        self.radioButton_Aicheng.setEnabled(True)
        self.radioButton_Aicheng.setGeometry(QtCore.QRect(430, 40, 121, 19))
        self.radioButton_Aicheng.setCheckable(True)
        self.radioButton_Aicheng.setChecked(False)
        self.radioButton_Aicheng.setObjectName("radioButton_Aicheng")
        self.radioButton_Sicheng = QtWidgets.QRadioButton(self.tab_ty)
        self.radioButton_Sicheng.setGeometry(QtCore.QRect(20, 40, 121, 19))
        self.radioButton_Sicheng.setChecked(False)
        self.radioButton_Sicheng.setObjectName("radioButton_Sicheng")
        self.radioButton_Aiqi = QtWidgets.QRadioButton(self.tab_ty)
        self.radioButton_Aiqi.setEnabled(True)
        self.radioButton_Aiqi.setGeometry(QtCore.QRect(150, 40, 131, 19))
        self.radioButton_Aiqi.setCheckable(True)
        self.radioButton_Aiqi.setChecked(False)
        self.radioButton_Aiqi.setObjectName("radioButton_Aiqi")
        self.radioButton_Ninger = QtWidgets.QRadioButton(self.tab_ty)
        self.radioButton_Ninger.setGeometry(QtCore.QRect(20, 70, 121, 19))
        self.radioButton_Ninger.setChecked(False)
        self.radioButton_Ninger.setObjectName("radioButton_Ninger")
        self.radioButton_Ruilin = QtWidgets.QRadioButton(self.tab_ty)
        self.radioButton_Ruilin.setEnabled(True)
        self.radioButton_Ruilin.setGeometry(QtCore.QRect(150, 70, 131, 19))
        self.radioButton_Ruilin.setCheckable(True)
        self.radioButton_Ruilin.setChecked(False)
        self.radioButton_Ruilin.setObjectName("radioButton_Ruilin")
        self.tabWidget.addTab(self.tab_ty, "")
        self.tab_kf = QtWidgets.QWidget()
        self.tab_kf.setObjectName("tab_kf")
        self.radioButton_Xiaomei = QtWidgets.QRadioButton(self.tab_kf)
        self.radioButton_Xiaomei.setEnabled(True)
        self.radioButton_Xiaomei.setGeometry(QtCore.QRect(290, 40, 131, 19))
        self.radioButton_Xiaomei.setCheckable(True)
        self.radioButton_Xiaomei.setChecked(False)
        self.radioButton_Xiaomei.setObjectName("radioButton_Xiaomei")
        self.radioButton_Aijing = QtWidgets.QRadioButton(self.tab_kf)
        self.radioButton_Aijing.setEnabled(True)
        self.radioButton_Aijing.setGeometry(QtCore.QRect(150, 40, 131, 19))
        self.radioButton_Aijing.setCheckable(True)
        self.radioButton_Aijing.setChecked(False)
        self.radioButton_Aijing.setObjectName("radioButton_Aijing")
        self.radioButton_Aiyu = QtWidgets.QRadioButton(self.tab_kf)
        self.radioButton_Aiyu.setEnabled(True)
        self.radioButton_Aiyu.setGeometry(QtCore.QRect(570, 10, 121, 19))
        self.radioButton_Aiyu.setCheckable(True)
        self.radioButton_Aiyu.setChecked(False)
        self.radioButton_Aiyu.setObjectName("radioButton_Aiyu")
        self.radioButton_Aixia = QtWidgets.QRadioButton(self.tab_kf)
        self.radioButton_Aixia.setEnabled(True)
        self.radioButton_Aixia.setGeometry(QtCore.QRect(290, 10, 131, 19))
        self.radioButton_Aixia.setCheckable(True)
        self.radioButton_Aixia.setChecked(False)
        self.radioButton_Aixia.setObjectName("radioButton_Aixia")
        self.radioButton_Aiyue = QtWidgets.QRadioButton(self.tab_kf)
        self.radioButton_Aiyue.setGeometry(QtCore.QRect(20, 40, 121, 19))
        self.radioButton_Aiyue.setChecked(False)
        self.radioButton_Aiyue.setObjectName("radioButton_Aiyue")
        self.radioButton_Aina = QtWidgets.QRadioButton(self.tab_kf)
        self.radioButton_Aina.setEnabled(True)
        self.radioButton_Aina.setGeometry(QtCore.QRect(570, 40, 121, 19))
        self.radioButton_Aina.setCheckable(True)
        self.radioButton_Aina.setChecked(False)
        self.radioButton_Aina.setObjectName("radioButton_Aina")
        self.radioButton_Sijing = QtWidgets.QRadioButton(self.tab_kf)
        self.radioButton_Sijing.setGeometry(QtCore.QRect(20, 70, 121, 19))
        self.radioButton_Sijing.setChecked(False)
        self.radioButton_Sijing.setObjectName("radioButton_Sijing")
        self.radioButton_Aimei = QtWidgets.QRadioButton(self.tab_kf)
        self.radioButton_Aimei.setEnabled(True)
        self.radioButton_Aimei.setGeometry(QtCore.QRect(430, 10, 121, 19))
        self.radioButton_Aimei.setCheckable(True)
        self.radioButton_Aimei.setChecked(False)
        self.radioButton_Aimei.setObjectName("radioButton_Aimei")
        self.radioButton_22 = QtWidgets.QRadioButton(self.tab_kf)
        self.radioButton_22.setEnabled(True)
        self.radioButton_22.setGeometry(QtCore.QRect(430, 40, 121, 19))
        self.radioButton_22.setCheckable(True)
        self.radioButton_22.setChecked(False)
        self.radioButton_22.setObjectName("radioButton_22")
        self.radioButton_Siyue = QtWidgets.QRadioButton(self.tab_kf)
        self.radioButton_Siyue.setGeometry(QtCore.QRect(20, 10, 121, 19))
        self.radioButton_Siyue.setChecked(True)
        self.radioButton_Siyue.setObjectName("radioButton_Siyue")
        self.radioButton_Aiya = QtWidgets.QRadioButton(self.tab_kf)
        self.radioButton_Aiya.setEnabled(True)
        self.radioButton_Aiya.setGeometry(QtCore.QRect(150, 10, 131, 19))
        self.radioButton_Aiya.setCheckable(True)
        self.radioButton_Aiya.setChecked(False)
        self.radioButton_Aiya.setObjectName("radioButton_Aiya")
        self.tabWidget.addTab(self.tab_kf, "")
        self.tab_wx = QtWidgets.QWidget()
        self.tab_wx.setObjectName("tab_wx")
        self.radioButton_Aide = QtWidgets.QRadioButton(self.tab_wx)
        self.radioButton_Aide.setEnabled(True)
        self.radioButton_Aide.setGeometry(QtCore.QRect(290, 40, 131, 19))
        self.radioButton_Aide.setCheckable(True)
        self.radioButton_Aide.setChecked(False)
        self.radioButton_Aide.setObjectName("radioButton_Aide")
        self.radioButton_Aixiao = QtWidgets.QRadioButton(self.tab_wx)
        self.radioButton_Aixiao.setEnabled(True)
        self.radioButton_Aixiao.setGeometry(QtCore.QRect(150, 70, 131, 19))
        self.radioButton_Aixiao.setCheckable(True)
        self.radioButton_Aixiao.setChecked(False)
        self.radioButton_Aixiao.setObjectName("radioButton_Aixiao")
        self.radioButton_Aifan = QtWidgets.QRadioButton(self.tab_wx)
        self.radioButton_Aifan.setEnabled(True)
        self.radioButton_Aifan.setGeometry(QtCore.QRect(150, 40, 131, 19))
        self.radioButton_Aifan.setCheckable(True)
        self.radioButton_Aifan.setChecked(False)
        self.radioButton_Aifan.setObjectName("radioButton_Aifan")
        self.radioButton_Aiye = QtWidgets.QRadioButton(self.tab_wx)
        self.radioButton_Aiye.setEnabled(True)
        self.radioButton_Aiye.setGeometry(QtCore.QRect(570, 10, 121, 19))
        self.radioButton_Aiye.setCheckable(True)
        self.radioButton_Aiye.setChecked(False)
        self.radioButton_Aiye.setObjectName("radioButton_Aiye")
        self.radioButton_Aixiang = QtWidgets.QRadioButton(self.tab_wx)
        self.radioButton_Aixiang.setEnabled(True)
        self.radioButton_Aixiang.setGeometry(QtCore.QRect(290, 10, 131, 19))
        self.radioButton_Aixiang.setCheckable(True)
        self.radioButton_Aixiang.setChecked(False)
        self.radioButton_Aixiang.setObjectName("radioButton_Aixiang")
        self.radioButton_Aiting = QtWidgets.QRadioButton(self.tab_wx)
        self.radioButton_Aiting.setGeometry(QtCore.QRect(20, 40, 121, 19))
        self.radioButton_Aiting.setChecked(False)
        self.radioButton_Aiting.setObjectName("radioButton_Aiting")
        self.radioButton_Aihao = QtWidgets.QRadioButton(self.tab_wx)
        self.radioButton_Aihao.setEnabled(True)
        self.radioButton_Aihao.setGeometry(QtCore.QRect(570, 40, 121, 19))
        self.radioButton_Aihao.setCheckable(True)
        self.radioButton_Aihao.setChecked(False)
        self.radioButton_Aihao.setObjectName("radioButton_Aihao")
        self.radioButton_Aiming = QtWidgets.QRadioButton(self.tab_wx)
        self.radioButton_Aiming.setGeometry(QtCore.QRect(20, 70, 121, 19))
        self.radioButton_Aiming.setChecked(False)
        self.radioButton_Aiming.setObjectName("radioButton_Aiming")
        self.radioButton_Aimo_2 = QtWidgets.QRadioButton(self.tab_wx)
        self.radioButton_Aimo_2.setEnabled(True)
        self.radioButton_Aimo_2.setGeometry(QtCore.QRect(430, 10, 121, 19))
        self.radioButton_Aimo_2.setCheckable(True)
        self.radioButton_Aimo_2.setChecked(False)
        self.radioButton_Aimo_2.setObjectName("radioButton_Aimo_2")
        self.radioButton_Ainan = QtWidgets.QRadioButton(self.tab_wx)
        self.radioButton_Ainan.setEnabled(True)
        self.radioButton_Ainan.setGeometry(QtCore.QRect(430, 40, 121, 19))
        self.radioButton_Ainan.setCheckable(True)
        self.radioButton_Ainan.setChecked(False)
        self.radioButton_Ainan.setObjectName("radioButton_Ainan")
        self.radioButton_Aiyuan = QtWidgets.QRadioButton(self.tab_wx)
        self.radioButton_Aiyuan.setGeometry(QtCore.QRect(20, 10, 121, 19))
        self.radioButton_Aiyuan.setChecked(True)
        self.radioButton_Aiyuan.setObjectName("radioButton_Aiyuan")
        self.radioButton_Aiying = QtWidgets.QRadioButton(self.tab_wx)
        self.radioButton_Aiying.setEnabled(True)
        self.radioButton_Aiying.setGeometry(QtCore.QRect(150, 10, 131, 19))
        self.radioButton_Aiying.setCheckable(True)
        self.radioButton_Aiying.setChecked(False)
        self.radioButton_Aiying.setObjectName("radioButton_Aiying")
        self.tabWidget.addTab(self.tab_wx, "")
        self.tab_ts = QtWidgets.QWidget()
        self.tab_ts.setObjectName("tab_ts")
        self.radioButton_Aibao = QtWidgets.QRadioButton(self.tab_ts)
        self.radioButton_Aibao.setEnabled(True)
        self.radioButton_Aibao.setGeometry(QtCore.QRect(570, 10, 121, 19))
        self.radioButton_Aibao.setCheckable(True)
        self.radioButton_Aibao.setChecked(False)
        self.radioButton_Aibao.setObjectName("radioButton_Aibao")
        self.radioButton_Aitong = QtWidgets.QRadioButton(self.tab_ts)
        self.radioButton_Aitong.setEnabled(True)
        self.radioButton_Aitong.setGeometry(QtCore.QRect(290, 10, 131, 19))
        self.radioButton_Aitong.setCheckable(True)
        self.radioButton_Aitong.setChecked(False)
        self.radioButton_Aitong.setObjectName("radioButton_Aitong")
        self.radioButton_Aiwei = QtWidgets.QRadioButton(self.tab_ts)
        self.radioButton_Aiwei.setEnabled(True)
        self.radioButton_Aiwei.setGeometry(QtCore.QRect(430, 10, 121, 19))
        self.radioButton_Aiwei.setCheckable(True)
        self.radioButton_Aiwei.setChecked(False)
        self.radioButton_Aiwei.setObjectName("radioButton_Aiwei")
        self.radioButton_Sitong = QtWidgets.QRadioButton(self.tab_ts)
        self.radioButton_Sitong.setGeometry(QtCore.QRect(20, 10, 121, 19))
        self.radioButton_Sitong.setChecked(True)
        self.radioButton_Sitong.setObjectName("radioButton_Sitong")
        self.radioButton_Xiaobei = QtWidgets.QRadioButton(self.tab_ts)
        self.radioButton_Xiaobei.setEnabled(True)
        self.radioButton_Xiaobei.setGeometry(QtCore.QRect(150, 10, 131, 19))
        self.radioButton_Xiaobei.setCheckable(True)
        self.radioButton_Xiaobei.setChecked(False)
        self.radioButton_Xiaobei.setObjectName("radioButton_Xiaobei")
        self.tabWidget.addTab(self.tab_ts, "")
        self.tab_fy = QtWidgets.QWidget()
        self.tab_fy.setObjectName("tab_fy")
        self.radioButton_Xiaoze = QtWidgets.QRadioButton(self.tab_fy)
        self.radioButton_Xiaoze.setEnabled(True)
        self.radioButton_Xiaoze.setGeometry(QtCore.QRect(20, 40, 191, 19))
        self.radioButton_Xiaoze.setCheckable(True)
        self.radioButton_Xiaoze.setChecked(False)
        self.radioButton_Xiaoze.setObjectName("radioButton_Xiaoze")
        self.radioButton_Qingqing = QtWidgets.QRadioButton(self.tab_fy)
        self.radioButton_Qingqing.setEnabled(True)
        self.radioButton_Qingqing.setGeometry(QtCore.QRect(310, 10, 131, 19))
        self.radioButton_Qingqing.setCheckable(True)
        self.radioButton_Qingqing.setChecked(False)
        self.radioButton_Qingqing.setObjectName("radioButton_Qingqing")
        self.radioButton_Cuijie = QtWidgets.QRadioButton(self.tab_fy)
        self.radioButton_Cuijie.setEnabled(True)
        self.radioButton_Cuijie.setGeometry(QtCore.QRect(200, 40, 151, 19))
        self.radioButton_Cuijie.setCheckable(True)
        self.radioButton_Cuijie.setChecked(False)
        self.radioButton_Cuijie.setObjectName("radioButton_Cuijie")
        self.radioButton_Shanshan = QtWidgets.QRadioButton(self.tab_fy)
        self.radioButton_Shanshan.setGeometry(QtCore.QRect(20, 10, 121, 19))
        self.radioButton_Shanshan.setChecked(True)
        self.radioButton_Shanshan.setObjectName("radioButton_Shanshan")
        self.radioButton_Xiaoyue = QtWidgets.QRadioButton(self.tab_fy)
        self.radioButton_Xiaoyue.setEnabled(True)
        self.radioButton_Xiaoyue.setGeometry(QtCore.QRect(150, 10, 161, 19))
        self.radioButton_Xiaoyue.setCheckable(True)
        self.radioButton_Xiaoyue.setChecked(False)
        self.radioButton_Xiaoyue.setObjectName("radioButton_Xiaoyue")
        self.tabWidget.addTab(self.tab_fy, "")
        self.horizontalSlider_YL = QtWidgets.QSlider(Form)
        self.horizontalSlider_YL.setGeometry(QtCore.QRect(580, 90, 131, 22))
        self.horizontalSlider_YL.setMinimum(1)
        self.horizontalSlider_YL.setMaximum(100)
        self.horizontalSlider_YL.setProperty("value", 50)
        self.horizontalSlider_YL.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_YL.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_YL.setObjectName("horizontalSlider_YL")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(540, 90, 31, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(540, 130, 31, 20))
        self.label_4.setObjectName("label_4")
        self.horizontalSlider_YS = QtWidgets.QSlider(Form)
        self.horizontalSlider_YS.setGeometry(QtCore.QRect(580, 130, 131, 22))
        self.horizontalSlider_YS.setMinimum(-500)
        self.horizontalSlider_YS.setMaximum(500)
        self.horizontalSlider_YS.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_YS.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_YS.setTickInterval(80)
        self.horizontalSlider_YS.setObjectName("horizontalSlider_YS")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(540, 170, 31, 20))
        self.label_5.setObjectName("label_5")
        self.horizontalSlider_YD = QtWidgets.QSlider(Form)
        self.horizontalSlider_YD.setGeometry(QtCore.QRect(580, 170, 131, 22))
        self.horizontalSlider_YD.setMinimum(-500)
        self.horizontalSlider_YD.setMaximum(500)
        self.horizontalSlider_YD.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_YD.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_YD.setTickInterval(80)
        self.horizontalSlider_YD.setObjectName("horizontalSlider_YD")
        self.spinBox_YS = QtWidgets.QSpinBox(Form)
        self.spinBox_YS.setGeometry(QtCore.QRect(720, 130, 51, 22))
        self.spinBox_YS.setMinimum(-500)
        self.spinBox_YS.setMaximum(500)
        self.spinBox_YS.setObjectName("spinBox_YS")
        self.spinBox_YD = QtWidgets.QSpinBox(Form)
        self.spinBox_YD.setGeometry(QtCore.QRect(720, 170, 51, 22))
        self.spinBox_YD.setMinimum(-500)
        self.spinBox_YD.setMaximum(500)
        self.spinBox_YD.setObjectName("spinBox_YD")
        self.clearbut = QtWidgets.QToolButton(Form)
        self.clearbut.setGeometry(QtCore.QRect(490, 200, 30, 30))
        self.clearbut.setStyleSheet("border-image: url(:/newPrefix/清除.png);")
        self.clearbut.setText("")
        self.clearbut.setObjectName("clearbut")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(80, 430, 72, 20))
        self.label_6.setObjectName("label_6")
        self.lineEditPath_name = QtWidgets.QLineEdit(Form)
        self.lineEditPath_name.setGeometry(QtCore.QRect(150, 430, 211, 21))
        self.lineEditPath_name.setObjectName("lineEditPath_name")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(380, 430, 72, 20))
        self.label_7.setObjectName("label_7")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(460, 420, 181, 41))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.radioButton_PCM = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_PCM.setGeometry(QtCore.QRect(120, 10, 61, 19))
        self.radioButton_PCM.setCheckable(True)
        self.radioButton_PCM.setChecked(False)
        self.radioButton_PCM.setObjectName("radioButton_PCM")
        self.radioButton_MP3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_MP3.setGeometry(QtCore.QRect(60, 10, 71, 19))
        self.radioButton_MP3.setChecked(False)
        self.radioButton_MP3.setObjectName("radioButton_MP3")
        self.radioButton_WAV = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_WAV.setGeometry(QtCore.QRect(0, 10, 71, 19))
        self.radioButton_WAV.setChecked(True)
        self.radioButton_WAV.setObjectName("radioButton_WAV")
        self.spinBox_YL = QtWidgets.QSpinBox(Form)
        self.spinBox_YL.setGeometry(QtCore.QRect(720, 90, 51, 22))
        self.spinBox_YL.setMinimum(1)
        self.spinBox_YL.setMaximum(100)
        self.spinBox_YL.setProperty("value", 50)
        self.spinBox_YL.setObjectName("spinBox_YL")
        self.AuditionBut_2 = QtWidgets.QPushButton(Form)
        self.AuditionBut_2.setEnabled(False)
        self.AuditionBut_2.setGeometry(QtCore.QRect(680, 210, 92, 28))
        self.AuditionBut_2.setObjectName("AuditionBut_2")
        self.aboutbut = QtWidgets.QPushButton(Form)
        self.aboutbut.setEnabled(True)
        self.aboutbut.setGeometry(QtCore.QRect(730, 10, 71, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.aboutbut.setFont(font)
        self.aboutbut.setStyleSheet("border-image: url(:/newPrefix/black_about.png);")
        self.aboutbut.setText("")
        self.aboutbut.setShortcut("")
        self.aboutbut.setCheckable(False)
        self.aboutbut.setAutoRepeat(False)
        self.aboutbut.setObjectName("aboutbut")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ai人声语音合成"))
        self.plainTextEdit.setPlainText(_translate("Form", "大家好，我是就喜欢虚拟！这是我制作的一句话Ai语音合成软件，使用的阿里云接口！"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Ai人声语音合成</span></p></body></html>"))
        self.AuditionBut.setToolTip(_translate("Form", "更改配置或更改文本，请重新获取试听！"))
        self.AuditionBut.setText(_translate("Form", "试听"))
        self.SubmitBut.setText(_translate("Form", "提交"))
        self.label_2.setText(_translate("Form", "保存路径："))
        self.browseBut.setText(_translate("Form", "浏览"))
        self.radioButton_Xiaoyun.setText(_translate("Form", "小云 标准女声"))
        self.radioButton_Xiaogang.setText(_translate("Form", "小刚 标准男声"))
        self.radioButton_Ruoxi.setText(_translate("Form", "若兮 温柔女声"))
        self.radioButton_Siqi.setText(_translate("Form", "思琪 温柔女声"))
        self.radioButton_Sijia.setText(_translate("Form", "思佳 标准女声"))
        self.radioButton_Aida.setText(_translate("Form", "艾达 标准男声"))
        self.radioButton_Aijia.setText(_translate("Form", "艾佳 标准女声"))
        self.radioButton_Aicheng.setText(_translate("Form", "艾诚 标准男声"))
        self.radioButton_Sicheng.setText(_translate("Form", "思诚 标准男声"))
        self.radioButton_Aiqi.setText(_translate("Form", "艾琪 温柔女声"))
        self.radioButton_Ninger.setText(_translate("Form", "宁儿 标准女声"))
        self.radioButton_Ruilin.setText(_translate("Form", "瑞琳 标准女声"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ty), _translate("Form", "通用"))
        self.radioButton_Xiaomei.setText(_translate("Form", "小美 甜美女声"))
        self.radioButton_Aijing.setText(_translate("Form", "艾婧 严厉女声"))
        self.radioButton_Aiyu.setText(_translate("Form", "艾雨 自然女声"))
        self.radioButton_Aixia.setText(_translate("Form", "艾夏 亲和女声"))
        self.radioButton_Aiyue.setText(_translate("Form", "艾悦 温柔女声"))
        self.radioButton_Aina.setText(_translate("Form", "伊娜 浙普女声"))
        self.radioButton_Sijing.setText(_translate("Form", "思婧 严厉女声"))
        self.radioButton_Aimei.setText(_translate("Form", "艾美 甜美女声"))
        self.radioButton_22.setText(_translate("Form", "艾娜 浙普女声"))
        self.radioButton_Siyue.setText(_translate("Form", "思悦 温柔女声"))
        self.radioButton_Aiya.setText(_translate("Form", "艾雅 严厉女声"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_kf), _translate("Form", "客服"))
        self.radioButton_Aide.setText(_translate("Form", "艾德 新闻男声"))
        self.radioButton_Aixiao.setText(_translate("Form", "艾笑 资讯女声"))
        self.radioButton_Aifan.setText(_translate("Form", "艾凡 情感女声"))
        self.radioButton_Aiye.setText(_translate("Form", "艾晔 青年男声"))
        self.radioButton_Aixiang.setText(_translate("Form", "艾祥 磁性男声"))
        self.radioButton_Aiting.setText(_translate("Form", "艾婷 电台女声"))
        self.radioButton_Aihao.setText(_translate("Form", "艾浩 资讯男声"))
        self.radioButton_Aiming.setText(_translate("Form", "艾茗 诙谐男声"))
        self.radioButton_Aimo_2.setText(_translate("Form", "艾墨 情感男声"))
        self.radioButton_Ainan.setText(_translate("Form", "艾楠 广告男声"))
        self.radioButton_Aiyuan.setText(_translate("Form", "艾媛 知心姐姐"))
        self.radioButton_Aiying.setText(_translate("Form", "艾颖 软萌童声"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_wx), _translate("Form", "文学"))
        self.radioButton_Aibao.setText(_translate("Form", "艾宝 萝莉女声"))
        self.radioButton_Aitong.setText(_translate("Form", "艾彤 儿童音"))
        self.radioButton_Aiwei.setText(_translate("Form", "艾薇 萝莉女声"))
        self.radioButton_Sitong.setText(_translate("Form", "思彤 儿童音"))
        self.radioButton_Xiaobei.setText(_translate("Form", "小北 萝莉女声"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ts), _translate("Form", "童声"))
        self.radioButton_Xiaoze.setText(_translate("Form", "小泽 湖南重口音男声"))
        self.radioButton_Qingqing.setText(_translate("Form", "青青 台湾话女声"))
        self.radioButton_Cuijie.setText(_translate("Form", "翠姐 东北话女声"))
        self.radioButton_Shanshan.setText(_translate("Form", "姗姗 粤语女声"))
        self.radioButton_Xiaoyue.setText(_translate("Form", "小玥 四川话女声"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fy), _translate("Form", "方言"))
        self.label_3.setText(_translate("Form", "音量"))
        self.label_4.setText(_translate("Form", "语速"))
        self.label_5.setText(_translate("Form", "语调"))
        self.label_6.setText(_translate("Form", "文件名："))
        self.lineEditPath_name.setText(_translate("Form", "试听"))
        self.label_7.setText(_translate("Form", "保存格式："))
        self.radioButton_PCM.setText(_translate("Form", "pcm"))
        self.radioButton_MP3.setText(_translate("Form", "mp3"))
        self.radioButton_WAV.setText(_translate("Form", "wav"))
        self.AuditionBut_2.setToolTip(_translate("Form", "重听上一次配置！"))
        self.AuditionBut_2.setText(_translate("Form", "重复试听"))
import yytubiao_rc