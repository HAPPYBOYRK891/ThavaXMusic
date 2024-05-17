import random
import math
from typing import Union
from config import SUPPORT_CHAT
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ThavaXMusic import app
from ThavaXMusic.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [    
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ]
        [    
            InlineKeyboardButton(
                text=_["✨sᴜᴘᴘᴏʀᴛ✨"],
                 url=SUPPORT_CHAT",
            )
    ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "𖣘⭑⭑⭑⭑⭑⭑⭑⭑⭑"
    elif 10 < umm < 20:
        bar = "⭑𖣘⭑⭑⭑⭑⭑⭑⭑⭑"
    elif 20 <= umm < 30:
        bar = "⭑⭑𖣘⭑⭑⭑⭑⭑⭑⭑"
    elif 30 <= umm < 40:
        bar = "⭑⭑⭑𖣘⭑⭑⭑⭑⭑⭑"
    elif 40 <= umm < 50:
        bar = "⭑⭑⭑⭑𖣘⭑⭑⭑⭑⭑"
    elif 50 <= umm < 60:
        bar = "⭑⭑⭑⭑⭑𖣘⭑⭑⭑⭑"
    elif 60 <= umm < 70:
        bar = "⭑⭑⭑⭑⭑⭑𖣘⭑⭑⭑"
    elif 70 <= umm < 80:
        bar = "⭑⭑⭑⭑⭑⭑⭑𖣘⭑⭑"
    elif 80 <= umm < 95:
        bar = "⭑⭑⭑⭑⭑⭑⭑⭑𖣘⭑"
    else:
        bar = "⭑⭑⭑⭑⭑⭑⭑⭑⭑𖣘"
    buttons = [
                [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
                 [
            InlineKeyboardButton(
                text="⇆ 𝐒ʜᴜғғʟᴇ ⇆",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(
                text="↻ 𝐋ᴏᴏᴩ ↻", callback_data=f"ADMIN Loop|{chat_id}"
            ),
         ],
        [
            InlineKeyboardButton(text="⏮ 10", callback_data=f"ADMIN 1|{chat_id}"),
            InlineKeyboardButton(text="⏮ 30", callback_data=f"ADMIN 3|{chat_id}"),
            InlineKeyboardButton(text="⏭ 10", callback_data=f"ADMIN 2|{chat_id}"),
            InlineKeyboardButton(text="⏭ 30", callback_data=f"ADMIN 4|{chat_id}"),             
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
                [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
                 [
            InlineKeyboardButton(
                text="⇆ 𝐒ʜᴜғғʟᴇ ⇆",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(
                text="↻ 𝐋ᴏᴏᴩ ↻", callback_data=f"ADMIN Loop|{chat_id}"
            ),
         ],
        [
            InlineKeyboardButton(text="⏮ 10", callback_data=f"ADMIN 1|{chat_id}"),
            InlineKeyboardButton(text="⏮ 30", callback_data=f"ADMIN 3|{chat_id}"),
            InlineKeyboardButton(text="⏭ 10", callback_data=f"ADMIN 2|{chat_id}"),
            InlineKeyboardButton(text="⏭ 30", callback_data=f"ADMIN 4|{chat_id}"),             
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"THAVAPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"THAVAPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
