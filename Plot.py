import matplotlib.pyplot as plt
import pandas as pd
import sys


def main(filename,Energy_MCS,OrderParameter_MCS):
    temp = str(pd.read_csv(filename,header=None,nrows=1,skiprows=4).iloc[0])[28:33]
    df = pd.read_csv(filename,header=None,names=["MCS","Ratio","Energy","Order"],skiprows=9,sep="\s+")
    if Energy_MCS == 0 or Energy_MCS == 1:
        fig,ax = plt.subplots()
        ax.plot(df["MCS"],df["Energy"],"r")
        ax.set_title(f"Reduced Temperature, T*= {temp}")
        ax.set_xlabel("MCS")
        ax.set_ylabel("Reduced Energy U/ε")
        if Energy_MCS==1:
            plt.savefig(f"Energy_MCS_{filename}.png")
        plt.show()
    if OrderParameter_MCS == 0 or OrderParameter_MCS == 1:
        fig,ax = plt.subplots()
        ax.plot(df["MCS"],df["Order"],"b")
        ax.set_title(f"Reduced Temperature, T*= {temp}")
        ax.set_xlabel("MCS")
        ax.set_ylabel("Order Parameter, S")
        if Energy_MCS==1:
            plt.savefig(f"OrderParameter_MCS_{filename}.png")
        plt.show()
    return 1

if __name__ == '__main__':
    if int(len(sys.argv)) == 4:
        filename= sys.argv[1]
        Energy_MCS = int(sys.argv[2])
        OrderParameter_MCS = int(sys.argv[3])
        main(filename, Energy_MCS, OrderParameter_MCS)
    else:
        print("Usage: python {} <filename> <Energy_MCS_flag> <OrderParameter_MCS_flag> ".format(sys.argv[0]))