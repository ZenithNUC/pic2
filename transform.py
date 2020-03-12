import numpy as np

def transform_str(preprogressed):
    # transform the array data return from function read_preprogress() to strpic
    x_max = len(preprogressed[0])
    y_max = len(preprogressed)
    strs_list_sort = ["#","8","X","O","H","L","T","I",")","i","=","+",";",":",",","."]
    strs_list = np.full((y_max,x_max),".")
    for x in range(x_max):
        for y in range(y_max):
            num = -int(preprogressed[y][x] / 15.5)
            strs_list[y][x] = strs_list_sort[num]
    return strs_list