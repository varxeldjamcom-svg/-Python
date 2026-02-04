import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import time

st.title("時計")

clock_placeholder = st.empty()

while True:
  now_jst = datetime.now(ZoneInfo("Asia/Tokyo"))
  st.write(now_jst.strftime("%Y/%m/%d %H:%M:%S(%Z)))
  time.sleep(1)

