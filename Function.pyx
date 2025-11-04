#cython: boundscheck=False
import numpy as np
from libc.math cimport cos
from cython.parallel cimport prange
cimport openmp


cpdef double one_energy(double[:,:] arr, int ix, int iy, int nmax) nogil:
    cdef double en = 0.0
    cdef int ixp = (ix + 1) % nmax
    cdef int ixm = (ix - 1) % nmax
    cdef int iyp = (iy + 1) % nmax
    cdef int iym = (iy - 1) % nmax
    cdef double ang
    
    ang = arr[ix,iy]-arr[ixp,iy]
    en += 0.5*(1.0-3.0*cos(ang)*cos(ang))
    ang = arr[ix,iy]-arr[ixm,iy]
    en += 0.5*(1.0-3.0*cos(ang)*cos(ang))
    ang = arr[ix,iy]-arr[ix,iyp]
    en += 0.5*(1.0-3.0*cos(ang)*cos(ang))
    ang = arr[ix, iy] - arr[ix, iym]
    en += 0.5*(1.0-3.0*cos(ang)*cos(ang))
    
    return en


cpdef double all_energy(double[:,:] arr, int nmax,int threads):
    cdef double enall = 0.0
    cdef int i, j
    cdef double local_energy
    with nogil:
        for i in prange(nmax, num_threads=threads):
            for j in range(nmax):
                enall += one_energy(arr, i, j, nmax)
    return enall
