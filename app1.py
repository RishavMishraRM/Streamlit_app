import streamlit as st
import yfinance as yf

st.write("""
# Finance app
This is a **finance** app!
""")

tickerSymbol = 'GME'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(
            period='1d',
            start='2019-5-1',
            end='2021-5-1')