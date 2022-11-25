import threading
import time

def msg():
	print("thread start")
	message = input("-->")
	#client_socket.send(message.encode())
	print(message)
	print("thread fin")

start = time.perf_counter()

t1 = threading.Thread(target=msg) # création de la thread
t1.start() # je démarre la thread
t1.join() # j'attends la fin de la thread

end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")