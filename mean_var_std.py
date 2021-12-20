import numpy as np
from numpy.core.fromnumeric import std
lists=[1,2,3,4,5,6,7,8,9]
#function initiat
def calculation(l):
    #matrix 3X3
    matrix=[]
    while l != []:
        matrix.append(l[:3])
        l=l[3:]
    #init variables
    sums=means=variances=std_dev=maxs=mins=[]
    #calculate values and append into array
    for x in matrix:
        array=np.array(x)
        sums.append(array.sum())
        means.append(np.array(x).mean())
        variances.append(np.array(x).var())
        std_dev.append(np.std(x, axis = None))
        maxs.append(np.max(x, axis = None))
        mins.append(np.min(x, axis = None))
        print(sums)
    #create dictionary and add values to keys
    # print(sums,"\n",means,"\n",variances,"\n",std_dev,"\n",mins,"\n",maxs)
    dicts={'mean':[means], 'variance':[variances], 'standard deviation':[std_dev], 'max':[maxs], 'min':[mins], 'sum':[sums]}
    # return dicts['max']
    

print(calculation(lists))