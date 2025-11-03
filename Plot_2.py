import matplotlib.pyplot as plt
import pandas as pd
import sys


def main(iteration,size,temp_boundary,plotflag):
    Reduced_Temp = []
    Order_parameter = []
    Order_parameter_STD = []
    for i in range(0, temp_boundary*10,1):
        filename = f"LL-Output-MSC={iteration}_size={size}_temp={float(i/10)}.txt"
        try:
            df = pd.read_csv(filename,header=None,names=["MCS","Ratio","Energy","Order"],skiprows=9,sep="\s+")
            temp = str(pd.read_csv(filename,header=None,nrows=1,skiprows=4).iloc[0])[28:33]
            Reduced_Temp.append(temp)
            Order_parameter.append(df["Order"].mean())
            Order_parameter_STD.append(df["Order"].std())
        except FileNotFoundError:
            pass
    print(Reduced_Temp)
    print(Order_parameter)
    print(Order_parameter_STD)
    fig,ax = plt.subplots()
    ax.errorbar(Reduced_Temp,Order_parameter,yerr=Order_parameter_STD, fmt='-o', capsize=5)
    ax.set_title(f"{size}x{size}Lebwohl-Lasher model")
    ax.set_xlabel("Reduced Temperature, T*")
    ax.set_ylabel("Order Parameter, S")
    if plotflag==1:
        plt.savefig(f"OrderParameter_MCS{filename}.png")
    plt.show()
    


if __name__ == '__main__':
    if int(len(sys.argv)) == 5:
        ITERATIONS= int(sys.argv[1])
        SIZE = int(sys.argv[2])
        temp_boundary = int(sys.argv[3])
        PLOTFLAG = int(sys.argv[4])
        main(ITERATIONS, SIZE, temp_boundary,PLOTFLAG)
    else:
        print("Usage: python {} <ITERATIONS> <SIZE> <temp_boundary> <PLOTFLAG> ".format(sys.argv[0]))