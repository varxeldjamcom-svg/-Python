import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import time

#定数として使用
ROWS = 3
COLS = 3

class ticker:
  def __init__(self, symbol, name, holder):
    self.symbol = symbol
    self.name = name
    self.holder = holder
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
  placeholders = []
  for i in range(ROWS):
    cols = st.columns(COLS)
    row_list = []
    for col in cols:
      with col:
        row_list.append(st.empty())
    placeholders.append(row_list)
  
  my_tickers = []
  my_tickers.append(ticker("^N225", "日経平均株価", placeholders[0][0]))
  my_tickers.append(ticker("USDJPY=X", "USD/JPY", placeholders[0][1]))
  my_tickers.append(ticker("1343.T", "東証REIT指数ETF", placeholders[0][2]))
  my_tickers.append(ticker("JOBY", "Joby Aviation", placeholders[1][0]))
  my_tickers.append(ticker("ACHR", "Archer Aviation", placeholders[1][1]))
  my_tickers.append(ticker("RACE", "Ferrari", placeholders[1][2]))
  my_tickers.append(ticker("NVDA", "NVIDIA", placeholders[2][0]))
  my_tickers.append(ticker("AMZN", "Amazon", placeholders[2][1]))
  my_tickers.append(ticker("GOOGL", "Google", placeholders[2][2]))

  while True:
    now_jst = datetime.now(ZoneInfo("Asia/Tokyo"))
    clock_placeholder.header(now_jst.strftime("%Y/%m/%d %H:%M:%S(%Z)"))
    if last_update_time.minute != now_jst.minute: 
      for tk in my_tickers:
        tkprice, tkdelta_day, tkdelta = tk.update()
        if 0 < tkprice:
          tk.holder.metric(label=f"{tk.name} ({tk.symbol})", value=f"{tkprice:,.2f} ({tkdelta_day:+,.2f})", delta= f"{tkdelta:,.2f}")
        else:
          tk.holder.metric(label=f"{tk.name} ({tk.symbol})", value="None",delta="--")
      last_update_time = now_jst
    time.sleep(1)

if __name__ == "__main__":
  main()