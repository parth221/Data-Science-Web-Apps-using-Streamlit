# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:20:59 2020
@author: parth
"""



import streamlit as st
import yfinance as yf
import pandas as pd
st.write("""
         
# Simple Stock Price App
Shown are the stock closing price and volume of Google!



""")
tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-7-31')
st.write("""
         
Line Chart of Closing

""")
st.line_chart(tickerDf.Close)
st.write("""
         
Line Chart of Volume

""")
st.line_chart(tickerDf.Volume)