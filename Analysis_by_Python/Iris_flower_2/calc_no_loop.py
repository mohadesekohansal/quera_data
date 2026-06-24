# coding: utf-8
import numpy as np
def calc_no_loop(new_points, points):
    # print(np.square(np.split(new_points,30) - points).shape)
    # print(np.sum(np.square(new_points.reshape(30,1,4)- points),axis=2))
    # np.sqrt(np.sum(np.square(new_points.reshape(m ,1 , 4) - points.reshape(1 , n , 4)), axis=1))
    #  return np.sum(np.square(new_points[:, np.newaxis] - points), axis=2)

    return np.sum(np.square(new_points.reshape(30,1,4)- points),axis=2)
