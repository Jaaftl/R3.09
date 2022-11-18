import threading
import time

def task(i):
    print(f"Task {i} starts for {i+1} second(s)")
    time.sleep(i+1)
    print(f"Task {i} ends")
'''start = time.perf_counter()
t1 = threading.Thread(target=task, args=[1])
t1.start()
t1.join() # j'attends la fin de la thread
end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")'''

if __name__ == '__main__':
    T = []
    for i in range(1):
        T.append(threading.Thread(target=task, args=[i]))
    for i in range(len(T)):
        T[i].start()
    for i in range(len(T)):
        T[i].join()