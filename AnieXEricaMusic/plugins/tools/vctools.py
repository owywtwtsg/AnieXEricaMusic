from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

import config
from AnieXEricaMusic import YouTube, app
from AnieXEricaMusic.core.call import AMBOT
from AnieXEricaMusic.misc import db
from AnieXEricaMusic.utils.database import is_vc_on, vc_on, vc_off
from AnieXEricaMusic.utils.decorators import AdminRightsCheck
from AnieXEricaMusic.utils.inline import close_markup, stream_markup
from AnieXEricaMusic.utils.stream.autoclear import auto_clean
from AnieXEricaMusic.utils.thumbnails import gen_thumb
from config import BANNED_USERS


@app.on_message(filters.command(["vcinfos"]) & filters.group & ~BANNED_USERS)
async def vcchecks(client, message):
  if len(message.command) != 2:
        await message.reply_text("Usage: /vcinfos [on/off]")
        return
  status = message.text.split(None, 1)[1].strip()
  status = status.lower()
  chat_id = message.chat.id
  if status in ("on", "yes"):
    if await is_vc_on(chat_id):
      await message.reply_text("vc check is already enabled.")
      return
    await vc_on(chat_id)
    await message.reply_text(
            "Enabled vc check System. I will send  Messages if new users joined in voice chat."
        )
  elif status in ("off", "no"):
    if not await is_vc_on(chat_id):
            await message.reply_text("vc check is already disabled.")
            return
    await vc_off(chat_id)
    await message.reply_text("Disabled vc check System.")
  else:
    await message.reply_text("Unknown Suffix, Use /vcinfos [on/off]")

