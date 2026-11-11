This package contains extra functionalities for the IBEX optimizer.

# Compilation of the package

```
mkdir build
cd build
cmake ..
make
make check
```

This package requires the ibex-affine package. If it was install in a directory unknown to CMake, you must either indicate the installation path with `CMAKE_PREFIX_PATH` or the exact location of the CMake configuration packages using `IBEX_AFFINE_DIR`:
Examples:

```
cmake -DCMAKE_PREFIX_PATH=/path-to-ibex-affine ...
```
```
cmake -DIBEX_AFFINE_DIR=/path-to-ibex-affine/share/ibex_affine/cmake ...
```



# Installation

```
sudo make install
```

To install to a specific directory, you need to specify it when calling CMake.
For example,
```
  cmake -DCMAKE_INSTALL_PREFIX=/another/path ..
```
