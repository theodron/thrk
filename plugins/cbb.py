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
├◈ <b>𝖬y 𝖭ᴀᴍᴇ</b> : <a href='https://t.me/Mrx369official_File_Share_Bot'>Mrx369officiall File Share Bot</a>\n
├◈ Sᴇᴄᴏɴᴅ Bᴏᴛ : ᴄᴏᴍɪɴɢ sᴏᴏɴ
├◈ <b>Owner</b> : <a href='https://t.me/mrx369official_support_bot'>Mrx369official</a>\n
├◈ <b>Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ</b> : <a href='https://t.me/+upoc5TQpjFJmZGZl'>All Bots - 369</a>\n
├◈ <b>Bᴜɪʟᴅ Vᴇʀꜱɪᴏɴ</b> : <a href='https://t.me/+9tl-HUIJj2ExYTA9'>file share V3</a>\n
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
