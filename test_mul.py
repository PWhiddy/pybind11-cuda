import gpu_library
import numpy as np
import time

size = 100000000
arr1 = np.linspace(1.0,100.0, size)
arr2 = np.linspace(1.0,100.0, size)

runs = 10
factor = 3.0

t0 = time.time()
for _ in range(runs):
    gpu_library.multiply_with_scalar(arr1, factor)
print("gpu time: " + str(time.time()-t0))
t0 = time.time()
for _ in range(runs):
    arr2 = arr2 * factor
print("cpu time: " + str(time.time()-t0))

print("results match: " + str(np.allclose(arr1,arr2)))
