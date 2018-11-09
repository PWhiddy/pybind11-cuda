cmake_minimum_required(VERSION 3.6)
find_package(CUDA REQUIRED)
find_package(PythonInterp 3.6 REQUIRED)
find_package(PythonLibs 3.6 REQUIRED)

include_directories(
    ${PYTHON_INCLUDE_DIRS}
    ./pybind11/include
    )

link_directories(
    /usr/local/cuda/lib64
    )

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

cuda_add_library(gpu_library SHARED
  gpu_library.cu)

target_link_libraries(gpu_library
  ${PYTHON_LIBRARIES}
  cudart)

set_target_properties(gpu_library PROPERTIES PREFIX "")
