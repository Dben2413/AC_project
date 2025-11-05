import matplotlib.pyplot as plt



run_time = [7.70,2.95,1.93,1.52,2.14,2.029609,2.253543]
cores = [2,4,6,8,10,12,14]
fig,ax1 =plt.subplots()
ax1.plot(cores,run_time,marker = ".",label="runtime",color = "red")
ax1.set_ylabel("number of cores")
ax1.set_xlabel("run time")
ax1.legend()
plt.show()
# plt.savefig("MPI_performance_comparison.pdf", format="pdf", bbox_inches="tight")