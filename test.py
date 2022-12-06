from strompris.message_compose import ComposeMessage
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

sync(tts.test_async_priceTest4())
sync(tts.test_today_current_price_attrs())

prices = sync(tts.async_get_price_for_record(0))


# cm = ComposeMessage(floors, roofs)
# roof = cm.get_roof()
# assert roof != None
# floor = cm.get_floor()
# assert floor != None
# 
# 
# messagees = cm.compose(floor, roof)
# print(messagees)


sync(tts.test_async_priceLevelOn(5))


prices = sync(tts.async_get_price_for_record(5))



tts._apply_tax(prices)
grouped = tts.get_price_level_grouped(tts.get_prices_with_level(prices))

for i, price in enumerate(grouped):
    print("\t \n")
    print("Group", str(i))
    for item in price.prices:
        print(f"{item.start.hour}h ", round(item.total, 3), item.level)
    
