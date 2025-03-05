#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"╭───────────⍟
├◈ <a>𝖬y 𝖭ᴀᴍᴇ</a> : <a href='https://t.me/Mrx369official_File_Share_Bot'> {bot_name} </a>\n
├◈ Sᴇᴄᴏɴᴅ Bᴏᴛ : ᴄᴏᴍɪɴɢ sᴏᴏɴ
├◈ <a>Owner</a> : <a href='https://t.me/mrx369official_support_bot'>Mrx369official</a>\n
├◈ <a>Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ</a> : <a href='https://t.me/+upoc5TQpjFJmZGZl'>All Bots - 369</a>\n
├◈ <a>Bᴜɪʟᴅ Vᴇʀꜱɪᴏɴ</a> : <a href='https://t.me/+9tl-HUIJj2ExYTA9'>file share V3</a>\n
╰───────────────⍟",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
