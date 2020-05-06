import matplotlib as mpl
import matplotlib.pyplot as plt
import investpy
import pandas as pd
import matplotlib.rcsetup
import matplotlib.font_manager as mfm

# For the font.
font_path = "‪C:\\Users\\BB\\Desktop\\kal.otf"
font_path = font_path.lstrip('\u202a')
prop = mfm.FontProperties(fname=font_path)

# mpl.rcParams['axes.facecolor'] = '#003E43'
# Stock ticks on investing.com
# ls_stocks = ['RELI','HDBK','HDFC','ICBK','INFY','TCS', 'ITC','HLL', 'KTKM', 'LART','AXBK','BRTI', 'ASPN','SBI',
#              'MRTI','NEST','BJFN','SUN','HCLT','TITN','ULTC','PGRD','NTPC','MAHM', 'BAJA','TEML','ONGC','INBK',
#              'HROM','TISC' ]

# Name of the stock
stocks_name = ['Reliance', 'HDFC Bank',' HDFC Housing', 'ICICI Bank', 'Infosys', 'TCS', 'ITC', 'Hindustan Uniliver',
               'Kotak Mahindra' , 'Larsen & Toubro',' Axis Bank','Airtel','Asian Paints', 'State Bank', 'Maruti',
               'Nestle India', ' Bajaj Finance', ' Sunpharma', 'HCL Technologies' , 'Titan', 'Ultratech', 'Power Grid',
               'NTPC', 'Mahinda & Mahindra', 'Bajaj Auto', 'Tech Mahindra', 'ONGC', 'Indusland Bank', 'Hero', 'Tata Steel']
# df = pd.DataFrame()
# Collect the data of each stock and make a dataframe of it.
# for i in range(0,len(ls_stocks)):
#     print(i)
#     df_ = investpy.get_stock_historical_data(stock=ls_stocks[i],
#                                         country='india',
#                                         from_date='30/01/2020',
#                                         to_date='04/06/2020')
#     close = df_['Close']
#
# df[stocks_name[i]] = close
#
# df.to_csv('stocks.csv')

df = pd.read_csv('stocks.csv')
fig, axs = plt.subplots(6, 5, dpi=300)
plt.tight_layout(h_pad=0.25, w_pad=-1.5)
i = 0
fig.set_facecolor('#282C34')
for ax in axs.flat:
    df_company = df[stocks_name[i]]
    # Check if stock has fallen more than 25%
    if df_company[1] < 1.25*df_company.iloc[-1]:
        color_ = '#FF6347'
    elif df_company[1] > df_company.iloc[-1]:
        color_ = '#b30000'
    # If stock is green
    if df_company[1] < df_company.iloc[-1]:
        color_ = '#1aff66'
    ax.set_title(stocks_name[i],fontproperties=prop,fontsize=4.5, pad=1, color='white')
    ax.plot(df[stocks_name[i]],color=color_)
    ax.axis('off')
    i = i +1

plt.savefig('stocks.svg', format='svg', dpi=1200,bbox_inches="tight", facecolor='#282C34')
#plt.show()
