from strompris import *
from strompris.const import SOURCE_HVAKOSTERSTROMMEN
from strompris.strompris import Strompris

pris = Strompris(SOURCE_HVAKOSTERSTROMMEN, 1)
priser = pris.getElPrices()
for p in priser:
    print(p.__dict__())
    
print("\nPrice now is: ", pris.getElPriceNow().__dict__())