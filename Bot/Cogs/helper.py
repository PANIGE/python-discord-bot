
from objects import Context
from discord.ext import commands
import discord
import os
from helpers.checks import *

from objects.Node import TreeNode, TreeExplorer




class Helper(commands.Cog):
    def __init__(self):
        self.pendings = {}
        self.bot = Context.Bot

    @commands.command()
    async def ask(self, ctx):
        """Allows to get some ressources from the bot"""
        if (ctx.message.author.id in self.pendings.keys()):
            return await ctx.send("You aready are in conv in <#{}>, if you left the server, well, it sucks, you'll have to wait for a bot restart".format(self.pendings[ctx.message.author.id]))
        self.pendings[ctx.message.author.id] = ctx.message.channel.id
        tree = Helper.GenerateTreeManager()
        run = True
        while run:


            while (len(tree.ListValues()) == 1):
                tree.GoTo(tree.ListValues()[0])


            msg = tree.Current.Value

            if not tree.CanGoLower:
                while (len(tree.ListValues()) == 1):
                    print(len(tree.ListValues()))
                    tree.GoUp()
                
            
            text = "**break** (exit discussion)\n"
            if (tree.CanGoUpper):
                text += "**back** (Go Back a Level)\n"
            text += '\n'.join(tree.ListValues())
            embed=discord.Embed(description=text, color=0xff0000)
            await ctx.send(msg, embed=embed)




            msg = await self.bot.wait_for('message', check=SameChannelAndAuthor(ctx))
            if msg.content in tree.ListValues():
                tree.GoTo(msg.content)
            else:
                msg = msg.content
                if msg.lower() == "break":
                    await ctx.send("Have a nice day !")
                    run = False
                elif msg.lower() == "back" and tree.CanGoUpper:
                    await ctx.send("Okay, going up !")
                    tree.GoUp()
                    while (len(tree.ListValues()) == 1):
                        print(len(tree.ListValues()))
                        tree.GoUp()
                else:

                    await ctx.send("Woops, sorry, but that's not what i expected, let's try this Again !")

        del self.pendings[ctx.message.author.id]


        

    @staticmethod
    def GenerateTreeManager():
        data = Helper.RecurFolder(os.path.join(os.getcwd(), ".data","repr"))
        node = TreeNode("What are you in need today ?")
        for key, value in data.items():
            node.AddChild(Helper.RecurTree(key, value))
        return TreeExplorer(node)

    @staticmethod
    def RecurTree(val, childs):
        node = TreeNode(val)
        if type(childs) is str:
            node.AddChild(TreeNode(childs))
            return node
        for key, value in childs.items():
            node.AddChild(Helper.RecurTree(key, value))
        return node

    @staticmethod
    def RecurFolder(fold):
        data = {}
        folders = os.listdir(fold)
        for folder in folders:
            if (os.path.isdir(os.path.join(fold, folder))):
                data[os.path.basename(folder)] = Helper.RecurFolder(os.path.join(fold, folder))
            else:
                with open(os.path.join(fold, folder), 'r', encoding="utf-8") as f:
                    data[os.path.basename(folder)] = f.read()
        return data
        


Context.Bot.add_cog(Helper())