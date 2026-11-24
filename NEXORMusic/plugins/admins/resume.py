# ─────────────────────────────────────────────────────────────
# NEXOR MUSIC  —  Developed & maintained by ADITYA
# Developer : https://t.me/NEXOR_BLAZE
# Channel   : https://t.me/MUSIXX_HUB
# Copyright (C) 2026 by Aditya (NEXOR_BLAZE), < https://t.me/NEXOR_BLAZE >.
# Modified by Aditya (NEXOR_BLAZE) from the original AloneMusic.
# ─────────────────────────────────────────────────────────────
# Original work (kept as required by GNU GPL v3):
#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/AloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/AloneMusic/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from NEXORMusic import app
from NEXORMusic.core.call import NEXOR
from NEXORMusic.utils.database import is_music_playing, music_on
from NEXORMusic.utils.decorators import AdminRightsCheck
from NEXORMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["resume", "cresume"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await NEXOR.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
