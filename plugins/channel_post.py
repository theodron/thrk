import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, UserNotParticipant

from bot import Bot
from config import CHANNEL_ID, DISABLE_CHANNEL_BUTTON, FORCE_SUB_CHANNEL_1, FORCE_SUB_CHANNEL_2
from helper_func import subscribed1, subscribed2, encode, decode, get_messages, present_user, add_user

@Bot.on_message(filters.private & filters.command('start') & subscribed1 & subscribed2)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except Exception as e:
            print(f"Error adding user: {e}")
            pass

    text = message.text
    if len(text) > 7:
        try:
            base64_string = text.split(" ", 1)[1]
        except IndexError:
            return

        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except ValueError:
                return

            if start <= end:
                ids = range(start, end + 1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break

            # Here you can add logic to handle the `ids` list as needed
            # For example, you might want to send a message with the IDs
            await message.reply_text(f"Generated IDs: {list(ids)}")
        else:
            await message.reply_text("Invalid argument format.")
    else:
        await message.reply_text("Please provide a valid command with parameters.")

@Bot.on_message(filters.private & ~filters.command(['start', 'users', 'broadcast', 'batch', 'genlink', 'stats']))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("Please Wait...!", quote=True)

    # Check if the user is a member of the required channels using subscribed1 and subscribed2
    is_member1 = await subscribed1(client, message.from_user.id)
    is_member2 = await subscribed2(client, message.from_user.id)

    if not (is_member1 and is_member2):
        buttons = [
            [
                InlineKeyboardButton(text="⚡Join Channel 1⚡", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="⚡Join Channel 2⚡", url=client.invitelink2),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)

        await reply_text.edit_text(
            "You need to join the following channels to generate a link:\n"
            "Please join them using the buttons below and try again.",
            reply_markup=reply_markup
        )
        return

    # If the user is a member, proceed to generate the link
    try:
        post_message = await message.copy(chat_id=client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id=client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return

    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])

    await reply_text.edit(f"<b>Here is your link</b>\n\n{link}", reply_markup=reply_markup, disable_web_page_preview=True)

    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(reply_markup)

@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):
    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{
