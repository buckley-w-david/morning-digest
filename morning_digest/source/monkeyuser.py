from bs4 import BeautifulSoup

from morning_digest.source import Source
from morning_digest.source import SourceContent


class MonkeyUser(Source):
    DEFAULT_URL = 'https://www.monkeyuser.com/'

    @staticmethod
    async def process(html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")
        image_tag = (
            soup.body.find("div", class_="content-container")
            .find("div", class_="post")
            .find("div", class_="content")
            .p.img
        )

        title = image_tag.get("title")
        origin = image_tag.get("src")

        return [SourceContent(title, origin)]
