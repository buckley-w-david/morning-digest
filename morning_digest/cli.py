import asyncio
import typing

import click

from morning_digest.component import ComponentType, ALL_COMPONENTS
from morning_digest.component import MonkeyUserComponent
from morning_digest import generate
from morning_digest import render


@click.group()
def main():
    pass


async def a_generate(output, components):
    components = [await MonkeyUserComponent.from_url("https://www.monkeyuser.com/")]
    output.write(render.render_components(components))


@main.command()
@click.argument("output", type=click.File("w"))
@click.option("--components", type=click.Choice(ALL_COMPONENTS))
def generate(output: typing.IO[str], components):
    asyncio.run(a_generate(output, components))
