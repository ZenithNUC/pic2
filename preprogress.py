from cv2 import cv2
import numpy as np

def read_preprogress(path):
    # read the picture and transform it to gray,and then return the array data of pic
    img = cv2.imread(path,1)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img_gray

def strdata_progress(preprogressed):
    str_data = []
    img_y_len = len(preprogressed)
    img_x_len = len(preprogressed[0])
    str_y_len = int(img_y_len / 16)
    str_x_len = int(img_x_len / 4)
    str_data = np.zeros((str_y_len,str_x_len))
    for y in range(str_y_len):
        for x in range(str_x_len):
            data_sum = 0
            for pic_y in range(y * 16,y * 16 + 16):
                for pic_x in range(x * 4,x * 4 + 4):
                    data_sum = data_sum + preprogressed[pic_y][pic_x]
            data_ave = int(data_sum / 64)
            str_data[y][x] = data_ave
    return str_data