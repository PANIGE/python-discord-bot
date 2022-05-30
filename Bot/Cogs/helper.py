
from objects import Context
from discord.ext import commands
import discord
import os
from helpers.checks import *

from objects.Node import TreeNode, TreeExplorer


class Handler(commands.Cog):
    def __init__(self):
        self.pendings = {}
        self.bot = Context.Bot

    @commands.command()
    async def ask(self, ctx):
        if (ctx.message.author.id in self.pendings.keys()):
            return await ctx.send("You aready are in conv in <#{}>, if you left the server, well, it sucks, you'll have to wait for a bot restart".format(self.pendings[ctx.message.author.id]))
        self.pendings[ctx.message.author.id] = ctx.message.channel.id
        tree = Handler.GenerateTreeManager()
        run = True
        while run:
            if not tree.CanGoLower:
                await ctx.send(tree.Current.Value)
                run = False
                continue

            if (len(tree.ListValues()) == 1):
                tree.GoTo(tree.ListValues()[0])
            
            text = "**break** (exit discussion)\n"
            if (tree.CanGoUpper):
                text += "**back** (Go Back a Level)\n"
            text += '\n'.join(tree.ListValues())
            embed=discord.Embed(description=text, color=0xff0000)
            await ctx.send(tree.Current.Value, embed=embed)




            msg = await self.bot.wait_for('message', check=SameChannelAndAuthor(ctx))
            if msg.content in tree.ListValues():
                tree.GoTo(msg.content)
            else:
                msg = msg.content
                if msg.lower() == "break":
                    await ctx.send("Exiting...")
                    run = False
                elif msg.lower() == "back" and tree.CanGoUpper:
                    await ctx.send("Okay, going up !")
                    tree.GoUp()
                else:

                    await ctx.send("Woops, sorry, but that's not what i expected, let's try this Again !")

        del self.pendings[ctx.message.author.id]


        

    @staticmethod
    def GenerateTreeManager():
        data = Handler.RecurFolder(os.path.join(os.getcwd(), ".data","repr"))
        node = TreeNode("What are you in need today ?")
        print(data)
        for key, value in data.items():
            node.AddChild(Handler.RecurTree(key, value))
        return TreeExplorer(node)

    @staticmethod
    def RecurTree(val, childs):
        node = TreeNode(val)
        if type(childs) is str:
            node.AddChild(TreeNode(childs))
            return node
        for key, value in childs.items():
            node.AddChild(Handler.RecurTree(key, value))
        return node

    @staticmethod
    def RecurFolder(fold):
        data = {}
        folders = os.listdir(fold)
        for folder in folders:
            if (os.path.isdir(os.path.join(fold, folder))):
                data[os.path.basename(folder)] = Handler.RecurFolder(os.path.join(fold, folder))
            else:
                with open(os.path.join(fold, folder), 'r') as f:
                    data[os.path.basename(folder)] = f.read()
        return data
        


Context.Bot.add_cog(Handler())