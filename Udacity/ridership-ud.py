'''
    Udacity - Data Analysis - ud1101
    Bidimentional Arrays with NumPy
    Developer: Gustavo S.
'''

import numpy as np

# Subway ridership for 5 stations on 10 different days
ridership = np.array([
    [   0,    0,    2,    5,    0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [  95,  229,  255,  496,  201],
    [   2,    0,    1,   27,    0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])

# Change False to True for each block of code to see what it does

# Accessing elements
if False:
    print (ridership[1, 3])
    print (ridership[1:3, 3:5])
    print (ridership[1, :])
    
# Vectorized operations on rows or columns
if False:
    print (ridership[0, :] + ridership[1, :])
    print (ridership[:, 0] + ridership[:, 1])
    
# Vectorized operations on entire arrays
if False:
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    print (a + b)

def mean_riders_for_max_station(ridership):
    '''
    Fill in this function to find the station with the maximum riders on the
    first day, then return the mean riders per day for that station. Also
    return the mean ridership overall for comparsion.
    
    Hint: NumPy's argmax() function might be useful:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html
    '''
    col = ridership.shape[1]
    lin = ridership.shape[0]
    mx1 = ridership[0,:].argmax()

    overall_mean = ridership.mean()
    mean_for_max = ridership[:, mx1].mean()

    print(overall_mean, mean_for_max)
    
    return (overall_mean, mean_for_max)

mean_riders_for_max_station(ridership) #check function

