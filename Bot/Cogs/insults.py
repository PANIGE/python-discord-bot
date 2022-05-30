from math import floor
from secrets import choice
from objects import Context
from discord.ext import commands
import discord

class Handler(commands.Cog):

    RESPONSES = [
        "C'était bien envoyé !"
    ]

    S_RESPONSES = [
        "Mes sentiments ont été bléssés"
    ]

    def __init__(self):
        self.bot = Context.Bot
        self._last_member = None


    #@commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or message.content.startswith(Context.ConfigManager.Get("Discord", "prefix")): return
        s = Context.Bot.user.name.lower() in message.content.lower() or Context.Bot.user.mentioned_in(message)
        ev = Context.Predicter.Evaluate(message.content)
        if (ev > 0.56):
            if s:
                await message.channel.send(choice(self.S_RESPONSES))
            else:
                await message.channel.send(choice(self.RESPONSES))



Context.Bot.add_cog(Handler())