from tests.MockPriceSource import *
from strompris.common import *
from tests.test_strompris import TestStrompris

# mock = MockPriceSource()
# today = mock.fetch_for_today()
# print(Common().getMax(today))
# print(Common().getAverage(today))
# print(Common().getMin(today))
# 
# print("Dagens")
# for price in today:
#     print(price.kwh)


tts = TestStrompris()

sync(tts.test_async_hasPriceJumpOrDrop())

print("\n\nToday")
sync(tts.test_async_priceTodayLevel())
print("\n\nTomorrow")
sync(tts.test_async_priceTomorrowLevel())
print("\n\nWith big changes")
sync(tts.test_async_priceBigChangesLevel())