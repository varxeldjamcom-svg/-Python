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

my_tickers = []
my_tickers.append(ticker("^N225", price_placeholder, "日経平均株価"))
my_tickers.append(ticker("USDJPY=X", price4_placeholder, "USD/JPY"))
my_tickers.append(ticker("1343.T", price5_placeholder, "東証REIT指数ETF"))
my_tickers.append(ticker("JOBY", price7_placeholder, "Joby Aviation"))
my_tickers.append(ticker("ACHR", price8_placeholder, "Archer Aviation"))
my_tickers.append(ticker("RACE", price9_placeholder, "Ferrari"))
my_tickers.append(ticker("NVDA", price10_placeholder, "NVIDIA"))
my_tickers.append(ticker())


def update(ticker_symbol):

  df = yf.Ticker(ticker_symbol).history(period="1d", interval="1m")
  current_price = df['Close'].iloc[-1]
  previous_price = df['Close'].iloc[-2]
  open_price = df['Open'].iloc[0]
  delta_day = current_price - open_price
  delta =current_price - previous_price

  return current_price, delta_day, delta

def main():
  st.set_page_config(layout="wide")

  st.title("株価チャート")

  ticker_n255 = "^N225"
  ticker_usd = "USDJPY=X"
  ticker_treit = "1343.T"
  ticker_joby = "JOBY"
  ticker_achr = "ACHR"
  ticker_Fer = "RACE" #フェラーリ
  ticker_nvda = "NVDA" #NVIDI
  ticker_amzn = "AMZN"
  ticker_googl = "GOOGL"

  last_update_time = datetime.now() - timedelta(minutes=1)
  clock_placeholder = st.empty()

  col1, col2 ,col3= st.columns([1.5,1,1])
  with col1:
    price_placeholder = st.empty()
  with col2:
    price2_placeholder = st.empty()
  with col3:
    price3_placeholder = st.empty()

  col4, col5, col6 = st.columns([1.2,1.2,1])
  with col4:
    price4_placeholder = st.empty()
  with col5:
    price5_placeholder = st.empty()
  with col6:
    price6_placeholder = st.empty()

  col7, col8, col9 = st.columns([1.2,1.2,1])
  with col7:
    price7_placeholder = st.empty()
  with col8:
    price8_placeholder = st.empty()
  with col9:  
    price9_placeholder = st.empty()

  col10, col11, col12 = st.columns([1.2,1.2,1])
  with col10:
    price10_placeholder = st.empty()
  with col11:
    price11_placeholder = st.empty()
  with col12:
    price12_placeholder = st.empty()

#df = yf.Ticker(ticker).history(period="1d",interval="1m")
  update_matrix = [
    ["^N225", price_placeholder, "日経平均株価"],
    ["USDJPY=X", price4_placeholder, "USD/JPY"],
    ["1343.T", price5_placeholder, "東証REIT指数ETF"],
    ["JOBY", price7_placeholder, "JOBY"],
    ["ACHR", price8_placeholder, "ACHR"],
    ["RACE", price9_placeholder, "Ferrari"],
    ["NVDA", price10_placeholder, "NVIDIA"],
    ["AMZN", price11_placeholder, "Amazon"],
    ["GOOL", price12_placeholder, "Google"]
  ]

  while True:
    now_jst = datetime.now(ZoneInfo("Asia/Tokyo"))
    clock_placeholder.header(now_jst.strftime("%Y/%m/%d %H:%M:%S(%Z)"))
    
    if last_update_time.minute != now_jst.minute:

      df =  yf.Ticker(ticker_n255).history(period="1d",interval="1m")
      if not df.empty:
        current_price = df['Close'].iloc[-1]
        previous_price = df['Close'].iloc[-2]
        open_price = df['Open'].iloc[0]
        delta_day = current_price - open_price
        delta = current_price - previous_price
        price_placeholder.metric(label="日経平均株価", value = f"{current_price:,.2f} ({delta_day:+,.2f})", delta = f"{delta:,.2f}")
      else:
        price_placeholder.metric(label="日経平均株価", value = "None" ,delta = "--")

      df = yf.Ticker(ticker_usd).history(period="1d",interval="1m")
      if not df.empty:
        current_price = df['Close'].iloc[-1]
        previous_price = df['Close'].iloc[-2]
        open_price = df['Open'].iloc[0]
        delta_day = current_price - open_price
        delta = current_price - previous_price
        price4_placeholder.metric(label="USD/JPY", value = f"{current_price:,.2f} ({delta_day:+,.2f})", delta = f"{delta:,.2f}")
      else:
        price4_placeholder.metric(label="USD/JPY", value = "None", delta ="--")

      df = yf.Ticker(ticker_treit).history(period="1d",interval="1m")
      if not df.empty:
        current_price = df['Close'].iloc[-1]
        previous_price = df['Close'].iloc[-2]
        open_price = df['Open'].iloc[0]
        delta_day = current_price - open_price
        delta = current_price - previous_price
        price5_placeholder.metric(label="東証REIT指数ETF", value = f"{current_price:,.2f} ({delta_day:+,.2f})",delta = f"{delta:,.2f}")
      else:
        price5_placeholder.metric(label="東証REIT指数ETF", value = "None",delta = "--")
    
      df = yf.Ticker(ticker_joby).history(period="1d",interval="1m")
      if not df.empty:
        current_price = df['Close'].iloc[-1]
        previous_price = df['Close'].iloc[-2]
        open_price = df['Open'].iloc[0]
        delta_day = current_price - open_price
        delta = current_price - previous_price
        price6_placeholder.metric(label="JOBY",value = f"{current_price:,.2f} ({delta_day:+,.2f})",delta = f"{delta:,.2f}")
      else:
        price6_placeholder.metric(label="JOBY", value = "None",delta = "--")
    
      df = yf.Ticker(ticker_achr).history(period="1d",interval = "1m")
      if not df.empty:
        current_price = df['Close'].iloc[-1]
        previous_price = df['Close'].iloc[-2]
        open_price = df['Open'].iloc[0]
        delta_day = current_price - open_price
        delta = current_price - previous_price
        price7_placeholder.metric(label="ACHR",value = f"{current_price:,.2f} ({delta_day:+,.2f})",delta = f"{delta:,.2f}")
      else:
        price7_placeholder.metric(label="ACHR",value = "None",delta ="--")

      df = yf.Ticker(ticker_Fer).history(period="1d",interval="1m")
      if not df.empty:
        current_price = df['Close'].iloc[-1]
        previous_price = df['Close'].iloc[-2]
        open_price = df['Open'].iloc[0]
        delta = current_price - previous_price
        price8_placeholder.metric(label="Ferrari",value = f"{current_price:,.2f} ({delta_day:+,.2f})",delta =f"{delta:,.2f}")
      else:
        price8_placeholder.metric(label="Ferrari",value ="None",delta ="--")
    
      df =yf.Ticker(ticker_nvda).history(period="1d",interval="1m")
      if not df.empty:
        current_price = df['Close'].iloc[-1]
        previous_price = df['Close'].iloc[-2]
        open_price = df['Open'].iloc[0]
        delta_day = current_price - open_price
        delta = current_price - previous_price
        price9_placeholder.metric(label="NVIDIA", value=f"{current_price:,.2f} ({delta_day:+,.2f})",delta =f"{delta:,.2f}")
      else:
        price9_placeholder.metric(label="NVIDIA",value="None",delta ="--")

      df =yf.Ticker(ticker_amzn).history(period="1d",interval="1m")
      if not df.empty:
        current_price = df['Close'].iloc[-1]
        previous_price = df['Close'].iloc[-2]
        open_price = df['Open'].iloc[0]
        delta_day = current_price - open_price
        delta = current_price - previous_price
        price10_placeholder.metric(label="Amazon",value=f"{current_price:,.2f} ({delta_day:+,.2f})",delta =f"{delta:,.2f}")
      else:
        price10_placeholder.metric(label="Amazon",value="None",delta="--")


      df=yf.Ticker(ticker_googl).history(period="1d",interval="1m")
      if not df.empty:
        current_price = df['Close'].iloc[-1]
        previous_price = df['Close'].iloc[-2]
        open_price = df['Open'].iloc[0]
        delta_day = current_price - open_price
        delta = current_price - previous_price
        price11_placeholder.metric(label="Google(GOOGL)",value=f"{current_price:,.2f} ({delta_day:+,.2f})",delta=f"{delta:,.2f}")
      else:
        price11_placeholder.metric(label="Google(GOOGL)",value="None",delta="--")
    
      last_update_time = now_jst
    time.sleep(1)

if __name__ == "__main__":
  main()