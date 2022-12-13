from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt
import sys
import socket
import threading


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setWindowTitle("Un logiciel de tchat")
        self.setCentralWidget(widget)
        self.__layout = QGridLayout()
        widget.setLayout(self.__layout)

        #Socket
        self.__socket = socket.socket()

        #Saisie Serveur
        self.__Server = QLabel('Serveur')
        self.__SaisieServer = QLineEdit('localhost')
        #self.__LineEditServer.setPlaceholderText('Serveur')

        #Saisie Port
        self.__Port = QLabel('Port')
        self.__SaisiePort = QLineEdit('10000')
        #self.__LineEditPort.setPlaceholderText('Port')

        # bouton de connexion
        self.__btnconnexion = QPushButton()
        self.__btnconnexion.setText('Connexion')
        #self.__btnconnexion.clicked.connect(self.__connect)


        #tchat
        self.__TchatBox = QTextEdit()
        self.__TchatBox.setReadOnly(True)
        self.__layout.setRowStretch(4, 0)

        #Saisie message
        self.__Message = QLabel('Message : ')
        self.__SaisieMessage = QLineEdit('')
        self.__SaisieMessage.setEnabled(False)

        #Envoyer message
        self.__Envoyer = QPushButton("Envoyer")
        self.__Envoyer.setEnabled(False)

        #Effacer & Quiter
        self.__Effacer = QPushButton('Effacer')
        self.__Quitter = QPushButton('Quitter')
        #self.__quitbutton.clicked.connect(self.__quitter)

        self.__layout.addWidget(self.__Server, 0, 0)
        self.__layout.addWidget(self.__SaisieServer, 0, 1)
        self.__layout.addWidget(self.__Port, 1, 0)
        self.__layout.addWidget(self.__SaisiePort, 1, 1)
        self.__layout.addWidget(self.__btnconnexion, 3, 0, 1, 2)
        self.__layout.addWidget(self.__TchatBox, 4, 0, 1, 2)
        self.__layout.addWidget(self.__Message, 5, 0)
        self.__layout.addWidget(self.__SaisieMessage, 5, 1)
        self.__layout.addWidget(self.__Envoyer, 6, 0, 1, 2)
        self.__layout.addWidget(self.__Effacer, 8, 0, 1, 2)
        self.__layout.addWidget(self.__Quitter, 9, 0, 1, 2)

        self.__btnconnexion.clicked.connect(self.__connexion)
        self.__Envoyer.clicked.connect(self.__envoyer)
        self.__Effacer.clicked.connect(self.__effacer)
        self.__Quitter.clicked.connect(self.__quitter)
        #self.__quitter.clicked.connect(self.__actionquitter)

        self.__serverSocket = socket.socket()
        self.__force_stop = False
        self.__serverStarted = False
        self.__clients = []

    def __connexion(self):
        if self.__btnconnexion.text() == "Deconnexion":
            self.__btnconnexion.setText('Connexion')
            self.__Envoyer.setEnabled(False)
            self.__SaisieMessage.setEnabled(False)
            self.__socket.close()
        elif self.__btnconnexion.text() == "Connexion":
            self.__btnconnexion.setText('Deconnexion')
            self.__Envoyer.setEnabled(True)
            self.__SaisieMessage.setEnabled(True)
            PORT = self.__SaisiePort.text()
            PORT = int(PORT)
            SERVEUR = self.__SaisieServer.text()
            SERVEUR = str(SERVEUR)
            try:
                self.__socket.connect((SERVEUR, PORT))
            except:
                print("La connexion n'a pas pu être établie..")

    def __envoyer(self):
        self.__thread = threading.Thread(target=self.__reception, args=[self.__socket])
        self.__thread.start()
        x = self.__SaisieMessage.text()
        self.__TchatBox.setAlignment(Qt.AlignRight)
        self.__TchatBox.append(x)
        self.__socket.send(x.encode())
        self.__SaisieMessage.clear()

    def __effacer(self):
        self.__TchatBox.setPlainText("")

    def __quitter(self):
        if self.__btnconnexion.text() == "Connexion":
            self.__TchatBox.append('deco-serveur')
            self.__socket.close()
        else:
            self.__socket.close()

    def __reception(self, conn):

        data = ""
        while data != "deco-server":
            data = str(conn.recv(1024).decode())
            self.__TchatBox.setAlignment(Qt.AlignLeft)
            self.__TchatBox.append(data)

