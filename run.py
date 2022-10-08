from strompris import *
from strompris.const import SOURCE_HVAKOSTERSTROMMEN
from strompris.strompris import Strompris

pris = Strompris(SOURCE_HVAKOSTERSTROMMEN)
priser = pris.getElPriceFromSource(1)
for p in priser:
    print(p.__dict__())
    
print("\nPrice now is: ", pris.getElPriceNow(1).__dict__())