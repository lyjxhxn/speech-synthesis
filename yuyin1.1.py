# -*- coding: utf-8 -*-
import threading
import ali_speech

import sys,os
from ali_speech.callbacks import SpeechSynthesizerCallback
from ali_speech.constant import TTSFormat
from ali_speech.constant import TTSSampleRate
from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia
from PyQt5.QtCore import *

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Ui_yyui import Ui_Form  #导入创建的GUI类
from Ui_about import Ui_Dialog #导入关于作者gui
from AccessToken import get_AccessToken
# from playsound import playsound







class mywindow(QtWidgets.QMainWindow, Ui_Form):
    #__init__:析构函数，也就是类被创建后就会预先加载的项目。
    # 马上运行，这个方法可以用来对你的对象做一些你希望的初始化。
    
    def __init__(self):
        #这里需要重载一下mywindow，同时也包含了QtWidgets.QMainWindow的预加载项。
        super(mywindow, self).__init__()
        
        self.setupUi(self)
        self.yinliang = 50
        self.yusu = 0
        self.yudiao = 0
        # self.geshi = 'wav'
        self.people_name = '小云 标准女声'
        self.lineEditPath.setText(os.getcwd())#设置默认路径
        self.tabindex = 0       
        self.spinBox_YL.valueChanged.connect(self.Valuechange_YL)#绑定槽函数联动
        self.horizontalSlider_YL.valueChanged.connect(self.huakuai_YL)
        self.spinBox_YS.valueChanged.connect(self.Valuechange_YS)#绑定槽函数联动
        self.horizontalSlider_YS.valueChanged.connect(self.huakuai_YS)
        self.spinBox_YD.valueChanged.connect(self.Valuechange_YD)#绑定槽函数联动
        self.horizontalSlider_YD.valueChanged.connect(self.huakuai_YD)
        self.AuditionBut_thread = MyBeautifulThread()#实例化试听
        self.AuditionBut_thread.trigger.connect(self.shiting)#链接多线程下载
        # self.tabWidget.tabBarClicked.connect(self.tabqh)#绑定槽函数联动
        # print(self.tabWidget.activateWindow())
        self.lineEditPath_name.setText('试听')
        self.buttonGroup=QtWidgets.QButtonGroup(self.tabWidget)#实例化radiobut组
        for RadioButton in self.tabWidget.findChildren(QRadioButton):
            self.buttonGroup.addButton(RadioButton)    #向radiobut组内添加按钮
        self.buttonGroup.buttonClicked.connect(self.get_people_name)#绑定buttonGroup按钮
        # self.tabWidget.tabBarClicked.connect(self.tabqiehuan)#切换标签发射信号
        # self.plainTextEdit.setPlaceholderText('哎呀，你要问我喜欢吃什么，我能答上一堆。问我不喜欢的啊，那我还真答不上来。')


    def tabqiehuan(self,index):
        self.tabindex = index

    def on_clearbut_pressed(self):
        '''清除编辑框'''
        self.plainTextEdit.clear()


    def on_aboutbut_pressed(self):
        '''关于作者'''
        # print('关于作者信息')
        author.textBrowser.setOpenExternalLinks(True)#设置超链接可以访问！
        author.show()



    def get_geshi(self):
        '''遍历groupBox获取单选按钮选中状态'''
        geshi = 'wav'
        for RadioButton in self.groupBox.findChildren(QRadioButton):
            if RadioButton.isChecked() == True :
                print(RadioButton.text())
                geshi = RadioButton.text()
        return geshi




    def get_people_name(self):
        '''获取选中人名'''
        for RadioButton in self.tabWidget.findChildren(QRadioButton):
            if RadioButton.isChecked() == True:
                self.people_name = RadioButton.text()
                print(self.people_name)
        
       

    def quit(self):
        app.exit()


    def on_browseBut_pressed(self):
        # print("浏览文件")
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self,"浏览", "%s"%self.lineEditPath.text())
        if download_path != '':   
            self.lineEditPath.setText(download_path)
        else:
            self.lineEditPath.setText(os.getcwd())



    def shiting(self):
        '''试听按钮'''
        self.player = QtMultimedia.QMediaPlayer()
        self.audio_name = os.path.expanduser('~')+'\\Music\\shiting.mp3'
        # try:
        #     os.remove(self.audio_name)#如果有试听这个文件就是删除
        #     print('删除上个文件')
        # except:
        #     pass
        if os.path.exists(self.audio_name):
            os.remove(self.audio_name)#如果有试听这个文件就是删除

        text = self.plainTextEdit.toPlainText()
        if text != '':
           
            mingzi = ren_name.get(self.people_name[:2])
            message = '名字：'+self.people_name+',格式：mp3'+',音量：'+str(self.yinliang)+',语速：'+str(self.yusu)+',语调：'+str(self.yudiao)
            process(client, appkey, token, text, self.audio_name,mingzi,'mp3',self.yinliang,self.yusu,self.yudiao)
            
    
            self.statusBar().showMessage(message+'-------正在试听...')
            url = QtCore.QUrl.fromLocalFile(self.audio_name)
        
            content = QtMultimedia.QMediaContent(url)
        
            self.player.setMedia(content)
            self.player.setVolume(80.0)
            self.player.play()
            self.AuditionBut_2.setEnabled(True)#再次试听可用
        else:
            self.statusBar().showMessage('请输入要合成的文字!')
        self.AuditionBut_thread.quit()
        self.AuditionBut_thread.wait()

    def on_AuditionBut_pressed(self):
        '''试听按钮'''
        self.AuditionBut_thread.start()

    def on_AuditionBut_2_pressed(self):
        '''重复试听'''
        
        # audio_name = self.audio_name
        # url = QtCore.QUrl.fromLocalFile(self.audio_name)
        
        # content = QtMultimedia.QMediaContent(url)
        
        # self.player.setMedia(content)
        # self.player.setVolume(80.0)
        self.player.play()
        





    def on_SubmitBut_pressed(self):
        '''提交按钮'''
                # print(self.plainTextEdit.toPlainText())#获取文本
        text = self.plainTextEdit.toPlainText()
        filename = self.lineEditPath_name.text()
        path = self.lineEditPath.text()
        geshi = self.get_geshi()
        audio_name = path + '\\'+filename + '.'+geshi
        # print(audio_name)
        # people_name = self.get_people_name()
        mingzi = ren_name.get(self.people_name[:2])
        message = '名字：'+self.people_name+',格式：'+geshi+',音量：'+str(self.yinliang)+',语速：'+str(self.yusu)+',语调：'+str(self.yudiao)
        process(client, appkey, token, text, audio_name,mingzi,geshi,self.yinliang,self.yusu,self.yudiao)
        self.statusBar().showMessage(message+'----恭喜----下载成功！')

    def Valuechange_YL(self):
        self.yinliang = self.spinBox_YL.value()
        self.horizontalSlider_YL.setValue(self.spinBox_YL.value())#设置滑块数值


    def Valuechange_YS(self):
        self.yusu = self.spinBox_YS.value()
        self.horizontalSlider_YS.setValue(self.spinBox_YS.value())#设置滑块数值
        # self.statusBar().showMessage(str(self.spinBox_YL.value()))
    def Valuechange_YD(self):
        self.yudiao = self.spinBox_YD.value()
        self.horizontalSlider_YD.setValue(self.spinBox_YD.value())#设置滑块数值
        # self.statusBar().showMessage(str(self.spinBox_YL.value()))

    def huakuai_YL(self):
        self.yinliang = self.horizontalSlider_YL.value()
        self.spinBox_YL.setValue(self.horizontalSlider_YL.value())#设置数值滑块
        # self.statusBar().showMessage(str(self.horizontalSlider_YL.value()))
    def huakuai_YS(self):
        self.yusu = self.horizontalSlider_YS.value()
        self.spinBox_YS.setValue(self.horizontalSlider_YS.value())#设置数值滑块
        # self.statusBar().showMessage(str(self.horizontalSlider_YL.value()))
    def huakuai_YD(self):
        self.yudiao = self.horizontalSlider_YD.value()
        self.spinBox_YD.setValue(self.horizontalSlider_YD.value())#设置数值滑块
        # self.statusBar().showMessage(str(self.horizontalSlider_YL.value()))
       
class MyBeautifulThread(QtCore.QThread):
    '''多线程'''
    trigger = QtCore.pyqtSignal()
 
    def __init__(self):
        super(MyBeautifulThread, self).__init__()

    def run(self):
        self.trigger.emit()

class Ui_Author(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(Ui_Author,self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height()) #禁止窗口大小化

class MyCallback(SpeechSynthesizerCallback):
    # 参数name用于指定保存音频的文件。
    def __init__(self, name):
        self._name = name
        self._fout = open(name, 'wb')
    def on_binary_data_received(self, raw):
        print('MyCallback.on_binary_data_received: %s' % len(raw))
        self._fout.write(raw)
    def on_completed(self, message):
        print('MyCallback.OnRecognitionCompleted: %s' % message)
        self._fout.close()
    def on_task_failed(self, message):
        print('MyCallback.OnRecognitionTaskFailed-task_id:%s, status_text:%s' % (
            message['header']['task_id'], message['header']['status_text']))
        self._fout.close()
    def on_channel_closed(self):
        print('MyCallback.OnRecognitionChannelClosed')
def process(client, appkey, token, text, audio_name,mingzi,geshi,yinliang,yusu,yudiao):
    callback = MyCallback(audio_name)
    synthesizer = client.create_synthesizer(callback)
    synthesizer.set_appkey(appkey)
    synthesizer.set_token(token)
    synthesizer.set_voice(mingzi)
    synthesizer.set_text(text)
    if geshi == 'wav':
        synthesizer.set_format(TTSFormat.WAV)
    elif geshi == 'mp3':
        synthesizer.set_format(TTSFormat.MP3)
    else:
        synthesizer.set_format(TTSFormat.PCM)
    synthesizer.set_sample_rate(TTSSampleRate.SAMPLE_RATE_16K)
    synthesizer.set_volume(yinliang)#音量
    synthesizer.set_speech_rate(yusu)#语速
    synthesizer.set_pitch_rate(yudiao)#语调
    try:
        ret = synthesizer.start()
        if ret < 0:
            return ret
        synthesizer.wait_completed()
    except Exception as e:
        print(e)
    finally:
        synthesizer.close()
    
def process_multithread(client, appkey, token, number):
    thread_list = []
    for i in range(0, number):
        text = "这是线程" + str(i) + "的合成。"
        audio_name = "sy_audio_" + str(i) + ".wav"
        thread = threading.Thread(target=process, args=(client, appkey, token, text, audio_name))
        thread_list.append(thread)
        thread.start()
    for thread in thread_list:
        thread.join()

people_list = []

ren_name = {'小云': 'Xiaoyun', '小刚': 'Xiaogang', '若兮': 'Ruoxi', '思琪': 'Siqi', '思佳': 'Sijia', '思诚': 'Sicheng', '艾琪': 'Aiqi', '艾佳': 'Aijia', '艾诚': 'Aicheng', '艾达': 'Aida', '宁儿': 'Ninger', '瑞琳': 'Ruilin', '思悦': 'Siyue', '艾雅': 'Aiya', '艾夏': 'Aixia', '艾美': 'Aimei', '艾雨': 'Aiyu', '艾悦': 'Aiyue', '艾婧': 'Aijing', '小美': 'Xiaomei', '艾娜': 'Aina', '伊娜': 'Yina', '思婧': 'Sijing', '思彤': 'Sitong', '小北': 'Xiaobei', '艾彤': 'Aitong', '艾薇': 'Aiwei', '艾宝': 'Aibao', 'Harry': 
'Harry', 'Abby': 'Abby', 'Andy': 'Andy', 'Eric': 'Eric', 'Emily': 'Emily', 'Luna': 'Luna', 'Luca': 'Luca', 'Wendy': 'Wendy', 'William': 'William', 'Olivia': 'Olivia', '姗姗': 'Shanshan', '艾媛': 'Aiyuan', '艾颖': 'Aiying', '艾祥': 'Aixiang', '艾墨': 'Aimo', '艾晔': 'Aiye', '艾婷': 'Aiting', '艾凡': 'Aifan', 'Lydia': 'Lydia', '小玥': 'Xiaoyue', '艾硕': 'Aishuo', '艾德': 'Aide', '青青': 'Qingqing', '翠姐': 'Cuijie', '小泽': 'Xiaoze', '艾楠': 'Ainan', '艾浩': 'Aihao', '艾茗': 'Aiming', '艾笑': 'Aixiao', '艾厨': 'Aichu', '艾倩': 'Aiqian', '智香': 'Tomoka', '智也': 'Tomoya', 'Annie': 'Annie'}

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #生成 mywindow 类的实例。
    window = mywindow()
    #有了实例，就得让它显示，show()是QWidget的方法，用于显示窗口。 
    window.setFixedSize(window.width(), window.height()) #禁止窗口大小化
    author = Ui_Author()
    
    window.show()
    client = ali_speech.NlsClient()
    get_AccessToken
    # 设置输出日志信息的级别：DEBUG、INFO、WARNING、ERROR。
    client.set_log_level('INFO')
    appkey = '<您的Appkey>' #获取链接：https://nls-portal.console.aliyun.com/applist
    try:
        token = get_AccessToken()
        window.statusBar().showMessage('服务器连接成功！')
    except:
        QMessageBox.critical(window,"错误","服务器连接失败，请连接网络！",QMessageBox.Yes,QMessageBox.Yes)
        window.quit()
    # token = ''
    # audio_name = 'sy_audio99.wav'
    # process(client, appkey, token, text, audio_name)

    # 多线程示例
    # process_multithread(client, appkey, token, 2)





    
    # window.get_people_name()获取人名
    
    # 调用sys库的exit退出方法，条件是app.exec_()，也就是整个窗口关闭。
    # 有时候退出程序后，sys.exit(app.exec_())会报错，改用app.exec_()就没事
    # https://stackoverflow.com/questions/25719524/difference-between-sys-exitapp-exec-and-app-exec
    sys.exit(app.exec_())
    