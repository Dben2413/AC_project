import matplotlib.pyplot as plt
import numpy as np



run_time = [0.561101,2.149186,8.523571,19.188503,26.054648,34.578286]
size = [20,40,80,120,140,160]
fig,ax1 =plt.subplots()
ax1.plot(size,run_time,marker = ".",label="runtime",color = "blue")
ax1.set_ylabel("run time(s)")
ax1.set_xlabel("size of grid")
ax1.legend()
plt.show()

y = np.log(np.array(run_time))
x = np.log(np.array(size)) 
fig,ax1 =plt.subplots()
ax1.plot(x,y,marker = ".",label="log runtime",color = "black")
ax1.set_ylabel("log(run time(s))")
ax1.set_xlabel("log(size of grid)")
ax1.legend()
plt.show()