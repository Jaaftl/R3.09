import multiprocessing
import time

def mult():
    print(f"Task starts for 1 second")
    time.sleep(1)
    print(f"Task ends")

if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=mult)
    p2 = multiprocessing.Process(target=mult)
    p1.start()
    p2.start()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")