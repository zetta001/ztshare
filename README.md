### Installation
- source package

```
$ python setup install
```

- PyPI

```
$ pip install ztshare
```
    
### Upgrade

    pip install ztshare --upgrade
    
### Quick Start
```
import ztshare as zs
zs.set_app(app_id='your appId', app_secret='yourappSecret')
zs.pro_bar(zcode='000001.SH', start_date='20210621', end_date='20210621')
```