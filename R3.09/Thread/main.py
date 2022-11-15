import threading
import time
import concurrent.futures
import requests
import multiprocessing

#threading
def task(i):
    print(f"Task {i} starts for {i+1} second(s)")
    time.sleep(i+1)
    print(f"Task {i} ends")

'''start = time.perf_counter()
t1 = threading.Thread(target=task, args=[1]) # création de la thread
t1.start() # je démarre la thread
t2 = threading.Thread(target=task, args=[2])
t2.start()
t1.join() # j'attends la fin de la thread
t2.join()
end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")


img_urls = [
    'https://cdn.pixabay.com/photo/2019/10/05/19/40/pumpkins-4528653__340.jpg'
]

#Thread
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    with open(img_name+".jpg", 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

#Multiprocessing
def mult():
    print(f"Task starts for 1 second")
    time.sleep(1)
    print(f"Task ends")'''

if __name__ == '__main__':

    #Threading
    T = []
    for i in range(5):
        T.append(threading.Thread(target=task, args=[i]))
    for i in range(len(T)):
        T[i].start()
    for i in range(len(T)):
        T[i].join()

    #Thread
    '''start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)

    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")'''

    #Multiprocessing
    '''start = time.perf_counter()
    p1 = multiprocessing.Process(target=mult)
    p2 = multiprocessing.Process(target=mult)
    p1.start()
    p2.start()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")'''