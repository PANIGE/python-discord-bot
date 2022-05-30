import os
from constants.exceptions import IgnoredException
from helpers import console
from objects import Context
from Bot import bot

from helpers import database
from helpers import generalHelper
from helpers.configHelper import configManager
import traceback

if __name__ == "__main__":
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.printAscii()
        console.writeColored("Hello, this is the Bot", console.Colors.GREEN)
        console.write("> Reading config file... ", True)
        Context.ConfigManager = configManager("config.ini")
        if Context.ConfigManager.default:
            console.writeCaution()
            console.writeColored("[!] config.ini not found. A default one has been generated.", console.Colors.YELLOW)
            console.writeColored("[!] Please edit your config.ini and run the server again.", console.Colors.YELLOW)
            raise IgnoredException()
        if not Context.ConfigManager.isValid():
            console.writeFailure()
            console.writeColored("[!] Invalid config.ini. Please configure it properly", console.Colors.RED)
            console.writeColored("[!] Delete your config.ini to generate a default one", console.Colors.RED)
            raise IgnoredException()
        else:
            console.writeSuccess()

        
        if generalHelper.stringToBool(Context.ConfigManager.Get("Database", "enabled")):
            try:
                console.write("> Connecting to MySQL database... ", True)
                Context.mysql = database.Db()
                console.writeSuccess()
            except:
                # Exception while connecting to db
                console.writeFailure()
                console.writeColored("[!] Error while connection to database. Please check your config.ini and run the server again", console.Colors.RED)
                raise IgnoredException()
        else:
            console.writeColored("[!] Mysql Server is disabled", console.Colors.YELLOW)

        try:
            console.write("> Creating Bot... ", True)
            bot.Load()
            console.writeSuccess()
        except:
            console.writeFailure()
            console.writeColored("[!] Error while Loading discord Cogs", console.Colors.RED)
            raise

        try:
            console.write("> Loading IA... ", True)
            from helpers.deepLearnHelper import predicter
            Context.Predicter = predicter(os.path.join(os.getcwd(), ".data", "model.hdf5"))
            console.writeSuccess()
        except:
            console.writeFailure()
            console.writeColored("[!] Error while Loading discord Cogs", console.Colors.RED)
            raise

        console.write("> Loading Bot Handlers...")
        bot.LoadCogs(Context.Bot)
        console.writeColored("All Handlers Loaded", console.Colors.GREEN)

        console.writeColored("Bot Ready", console.Colors.YELLOW)
        Context.Bot.run(Context.ConfigManager.Get("Discord", "token"))



    except IgnoredException:
        pass
    except Exception as e:
        console.error(traceback.print_exc())
    finally:
        console.writeColored("Goodbye !", console.Colors.GREEN)