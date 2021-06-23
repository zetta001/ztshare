# -*- coding:utf-8 -*- 
import codecs
import os

__version__ = codecs.open(os.path.join(os.path.dirname(__file__), 'VERSION.txt')).read()
__name__ = "ztshare"
__author__ = 'zetta'



"""
for token
"""
from ztshare.util.upass import (get_app, set_app)


"""
for ztshare pro api
"""
from ztshare.data_pro import (pro_api, pro_bar)
