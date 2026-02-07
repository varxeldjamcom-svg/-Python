import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import time

class ticker:
  def __init__(self, symbol, holder, name):
    self.symbol = symbol
    self.holder = holder
    self.name = name

  def update(self):
    
    try:
      df = yf.Ticker(self.symbol).history(period="1d", interval="1m")
    except Exception as e:
      st.warning("更新が中断されました。({e})")

    if not df.empty:
      current_price = df['Close'].iloc[-1]
      previous_price = df['Close'].iloc[-2]
      open_price = df['Open'].iloc[0]
      delta_day = current_price - open_price
      delta = current_price - previous_price
      return current_price, delta_day, delta
    else:
      return -1, -1, -1 

def main():
  st.set_page_config(layout="wide")
  st.title("株価チャート")

  last_update_time = datetime.now() - timedelta(minutes=1)
  clock_placeholder = st.empty()

  col1, col2, col3 = st.columns(3)
  col4, col5, col6 = st.columns(3)
  col7, col8, col9 = st.columns(3)
  col10, col11, col12 = st.columns(3)

  price_holders = [
    [col1, col2, col3],
    [col4, col5, col6],
    [col7, col8, col9],
    [col10, col11, col12]
  ]
  
  


  with col1:
    price_placeholder = st.empty()
  with col2:
    price2_placeholder = st.empty()
  with col3:
    price3_placeholder = st.empty()
  with col4:
    price4_placeholder = st.empty()
  with col5:
    price5_placeholder = st.empty()
  with col6:
    price6_placeholder = st.empty()
  with col7:
    price7_placeholder = st.empty()
  with col8:
    price8_placeholder = st.empty()
  with col9:  
    price9_placeholder = st.empty()
  with col10:
    price10_placeholder = st.empty()
  with col11:
    price11_placeholder = st.empty()
  with col12:
    price12_placeholder = st.empty()
  
  my_tickers = []
  my_tickers.append(ticker("^N225", price_placeholder, "日経平均株価"))
  my_tickers.append(ticker("USDJPY=X", price2_placeholder, "USD/JPY"))
  my_tickers.append(ticker("1343.T", price3_placeholder, "東証REIT指数ETF"))
  my_tickers.append(ticker("JOBY", price7_placeholder, "Joby Aviation"))
  my_tickers.append(ticker("ACHR", price8_placeholder,"Archer Aviation"))
  my_tickers.append(ticker("RACE", price9_placeholder, "Ferrari"))
  my_tickers.append(ticker("NVDA", price10_placeholder, "NVIDIA"))
  my_tickers.append(ticker("AMZN", price11_placeholder, "Amazon"))
  my_tickers.append(ticker("GOOGL", price12_placeholder, "Google"))

  while True:
    now_jst = datetime.now(ZoneInfo("Asia/Tokyo"))
    clock_placeholder.header(now_jst.strftime("%Y/%m/%d %H:%M:%S(%Z)"))
    if last_update_time.minute != now_jst.minute: 
      for tk in my_tickers:
        tkprice, tkdelta_day, tkdelta = tk.update()
        if tkprice > 0:
          tk.holder.metric(label=f"{tk.name} ({tk.symbol})", value=f"{tkprice:,.2f} ({tkdelta_day:+,.2f})", delta= f"{tkdelta:,.2f}")
        else:
          tk.holder.metric(label=f"{tk.name} ({tk.symbol})", value="None",delta="--")
      last_update_time = now_jst
    time.sleep(1)

if __name__ == "__main__":
  main()