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


    #@commands.Cog.listener() #On l'as commanté car sinon il interferai avec le debug des autre bots... en les faisant chier niveau 80
    async def on_message(self, message):
        if message.author.bot or message.content.startswith(Context.ConfigManager.Get("Discord", "prefix")): return
        s = Context.Bot.user.name.lower() in message.content.lower() or Context.Bot.user.mentioned_in(message)
        ev = Context.Predicter.Evaluate(message.content)
        if (ev > 0.56):
            if s:
                await message.channel.send(choice(self.S_RESPONSES))
            else:
                await message.channel.send(choice(self.RESPONSES))
            await message.channel.send(f"you won {round(ev*1000)} points for this (Just kidding i don't count)")



Context.Bot.add_cog(Handler())