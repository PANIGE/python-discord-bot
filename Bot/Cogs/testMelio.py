from objects import Context
from discord.ext import commands
import discord

class LoupGarou(commands.Cog):
    def __init__(self):
        self.bot = Context.Bot
        self._last_member = None

    @commands.command()
    async def hello45(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member


Context.Bot.add_cog(LoupGarou())