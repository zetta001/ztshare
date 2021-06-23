import ztshare as zs

zs.set_app(app_id='your appId', app_secret='your appSecret') 
df = zs.pro_bar(zcode='000001.SH', start_date='20210501', end_date='20210601')
print(df)

