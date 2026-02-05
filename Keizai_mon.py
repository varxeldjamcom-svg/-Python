import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import time

st.title("株価チャート")

ticker = "^N225"
df = yf.Ticker(ticker).history(period="1d",interval="1m")

last_update_time = datetime.now() - timedelta(minutes=1)
clock_placeholder = st.empty()
price_placeholder = st.empty()

#df = yf.Ticker(ticker).history(period="1d",interval="1m")


while True:
  now_jst = datetime.now(ZoneInfo("Asia/Tokyo"))
  clock_placeholder.header(now_jst.strftime("%Y/%m/%d %H:%M:%S(%Z)"))
  if last_update_time.minute != now_jst.minute:
    df =  yf.Ticker(ticker).history(period="1d",interval="1m")
    current_price = df['Close'].iloc[-1]
    previos_price = df['Close'].iloc[-2]
    delta = current_price - previos_price
    price_placeholder.metric(label="日経平均株価", value = f"{current_price:,.2f}", delta = f"{delta:,.2f}")
    last_update_time = now_jst
  time.sleep(1)

