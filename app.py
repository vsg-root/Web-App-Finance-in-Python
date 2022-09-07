"""

WEB APP FINANCE IN PYTHON
-------------------------

By: Vinícius da Silva Gomes
Student of Information Systems with Scientific Emphasis (UFRPE)

"""

import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Simple - Stock Price

Stock closing price and volume of Google 

""")

SYMBOL = 'GOOGL'
DATA = yf.Ticker(SYMBOL)

tickerdf = DATA.history(period="1d", start="2010-5-31", end="2020-5-31")

st.write("""
## Closing Price
""")
st.line_chart(tickerdf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerdf.Volume)
