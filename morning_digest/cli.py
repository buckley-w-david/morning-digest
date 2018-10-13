import asyncio
import typing

import click

from morning_digest.source import SourceType, ALL_SOURCES, TYPE_MAP
from morning_digest import render


@click.group()
def main():
    pass

# TODO
# Come up with a method fo specifying alternate URLS
# Instead of always pulling the default
async def a_generate(output, source_names):
    if 'ALL' in source_names:
        types = [c for c in SourceType]
    else:
        seen = set()
        # Remove duplicates while maintaing order
        types = [SourceType.from_name(c) for c in source_names if not (c in seen or seen.add(c))]

    sources = [await TYPE_MAP[t].default() for t in types]
    output.write(render.render_sources(sources))


@main.command()
@click.argument("output", type=click.File("w"))
@click.option("--source", type=click.Choice(ALL_SOURCES + ['ALL']), multiple=True, default=('ALL',))
def generate(output: typing.IO[str], source):
    asyncio.run(a_generate(output, source))
