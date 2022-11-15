import time
import concurrent.futures
import requests
import threading

img_urls = [
    'https://cdn.pixabay.com/photo/2019/10/05/19/40/pumpkins-4528653__340.jpg',
    'https://cdn.pixabay.com/photo/2022/10/28/18/53/bird-7553736__340.jpg',
    'https://static.wikia.nocookie.net/minecraft_gamepedia/images/b/b1/Stone_Sword_JE2_BE2.png/revision/latest?cb=20200217235849'

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
        executor.map(download_image, img_urls)
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")