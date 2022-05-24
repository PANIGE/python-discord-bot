import os
import configparser

class configManager:
    """
    config.ini object

    config -- list with ini data
    default -- if true, we have generated a default config.ini
    """

    config = configparser.ConfigParser()
    extra = {}
    fileName = ""        # config filename
    default = True

    # Check if config.ini exists and load/generate it
    def __init__(self, filename):
        """
        Initialize a config object
        """

        self.fileName = filename
        if os.path.isfile(self.fileName):
            # config.ini found, load it
            self.config.read(self.fileName)
            self.default = False
        else:
            # config.ini not found, generate a default one
            self.CreateConfig()
            self.default = True

    # Check if config.ini has all needed the keys
    def isValid(self):
        """
        Check if this config has the required keys

        return -- True if valid, False if not
        """

        try:
            # Try to get all the required keys
            self.config.get("Database", "enabled")
            self.config.get("Database", "host")
            self.config.get("Database", "username")
            self.config.get("Database", "password")
            self.config.get("Database", "database")
            self.config.get("Database", "workers")

            self.config.get("Discord", "token")
            self.config.get("Discord", "prefix")
            return True
        except:
            return False


    # Generate a default config.ini
    def CreateConfig(self):
        """Open and set default keys for that config file"""

        # Open config.ini in write mode
        f = open(self.fileName, "w")

        # Set keys to config object
        self.config.add_section("Database")
        self.config.set("Database", "enabled", "True")
        self.config.set("Database", "host", "127.0.0.1")
        self.config.set("Database", "username", "root")
        self.config.set("Database", "password", "")
        self.config.set("Database", "database", "system")
        self.config.set("Database", "workers", "16")

        self.config.add_section("Discord")
        self.config.set("Discord", "token", "potato")
        self.config.set("Discord", "prefix", "!")
        # Write ini to file and close
        self.config.write(f)
        f.close()

    def Get(self, cat, item):
        return self.config.get(cat, item)