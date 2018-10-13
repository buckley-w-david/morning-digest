from bs4 import BeautifulSoup

from morning_digest.source import Source
from morning_digest.source import SourceContent


class XKCD(Source):
    DEFAULT_URL = 'https://xkcd.com/'

    @staticmethod
    async def process(html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")
        image_tag = (
            soup.body.find("div", id="middleContainer")
            .find("div", id="comic")
            .img
        )

        image_text = image_tag.get("title")
        origin = 'https:' + image_tag.get("src")
        title = image_tag.get("alt")


        return [
            SourceContent(title, origin),
            SourceContent(image_text),
        ]
