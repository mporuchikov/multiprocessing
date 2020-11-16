import cv2
import os
import numpy as np

data_dir = '../images_in'


# create directory
os.makedirs(data_dir, exist_ok=True)

# create images
n = 100


def draw_poly(img_src):
    n_corners = np.random.randint(3, 6)
    size = img_src.shape[0]
    coords = np.random.randint(0, size, (n_corners,2))
    color = tuple([int(v) for v in (np.random.randint(0, 255, 3, dtype=int))])
    img_dst = cv2.fillPoly(img=img, pts=[coords.reshape(-1,1,2)], color=color)
    return img_dst


for i in range(n):

  # create blank image with random size
  size = np.random.randint(20, 50) * 100
  img = np.zeros((size, size, 3), dtype=np.uint8) + 255

  # draw some polygons
  for j in range(50):
      img = draw_poly(img)
  

  # save image to file
  fname = '{:04}.jpg'.format(i)
  fname_rel = os.path.join(data_dir, fname)
  cv2.imwrite(fname_rel, img)
  
  print(fname)
