# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os
from AstrakoBot.sample_config import Config 
class Development(Config): 
    OWNER_ID = "902525829" # your telegram ID 
    OWNER_USERNAME = "TheeDon93" 
    # your telegram username 
    API_KEY = "1445580967:AAEJE_Aj9xRih3HKN1Kom5ag4-RCuO2-VIk" 
    # your api key, as provided by the @botfather 
    SQLALCHEMY_DATABASE_URI = 'postgres://arzqzhqwlyiuyf:8ddc700b99ae4831102b913a50010b8a0bd02a3b50e72deaf326bd96faf89ee9@ec2-54-247-158-179.eu-west-1.compute.amazonaws.com:5432/d22j3b0q337urk"  # needed for any database modules


    # sample db credentials 
    JOIN_LOGGER = '-1234567890' 
    # some group chat that your bot is a member of USE_JOIN_LOGGER = True 
    DRAGONS = [183980, 834895] 
    # List of id's for users which have sudo access to the bot. 
    LOAD = [] 
    NO_LOAD = []

def get_user_list(config, key):
    with open("{}/AstrakoBot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 123456  # integer value, dont use ""
    API_HASH = "pogobutler_bot"
    TOKEN = "1445580967:AAEJE_Aj9xRih3HKN1Kom5ag4-RCuO2-VIk"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 902525829  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "TheeDon93"
    SUPPORT_CHAT = "pogobutler_bot"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1234567890123
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1234567890123
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    ALLOW_CHATS = True

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://arzqzhqwlyiuyf:8ddc700b99ae4831102b913a50010b8a0bd02a3b50e72deaf326bd96faf89ee9@ec2-54-247-158-179.eu-west-1.compute.amazonaws.com:5432/d22j3b0q337urk"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = "https://pogobutler.herokuapp.com/"
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    WEATHER_API = ""  # go to openweathermap.org/api to get key

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
