import sys
from PyQt5.QtWidgets import *
import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow.MainWindow()
    window.show()

    app.exec()