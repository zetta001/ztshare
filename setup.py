from setuptools import setup, find_packages
import codecs
import os


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

long_desc = """
ZtShare
===============

Target Users
--------------

* financial market analyst of China
* learners of financial data analysis with pandas/NumPy
* people who are interested in China financial data

Installation
--------------

    pip install ztshare
    
Upgrade
---------------

    pip install ztshare --upgrade
    
Quick Start
--------------

::

    import ztshare as zs
    zs.set_app(app_id='your appId', app_secret='your appSecret')
    zs.pro_bar(zcode='000001.SH', start_date='20210621', end_date='20210621')
    
return::

        date       high       amount          vol        low  adj      close       open
    20210506  3471.2400  400525169.6  310424192.0  3426.8487  1.0  3441.2826  3446.0743
    20210507  3457.8924  411078841.6  353785389.0  3416.7755  1.0  3418.8741  3446.4070
    20210510  3429.7359  399717549.0  374170884.0  3401.9346  1.0  3427.9909  3423.5900
    20210511  3448.0959  390326273.8  350934112.0  3384.6966  1.0  3441.8454  3406.5980
    20210512  3466.3708  343860406.4  311444547.0  3428.3944  1.0  3462.7513  3429.7544
    20210513  3448.0169  356376917.8  319325327.0  3418.3846  1.0  3429.5361  3432.1380
    20210514  3490.6437  411116942.8  336982309.0  3422.5649  1.0  3490.3762  3436.0919
    20210517  3530.5055  424476783.4  322135969.0  3490.1438  1.0  3517.6158  3490.4091
    20210518  3529.0144  336028774.7  271308558.0  3510.8620  1.0  3529.0144  3520.6488
    20210519  3521.1100  349973152.3  278321117.0  3503.8151  1.0  3510.9647  3521.1100
    20210520  3517.7400  390355321.5  326009333.0  3486.0662  1.0  3506.9444  3500.8773
    20210521  3518.3769  356025931.3  283826285.0  3479.6744  1.0  3486.5569  3510.8353
    20210524  3498.3037  367181627.9  289509242.0  3469.8746  1.0  3497.2821  3486.2711
    20210525  3584.5774  472213531.4  341241127.0  3502.4429  1.0  3581.3418  3502.5390
    20210526  3603.4881  455831256.7  341980288.0  3585.3700  1.0  3593.3570  3586.8388
    20210527  3626.3584  429004239.3  309551486.0  3579.2600  1.0  3608.8507  3585.7337
    20210528  3622.1800  452445032.0  349208830.0  3582.3580  1.0  3600.7844  3610.7668
    20210531  3615.6568  449694381.0  331523770.0  3580.6524  1.0  3615.4773  3600.0700
    20210601  3626.0737  471663104.8  352811413.0  3581.9115  1.0  3624.7138  3608.5978
"""

def read_install_requires():
    reqs = [
            'numpy>=1.16.5',
            'pandas>=1.0.0',
            'requests>=2.0.0',
            ]
    return reqs


setup(
    name='ztshare',
    version=read('ztshare/VERSION.txt'),
    description='ztshare open platform interface package',
#     long_description=read("READM.rst"),
    long_description = long_desc,
    author='zetta',
    license='BSD',
    install_requires=read_install_requires(),
    keywords='Global Financial Data',
    classifiers=['Development Status :: 4 - Beta',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: BSD License'],
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.csv', '*.txt']},
)