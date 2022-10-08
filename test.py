from tests.helper import *
from strompris.common import *

mock = MockPriceSource()
today = mock.fetch_for_today()
print(Common().getMax(today))
print(Common().getAverage(today))
print(Common().getMin(today))

print("Dagens")
for price in today:
    print(price.kwh)