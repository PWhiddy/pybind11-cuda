import sys
sys.path.append('./build')

import gpu_library
import numpy

vec = numpy.linspace(0,1,10)

print("before: ", vec)
gpu_library.multiply_with_scalar(vec, 10)
print("after: ", vec)
