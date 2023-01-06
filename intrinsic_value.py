import numpy as np
import yfinance as yf


def get_IV(sym, growth_r):  #fucntion to get Intrinsic value of a stock

    ## get ticker information for calculating free cash flows
    tkr = yf.Ticker(sym)
    tkr_cf_info = tkr.cashflow  # setting variable for ticker.cashflow
    #print(tkr_cf_info)

    # getting outstanding shares of the company
    otsd_shr = tkr.info['sharesOutstanding']

    # getting Total Cash From Operating Activities
    #tkr_op_act = (tkr_cf_info.iloc[9, :]) / 1000
    tkr_op_act = (tkr_cf_info.loc['Total Cash From Operating Activities']) / 1000
    #print(f'op_act:{tkr_op_act}')

    # getting capital expenditure
    #tkr_cap_exp = (tkr_cf_info.iloc[17, :]) / 1000
    tkr_cap_exp = (tkr_cf_info.loc['Capital Expenditures']) / 1000
    #print(f'cap_exp:{tkr_cap_exp}')

    # adding total cash from operating activities and capital exp to get free cash flows
    fcf = tkr_op_act + tkr_cap_exp
    df_fcf = fcf.to_frame().T
    #print(df_fcf)  # print 0

    df_fcf['nc'] = np.nan

    # print(df_fcf) #print 1

    # calculate the future cash flow values for upcoming yeras upto 10 years
    it = iter(range(4, 9))
    for i in it:
        if i == 4:
            next(it)
        cf = [df_fcf.iloc[0, i - 1] * (growth_r / 100)] + df_fcf.iloc[0, i - 1]
        # print(f'{i}:{cf}')
        # print(cf)
        df_fcf['FCF' + str(i)] = cf

    # print(df_fcf.iloc[:,5:])  # print 2

    # terminal value
    project_p = 15  # projection period
    tv = df_fcf.iloc[0, -1] * project_p
    df_fcf['tv'] = tv

    # print(df_fcf)  # print 3

    # calculating the discounted cash flow
    term = 0
    t_bond_rate = 3.3

    # implementing the discounted cash flow formula
    for i in range(1, 6):
        term = ((df_fcf.iloc[0, i + 4]) / ((1 + (t_bond_rate / 100)) ** i))
        # print(f'term value for {i} year: {term}')
        term = term + term
    # final dcf = add terminal value
    # print(f'printing type of term{type(term)}')
    # print(f'printing type of ootd: {type(otsd_shr)}')
    # print(f'value of otsd_shr:{otsd_shr}')
    intrinsic_val = (term / int(otsd_shr)) * 1000
    # print(f'intrinsic_val:{intrinsic_val}')

    return intrinsic_val

def find_uv_ov(sym,intrinsic_val): #function to find if stock is undervalued or overvalued

    ## get ticker information for calculating current stock price
    tkr = yf.Ticker(sym)
    tkr_cuu_p = tkr.info['currentPrice']
    #print(tkr_cuu_p)
    if intrinsic_val > tkr_cuu_p:
        return 1, tkr_cuu_p
    elif intrinsic_val< tkr_cuu_p:
        return -1, tkr_cuu_p
    else: return 0, tkr_cuu_p

    return




