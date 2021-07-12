# NullRAT
Remote Access Trojan that uses Discord as C&C

One of the main things about this RAT is it will be under 8mb, so you can always upload it without nitro

That's also why it doesn't have too many features compared to other Discord RATs

## Features:
- Find the public IP of the victim
- Find their Discord token(s)
- Find victim's approximate location
- Add payload to startup with one command
- Take pictures using victim's webcam 
- Take screenshot of victim's PC
- Download files from victim's PC
- Upload files to victim's PC
- Get some information about their PC
- Execute command prompt commands (Thank you Sp00p)
- Browse around their PC, see directory contents, and much more
`It's windows-only by the way; sorry :(`

## How to use:
- Python should be installed on the PC
1) [Create a Discord bot and obtain it's token](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)
2) Download this repository as zip/dowload the release/git clone it to your PC
3) Execute "Install Dependencies.bat"
4) Fill up the empty variables & bot token in RAT.py
5) Execute "Obfuscate and compile.bat"
6) That should be everything 

## Credits
- Monst3red for inspiration
- Sp00p64 for some commands from [his RAT](https://github.com/Sp00p64/DiscordRAT)
- NullCode
