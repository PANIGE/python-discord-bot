import aiohttp
import asyncio
import logging

from discord.ext import commands
from objects import Context

__author__ = "tmerc" #Respect authors


class CatFact(commands.Cog):
    """Gets a random cat fact."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__url: str = "https://catfact.ninja/fact"
        self.__session = aiohttp.ClientSession()

    @commands.command()
    async def catfact(self, ctx: commands.Context) -> None:
        """Gets a random cat fact."""

        await ctx.trigger_typing()

        try:
            async with self.__session.get(self.__url) as response:
                fact = (await response.json())["fact"]
                await ctx.send(fact)
        except aiohttp.ClientError:
            log.warning("API call failed; unable to get cat fact")
            await ctx.send("I was unable to get a cat fact.")

Context.Bot.add_cog(CatFact())