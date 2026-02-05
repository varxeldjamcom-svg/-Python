import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import time

st.title("株価チャート")

ticker_n255 = "^N225"
#df = yf.Ticker(ticker).history(period="1d",interval="1m")

ticker_usd = "USDJPY=X"
#df_usd = yf.Ticker(ticker_usd).history(period="")
ticker_treit = "^TREIT"

ticker_joby = "JOBY"
ticker_achr = "ACHR"
ticker_Fer = "RACE" #フェラーリ
ticker_nvda = "NVDA" #NVIDI
ticker_amzn = "AMZN"
ticker_googl = "GOOGL"


last_update_time = datetime.now() - timedelta(minutes=1)
clock_placeholder = st.empty()

col1, col2 ,col3= st.columns(3)
with col1:
  price_placeholder = st.empty()
with col2:
  price2_placeholder = st.empty()
with col3:
  price3_placeholder = st.empty()

col4, col5, col6 = st.columns(3)
with col4:
  price4_placeholder = st.empty()
with col5:
  price5_placeholder = st.empty()
with col6:
  price6_placeholder = st.empty()

col7, col8, col9 = st.columns(3)
with col7:
  price7_placeholder = st.empty()
with col8:
  price8_placeholder = st.empty()
with col9:
  price9_placeholder = st.empty()


#df = yf.Ticker(ticker).history(period="1d",interval="1m")


while True:
  now_jst = datetime.now(ZoneInfo("Asia/Tokyo"))
  clock_placeholder.header(now_jst.strftime("%Y/%m/%d %H:%M:%S(%Z)"))
  if last_update_time.minute != now_jst.minute:

    df =  yf.Ticker(ticker_n255).history(period="1d",interval="1m")
    if not df.empty:
      current_price = df['Close'].iloc[-1]
      previous_price = df['Close'].iloc[-2]
      delta = current_price - previous_price
      price_placeholder.metric(label="日経平均株価", value = f"{current_price:,.2f}", delta = f"{delta:,.2f}")
 
    df = yf.Ticker(ticker_usd).history(period="1d",interval="1m")
    if not df.empty:
      current_price = df['Close'].iloc[-1]
      previous_price = df['Close'].iloc[-2]
      delta = current_price - previous_price
      price2_placeholder.metric(label="USD/JPY", value = f"{current_price:,.2f}", delta = f"{delta:,.2f}")

    df = yf.Ticker(ticker_treit).history(period="1d",interval="1m")
    if not df.empty:
      current_price = df['Close'].iloc[-1]
      previous_price = df['Close'].iloc[-2]
      delta = current_price - previous_price
      price3_placeholder.metric(label="東証リート指数", value = f"{current_price:,.2f}",delta = f"{delta:,.2f}")
    else:
      price3_placeholder.metric(label="東証リート指数", value = "None",delta = "--")
    
    df = yf.Ticker(ticker_joby).history(period="1d",interval="1m")
    if not df.empty:
      current_price = df['Close'].iloc[-1]
      previous_price = df['Close'].iloc[-2]
      delta = current_price - previous_price
      price4_placeholder.metric(label="JOBY",value = f"{current_price:,.2f}",delta = f"{delta:,.2f}")
    else:
      price4_placeholder.metric(label="JOBY", value = "None",delta = "--")
    
    df = yf.Ticker(ticker_achr).history(period="1d",interval = "1m")
    if not df.empty:
      current_price = df['Close'].iloc[-1]
      previous_price = df['Close'].iloc[-2]
      delta = current_price - previous_price
      price5_placeholder.metric(label="ACHR",value = f"{current_price:,.2f}",delta = f"{delta:,.2f}")
    else:
      price5_placeholder.metric(label="ACHR",value = "None",delta ="--")

    df = yf.Ticker(ticker_Fer).history(period="1d",interval="1m")
    if not df.empty:
      current_price = df['Close'].iloc[-1]
      previous_price = df['Close'].iloc[-2]
      delta = current_price - previous_price
      price6_placeholder.metric(label="Ferrari",value = f"{current_price:,.2f}",delta =f"{delta:,.2f}")
    else:
      price6_placeholder.metric(label="Ferrari",value ="None",delta ="--")
    
    df =yf.Ticker(ticker_nvda).history(period="1d",interval="1m")
    if not df.empty:
      current_price = df['Close'].iloc[-1]
      previous_price = df['Close'].iloc[-2]
      delta = current_price - previous_price
      price7_placeholder.metric(label="NVIDIA", value=f"{current_price:,.2f}",delta =f"{delta:,.2f}")
    else:
      price7_placeholder.metric(label="NVIDIA",value="None",delta ="--")

    df =yf.Ticker(ticker_amzn).history(period="1d",interval="1m")
    if not df.empty:
      current_price = df['Close'].iloc[-1]
      previous_price = df['Close'].iloc[-2]
      delta = current_price - previous_price
      price8_placeholder.metric(label="Amazon",value=f"{current_price:,.2f}",delta =f"{delta:,.2f}")
    else:
      price8_placeholder.metric(label="Amazon",value="None",delta="--")

    df=yf.Ticker(ticker_googl).history(period="1d",interval="1m")
    if not df.empty:
      current_price = df['Close'].iloc[-1]
      previous_price = df['Close'].iloc[-2]
      delta = current_price - previous_price
      price9_placeholder.metric(label="Google(GOOGL)",value=f"{current_price:,.2f}",delta=f"{delta:,.2f}")
    else:
      price9_placeholder.metric(label="Google(GOOGL)",value="None",delta="--")
    
    last_update_time = now_jst
  time.sleep(1)

