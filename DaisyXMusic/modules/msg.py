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
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /cmute - mute song play
- /mute - mute song play
- /unmute - mute song play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group. (remember to use /ytplay instead /play)
""",
        f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
""",
        f"""
**=>> Song Download 🎸**

- /video [song mame]: Download video song from youtube
- /song [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer

**=>> Search Tools 📄**

- /search [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics
""",
        f"""
**=>> Commands for Sudo Users ⚔️**

 - /userbotleaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

""",
    ]
