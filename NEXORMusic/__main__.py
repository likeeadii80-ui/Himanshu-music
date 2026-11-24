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
# This file is part of < https://github.com/TheAloneTeam/AloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/AloneMusic/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import importlib
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from NEXORMusic import LOGGER, app, userbot
from NEXORMusic.core.call import NEXOR
from NEXORMusic.misc import sudo
from NEXORMusic.plugins import ALL_MODULES
from NEXORMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


class _Health(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"NEXOR MUSIC is running | t.me/NEXOR_BLAZE")

    def log_message(self, *args):
        pass


def _keepalive():
    """Tiny web server so Render/Koyeb web services see an open port."""
    port = os.environ.get("PORT")
    if not port:
        return
    server = HTTPServer(("0.0.0.0", int(port)), _Health)
    threading.Thread(target=server.serve_forever, daemon=True).start()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        sys.exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("NEXORMusic.plugins" + all_module)
    LOGGER("NEXORMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await NEXOR.start()
    try:
        await NEXOR.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("NEXORMusic").error(
            "Please turn on the videochat of your log group/channel.\n\nStopping Bot..."
        )
        sys.exit()
    except:
        pass
    await NEXOR.decorators()
    LOGGER("NEXORMusic").info(
        "NEXOR MUSIC started successfully | Dev: @NEXOR_BLAZE | Channel: @MUSIXX_HUB"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("NEXORMusic").info("Stopping NEXOR MUSIC Bot...")


def main():
    _keepalive()
    asyncio.get_event_loop().run_until_complete(init())


if __name__ == "__main__":
    main()
