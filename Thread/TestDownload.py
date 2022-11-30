import time
import concurrent.futures
import requests
import threading
import multiprocessing

img_urls = [
    'https://cdn.pixabay.com/photo/2019/10/05/19/40/pumpkins-4528653__340.jpg'
]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    with open(img_name + ".jpg", 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

if __name__ == '__main__':
    '''start = time.perf_counter()
    for i in range(3):
        t1 = threading.Thread(target=download_image, args=img_urls[i])
        t1.start()
        t1.join()
    end = time.perf_counter()'''




    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(10):
            executor.map(download_image, img_urls)
    end = time.perf_counter()
    print(f"POOL THREAD: Tasks ended in {round(end - start, 2)} second(s)")
    print("")

    T = []
    start = time.perf_counter()
    for i in range(10):
        T.append(threading.Thread(target=download_image(img_urls[0])))
    for i in range(len(T)):
        T[i].start()
    for i in range(len(T)):
        T[i].join()
    end = time.perf_counter()
    print(f"THREADING: Tasks ended in {round(end - start, 2)} second(s)")
    print("")

    start = time.perf_counter()
    for i in range(10):
        p1 = multiprocessing.Process(target=download_image(img_urls[0]))
        p1.start()
    end = time.perf_counter()
    print(f"MULTIPROCESSING: Tasks ended in {round(end - start, 2)} second(s)")