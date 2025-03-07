#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7782236845:AAEbUxxck_yBuXkZi7O6ETqPOOgvexVYU1U")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28450765"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "36f00f11f9d5c65e69b81fd804453a93")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002259290366"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6636180199"))

#Port
PORT = os.environ.get("PORT", "7070")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://paidtron:paidtron@fl4me.ucvbg.mongodb.net/?retryWrites=true&w=majority&appName=Fl4me")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1002164597795"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1002198414165"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "-1002211737945")) #don't remove 0 from here 😐
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "-1002304692243")) #don't remove 0 from here 😐


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#pic
START_PIC = os.environ.get("START_PIC", "https://files.catbox.moe/jqjnsi.jpg")

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {ᴜꜱᴇʀɴᴀᴍᴇ}\n\n     ɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱʜᴀʀᴇ ʙᴏᴛ. ᴘᴏᴡᴇʀᴇᴅ ʙʏ \n@Mrx369official_Dev369devil_Index\n╭─────────────────────────\nᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/+-66Rn1OysMYyYTI1'>369 ʙᴏᴛꜱ✨</a>\nꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : <a href='https://t.me/+XFTfRRjtdgswOTM1'>369 ꜱᴜᴘᴘᴏʀᴛ✨</a>\n\nᴅᴇᴠɪʟ'ꜱ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/addlist/E5In_fLSLyU0MjU1'>2.0</a>\nᴄᴏɴᴛᴇɴᴛ ᴜᴘᴅᴀᴛᴇꜱ : @Content_Updates_369\n╰─────────────────────────</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = ""

ADMINS.append(OWNER_ID)
ADMINS.append(7533047591)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
