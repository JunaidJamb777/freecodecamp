import numpy as np
from numpy.core.fromnumeric import std
#function initiat
def calculation(l):
    #matrix 3X3
    matrix=[]
    while l != []:
        matrix.append(l[:3])
        l=l[3:]
    #init variables
    sums=[] 
    means=[]
    variances=[]
    std_dev=[]
    maxs=[]
    mins=[]
    arrays=[]
    #calulations of each mathmatical operation
    for x in matrix:
        arrays=np.array(x)
        sums.append(arrays.sum())
        means.append(arrays.mean())
        variances.append(arrays.var())
        std_dev.append(np.std(x, axis = None))
        maxs.append(np.max(x, axis = None))
        mins.append(np.min(x, axis = None))
#dictionary
    dicts={'mean':means, 'variance':variances, 'standard deviation':std_dev, 'max':maxs, 'min':mins, 'sum':sums}
    return dicts