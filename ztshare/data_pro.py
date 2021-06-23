# -*- coding:utf-8 -*- 
from ztshare import client
from ztshare.util import upass


def pro_api(app_id='', app_secret=''):
    """ pro API
    初始化pro API,第一次可以通过zs.set_app(app_id='your appId', app_secret='your appSecret')来记录自己的凭证
    """
    if app_id == '' or app_id is None or app_secret == '' or app_secret is None:
        app_id, app_secret = upass.get_app()
    if app_id is not None and app_id != '' and app_secret is not None and app_secret != '':
        pro = client.DataApi(app_id=app_id, app_secret=app_secret)
        return pro
    else:
        raise Exception('api init error.')


def pro_bar(zcode='', api=None, start_date=None, end_date=None, freq='D', retry_count = 3):
    """ BAR数据
    Args:
        zcode:        数据代码
        api:      api对象，如果初始化了set_app，此参数可以不需要
        start_date:   开始日期  YYYYMMDD
        end_date:     结束日期  YYYYMMDD
        freq:         支持日/周/月/年  D/W/M/Y
        retry_count:  网络重试次数
    Return:
        DataFrame
    """
    zcode = zcode.strip()
    if zcode is None or zcode == '':
        raise Exception('missing parameter zcode!')
    api = api if api is not None else pro_api()
    for _ in range(retry_count):
        try:
            freq = freq.strip().upper()
            df = api.stock(zcode=zcode, start_date=start_date, end_date=end_date, freq=freq)
            data = df
            return data
        except Exception as e:
            print(e)
            return None
        else:
            return
    raise IOError("RRROR.")