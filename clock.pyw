from ast import Try
import sys 
import time
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap
from PyQt5.QtCore import Qt, QThread, QEventLoop
from threading import Timer
from multiprocessing import Process
import ctypes
myappid = 'mycompany.myproduct.subproduct.version' #
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# class loop(QThread):
#     # 초기화 메서드 구현 
#     def __init__(self, parent): 
#         #parent는 WndowClass에서 전달하는 self이다.(WidnowClass의 인스턴스) 
#         super().__init__(parent) 
#         self.parent = parent 
#         #self.parent를 사용하여 WindowClass 위젯을 제어할 수 있다. 
#     def run(self): 
#         timer = 0
#         is_timer = False
#         while(True):
#             # print('{0} / {1}'.format(self.parent.isLockHide, self.parent.label_lock.isHidden()))
#             if self.parent.isSettingHide and self.parent.isLockHide and not self.parent.label_lock.isHidden():
#                 self.parent.label_lock.setHidden(True)
#             elif not self.parent.isLockHide and self.parent.label_lock.isHidden():
#                 self.parent.label_lock.setHidden(False)
#                 timer = 0
#                 is_timer = True
#             if is_timer:
#                 timer += 1
#                 # print(timer)
#             if self.parent.isSettingHide and timer > 6000000:
#                 self.parent.isLockHide = True
#                 is_timer = False
#                 timer = 0
            
#         #     str = self.parent.text_size.text()
#         #     print(str)
#         #     if str.isdigit():
#         #         txt_size = int(str)
#         #     else:
#         #         txt_size = 10
#         #         self.parent.text_size.setText('10')
#         #     if self.parent.size != txt_size:
#         #         self.parent.size = txt_size
#         #         self.parent.size_x = txt_size*6
#         #         self.parent.size_y = txt_size + int(txt_size / 2)
#         #         self.parent.label_clock.resize(self.parent.size_x, self.parent.size_y)
#         #         # self.parent.label_clock.setGeometry(QtCore.QRect(int(self.parent.size/2), 0, self.parent.size_x, self.parent.size_y)) 
#         #         # self.parent.label_lock.setGeometry(QtCore.QRect(0, 0, int(self.parent.size/2), int(self.parent.size/2))) 
#         #         # self.parent.label_arrow.setGeometry(QtCore.QRect(0, int(self.parent.size/2) + 10, int(self.parent.size/2), int(self.parent.size/2))) 
#         #         # self.parent.text_size.setGeometry(QtCore.QRect(0, 2*int(self.parent.size/2+10), int(self.parent.size/2), int(self.parent.size/4))) 
            
#         # #쓰레드로 동작시킬 함수 내용 구현


class basic_window(QWidget): 
    def __init__(self): 
        super().__init__()
        
        self.size = 100
        self.location_x = 2250
        self.location_y = 1100
        self.size_x = self.size*6
        self.size_y = self.size + int(self.size / 2)
        self.isLockHide = True
        self.isSettingHide = True
        self.m_flag=False
        self.wdays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

        fontDB = QFontDatabase()
        fontDB.addApplicationFont('./res/Blueberry_Pie.ttf')

        self.initUI() 
        
    def initUI(self): 
        centralWidget = QWidget(self)
        self.centralWidget = centralWidget

        # flags = QtCore.Qt.WindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        flags = Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnBottomHint | QtCore.Qt.Tool)
        self.setWindowFlags(flags)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_ShowWithoutActivating, True)

        self.setGeometry(self.location_x , self.location_y ,self.size_x, self.size_y) 
        
        self.label_clock = QLabel(self.centralWidget) 
        self.label_clock.setGeometry(QtCore.QRect(int(self.size/2)+30, 0, self.size_x, self.size_y)) 
        # self.label_clock.mousePressEvent = self.mouseClickEvent
        self.label_clock.setObjectName("label_clock")
        self.label_clock.setText("00:00:00") #텍스트 변환 S
        self.label_clock.setFont(QFont("Blueberry Pie",self.size)) #폰트,크기 조절 
        self.label_clock.setStyleSheet("Color : white") #글자색 변환

        # self.label_lock = QLabel(self.centralWidget) 
        # self.label_lock.setGeometry(QtCore.QRect(0, 0, int(self.size/2), int(self.size/2))) 
        # self.label_lock.mousePressEvent = self.LockClickEvent
        # self.label_lock.setObjectName("label_lock")
        # self.label_lock.setScaledContents(True)
        # self.pm_lock = QPixmap('./res/lock.png')
        # self.pm_unlock = QPixmap('./res/unlock.png')
        # self.label_lock.setPixmap(self.pm_lock)
        # self.label_lock.setHidden(True)

        # self.label_arrow = QLabel(self.centralWidget) 
        # self.label_arrow.setGeometry(QtCore.QRect(0, int(self.size/2) + 10, int(self.size/2), int(self.size/2))) 
        # self.label_arrow.mouseMoveEvent = self.ArrowMoveEvent
        # self.label_arrow.mousePressEvent = self.ArrowPressEvent
        # self.label_arrow.mouseReleaseEvent = self.ArrowReleaseEvent
        # self.label_arrow.setObjectName("label_arrow")
        # self.label_arrow.setScaledContents(True)
        # self.pm_arrow = QPixmap('./res/arrow.png')
        # self.label_arrow.setPixmap(self.pm_arrow)
        # self.label_arrow.setHidden(True)

        self.label_wday = QLabel(self.centralWidget) 
        self.label_wday.setGeometry(QtCore.QRect(0, int(self.size/2), int(self.size/2)+20, int(self.size/2))) 
        self.label_wday.setFont(QFont("Blueberry Pie",int(self.size/4))) #폰트,크기 조절 
        self.label_wday.setText("MON")
        self.label_wday.setStyleSheet("Color : white") #글자색 변환
        
        self.label_date = QLabel(self.centralWidget) 
        self.label_date.setGeometry(QtCore.QRect(0, 2*int(self.size/2), int(self.size/2)+20, int(self.size/2))) 
        self.label_date.setFont(QFont("Blueberry Pie",int(self.size/4))) #폰트,크기 조절 
        self.label_date.setText(" 0 / 0")
        self.label_date.setStyleSheet("Color : white") #글자색 변환

        # self.loop = loop(self)
        # self.loop.start()

        self.showtime() 
        self.show() 
    
    # def mouseClickEvent(self, e):
    #     if e.buttons() & Qt.LeftButton:
    #         self.isLockHide = False
    #     # self.label.setText(text) #텍스트 변환 (mouse_pt)
    

    # def LockClickEvent(self, event):  #event : QMouseEvent
    #     if event.buttons() & Qt.LeftButton:
    #         self.isSettingHide = not self.isSettingHide
    #     if self.isSettingHide:
    #         self.label_lock.setPixmap(self.pm_lock)
    #         self.label_arrow.setHidden(True)
    #         # self.text_size.setHidden(True)
    #     else:
    #         self.label_lock.setPixmap(self.pm_unlock)
    #         self.label_arrow.setHidden(False)
    #         # self.text_size.setHidden(False)

    # def ArrowPressEvent(self, event): 
    #     if event.button()==Qt.LeftButton: 
    #         self.m_flag=True 
    #         self.m_Position=event.globalPos()-self.pos() 
    #         #Get the position of the mouse relative to the window 
    #         event.accept() 
    #         #Change mouse icon 

    # def ArrowMoveEvent(self, e): 
    #     if Qt.LeftButton and self.m_flag: 
    #         self.move(e.globalPos()-self.m_Position)
    #         #Change window position 
    #         e.accept() 

    # def ArrowReleaseEvent(self, e): 
    #     self.m_flag=False 
    #     print(self.pos())
    #     self.location_x = self.pos().x()
    #     self.location_y = self.pos().y()

    
    def showtime(self):
        # 1970년 1월 1일 0시 0분 0초 부터 현재까지 경과시간 (초단위)
        t = time.time()
        # 한국 시간 얻기
        kor = time.localtime(t)
        # LCD 표시
        current_wday = self.wdays[kor.tm_wday]
        current_date = str(kor.tm_mon)+"/"+ str(kor.tm_wday)+" "
        if kor.tm_min < 10:
            current_time = str(kor.tm_hour)+":0"+str(kor.tm_min)
        else:
            current_time = str(kor.tm_hour)+":"+str(kor.tm_min)
        self.label_clock.setText(current_time)
        self.label_date.setText(current_date)
        self.label_wday.setText(current_wday)
    
        # 타이머 설정  (1초마다, 콜백함수)
        timer = Timer(1, self.showtime)
        timer.start()



if __name__ == '__main__':
    try:
        app = QApplication(sys.argv) 
        a = basic_window() 
        app.exec_()
    except Exception:
        import logging
        logging.exception('?')