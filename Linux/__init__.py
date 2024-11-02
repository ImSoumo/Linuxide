import os
import sys
import Config
import logging, asyncio, time
from Graph import Clean_Stage
from telethon import TelegramClient
from telegram.ext import Application
from pyrogram import Client as PyGram
from hydrogram import Client as HyGram
from telethon.sessions import MemorySession
from logging import StreamHandler, basicConfig
from logging.handlers import RotatingFileHandler

GUARDS = []
for GUARD_USERS in Config.GUARDS:
    if GUARD_USERS not in GUARDS:
        GUARDS.append(GUARD_USERS)
    elif GUARDS not in GUARD_USERS:
        GUARD_USERS.append(GUARDS)

DELETE_COMMANDS = True
START_TIME = time.time()
Loop = asyncio.get_event_loop() 
__version__ = (
    {"version": 0.2},
    {"status": "on"}
)

if os.path.exists("Logs.txt"):
    with open("logs.txt", "r+") as aeo:
        aeo.truncate(0)

basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - [%(asctime)s - %(name)s - %(message)s] -> [%(module)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", mode="w+", maxBytes=50000000, backupCount=10),
        StreamHandler()
    ]
)
LOGGER = logging.getLogger("Lɪɴᴜxɪᴅᴇ")
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("hydrogram").setLevel(logging.WARNING)

if not Config.API_ID:
    LOGGER.warning("» Wᴀʀɴɪɴɢ: ᴀᴘɪ_ɪᴅ ɴᴏᴛ ғᴏᴜɴᴅ ɪɴ ᴄᴏɴғɪɢ ғɪʟᴇs sʜᴜᴛᴅᴏᴡɴ ʙᴏᴛ !")
    sys.exit()
elif not Config.API_HASH:
    LOGGER.warning("» Wᴀʀɴɪɴɢ: ᴀᴘɪ_ʜᴀsʜ ɴᴏᴛ ғᴏᴜɴᴅ ɪɴ ᴄᴏɴғɪɢ ғɪʟᴇs sʜᴜᴛᴅᴏᴡɴ ʙᴏᴛ !")
    sys.exit()
elif not Config.BOT_TOKEN:
    LOGGER.warning("» Wᴀʀɴɪɴɢ: ʙᴏᴛ_ᴛᴏᴋᴇɴ ɴᴏᴛ ғᴏᴜɴᴅ ɪɴ ᴄᴏɴғɪɢ ғɪʟᴇs sʜᴜᴛᴅᴏᴡɴ ʙᴏᴛ !")
    sys.exit()

class Pyro():
    Soumo = PyGram(
        name="PyroSoumo",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="Packages"),
        in_memory=True
    )
App = Pyro.Soumo

class Hydro():
    Soumo = HyGram(
        name="HydroSoumo",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins={"root": "Packages"},
        in_memory=True
    )
Sakura = Hydro.Soumo

app = TelegramClient(
    MemorySession(),
    Config.API_ID,
    Config.API_HASH
)

app2 = PyGram(
    name="pyUB2",
    api_id=29400566,
    api_hash="8fd30dc496aea7c14cf675f59b74ec6f",
    in_memory=True,
    session_string="BQHAnfYAlviETjEp77nFPQv1Wc6qOZYasRnPXWLXZypy6XOXHlXKwhLcLK7wEtx-LAKQeDmvQnlLB4hKsH7Jva1I9ZJje0s1-aI9irIJc09Ctl1a2mDoMc9U2ndlGfa0XJvSV7NajQx-j5buv5Auqqn0Mj_FevtqbLcbL6kRDotmHiqkcx3due2Uk8geGNTGbe_xU9pYDD9FX4qx9gbNthevEeT4DCeR14ezSaKdJ5-mG7O7vsxaPS_oGbrJa_svPAv5muxMCmm_qvpxc_srTiPkgHGQofmyL5YS5kwwPtb81F6CyT4O_SBMDvMS2sQ-Xmuhtwd_5AZNSlN5z7HAaKe5PBmCFAAAAAGAI4AQAA",
    plugins=dict(root="Linux")
)
async def pyroUser():
    await app2.start()
    
async def addPackages():
    await App.start()
    await Sakura.start()
    try:
        Resocs = await Clean_Stage()
        if Resocs:
            await App.edit_message_text(
                Resocs["chat_id"],
                Resocs["message_id"],
                "**🔮 Lɪɴᴜxɪᴅᴇ Rᴇsᴛᴀʀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ !**"
            )
        else:
            await App.send_message(Config.SUPPORT, "**🔮 Lɪɴᴜxɪᴅᴇ Cʟᴏᴜᴅ Sᴇʀᴠᴇʀ Sᴛᴀʀᴛᴇᴅ !**")
    except Exception:
        LOGGER.info("» Bᴏᴛ ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ.")

pyApp = Application.builder().token(Config.BOT_TOKEN).build()
Func = pyApp.add_handler
#app2Task = Loop.create_task(pyroUser())
Loop.run_until_complete(
    asyncio.gather(pyApp.bot.initialize(), addPackages())
)
LOGGER.info("[INFO]: Gᴇᴛᴛɪɴɢ Bᴏᴛ Iɴғᴏʀᴍᴀᴛɪᴏɴs...")
BOT_ID = pyApp.bot.id
BOT_NAME = pyApp.bot.first_name
BOT_USERNAME = pyApp.bot.username
