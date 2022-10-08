from datetime import datetime, timedelta
import aiohttp
import asyncio
import json
import os
import pytest
from typing import Final, List, Optional, final
from strompris.schemas import Prising
from strompris.PriceSource import PriceSource, Hvakosterstrommen

def sync(func):
    return asyncio.get_event_loop().run_until_complete(func)

class MockPriceSource(Hvakosterstrommen):
    
    def readPriceAsset(self, file: str) -> Optional[List[dict]]:
        f = open(os.path.dirname(__file__)+'/assets/' + file, "r")
        txt = f.read()
        return json.loads(txt)
    
    @pytest.mark.asyncio
    async def async_fetch_for_today(self, zone: int = -1) -> Optional[List[Prising]]:
        return await self._map_response(self.readPriceAsset("2022-10-08_NO1.json"))
    
    @pytest.mark.asyncio
    async def async_fetch_for_tomorrow(self, zone: int = -1) -> Optional[List[Prising]]:
        return await self._map_response(self.readPriceAsset("2022-10-09_NO1.json"))
    
    
    def fetch_for_today(self, zone: int = -1) -> Optional[List[Prising]]:
        return sync(self.async_fetch_for_today(zone))
    
    def fetch_for_tomorrow(self, zone: int = -1) -> Optional[List[Prising]]:
        return sync(self.async_fetch_for_tomorrow(zone))