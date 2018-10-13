import asyncio
import typing

import click

from morning_digest.component import ComponentType, ALL_COMPONENTS, TYPE_MAP
from morning_digest import render


@click.group()
def main():
    pass


# TODO
# Come up with a method fo specifying alternate URLS
# Instead of always pulling the default
async def a_generate(output, components_names):
    types = [ComponentType.from_name(c) for c in components_names]
    components = [await TYPE_MAP[t].default() for t in types]
    output.write(render.render_components(components))


@main.command()
@click.argument("output", type=click.File("w"))
@click.option("--component", type=click.Choice(ALL_COMPONENTS), multiple=True)
def generate(output: typing.IO[str], component):
    asyncio.run(a_generate(output, component))
