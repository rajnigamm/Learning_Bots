import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "25033979"
API_HASH = "a2640868faffd7c134e1a5be84197c43"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7365930400:AAGFltWJx3LnnN4QQ9ot8LVqPsBN7Ob0eWk"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://krnigam82:krnigam82@cluster0.50v7btc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"



DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = "-1002227877496"

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = "7184929227"

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/zffjsuf"
SUPPORT_CHAT = "https://t.me/zffjsuf"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQF9_PsAFEKvXfk1D9wCgDwVJAj7RatYq2d3b2Ip0Qpa-OGM5xvz_grXjKkLm6z7zbivr3IYWaaB4s-E0AOxtrIDFW6CTJwivr5o-I493DsMZaFWytfTllUt0Ge5dF0zR27fpAiYyP4DZj35yAOVTApZuTHidRc_SmpF4yWpa9rXGWx-U7HSoHtxBq0riZoOb6_IErW5jlMUlAMAAk7GGMsldtWHBCK7OXqC68jie6XGRI1zhBqxuyIvxZO1KQNeG_YZKAlw4h762spiwuHJKcXMMDXVguHESM3F21w2UzFRaSblQS4Rlg1YkkkgfeUdLqAs3ry76-F0IS0HSCMDYKBNT-eMIQAAAAGsQVHLAA", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/69121df638b347a5c7464.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/69121df638b347a5c7464.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/69121df638b347a5c7464.jpg"
STATS_IMG_URL = "https://graph.org/file/69121df638b347a5c7464.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/69121df638b347a5c7464.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/69121df638b347a5c7464.jpg"
STREAM_IMG_URL = "https://graph.org/file/69121df638b347a5c7464.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/69121df638b347a5c7464.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/69121df638b347a5c7464.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/69121df638b347a5c7464.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/69121df638b347a5c7464.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/69121df638b347a5c7464.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
