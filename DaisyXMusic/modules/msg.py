# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from DaisyXMusic.config import ASSISTANT_NAME, PROJECT_NAME


class Messages:
    START_MSG = "Hi [{}](tg://user?id={}) 🙂\n\nI'm An Advanced Bot Created For Playing Music In The Voice Chats OF Telegram Groups & Channels.\n\nSend Me /help For More Info !"
    HELP_MSG = [
        ".",
        f"""
**Hey [{}](tg://user?id={}) Welcome Back To {PROJECT_NAME}

⚪️ {PROJECT_NAME} Can Play Music In Your Group's Voice Chat As Well As Channel Voice Chats

⚪️ Assistant Name >> @{ASSISTANT_NAME}\n\nClick Next For Instructions**
""",
        f"""
**Setting Up**

1) Make Bot Admin (Group And In Channel If Use Cplay)
2) Start A Voice Chat
3) Try /play [Song Name] For The First Time By An Admin
*) If Userbot Joined Enjoy Music, If Not Add @{ASSISTANT_NAME} To Your Group And Retry

**For Channel Music Play**
1) Make Me Admin Of Your Channel 
2) Send /userbotjoinchannel In Linked Group
3) Now Send Commands In Linked Group
""",
        f"""
**Commands**

**=>> Song Playing 🎧**

- /play: Play The Requestd Song
- /play [YT Url] : Play The Given YT Url
- /play [Reply Yo Audio]: Play Replied Audio
- /splay: Play Song Via Jio Saavn
- /ytplay: Directly Play Song Via Youtube Music

**=>> Playback ⏯**

- /player: Open Settings Menu Of Player
- /skip: Skips The Current Track
- /pause: Pause Track
- /resume: Resumes The Paused Track
- /end: Stops Media Playback
- /mute: Mute Song Play
- /unmute: Unmute Song Play
- /current: Shows The Current Playing Track
- /playlist: Shows Playlist

*Player Cmd And All Other Cmds Except /play, /current And /playlist Are Only For Admins Of The Group.
""",
        f"""
**=>> Channel Music Play 🛠**

⚪️ For Linked Group Admins Only:

- /cplay [Song Name] - Play Song You Requested
- /csplay [Song Name] - play Song You Requested Via Jio Saavn
- /cplaylist - Show Now Playing List
- /cccurrent - Show Now playing
- /cplayer - Open Music Player Settings Panel
- /cpause - Pause Song play
- /cresume - Resume Song play
- /cskip - Play Next Song
- /cend - Stop Music Play
- /cmute - Mute Song Play
- /mute - Mute Song Play
- /unmute - Mute Song Play
- /userbotjoinchannel - Invite Assistant To Your Chat

Channel Is Also Can Be Used Instead OF C ( /cplay = /channelplay )

⚪️ If You Donlt Like To Play In Linked Group:

1) Get your channel ID.
2) Create A Group With Tittle: Channel Music: your_channel_id
3) Add Bot As Channel Admin With Full Perms
4) Add @{ASSISTANT_NAME} To The Channel As An Admin.
5) Simply Send Commands In Your Group. (Remember To Use /ytplay Instead /play)
""",
        f"""
**=>> More Tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates Admin Info OF Your Group. Try If Bot Isn't Recognize Admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot To Your Chat
""",
        f"""
**=>> Song Download 🎸**

- /video [Song Mame]: Download Video Song From Youtube
- /song [Song Name]: Download Audio Song From Youtube
- /saavn [Song Name]: Download Song From Saavn
- /deezer [Song Name]: Download Song From Deezer

**=>> Search Tools 📄**

- /search [Song Name]: Search Youtube For Songs
- /lyrics [Song Name]: Get Song Lyrics
""",
        f"""
**=>> Commands For Sudo Users ⚔️**

 - /userbotleaveall - Remove Assistant From All Chats
 - /broadcast <reply to message> - Globally Brodcast Replied Message To All Chats
 - /pmpermit [on/off] - Enable/Disable PMPermit Message
*Sudo Users Can Execute Any Command In Any Groups

""",
    ]
