

def get_sect_choice(): #display and get model choice
    print()
    sect_list = ['Information Technology',
                 'Health Care',
                 'Consumer Discretionary',
                 'Communication Services',
                 'Financials',
                 'Industrials',
                 'Consumer Staples',
                 'Utilities',
                 'Real Estate',
                 'Materials',
                 'Energy']
    for i in range(0,11):
        print(f'Enter {i+1} to choose {sect_list[i]}')

    sector = input(f'Choose the Sector to build your portfolio: ')
    sector_name = sect_list[int(sector)-1]
    return sector, sector_name


def all_sect(sector): #pass the sector list of stocks to the main function
    sect_list = [
        ['AAPL', 'MSFT', 'GOOG', 'HPQ', 'INTC'],  # 'KEYS', 'CTSH', 'CDNS', 'CSCO', 'MSI'],  # inf_tech =
        ['ABT', 'BAX', 'BSX', 'BIIB', 'BIO', 'CI'],  # 'CVS', 'JNJ', 'MRNA', 'PFE'],  # health_c =
        ['AMZN', 'BBWI', 'DPZ', 'F', 'RCL'],  # 'TGT', 'WHR', 'NKE', 'GM', 'GPC'],  # consumer_d =
        ['VZ', 'TMUS', 'T', 'LYV'],  # 'CHTR', 'CMCSA', 'DIS', 'FOX', 'IPG'],  # comm_serv =
        ['AXP', 'GS', 'C', 'MS', 'SCHW'],  # 'GS', 'AXP', 'CB', 'C', 'PGR'],  # fin_sec =
        ['UPS', 'RTX', 'HON', 'DE', 'UNP'],  # 'LMT', 'CAT', 'BA', 'PWR', 'EXPD'],  # ind =
        ['SJM', 'LW', 'TAP', 'WMT', 'PG'],  # 'PEP', 'COST', 'PM', 'MDLZ', 'MO'],  # cons_st =
        ['SRE', 'AEP', 'D', 'NEE', 'DUK'],  # 'SO', 'EXC', 'XEL', 'ED', 'ES'],  # utl =
        ['IRM', 'CPT', 'CBRE'],  # 'IRM', 'UDR', 'CPT', 'BXP', 'VNO'],  # real_est =
        ['LIN', 'ECL', 'ALB', 'PPG', 'LYB'],  # 'CF', 'MOS', 'IP', 'EMN', 'SEE'],  # mat =
        ['XOM', 'EOG', 'PXD', 'VLO', 'XEL'],  # 'OKE', 'CTRA', 'MRO', 'TRGP', 'EQT'],  # energy =
    ]
    for i in range(0, 11):
        if i == (int(sector) - 1):
            return sect_list[i]
    return


