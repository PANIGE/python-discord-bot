from objects import Context
from discord.ext import commands
import discord

class LoupGarou(commands.Cog):
    def __init__(self):
        self.bot = Context.Bot
        

    @commands.command()
    async def players(self, ctx):
        pass

Context.Bot.add_cog(LoupGarou())