import matplotlib
import numpy as np
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def plot_barchart(all_syms, int_vals, curr_p_list):  #function to plot a barchart showing intrinsic values and current price of each stock
    X_axis = np.arange(len(all_syms))

    plt.bar(X_axis - 0.2, int_vals, 0.4, label='Intrinsic value', color = 'darkcyan')
    plt.bar(X_axis + 0.2, curr_p_list, 0.4, label='Current Price', color = 'orange')

    plt.xticks(X_axis, all_syms)
    plt.xlabel("Symbols")
    plt.ylabel("Value")
    plt.title("Intrinsic Value and Current Price")
    plt.legend()
    plt.show()

    return

def plot_lr_cal(intrinsic_val_lr, int_vals_AAPL, current_p): # function to plot linear regression intrinsic value vs. calculated
    # intrinsic value
    X_axis = ['Linear Reg IV', 'Calculated IV','Current Price']
    y_axis = [intrinsic_val_lr,int_vals_AAPL,current_p ]
    plt.bar(X_axis , y_axis, color = ['olive', 'lightseagreen', 'orange'], width = 0.2)

    plt.xticks(np.arange(3), X_axis)
    plt.xlabel("Two methods")
    plt.ylabel("Value")
    plt.title("Linear regression Intrinsic value vs Calculated Intrinsic Value")
    plt.legend()
    plt.show()

    return

def plot_all_sects(dict_sect):  #function to plot a line chart of multiple sector analysis
    #key = list(dict_sect.keys())
    values = list(dict_sect.values())
    print(values[0])
    print(values[1])
    # ax = plt.plot()
    fig, ax = plt.subplots()
    ax.plot(values[0], values[1], linestyle='-.', color='darkblue', marker='o')
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right', fontsize='x-small')
    ax.set_xlabel("Sectors")
    ax.set_ylabel("No. of stocks undervalued")
    ax.set_title("Undervalued stocks in different sectors")
    # plt.xlabel("Sectors")
    # plt.ylabel("No. of stocks undervalued")
    # plt.title("Undervalued stocks in different sectors")
    plt.show()
    return