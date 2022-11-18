from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        self.__temperature = QLabel("Température")
        self.__saisietemp = QLineEdit("")


        self.__convertir = QPushButton("Convertir")
        self.__cb = QComboBox()
        self.__cb.addItems(["°C -> K", "K -> °C"])

        self.__symbol1 = QLabel("°C")
        self.__symbol2 = QLabel("k")

        self.__conversion = QLabel("Conversion")
        self.__resultat = QLabel("")

        self.__buttonhelp = QPushButton("?")

        # Ajouter les composants au grid layout
        grid.addWidget(self.__temperature, 0, 0)
        grid.addWidget(self.__saisietemp, 0, 1)
        grid.addWidget(self.__symbol1, 0, 2)
        grid.addWidget(self.__convertir, 1, 1)
        grid.addWidget(self.__cb, 1, 2)
        grid.addWidget(self.__conversion, 2, 0)
        grid.addWidget(self.__resultat, 2, 1)
        grid.addWidget(self.__symbol2, 2, 2)
        grid.addWidget(self.__buttonhelp, 3, 3)

        self.__cb.activated.connect(self._convert)
        self.__convertir.clicked.connect(self._changervaleur)
        self.__buttonhelp.clicked.connect(self._aide)

        self.setWindowTitle("Une première fenêtre")


    def _convert(self):

        if self.__cb.currentText() == "°C -> K":
            self.__symbol1.setText("°C")
            self.__symbol2.setText("k")
        elif self.__cb.currentText() == "K -> °C":
            self.__symbol1.setText("K")
            self.__symbol2.setText("°C")

    def _changervaleur(self):
        try:
            float(self.__saisietemp.text())
        except:
            erreur = QMessageBox()
            erreur.setWindowTitle("Aide")
            erreur.setText("La valeur n'est pas correct !")
            erreur.resize(250, 500)
            erreur.setIcon(QMessageBox.Critical)

            erreur.exec_()

        else:

            valeur = float(self.__saisietemp.text())
            if self.__cb.currentText() == "°C -> K":
                valeur = valeur + 273.15
                self.__resultat.setText(f"{round(valeur, 2)}")
            elif self.__cb.currentText() == "K -> °C":
                valeur = valeur - 273.15
                self.__resultat.setText(f"{round(valeur, 2)}")

    def _aide(self):
        aide = QMessageBox()
        aide.setWindowTitle("Aide")
        aide.setText("Permet de convertir un nombre soit de Kelvin vers Celcius, soit de Celcius vers Kelvin")
        aide.resize(250,500)
        aide.setIcon(QMessageBox.Information)
        aide.exec_()

