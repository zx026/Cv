"""
╔════════════════════════════════════════════════╗
║   ⚡ POWERFUL CONFIG SYSTEM for Pyrogram Bots ⚡  ║
║   🔥 Advanced Version with Auto Validation 🔥     ║
║   ✅ Made for SPOTIFY / MUSIC / VIDEO Bots       ║
╚════════════════════════════════════════════════╝
"""

import os
import re
import logging
from dotenv import load_dotenv
from pyrogram import filters

# ╭───────────────────────────────╮
# │ Load Environment Variables    │
# ╰───────────────────────────────╯
load_dotenv()

# ╭───────────────────────────────╮
# │ Logging Setup                 │
# ╰───────────────────────────────╯
logging.basicConfig(
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
LOG = logging.getLogger(__name__)


# ╭───────────────────────────────╮
# │ Helper: Safe Getter           │
# ╰───────────────────────────────╯
def get_env(name: str, default=None, required=False, cast_type=None):
    """Safely fetch environment variable."""
    value = os.getenv(name, default)
    if required and not value:
        LOG.error(f"❌ Required environment variable '{name}' is missing.")
        raise SystemExit(1)
    if cast_type and value:
        try:
            value = cast_type(value)
        except ValueError:
            LOG.warning(f"⚠️ Environment variable '{name}' has invalid type.")
            value = default
    return value


# ╭───────────────────────────────╮
# │ Telegram Bot Configuration    │
# ╰───────────────────────────────╯
API_ID = get_env("API_ID", required=True, cast_type=int)
API_HASH = get_env("API_HASH", required=True)
BOT_TOKEN = get_env("BOT_TOKEN", required=True)

OWNER_ID = get_env("OWNER_ID", required=True, cast_type=int)
OWNER_USERNAME = get_env("OWNER_USERNAME", "@ll_Oye_Zayn_ll")
BOT_USERNAME = get_env("BOT_USERNAME", "Gaana_MusicROBot")
BOT_NAME = get_env("BOT_NAME", "╼⃝𖠁 𝐁ʌʙʏ ꭙ 𝐌ᴜsɪᴄ 𖠁⃝╾")
ASSUSERNAME = get_env("ASSUSERNAME", "╼⃝𖠁 𝐁ʌʙʏ ꭙ 𝐌ᴜsɪᴄ 𖠁⃝╾")

# ╭───────────────────────────────╮
# │ Database / APIs               │
# ╰───────────────────────────────╯
MONGO_DB_URI = get_env(
    "MONGO_DB_URI",
    "mongodb+srv://TEAMBABY01:UTTAMRATHORE09@cluster0.vmjl9.mongodb.net/?retryWrites=true&w=majority",
)
API_URL = get_env("API_URL", "https://BabyAPI.Pro")
VIDEO_API_URL = get_env("VIDEO_API_URL", "https://BabyAPI.Pro/video")

# ╭───────────────────────────────╮
# │ Log Group / Channel           │
# ╰───────────────────────────────╯
LOGGER_ID = get_env("LOGGER_ID", None, required=True, cast_type=int)
if not str(LOGGER_ID).startswith("-100"):
    LOG.error("❌ LOGGER_ID must start with -100 (Supergroup/Channel ID).")
    raise SystemExit(1)

# ╭───────────────────────────────╮
# │ Heroku / Git Settings         │
# ╰───────────────────────────────╯
HEROKU_APP_NAME = get_env("HEROKU_APP_NAME")
HEROKU_API_KEY = get_env("HEROKU_API_KEY")
UPSTREAM_REPO = get_env("UPSTREAM_REPO", "https://github.com/TrickBySaqib/SPOTIFY_MUSIC")
UPSTREAM_BRANCH = get_env("UPSTREAM_BRANCH", "main")
GIT_TOKEN = get_env("GIT_TOKEN")

# ╭───────────────────────────────╮
# │ Support Links                 │
# ╰───────────────────────────────╯
SUPPORT_CHANNEL = get_env("SUPPORT_CHANNEL", "https://t.me/ll_Bot_Promotion_ll")
SUPPORT_CHAT = get_env("SUPPORT_CHAT", "https://t.me/ll_Bot_Promotion_ll")
SOURCE = get_env("SOURCE", "https://t.me/ll_Bot_Promotion_ll")

# URL Validation
for name, url in {
    "SUPPORT_CHANNEL": SUPPORT_CHANNEL,
    "SUPPORT_CHAT": SUPPORT_CHAT,
    "SOURCE": SOURCE,
}.items():
    if url and not re.match(r"^(?:http|https)://", url):
        LOG.error(f"[CONFIG ERROR] Invalid URL for {name}: {url}")
        raise SystemExit(1)

# ╭───────────────────────────────╮
# │ Limits and Timers             │
# ╰───────────────────────────────╯
DURATION_LIMIT_MIN = get_env("DURATION_LIMIT", 17000, cast_type=int)
AUTO_LEAVE_ASSISTANT_TIME = get_env("ASSISTANT_LEAVE_TIME", 9000, cast_type=int)
SONG_DOWNLOAD_DURATION = get_env("SONG_DOWNLOAD_DURATION", 9999999, cast_type=int)
TG_AUDIO_FILESIZE_LIMIT = get_env("TG_AUDIO_FILESIZE_LIMIT", 5242880000, cast_type=int)
TG_VIDEO_FILESIZE_LIMIT = get_env("TG_VIDEO_FILESIZE_LIMIT", 5242880000, cast_type=int)
PLAYLIST_FETCH_LIMIT = get_env("PLAYLIST_FETCH_LIMIT", 25, cast_type=int)

# ╭───────────────────────────────╮
# │ Spotify API Keys              │
# ╰───────────────────────────────╯
SPOTIFY_CLIENT_ID = get_env("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = get_env("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# ╭───────────────────────────────╮
# │ String Sessions               │
# ╰───────────────────────────────╯
STRING_SESSION = get_env("STRING_SESSION")
if not STRING_SESSION:
    LOG.warning("⚠️ STRING_SESSION missing. Assistant may not join voice calls automatically.")

# ╭───────────────────────────────╮
# │ Assets / Thumbnails           │
# ╰───────────────────────────────╯
ASSETS = {
    "START_IMG_URL": get_env("START_IMG_URL", "https://files.catbox.moe/tapkqc.jpg"),
    "PING_IMG_URL": get_env("PING_IMG_URL", "https://telegra.ph/file/fd827f9a4fe8eaa3e8bf4.jpg"),
    "PLAYLIST_IMG_URL": "https://telegra.ph/file/d723f4c80da157fca1678.jpg",
    "STATS_IMG_URL": "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg",
    "YOUTUBE_IMG_URL": "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg",
}


# ╭───────────────────────────────╮
# │ Utility: Time Conversion      │
# ╰───────────────────────────────╯
def time_to_seconds(time_str: str) -> int:
    """Convert HH:MM or MM:SS format to seconds."""
    try:
        parts = [int(x) for x in time_str.strip().split(":")]
        return sum(x * 60 ** i for i, x in enumerate(reversed(parts)))
    except Exception:
        LOG.warning(f"⚠️ Invalid time format: {time_str}, defaulting to 10 hours.")
        return 36000


DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# ╭───────────────────────────────╮
# │ Runtime Globals               │
# ╰───────────────────────────────╯
BANNED_USERS = filters.user()
adminlist, lyrical, votemode = {}, {}, {}
autoclean, confirmer = [], {}

# ╭───────────────────────────────╮
# │ Final Log Output              │
# ╰───────────────────────────────╯
LOG.info("✅ Configuration Loaded Successfully!")
LOG.info(f"🤖 BOT: {BOT_NAME} ({BOT_USERNAME}) | OWNER: {OWNER_USERNAME}")
LOG.info(f"🌐 MongoDB: {'Connected' if MONGO_DB_URI else 'Not Set'}")
LOG.info(f"🎧 Duration Limit: {DURATION_LIMIT_MIN} min | Filesize Limit: {TG_AUDIO_FILESIZE_LIMIT / 1024**2:.1f} MB")
LOG.info(f"🧾 Log Group ID: {LOGGER_ID}")
