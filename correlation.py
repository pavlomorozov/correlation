import numpy as np

def correlation(array1, array2):
    # Original array1
    print("array1:", array1)
    # Original array2
    print("array2:", array2)
    # cross-correlation of the arrays
    print("\nCross-correlation:\n",
          np.correlate(array1, array2))

array1 = np.array([-2, 1, 2, 0])
array2 = np.array([-4, 2, 4, 0])
correlation(array1, array2)

array1 = array1*-1
correlation(array1, array2)

array1 = np.array([7, 4, -3, 3])
correlation(array1, array2)