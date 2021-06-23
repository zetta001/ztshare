# -*- coding:utf-8 -*-
import os
from numpy import mask_indices
import pandas as pd
from ztshare.common import cons as ct


def set_app(app_id: str, app_secret: str):
    df = pd.DataFrame([[app_id, app_secret]], columns=["id", 'secret'])
    user_home = os.path.expanduser("~")
    fp = os.path.join(user_home, ct.TOKEN_F_P)
    df.to_csv(fp, index=False)


def get_app():
    user_home = os.path.expanduser("~")
    fp = os.path.join(user_home, ct.TOKEN_F_P)
    if os.path.exists(fp):
        df = pd.read_csv(fp)
        return str(df.loc[0]["id"]), str(df.loc[0]["secret"])
    else:
        print(ct.TOKEN_ERR_MSG)
        return None, None

