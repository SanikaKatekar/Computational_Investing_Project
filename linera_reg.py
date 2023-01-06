
import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
from sklearn import linear_model
import yfinance as yf

def linear_reg():  #fucntion to perform linear regression
    dataset = pd.read_csv('AAPL_FCF.csv')
    #print(dataset)
    dataset = pd.DataFrame(dataset)
    x_feat = dataset.iloc[:,0]  #split dataset into x and y
    y = dataset.iloc[:, 1]
    
    # plt.plot(x_feat, y, color="blue", linewidth=3)


    X_train = x_feat.loc[0:13].values.reshape(-1, 1)
    y_train = y.loc[0:13]
    X_test = x_feat.loc[14:].values.reshape(-1, 1)


    # # Create linear regression object
    regr = linear_model.LinearRegression()
    #
    # # # Train the model using the training sets
    regr.fit(X_train, y_train)
    # #
    # # # Make predictions using the testing set
    y_pred = regr.predict(X_test)



    return y_pred

def linera_reg_IV(FCF_list, growth_r): #find intrinsic value using the predicted cash flows from linear regression model

    FCF_list = pd.DataFrame(FCF_list).T

    # terminal value
    project_p = 15  # projection period
    tv = FCF_list.iloc[0, -1] * project_p
    FCF_list['tv'] = tv
    # print(FCF_list)

    # calculating the discounted cash flow
    term = 0
    t_bond_rate = 3.3

    # implementing the discounted cash flow formula
    for i in range(1, 6):
        term = ((FCF_list.iloc[0, i-1]) / ((1 + (t_bond_rate / 100)) ** i))
        # print(f'term value for {i} year: {term}')
        term = term + term

    tkr = yf.Ticker('AAPL')
    otsd_shr = tkr.info['sharesOutstanding']

    # final dcf = add terminal value
    intrinsic_val = (term / otsd_shr) * 1000000
    # print(f'intrinsic_val:{intrinsic_val}')

    return intrinsic_val

