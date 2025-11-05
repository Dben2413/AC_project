import matplotlib.pyplot as plt
import numpy as np



# run_time = [7.70,2.95,1.93,1.52,2.14,2.029609,2.253543]
# cores = [2,4,6,8,10,12,14]
# fig,ax1 =plt.subplots()
# ax1.plot(cores,run_time,marker = ".",label="runtime",color = "red")
# ax1.set_xlabel("number of cores")
# ax1.set_ylabel("run time(s)")
# ax1.legend()
# plt.show()


# run_time_serial = [0.788910,3.089844,12.251605,27.195740,36.972238,48.093857]
# run_time_mpi4py = [0.189916,0.593003,2.198197,5.016885,6.680077,8.647348]
run_time_numba = [0.612953,0.709645,0.845497,1.119290,1.327682,1.702676]
run_time_cython = [0.016996,0.047707,0.175356,0.374829,0.542549,0.703961]
# run_time_numpy = [0.561101,2.149186,8.523571,19.188503,26.054648,34.578286]
size = [20,40,80,120,140,160]
fig,ax1 =plt.subplots()
# ax1.plot(size,run_time_serial,marker = ".",label="serial",color = "blue")
# ax1.plot(size,run_time_mpi4py,marker = ".",label="mpi4py",color = "black")
ax1.plot(size,run_time_numba,marker = ".",label="numba",color = "orange")
ax1.plot(size,run_time_cython,marker = ".",label="cython",color = "red")
# ax1.plot(size,run_time_numpy,marker = ".",label="numpy",color = "green")
ax1.set_ylabel("run time(s)")
ax1.set_xlabel("size of grid")
ax1.legend()
plt.show()

# y_serial = np.log(np.array(run_time_serial))
# y_mpi4py = np.log(np.array(run_time_mpi4py))
# y_numba = np.log(np.array(run_time_numba))
# y_cython = np.log(np.array(run_time_cython))
# y_numpy = np.log(np.array(run_time_numpy))
# x = np.log(np.array(size)) 
# fig,ax1 =plt.subplots()
# ax1.plot(x,y_serial,marker = ".",label="serial",color = "blue")
# ax1.plot(x,y_mpi4py,marker = ".",label="mpi4py",color = "black")
# ax1.plot(x,y_numba,marker = ".",label="numba",color = "orange")
# ax1.plot(x,y_cython,marker = ".",label="cython",color = "red")
# ax1.plot(x,y_numpy,marker = ".",label="numpy",color = "green")
# ax1.set_ylabel("log(run time(s))")
# ax1.set_xlabel("log(size of grid)")
# ax1.legend()
# plt.show()