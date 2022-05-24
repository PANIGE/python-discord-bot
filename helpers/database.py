import mysql.connector
from mysql.connector.connection import MySQLConnection
from objects import Context
from helpers import console

class Db:
    def __init__(self) -> None:
        dbConfig = {
            "host" : Context.configManager.config.get("Database", "host"),
            "username" : Context.configManager.config.get("Database", "username"),
            "password" : Context.configManager.config.get("Database", "password"),
            "database" : Context.configManager.config.get("Database", "database"),
            "pool_size" : int(Context.configManager.config.get("Database", "workers")),
            "pool_name" : "DiscordPool",
        }
        self.cnx:MySQLConnection = mysql.connector.connect(**dbConfig)
        

    def fetch(self, request, *args):
        console.debug(f"sql fetch : {request}" % args)
        cur = self.cnx.cursor(dictionary=True, buffered=True)
        cur.execute(request, args)
        c = cur.fetchone()
        console.debug(f"sql response : {c}")
        cur.close()
        return c

    def fetchAll(self, request, *args):
        console.debug(f"sql fetchAll : {request}" % args)
        cur = self.cnx.cursor(dictionary=True, buffered=True)
        cur.execute(request, args)
        c = cur.fetchall()
        console.debug(f"sql response : {c}")
        cur.close()
        return c

    def execute(self, request, *args):
        console.debug(f"sql Execute : {request}" % args)
        cur = self.cnx.cursor(dictionary=True, buffered=True)
        cur.execute(request, args)
        self.cnx.commit()
        cur.close()

    def ping(self):
        self.fetch("SELECT 1+1")