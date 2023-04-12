import pandas as pd
import numpy as np
from datetime import datetime

def bh(df, x, start, end):
    start = datetime.strptime(start, '%Y%m%d').isoformat()
    end = datetime.strptime(end, '%Y%m%d').isoformat()
    df = df.loc[start : end]

    df = df.loc[~df.isin([np.nan, np.inf, -np.inf]).any(1)] # 결측치, 무한대 제거
    price_df = df[[x]]
    price_df['daily_rtn'] = price_df[x].pct_change()
    price_df['st_rtn'] = (1 + price_df['daily_rtn']).cumprod()

    return price_df

