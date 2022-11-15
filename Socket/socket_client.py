import socket
import time

def client():
    host = socket.gethostname()  # pour avoir l'adresse du serveur
    port = 10000  # port du serveur

    client_socket = socket.socket()  # initation
    print ("connexion...")
    client_socket.connect((host, port))  # connexion au serveur
    print ("connecté au serveur")

    message = ''  # message

    while message != 'bye':
        message = input(" --> ")
        if message == 'bye':
            client_socket.send(message.encode())  # pour envoyer le message
            time.sleep(1)
        else :
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()  # recevoir le reply
            print('Depuis le serveur: ' + data)  # affichage
            if data == 'bye' or data == 'arret':
                message = 'bye'
                time.sleep(1)
    print("deconnexion du serveur")
    client_socket.close()  # fermer la connexion

if __name__ == '__main__' :
    client()

