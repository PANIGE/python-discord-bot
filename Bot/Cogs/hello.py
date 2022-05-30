from objects import Context
from discord.ext import commands
import discord

class General(commands.Cog):
    def __init__(self):
        self.bot = Context.Bot
        self._last_member = None

    @commands.command()
    async def hello(self, ctx):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member  

    @commands.command(hidden=True)
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def foob(self, ctx, *, msg):
        """Says a fooby message"""
        await ctx.message.delete()
        await ctx.send('<:foob:978233280392466473> {} <:foob:978233280392466473>'.format(msg))



Context.Bot.add_cog(General())