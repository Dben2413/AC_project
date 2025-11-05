import matplotlib.pyplot as plt
import numpy as np



run_time = [0.540220,2.167920,8.599709,21.874488,26.375643,34.617553]
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