
import datetime as dt
from intrinsic_value import get_IV, find_uv_ov
from Sector_analysis import get_sect_choice, all_sect
from linera_reg import linear_reg, linera_reg_IV
from plots import plot_barchart, plot_lr_cal, plot_all_sects


def multiple_st_iv(all_syms, growth_r):  # send in multiple company names and get intrinsic value of them all

    int_vals = []
    curr_p_list = []
    under_valued = []
    count = 0
    print()
    print(f'The following stocks are a part of the sector chosen:')
    print()
    for i in range(0, len(all_syms)):  #loop over all symbols  to get intrinsic value of each
        intrinsic_val = get_IV(all_syms[i], growth_r)
        int_vals.append(intrinsic_val)
        ov_uv_res, curr_p = find_uv_ov(all_syms[i], intrinsic_val) # returns if stock is overvalued or undervalued,
        # also returns the current price

        curr_p_list.append(curr_p) # list of current price of respective stocks
        if ov_uv_res == 1:  #checks is stock is overvalued or undervalued
            count = count + 1
            # print(f'count = {count}')
            print(f'{all_syms[i]} is undervalued')
            print(f'Intrinsic value of {all_syms[i]}: {intrinsic_val}')
            print(f'Current value of {all_syms[i]}: {curr_p}')
            print()
            under_valued.append(all_syms[i])
        elif ov_uv_res == -1:
            print(f'{all_syms[i]} is overvalued')
            print(f'Intrinsic value of {all_syms[i]}: {intrinsic_val}')
            print(f'Current value of {all_syms[i]}: {curr_p}')
            print()
        else:
            print(f'{all_syms[i]} is perfectly valued!')
            print(f'Intrinsic value of {all_syms[i]}: {intrinsic_val}')
            print(f'Current value of {all_syms[i]}: {curr_p}')
            print()
    print(f'The following stocks can form a part of your portfolio: {under_valued}')
    print()
    return int_vals, curr_p_list, count


def lR_AAPL(growth_r):  # linear regression for predicting future free cash flows on AAPL and then calculating
    # Intrinsic value

    FCF_list = linear_reg()
    intrinsic_val_lr = linera_reg_IV(FCF_list, growth_r)
    uv_ov_res, tkr_cuu_p =find_uv_ov('AAPL', intrinsic_val_lr)
    print(
        f'Intrinsic value of AAPL obtained through linear regression model for Cash flow prediction is: {intrinsic_val_lr}')
    if uv_ov_res == 1: #checks if stock is overvalued or undervalued
        print(f'AAPL is undervalued')
        print(f'Current value of AAPL: {tkr_cuu_p}')
        print()
    elif uv_ov_res == -1:
        print(f'AAPL is overvalued')
        print(f'Current value of AAPL: {tkr_cuu_p}')
        print()
    else:
        print(f'AAPL is perfectly valued!')
        print(f'Current value of AAPL: {tkr_cuu_p}')
        print()

    int_vals_AAPL, curr_p_list = our_stock_analysis(['AAPL'], growth_r)
    print(f'int_vals_AAPL:{int_vals_AAPL}')
    print(f'curr_p_list:{curr_p_list}')
    plot_lr_cal(intrinsic_val_lr, int_vals_AAPL, curr_p_list)

    return


def multiple_sector_analysis(
        growth_r):  # function to select multiple sectors of S&P 500 to see the intrinsic value of various stocks in
    # that sector
    print(f'Running an experiment to find the undervalued stocks of all sectors:')
    no_of_sects = input('How many sectors do you want to include in your portfolio:')
    list_allsyms_p = []
    dict_sect = {"Sector": [], "count": []}
    sector_names = []
    sectors_count = []
    for i in range(0, int(no_of_sects)):
        sector_p, sector_name = get_sect_choice()
        sector_names.append(sector_name)
        all_syms_p = all_sect(sector_p)
        list_allsyms_p.append(all_syms_p)
    dict_sect["Sector"] = sector_names
    # print(list_allsyms_p)

    for i in range(0, int(no_of_sects)):
        int_vals, curr_p_list, count = multiple_st_iv(list_allsyms_p[i], growth_r)
        sectors_count.append(count)
    dict_sect["count"] = sectors_count
    # print(dict_sect)
    # plot_all_sects(dict_sect)
    return dict_sect

def our_stock_analysis(all_syms, growth_r): #analysis of stocks chosen by us instead of sector wise

    int_vals_our_stock, curr_p_list, count = multiple_st_iv(all_syms, growth_r)
    plot_barchart(all_syms, int_vals_our_stock, curr_p_list)

    return int_vals_our_stock, curr_p_list

if __name__ == "__main__":
    start_date = dt.datetime(2010, 1, 1)
    end_date = dt.datetime(2010, 12, 31)
    growth_r = 5

    print('There are three parts to this project. Please select the part that you wish to implement.')
    print()
    print('PART 1: Perform sector analysis within a sector. Here you can select one sector and watch the intrinsic values of stocks in that sector.')
    print('PART 2: Perform a comparison of the linear regression intrinsic value and manually calculated intrinsic value of AAPL stock.')
    print('PART 3: Perform sector analysis by selecting multiple sectors.')

    choice = input('Select the part you would like to implement.')
    choice = int(choice)
    if choice == 1:
        # ##PART1
        # #this is to perform sector analysis within a sector
        sector, sector_name = get_sect_choice()
        all_syms = all_sect(sector)
        #if you wish to give your own set of symbols other than choosing a sector uncomment the below line and comment the two lines above
        # all_syms = ['AAPL', 'GOOG', 'AMZN']
        int_vals_our_stock,curr_price = our_stock_analysis(all_syms, growth_r)

    elif choice == 2:
        #PART2
        #Linear Regression analysis of AAPL
        lR_AAPL(growth_r)

    elif choice == 3:
        #PART3
        #multiple sector analysis
        dict_sect = multiple_sector_analysis(growth_r)
        print(f'The following is the dictionary of the sectors you chose and the number of corresponding undervalued '
              f'stocks present in that sector:{dict_sect}')

        plot_all_sects(dict_sect)




