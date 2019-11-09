import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from pyowm import OWM

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        btn1 = QPushButton('ye', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn1.clicked.connect(self.onChanged)
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)

        oImage = QImage("./image/weather_bg_pastel1.png")
        sImage = oImage.scaled(QSize(300,200))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        self.lbl = QLabel(self)
        self.lbl.move(60, 140)
        self.font = QtGui.QFont()
        self.font.setPointSize(56)
        self.qle = QLineEdit(self)
        self.qle.move(100, 50)
        self.qle.editingFinished.connect(self.onChanged)
        self.setLayout(vbox)
        self.setWindowTitle('Weather is you')
        self.setGeometry(300, 300, 300, 200)
        self.show()



    def onChanged(self):
        try:
            self.lbl.setText(self.weather(self.qle.text()))
        except:
            self.lbl.setText("No Matching Data Found.")
        self.lbl.adjustSize()



    def weather(self, city):
        owm = OWM(API_key='852402acec6a21be7f4fb7db7ec6df67')
        obs = owm.weather_at_place(city)
        w = obs.get_weather()
        return "{} - {} {} ℃\nMax: {}".format(city,w.get_status(), w.get_temperature(unit="celsius")['temp'], w.get_temperature(unit="celsius")["temp_max"])

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())