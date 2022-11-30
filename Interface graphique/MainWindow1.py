import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        label1 = QLabel("Saisir votre nom")
        self.__label2 = QLabel("")
        self.__text = QLineEdit("")
        ok = QPushButton("Ok")
        quit = QPushButton("Quitter")
        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.__text, 1, 0)
        grid.addWidget(ok, 0, 1)
        grid.addWidget(quit, 2, 1)
        grid.addWidget(self.__label2, 2, 0)
        ok.clicked.connect(self.actionOk)
        quit.clicked.connect(self.actionQuitter)
        self.setWindowTitle("Une première fenêtre")

    def actionOk(self):
        x = self.__text.text()
        self.__label2.setText('Bonjour ' + x + ' !')

    def actionQuitter(self):
        QCoreApplication.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
