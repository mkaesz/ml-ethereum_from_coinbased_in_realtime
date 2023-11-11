import pandas as pd
import streamlit as st
from datetime import timedelta

from bokeh.plotting import figure

from src.helpers.config import WINDOW_SECONDS
from src.helpers.logger import get_console_logger

logger = get_console_logger()

st.set_page_config(layout="wide")
st.title(f"ETH/USD OHLC data every {WINDOW_SECONDS} seconds")

# here we store the data our Stream processing outputs
df = pd.DataFrame()

placeholder = st.empty()

import pandas as pd
def load_ohlc_data_from_feature_store() -> pd.DataFrame:
    """"""
    from src.helpers.feature_store_api import get_or_create_feature_view
    feature_view = get_or_create_feature_view()

    # get current epoch in seconds
    from time import time
    current_epoch_sec = int(time())

    # read time-series data from the feature store
    fetch_data_to = current_epoch_sec
    fetch_data_from = current_epoch_sec - 24*60*60

    logger.info(f'Fetching data from {fetch_data_from} to {fetch_data_to}')
    
    from datetime import datetime
    fetch_data_to = int(pd.to_datetime(datetime.utcnow()).timestamp())
    fetch_data_from = fetch_data_to - 1*60*60 # 1 hour
    
    ohlc_data = feature_view.get_feature_vectors(
        entry = [{"time": t} for t in range(fetch_data_from, fetch_data_to)]
    )

    columns = ['upper_band', 'mid_band', 'lower_band', 'time', 'open', 'high', 'low', 'close', 'volume', 'product_id']
    # list of lists to Pandas DataFrame
    ohlc_data = pd.DataFrame(ohlc_data, columns=columns)
    #ohlc_data.columns = ['upper_band', 'mid_band', 'lower_band', 'time', 'open', 'high', 'low', 'close', 'volume', 'product_id']
    ohlc_data.sort_values(by=['time'], inplace=True)

    return ohlc_data

while True:

    df = load_ohlc_data_from_feature_store()
    df = df.fillna('')
    with placeholder.container():
        #p = get_candlestick_plot(df, WINDOW_SECONDS)
        df["date"] = pd.to_datetime(df["time"], unit="s")

        inc = df.close > df.open
        dec = df.open > df.close
        w = 1000 * WINDOW_SECONDS / 2 # band width in ms

        TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

        x_max = df['date'].max() + timedelta(minutes=2)
        x_min = df['date'].max() - timedelta(minutes=4)
        p = figure(x_axis_type="datetime", tools=TOOLS, width=1000,
                   title = "ETH/USD", x_range=(x_min, x_max))
        p.grid.grid_line_alpha=0.3

        p.segment(df.date, df.high, df.date, df.low, color="black")
        p.vbar(df.date[inc], w, df.open[inc], df.close[inc], fill_color="#70bd40", line_color="black")
        p.vbar(df.date[dec], w, df.open[dec], df.close[dec], fill_color="#F2583E", line_color="black")
        st.bokeh_chart(p, use_container_width=True)