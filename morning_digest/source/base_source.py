import asyncio
import typing

import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


class SourceContent:
    def __init__(self, text, image=None):
        self.text = text
        self.image = image

    def __str__(self):
        if self.image:
            return f"""{self.text}: {self.image}"""
        else:
            return self.text

    def __repr__(self):
        return f"SourceContent({repr(self.text)}, {repr(self.image)})"


class Source:
    DEFAULT_URL = None

    def __init__(self, url: str, content: typing.Sequence[SourceContent]) -> None:
        self.url = url
        self.content = content

    @classmethod
    async def from_url(cls, url: str) -> "Source":
        async with aiohttp.ClientSession() as session:
            html = await fetch(session, url)
            content = await cls.process(html)

        return Source(url, content)

    @classmethod
    async def default(cls) -> "Source":
        return await cls.from_url(cls.DEFAULT_URL)

    @staticmethod
    async def process(html: str, aio_session) -> str:
        raise NotImplementedError("Base Source cannot process")

    def __str__(self):
        return "\n".join(str(content) for content in self.content)

    def __repr__(self):
        return f"Source({repr(self.url)}, {repr(self.content)})"
