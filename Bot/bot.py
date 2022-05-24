import os
from objects import Context
from discord.ext import commands
from helpers import console
import traceback
import discord


def Load():
    intents = discord.Intents.all()
    Context.Bot = commands.Bot(command_prefix=Context.ConfigManager.Get("Discord", "prefix"), intents=intents)

    @Context.Bot.event
    async def on_ready():
        console.info("Bot Ready")
        console.info(f"https://discord.com/oauth2/authorize?client_id={Context.Bot.user.id}&scope=bot&permissions=8")
        await Context.Bot.change_presence(activity=discord.Game(name="with you"))

    @Context.Bot.event
    async def on_command_error(ctx, error):
        console.error(error)
        await ctx.send(error)
        
        

def LoadCogs(bot):
    path = "Bot/Cogs"
    files = os.listdir(os.path.join(os.getcwd(), path))
    baseimport = path.replace("/", ".")
    baseimport.strip(".")
    for file in files:
        if file.endswith(".py"):
            file = file.replace(".py", "")
            console.writeColored("loading Handler {}{}{} ...".format(console.Colors.ENDC,file, console.Colors.BLUE), console.Colors.BLUE, True)
            try:
                __import__(baseimport + "." + file)
                console.writeSuccess()
            except Exception as e:
                console.writeFailure()
                console.error(traceback.format_exc())




