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


class AssistantErr(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)


IGNORED_ERROR_KEYWORDS = [
    "Nᴏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛ ғᴏᴜɴᴅ",
    "لم يتم العثور على مكالمة فيديو نشطة",
    "Активный видеочат не найден",
    "Aktif video sohbet bulunamadı",
    "कोई सक्रिय वीडियोचैट नहीं मिला।",
]

import asyncio

IGNORED_EXCEPTION_CLASSES = (
    TimeoutError,
    asyncio.TimeoutError,
)


def is_ignored_error(err: Exception | BaseException) -> bool:
    if isinstance(err, IGNORED_EXCEPTION_CLASSES):
        return True

    err_str = str(err).lower()
    return any(keyword.lower() in err_str for keyword in IGNORED_ERROR_KEYWORDS)
