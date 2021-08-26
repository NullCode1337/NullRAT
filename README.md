# NullRAT
Remote Access Trojan that uses Discord as C&C

It is under 8mb, so you can upload it without nitro

As such, only the useful RAT Features are present inside this program

## Features:
- Find the public IP of the victim
- Find their Discord token(s)
- Find victim's approximate location
- Add payload to startup with one command
- Take pictures using victim's webcam 
- Take screenshot of victim's PC
- Download files from victim's PC
- Upload files to victim's PC
- Get victim's system information
- Execute command prompt commands (Thank you Sp00p)
- Find any environment variables, and chdir there
- See all the files inside a specified directory
- Any other commands you (the based people) want

`It's windows-only by the way; sorry :(`

## How to use:
- Python 3.6+ should be installed on the PC and added to path (pip folder should be added too)
- Don't compile normally using pyinstaller, use the compiler provided
1) [Create a Discord bot and obtain it's token](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)
2) Clone / Download this repository as zip [recommended] / Dowload the release
3) Execute "Install Dependencies.bat"
4) Fill up the empty variables & bot token in RAT.py
5) Execute "RATCompiler.bat"
6) That should be everything 

## Credits
- Monst3red for inspiration
- Sp00p64 for some commands from [his RAT](https://github.com/Sp00p64/DiscordRAT)
- Buntii for ideas
