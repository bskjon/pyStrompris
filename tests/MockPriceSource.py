from datetime import datetime, timedelta
import aiohttp
import asyncio
import json
import os
import pytest
from typing import Final, List, Optional, final
from strompris.schemas import Pris
from strompris.PriceSource import PriceSource, Hvakosterstrommen

def sync(func):
    return asyncio.get_event_loop().run_until_complete(func)

class MockPriceSource(Hvakosterstrommen):
    
    price_files = [
        "2022-09-20_NO1.json",
        "2022-10-08_NO1.json",
        "2022-10-09_NO1.json",
        "2022-10-30_NO1.json",
        "2022-12-04_NO1.json",
        "2022-12-06_NO1.json"
        
    ]
    
    def __init__(self, price_zone: int = -1) -> None:
        super().__init__(price_zone)
    
    def readPriceAsset(self, file: str) -> Optional[List[dict]]:
        f = open(os.path.dirname(__file__)+'/assets/' + file, "r")
        txt = f.read()
        return json.loads(txt)
    
    @pytest.mark.asyncio
    async def async_fetch_for_today(self) -> list[Pris]:
        self._price_today = await self._map_response(self.readPriceAsset(self.price_files[1]))
        return self._price_today
    
    @pytest.mark.asyncio
    async def async_fetch_for_tomorrow(self) -> list[Pris]:
        self._price_tomorrow = await self._map_response(self.readPriceAsset(self.price_files[2]))
        return self._price_tomorrow
        
    @pytest.mark.asyncio
    async def async_fetch_for_spesific_record(self, itemNo: int) -> Optional[List[Pris]]:
        self._price_tomorrow = await self._map_response(self.readPriceAsset(self.price_files[itemNo]))
        return self._price_tomorrow
            
    
    def fetch_for_today(self) -> Optional[List[Pris]]:
        return sync(self.async_fetch_for_today())
    
    def fetch_for_tomorrow(self) -> Optional[List[Pris]]:
        return sync(self.async_fetch_for_tomorrow())