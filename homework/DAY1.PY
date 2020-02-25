import numpy as np
def mean_squared_error(y):
    sum1 = 0
    w = 3
    b = 0.5    
    sum1 = 0
    for i in y:
        x1 = (i + np.random.randn(101) * 5) * w + b
        x2 = i * w + b
        sum1 += np.square(x1-x2)
    MSE = sum1 / len(y)
    return MSE
a = np.linspace(0,100,101)
print(mean_squared_error(a))