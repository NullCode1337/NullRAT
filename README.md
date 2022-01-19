![NullRAT](https://user-images.githubusercontent.com/70959549/150108231-0c8a8b30-a3cf-4a94-8712-2277cd833731.png)
<h3 align=center><b>{ The next-generation of Discord RATs }</b></h3>

## Features:
```
1) Redesigned from the ground up & very user friendly
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
10) Upload payloads to victim's PC
11) Get victim's system information
12) Execute CMD/Powershell command 
13) Find any environment variables
14) See directory contents, and do other directory manipulation 
15) Get victim's clipboard text history
16) Add executable to startup with one command
**) ...and more!
```

## How to use:
<h4>Preparation:</h4>

- Python 3.8+ should be installed on the PC (Tick "Add to PATH" while installing)
- **Do not under any circumstances use the Microsoft Store version of Python, does not work**
- Add PIP folder to path as well (`%APPDATA%\Python\{insert python folder}\Scripts`)

<h4>IMPORTANT:</h4>
Using the provided Dependencies Installer and Compiler is the key to success. 

Only people who know what they're doing should not use the compiler. I won't help anyone who does.

<h4>Steps:</h4>

- [Create a Discord BOT and obtain it's token](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)
- Dowload the latest release of NullRAT (git cloning/download zip will no longer work)
- Run the Cleanup exe to clean up the source directory
- Run the Dependencies Installer which will install all the necessary dependencies (except Python)
- Before running the compiler, read [Getting Variables.md](Getting Variables.md) and grab all the variables you need
- Run the Compiler, and feed it all the necessary information. NullRAT payload will be right there!

## Credits
1) Monst3red for inspiration
2) Sp00p64 and [his RAT](https://github.com/Sp00p64/DiscordRAT)

<h5 align=right>Software designed by NullCode</h6>
