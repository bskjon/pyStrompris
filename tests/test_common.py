import unittest
from strompris import common
from strompris.schemas import Prising
from tests.helper import MockPriceSource, sync
from strompris.common import Common


class TestCommon(unittest.TestCase):
    common = Common()
    today: list[Prising] = []
    
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.today = MockPriceSource().fetch_for_today()
    
    def test_getMax(self):
        assert self.common.getMax(prices=self.today) == 0.711
    
    def test_getAverage(self):
        assert self.common.getAverage(prices=self.today) == 0.5008750000000001
    
    def test_getMin(self):
        assert self.common.getMin(prices=self.today) == 0.312
        
    def test_onlyExpensiveIsTrue(self):
        now = next(p for p in self.today if p.kwh == self.common.getMax(self.today))
        
        assert self.common.isVeryExpensive(now, self.today) is True
        assert self.common.isExpensive(now, self.today) is True
        self.assertFalse(self.common.isCheap(now, self.today), "Price {kwhCost} is identified as Expensive, and threshold is {threshold}".format(kwhCost=now.kwh, threshold=self.common._isExpensiveThreadhold(self.today)))
        self.assertFalse(self.common.isVeryCheap(now, self.today), "Price {kwhCost} is identified as Expensive, and threshold is {threshold}".format(kwhCost=now.kwh, threshold=self.common._isExpensiveThreadhold(self.today)))
        
    def test_onlyCheapIsTrue(self):
        now = next(p for p in self.today if p.kwh == self.common.getMin(self.today))
        
        assert self.common.isVeryExpensive(now, self.today) is False
        assert self.common.isExpensive(now, self.today) is False
        self.assertTrue(self.common.isCheap(now, self.today), "Price {kwhCost} is not identified as Cheap, and threshold is {threshold}".format(kwhCost=now.kwh, threshold=self.common._isCheapThreshold(self.today)))
        self.assertTrue(self.common.isVeryCheap(now, self.today), "Price {kwhCost} is not identified as Very Cheap, and threshold is {threshold}".format(kwhCost=now.kwh, threshold=self.common._isCheapThreshold(self.today)))
        
    def test_findOnlyCheap(self):
        cheap = list(filter(lambda p: p.start.hour >= 12 and p.start.hour < 16, self.today))
        for price in cheap:
            assert self.common.isCheap(price, self.today) is True
    
    def test_pricesAreOnlyAverage(self):        
        average = list(filter(lambda p: p.start.hour <= 6, self.today))
        avg_2 = list(filter(lambda p: p.start.hour >= 19 and p.start.hour <= 21, self.today))
        average.extend(avg_2)
        for price in average:
            self.assertFalse(self.common.isCheap(price, self.today), "Price {kwhCost} is identified as Cheap @ {hour}, and threshold is {threshold}".format(hour=price.start.hour, kwhCost=price.kwh, threshold=self.common._isCheapThreshold(self.today)))
            self.assertFalse(self.common.isExpensive(price, self.today), "Price {kwhCost} is identified as Expensive".format(kwhCost=price.kwh))
            
    def test_pricesAreOnlyExpensive(self):
        expensive: list[Prising] = []
        exp_1 = list(filter(lambda p: p.start.hour >= 7 and p.start.hour <= 10, self.today))
        exp_2 = list(filter(lambda p: p.start.hour >= 22, self.today))
        expensive.extend(exp_1)
        expensive.extend(exp_2)
        
        for price in expensive:
            self.assertFalse(self.common.isCheap(price, self.today), "Price {kwhCost} is identified as Cheap @ {hour}, and threshold is {threshold}".format(hour=price.start.hour, kwhCost=price.kwh, threshold=self.common._isCheapThreshold(self.today)))
            self.assertTrue(self.common.isExpensive(price, self.today), "Price {kwhCost} is not identified as Expensive, and is {threshold}".format(kwhCost=price.kwh, threshold=self.common._isCheapThreshold(self.today)))