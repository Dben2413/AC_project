import matplotlib.pyplot as plt
import numpy as np





run_time_100 = [0.612953,0.709645,0.845497,1.119290,1.327682,1.702676]
run_time_1000 = [0.744468,1.208097,2.885229,5.596925,7.681527,9.987303]
size = [20,40,80,120,140,160]
fig,ax1 =plt.subplots()
ax1.plot(size,run_time_1000,marker = ".",label="runtime",color = "blue")
ax1.set_ylabel("run time(s)")
ax1.set_xlabel("size of grid")
ax1.legend()
plt.show()

y = np.log(np.array(run_time_1000))
x = np.log(np.array(size)) 
fig,ax1 =plt.subplots()
ax1.plot(x,y,marker = ".",label="log runtime",color = "black")
ax1.set_ylabel("log(run time(s))")
ax1.set_xlabel("log(size of grid)")
ax1.legend()
plt.show()