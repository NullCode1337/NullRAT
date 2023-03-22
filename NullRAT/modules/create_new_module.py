import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class CMDNAME(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command( )
    async def CMDNAME(self, ctx, victim, argumentsss):     
        """CMD DESCRIPTION
        
        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        argumentsss: ARGUMENT DESCRIPTION
        """
        
        if str(victim) == str(self.bot.identifier):
            """ command here... """

def setup(bot: commands.Bot):
    bot.add_cog(CMDNAME(bot))
