This package contains extra functionalities for the IBEX optimizer.

Status: experimental.

It generates an executable called `optimizer04` which allows to fully customize the Ibex optimizer (contrary to the generic optimizer `ibexopt` which has a limited number of options).
However, **documentation is missing**. An example of usage is given below.

# Compilation of the package

```
mkdir build
cd build
cmake ..
make
make check
```

This package requires the `ibex-affine` package (mandatory) and the `ibex-ampl` package (optional). If these pacakges are installed in a directory unknown to CMake, you must either indicate the installation path with `CMAKE_PREFIX_PATH` or the exact location of the CMake configuration files using `IBEX_AFFINE_DIR` (or `IBEX_AMPL_DIR`):
Examples:

```
cmake -DCMAKE_PREFIX_PATH=/path-to-ibex-affine ..
```
```
cmake -DIBEX_AFFINE_DIR=/path-to-ibex-affine/share/ibex_affine/cmake ..
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


# Usage

Here is a usage example:

```
optimizer04 */path/to/benchmark-file* acidhc4 compo smearsumrel bfs 1.e-8 1.e-8 100 1
```
