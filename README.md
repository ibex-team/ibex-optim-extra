This repository contains the plugin Optim extra for the Ibex library.

# Compilation of the plugin

```
mkdir build
cd build
cmake ..
make
make check
```

This plugin requires the plugin Affine. If it was install in a directory unknown
to CMake, you must set the environment variable `IBEX_AFFINE_DIR` to indicate
this directory, before calling
CMake. For example,

```
IBEX_AFFINE_DIR=/my/special/path cmake ..
```

# Installation

```
sudo make install
```

To install to a specific directory, you need to specify it when calling CMake.
For example,
```
  IBEX_AFFINE_DIR=/my/special/path cmake -DCMAKE_INSTALL_PREFIX=/another/path ..
```
