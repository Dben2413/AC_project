from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

ext_modules = [
    Extension(
        "Function",
        ["Function.pyx"],
        extra_compile_args=['/openmp','-v'],
#        extra_link_args=['-fopenmp'],
        include_dirs=[numpy.get_include()],
        extra_link_args=['-lgomp', '-Wl,-rpath,/usr/local/opt/gcc/lib/gcc/13/'],
    )
]

setup(name="Function",
      ext_modules=cythonize(ext_modules))

