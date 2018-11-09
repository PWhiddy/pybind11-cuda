git submodule init
git submodule update
cd build
cmake3 ..
make
export PYTHONPATH=$PWD:$PYTHONPATH
cd ..
