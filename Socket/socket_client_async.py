import socket
import time
import threading

def client():
    host = socket.gethostname()  # pour avoir l'adresse du serveur
    port = 10000  # port du serveur

    client_socket = socket.socket()  # initation
    print ("connexion...")

    try:
        client_socket.connect((host, port))  # connexion au serveur
        print ("connecté au serveur")
    except :
        print("Aucune connexion n’a pu être établie car l’ordinateur cible l’a expressément refusée")

    message = ''  # message
    time.sleep(0.2)
    init = 'je suis là'
    client_socket.send(init.encode())

    def msg():
        exec = ''
        while exec != 'stop':
            data = input(" --> ")
            client_socket.send(message.encode())
            time.sleep(0.5)


            if data == 'bye' :
                print("deconnexion du serveur")
                time.sleep(1)
                client_socket.close()  # fermer la connexion
                exec = 'stop'
            if data == 'arret':
                print("redémarrage du serveur")
                time.sleep(1)
                client_socket.close()  # fermer la connexion
                exec = 'stop'


    def msgrcv():
        exec = ''
        while exec != 'stop':
            data = client_socket.recv(1024).decode()


            if data == 'ok, bye !':
                print(' le serveur: ' + data)
                exec = 'stop'
            elif data == 'ok, je redémarre !':
                print(' le serveur: ' + data)
                exec = 'stop'
            else:
                print(' le serveur: ' + data)
                print(' --> ')

    t1 = threading.Thread(target=msg)
    t2 = threading.Thread(target=msgrcv)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__' :
    client()

