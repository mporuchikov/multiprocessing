import os
from multiprocessing import Pool
import cv2
from time import time
import numpy as np



def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result



def process(fname):

    img = cv2.imread(fname)
    for i in range(20):
        img = rotate_image(img, 18)

    return img.mean()




if __name__ == '__main__':

    dir_in = '../images_in'
    files = [os.path.join(dir_in, fname) for fname in os.listdir(dir_in)]
    print(files)


    # serial execution
    t = time()
    results = []
    for fname in files:
        results.append(process(fname))
    t = time() - t
    #print(results)
    print(t)        
    

    # parallel execution
    for n_proc in range(1, 9):

        print(n_proc)
    
        t = time()
        pool = Pool(2)
        results = pool.map(process, files)
        pool.close()
        pool.join()
        t = time() - t
        print(t)
        #print(results)
