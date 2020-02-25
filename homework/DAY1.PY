import numpy as np
def mean_squared_error(y):
    sum1 = 0
    for i in y:
        sum1 += i
    yp = sum1/len(y)
    sum1 = 0
    for i in y:
        sum1 += np.square(i-yp)
    MSE = sum1 / len(y)
    return MSE
a = [20,50,77,62,30,88]
print(mean_squared_error(a))