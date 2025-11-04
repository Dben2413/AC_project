#cython: boundscheck=False, OMP_NESTED=TRUE
import numpy as np
cimport numpy as np
from libc.math cimport cos,exp
from libc.stdlib cimport rand, srand, RAND_MAX
from cython.parallel cimport prange
cimport openmp


cpdef double one_energy(double[:,:] arr, int ix, int iy, int nmax) nogil:
    cdef double en = 0.0
    cdef int ixp = (ix+1)%nmax
    cdef int ixm = (ix-1)%nmax
    cdef int iyp = (iy+1)%nmax
    cdef int iym = (iy-1)%nmax
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
    with nogil:
        for i in prange(nmax, num_threads=threads):
            for j in prange(nmax,num_threads=threads):
                enall += one_energy(arr, i, j, nmax)
    return enall


cpdef double MC_step(double[:,:] arr, double Ts,int nmax, int threads):

    cdef double scale = 0.1 + Ts
    cdef int accept = 0
    cdef int i, j, ix, iy
    cdef double ang, en0, en1, boltz

    cdef int[:,:] xran = np.random.randint(0,high=nmax,size=(nmax,nmax))
    cdef int[:,:] yran = np.random.randint(0,high=nmax,size=(nmax,nmax))
    cdef double[:,:] aran = np.random.normal(scale=scale,size=(nmax,nmax))
    cdef double[:,:] bran = np.random.uniform(0.0,1.0,size=(nmax,nmax))

    with nogil:
        for i in prange(nmax,num_threads=threads):
            for j in range(nmax):
                ix = xran[i,j]
                iy = yran[i,j]
                ang = aran[i,j]
                en0 = one_energy(arr,ix,iy,nmax)
                arr[ix,iy] += ang
                en1 = one_energy(arr,ix,iy,nmax)
                if en1<=en0:
                    accept += 1
                else:
                    boltz = exp( -(en1 - en0) / Ts )
                    if boltz >= bran[i,j]:
                        accept += 1
                    else:
                        arr[ix,iy] -= ang
    return accept/(nmax*nmax)

cpdef double get_order(double[:,:] arr,int nmax,int threads):

    cdef int a,b,i,j

    cdef np.ndarray[np.double_t, ndim=2] Qab = np.asarray(np.zeros((3,3)))
    cdef double[:,:] delta = np.eye(3,3)
    cdef double[:,:,:] lab = np.vstack((np.cos(arr),np.sin(arr),np.zeros_like(arr))).reshape(3,nmax,nmax)

    for a in range(3):
        for b in range(3):
            with nogil:
                for i in range(nmax):
                    for j in prange(nmax,num_threads=threads):
                        Qab[a,b] += 3*lab[a,i,j]*lab[b,i,j] - delta[a,b]
    Qab = Qab/(2*nmax*nmax)
    eigenvalues,eigenvectors = np.linalg.eig(Qab)
    return np.max(eigenvalues.real)
