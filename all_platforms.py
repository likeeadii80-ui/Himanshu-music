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

import os

# -------------------------------------------------------------
# Configuration: Aap yahan direct apna API_URL aur API_KEY daal sakte hain
# Sabhi platforms (YouTube, Spotify, Apple, JioSaavn, Instagram, etc.) yahi se chalenge.
# -------------------------------------------------------------
API_URL = (
    os.getenv("API_URL")
    or os.getenv("NEXOR_API_URL")
    or os.getenv("RITESH_API_URL")
    or "https://api.riteshyt.in"
).rstrip("/")

API_KEY = (
    os.getenv("API_KEY")
    or os.getenv("NEXOR_API_KEY")
    or os.getenv("RITESH_API_KEY")
    or "riteshpermanent_6e2e564b3b37175d82acfce7"
)

DEFAULT_API_URL = API_URL
DEFAULT_API_KEY = API_KEY
