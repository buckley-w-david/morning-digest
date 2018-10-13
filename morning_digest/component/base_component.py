import asyncio
import typing

import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


class ComponentContent:
    def __init__(self, text, image=None):
        self.text = text
        self.image = image

    def __str__(self):
        if self.image:
            return f"""{self.text}: {self.image}"""
        else:
            return self.text

    def __repr__(self):
        return f"ComponentContent({repr(self.text)}, {repr(self.image)})"


class Component:
    def __init__(self, url: str, content: typing.Sequence[ComponentContent]) -> None:
        self.url = url
        self.content = content

    @classmethod
    async def from_url(cls, url: str) -> "Component":
        async with aiohttp.ClientSession() as session:
            html = await fetch(session, url)
            content = await cls.process(html)

        return Component(url, content)

    @staticmethod
    async def process(html: str, aio_session) -> str:
        raise NotImplementedError("Base Component cannot process")

    def __str__(self):
        return "\n".join(str(content) for content in self.content)

    def __repr__(self):
        return f"Component({repr(self.url)}, {repr(self.content)})"
