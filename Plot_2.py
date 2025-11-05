import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import sys


def main(iteration,size,temp_boundary,plotflag):
    Reduced_Temp = []
    Order_parameter = []
    Order_parameter_STD = []
    for i in range(0, temp_boundary*20):
        filename = f"LL-Output-MSC={iteration}_size={size}_temp={i*0.05}.txt"
        
        try:
            df = pd.read_csv(filename,header=None,names=["MCS","Ratio","Energy","Order"],skiprows=9,sep="\s+")
            # print(i*0.05)
            temp = str(pd.read_csv(filename,header=None,nrows=1,skiprows=4).iloc[0])[28:33]
            Reduced_Temp.append(temp)
            Order_parameter.append(df[(df['MCS'] >2000)]["Order"].mean())
            Order_parameter_STD.append(df[(df['MCS'] >2000)]["Order"].std())
        except FileNotFoundError:
            pass
    # print(Reduced_Temp)
    # print(Order_parameter)
    # print(Order_parameter_STD)
    fig,ax = plt.subplots()
    ax.errorbar(Reduced_Temp,Order_parameter,yerr=Order_parameter_STD, fmt='-o', capsize=5)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(len(Reduced_Temp)/8))
    ax.set_title(f"{size}x{size}Lebwohl-Lasher model")
    ax.set_xlabel("Reduced Temperature, T*")
    ax.set_ylabel("Mean Order Parameter, <S>")
    if plotflag==1:
        plt.savefig(f"OrderParameter_Temp_{filename}.png")
    plt.show()
    return 1
    


if __name__ == '__main__':
    if int(len(sys.argv)) == 5:
        ITERATIONS= int(sys.argv[1])
        SIZE = int(sys.argv[2])
        temp_boundary = int(sys.argv[3])
        PLOTFLAG = int(sys.argv[4])
        main(ITERATIONS, SIZE, temp_boundary,PLOTFLAG)
    else:
        print("Usage: python {} <ITERATIONS> <SIZE> <temp_boundary> <PLOTFLAG> ".format(sys.argv[0]))