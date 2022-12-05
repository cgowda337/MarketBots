import discord
import os

import yfinance as yf
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as ts
from matplotlib import pyplot as plt

def generate_corr_plot(fut_list = ['ES=F', 'NQ=F','YM=F','^VIX','ZT=F','ZF=F','ZN=F','ZB=F', 'DX-Y.NYB']):
    datacorr= yf.download(fut_list, start="2022-01-01", end="2022-12-31")['Close']

    df = pd.DataFrame(data=datacorr)
    matrix = np.triu(df.corr())

    fig, ax = plt.subplots(figsize=(6,4))
    sns.heatmap(df.corr(), annot=False, mask=matrix, cmap="YlGnBu")

    plt.savefig("test.png")


bot = discord.Bot()

@bot.event

async def on_ready():
    print(f"We have logged in as {bot.user}")

async def on_message(self, message):
    print(f'Message from {message.author}: {message.content}')

@bot.slash_command()
async def hello(ctx, tickers=[]):
    # filename =  "test.png"

    # plt.savefig("test.png")
    
    generate_corr_plot(fut_list=eval(tickers))
    image = discord.File("test.png")
    await ctx.respond(file=image)

bot.run('x') 
