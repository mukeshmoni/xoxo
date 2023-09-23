"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID","17713634"))
        self.API_HASH: str = os.environ.get("API_HASH", "a8c943a69022fef3ac66accc7ba8ce6b")
        self.SESSION: str = os.environ.get("SESSION", "BQAtV1fEhl3iexzF4dMp0kv_q8CuVyTVdSwLz6e9DUsgQdWJDiv5ek_kB0Qj6BLJLeeXmqeVjyS_QDcemzMuUQEj4Ri_lOquqiRJoDnK90SWU7sRBAVmnfsOjLRe3YafnWMEo95QLOPrNAYVObx43_3LLru2Rue0K54AcKTG6upq8y1mDqGV4qBr2jNvG7YHR4DHd_FBDI-jbsZZUPcukzxyKYyzzHNBDP0U2b_Nnrq1W4ZGSXjkq4gXQKyMyAT4WWnXYUXSDCxd5FDoHZREIr-1_GVpZZXoxJtbyK8E35k-SD3DKq6ZuAmh2iSibuwijxvrUMH4q3Pxsuy4qV9rFF1kAAAAAYxVunwA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "6443029397:AAFLghTQUsS1oohwMA6O_4CNC-DhTDiOPns")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "6649395836").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
