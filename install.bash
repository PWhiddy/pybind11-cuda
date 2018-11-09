git submodule init
git submodule update
cd build
cmake ..
make
export PYTHONPATH=$PWD/build:$PYTHONPATH
cd ..
