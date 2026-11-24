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

from NEXORMusic.core.bot import NEXOR
from NEXORMusic.core.dir import dirr
from NEXORMusic.core.userbot import Userbot
from NEXORMusic.misc import dbb, heroku

from .log import LOGGER

dirr()
dbb()
heroku()

app = NEXOR()
userbot = Userbot()


from .platforms import (
    AllSupport as AllSupportClass,
    NEXORAPI as NEXORAPIClass,
    UniversalAPI as UniversalAPIClass,
    all_support,
    Anghami,
    Apple,
    Audiomack,
    Bandcamp,
    Bilibili,
    Boomplay,
    Carbon,
    Coub,
    Dailymotion,
    Deezer,
    Facebook,
    Gaana,
    Instagram,
    Kick,
    Mixcloud,
    Okru,
    Pinterest,
    Reddit,
    Resso,
    Rumble,
    Saavn,
    Snapchat,
    Soundcloud,
    Spotify,
    Streamable,
    Telegram,
    Terabox,
    Threads,
    Tidal,
    Tiktok,
    Tumblr,
    Twitch,
    Twitter,
    Vimeo,
    Vk,
    Youtube,
)

AllSupport = all_support
NEXORAPI = all_support
UniversalAPI = all_support

Anghami = Anghami.AnghamiAPI()
Apple = Apple.AppleAPI()
Audiomack = Audiomack.AudiomackAPI()
Bandcamp = Bandcamp.BandcampAPI()
Bilibili = Bilibili.BilibiliAPI()
Boomplay = Boomplay.BoomplayAPI()
Carbon = Carbon.CarbonAPI()
Coub = Coub.CoubAPI()
Dailymotion = Dailymotion.DailymotionAPI()
Deezer = Deezer.DeezerAPI()
Facebook = Facebook.FacebookAPI()
Gaana = Gaana.GaanaAPI()
Instagram = Instagram.InstagramAPI()
Kick = Kick.KickAPI()
Mixcloud = Mixcloud.MixcloudAPI()
Okru = Okru.OkruAPI()
Pinterest = Pinterest.PinterestAPI()
Reddit = Reddit.RedditAPI()
Resso = Resso.RessoAPI()
Rumble = Rumble.RumbleAPI()
Saavn = Saavn.SaavnAPI()
Snapchat = Snapchat.SnapchatAPI()
SoundCloud = Soundcloud.SoundAPI()
Spotify = Spotify.SpotifyAPI()
Streamable = Streamable.StreamableAPI()
Telegram = Telegram.TeleAPI()
Terabox = Terabox.TeraboxAPI()
Threads = Threads.ThreadsAPI()
Tidal = Tidal.TidalAPI()
Tiktok = Tiktok.TiktokAPI()
Tumblr = Tumblr.TumblrAPI()
Twitch = Twitch.TwitchAPI()
Twitter = Twitter.TwitterAPI()
Vimeo = Vimeo.VimeoAPI()
Vk = Vk.VkAPI()
YouTube = Youtube.YouTubeAPI()
