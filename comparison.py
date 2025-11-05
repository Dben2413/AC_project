import matplotlib.pyplot as plt
import numpy as np



run_time = [7.70,2.95,1.93,1.52,2.14,2.029609,2.253543]
cores = [2,4,6,8,10,12,14]
fig,ax1 =plt.subplots()
ax1.plot(cores,run_time,marker = ".",label="runtime",color = "red")
ax1.set_xlabel("number of cores")
ax1.set_ylabel("run time(s)")
ax1.legend()
plt.show()


# run_time = [0.189916,0.593003,2.198197,5.016885,8.647348,19.044871,37.389928]
# size = [20,40,80,120,160,240,320]
# fig,ax1 =plt.subplots()
# ax1.plot(size,run_time,marker = ".",label="runtime",color = "blue")
# ax1.set_ylabel("run time(s)")
# ax1.set_xlabel("size of grid")
# ax1.legend()
# plt.show()

# y = np.log(np.array(run_time))
# x = np.log(np.array(size)) 
# fig,ax1 =plt.subplots()
# ax1.plot(x,y,marker = ".",label="log runtime",color = "black")
# ax1.set_ylabel("log(run time(s))")
# ax1.set_xlabel("log(size of grid)")
# ax1.legend()
# plt.show()