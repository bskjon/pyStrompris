# Strømpris


## Usage

Supported sources:
- Hvakosterstrommen

```python
from strompris.strompris import Strompris 
from strompris.const import SOURCE_HVAKOSTERSTROMMEN

strompris = Strompris(SOURCE_HVAKOSTERSTROMMEN) # Can also be used with direct string

"""Returns pricing for today and tomorrow if available on NO1 price zone"""
priser = strompris.getElPriceFromSource(zone=1, withFuture=True) # Zone 1-5

"""Returns pricing for current hour using GMT+1|+2"""
now = strompris.getElPriceNow(zone=1)

"""Returns pricing for current hour along with extra info:

total (kwh + tax)
min
max
avg
tax
price_level
"""
nowAttrs = strompris.getPriceAttrs(zone=1)


```


![hvakosterstrommen.no](./static-assets/hvakosterstrommen.png)