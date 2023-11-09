import investpy as inv
import yfinance as yf
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd

def downloader_stocks():
    n_backtesting_years = 1
    br = inv.stocks.get_stocks(country='brazil')
    carteira=[]
    blacklist= ['VSPT3']

    for a in br['symbol']:
        if ((a[(-2):] != '11')&(a not in blacklist)):
            carteira.append(a+'.SA')
            
    dt=yf.download(carteira,  start=(date.today() - relativedelta(years=n_backtesting_years)),end=date.today(), interval='1d')
    #dt=yf.download(carteira,start='2022-01-13',end='2023-01-13')
    dt.sort_index(inplace=True)
    dt=dt.reset_index().sort_values("Date").dropna(axis=1, how='all')
    #dt=pd.read_excel('offline_database.xlsx')

    dt['Date'] = pd.to_datetime(dt['Date'],utc=True).dt.date
    dt.set_index('Date',inplace=True)
    dt = dt.groupby(dt.index).sum()
    print(dt)

    df3=dt.reset_index().sort_values("Date").dropna(axis=1, how='all').set_index("Date").sort_index().copy()
    #df2 = df3.drop(columns=[col for col in df3.columns if (df3[col].isnull().sum()==0)],axis=1).sort_index()
    print(df3.isnull().sum().sort_values())
    return df3