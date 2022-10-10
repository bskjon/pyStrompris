from strompris import *
from strompris.const import SOURCE_HVAKOSTERSTROMMEN
from strompris.strompris import Strompris
import json

pris = Strompris(SOURCE_HVAKOSTERSTROMMEN, 1)
priser = pris.get_available_prices()
for p in priser:
    print(p.__dict__())
    
print("\nPrice now is: ", pris.get_current_price().__dict__())

print("Attrs", json.dumps(pris.get_current_price_attrs()))

print(" --- ")
print("Price + Levels")
for p in priser:
    print(pris.get_price_attrs(p))