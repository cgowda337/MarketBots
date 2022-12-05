
import yfinance as yf
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as ts
from matplotlib import pyplot as plt

# Read and print the stock tickers that make up S&P500
tickers = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
symbol = tickers['Symbol']
symbol.head()

# Get the data for this tickers from yahoo finance
data = yf.download(tickers.Symbol.to_list(),'2022-1-1','2022-12-31')
data.head()
df = pd.DataFrame(data=data)

# create dataframe & remove double values
x=df["Close"].corr()
matrix = np.triu(x)

#convert 'matrix' to dataframe & have input value for correlated ticker 'name'
df2 = pd.DataFrame(data=x)
name = 'TSLA'

# highest corr
y = df2.nlargest(11,[name])
for row in y.index:
    print(row, end= " ")
y[name]

#lowest corr
z = df2.nsmallest(10,[name])
for row in z.index:
    print(row, end= " ")
z[name]