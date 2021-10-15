<h1 align=center> ☠️ NullRAT</h1>
<p align=center>Windows-Only Remote Access Trojan that uses Discord as C&C</p>

## Features:
```
0) Redesigned from the ground up
1) Relatively small size for a Python RAT
2) Find the public IP of the victim
3) Find their Discord token(s) and all user info
4) Find victim's geographic information (zip, region, country, latitude, longitude)
5) Add executable to startup with one command
6) Take pictures using victim's webcam 
7) Take screenshot of victim's monitor
8) Download files from victim's PC
9) Upload files to victim's PC
10) Get victim's system information
11) Execute command prompt/powershell commands
12) Find any environment variables, and cd there
13) See all the files inside a specified directory
14) Inbuilt Fast Discord Token Checker
15) Get victim's clipboard text history
16) ...and more!
```

## How to use:
<h4>IMPORTANT:</h4>
Python 3.6+ should be installed on the PC and added to path (pip folder should be added too)

Also don't compile normally using pyinstaller, use the compiler provided

- [Create a Discord bot and obtain it's token](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)
- Git clone / Download repo as zip / Dowload the release
- Fill up the empty variables & bot token in RAT.py
- Finally, execute the following: 
```cmd
Install Dependencies.bat
RATCompiler.bat
```

## Credits
1) Monst3red for inspiration
2) Sp00p64 for some commands from [his RAT](https://github.com/Sp00p64/DiscordRAT)
3) Buntii for ideas
