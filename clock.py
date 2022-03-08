import sys 
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtGui import QFontDatabase, QFont

class basic_window(QWidget): 
    def __init__(self): 
        super().__init__()

        self.size = 200
        self.location_x = 200
        self.location_y = 100
        self.size_x = self.size*6
        self.size_y = self.size + int(self.size / 2)

        fontDB = QFontDatabase()
        fontDB.addApplicationFont('./res/Blueberry_Pie.ttf')

        self.initUI() 
        
    def initUI(self): 
        centralWidget = QtWidgets.QWidget(self)
        self.centralWidget = centralWidget

        self.setGeometry(self.location_x , self.location_y ,self.size_x, self.size_y) 
        
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.label = QtWidgets.QLabel(self.centralWidget) 
        self.label.setGeometry(QtCore.QRect(int(self.size/2), 0, self.size_x, self.size_y)) 
        self.label.setObjectName("label")
        self.label.setText("00:00:00") #텍스트 변환 
        self.label.setFont(QtGui.QFont("Blueberry Pie",self.size)) #폰트,크기 조절 
        self.label.setStyleSheet("background-color : red;Color : green") #글자색 변환


        self.show() 


if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    basic_window = basic_window() 
    sys.exit(app.exec_())

#   centralWidget = QtWidgets.QWidget(self)
# self.setCentralWidget(centralWidget)

# flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint if self.on_top else QtCore.Qt.FramelessWindowHint)
# self.setWindowFlags(flags)
# self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
# self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

# label = QtWidgets.QLabel(centralWidget)
# movie = QMovie(self.img_path)
# label.setMovie(movie)
# movie.start()
# movie.stop()

# w = int(movie.frameRect().size().width() * self.size)
# h = int(movie.frameRect().size().height() * self.size)
# movie.setScaledSize(QtCore.QSize(w, h))
# movie.start()

# self.setGeometry(self.xy[0], self.xy[1], w, h)
