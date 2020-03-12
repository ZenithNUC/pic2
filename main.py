# -*- encoding:utf-8 -*-
# author:zenith
# content:A python program which can transform picture to string picture

import preprogress
import transform

if __name__ == "__main__":
    path = "data/test.jpg"
    img = preprogress.read_preprogress(path)
    data = preprogress.strdata_progress(img)
    result = transform.transform_str(data)
    for y in range(len(result)):
        for x in range(len(result[0])):
            print(result[y][x],end='')
        print('\n')