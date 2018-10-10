import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

class Component:

    def __init__(self, url: str, content: str) -> None:
        self.url = url
        self.content = content

    @classmethod
    async def from_url(cls, url: str) -> 'Component':
        async with aiohttp.ClientSession() as session:
            html = await fetch(session, url)

        content = await cls.process(html)
        return Component(url, content)

    @staticmethod
    async def process(html: str) -> str:
        raise NotImplementedError("Base Component cannot process")

    def render(self):
        raise NotImplementedError("Base Component cannot be rendered")
